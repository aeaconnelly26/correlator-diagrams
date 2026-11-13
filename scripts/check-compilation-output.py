#!/usr/bin/env python3
"""Compare every rendered page of paired workloads and compatibility probes."""
import argparse
import json
from pathlib import Path
import subprocess
import tempfile

from PIL import Image, ImageChops


def compare(baseline, candidate, dpi, output):
    with tempfile.TemporaryDirectory(prefix='feynmanfun-output-') as tmp:
        tmp = Path(tmp)
        for name, pdf in [('baseline', baseline), ('candidate', candidate)]:
            subprocess.run(['pdftoppm', '-r', str(dpi), '-png', str(pdf), str(tmp / name)],
                           check=True, capture_output=True)
        images = {n: sorted(tmp.glob(n + '-*.png')) for n in ['baseline', 'candidate']}
        assert images['baseline'] and len(images['baseline']) == len(images['candidate'])
        pages = []
        for a, b in zip(images['baseline'], images['candidate']):
            with Image.open(a) as left, Image.open(b) as right:
                assert left.size == right.size, (a.name, left.size, right.size)
                difference = ImageChops.difference(left.convert('RGB'), right.convert('RGB'))
                pixels = difference.tobytes() if difference.getbbox() else b''
                changed = sum(any(pixels[i:i + 3]) for i in range(0, len(pixels), 3))
                pages.append({'page': int(a.stem.rsplit('-', 1)[1]), 'changed_pixels': changed})
                if changed:
                    output.mkdir(parents=True, exist_ok=True)
                    difference.save(output / (a.stem + '-difference.png'))
        return {'dpi': dpi, 'pages': pages, 'identical': all(p['changed_pixels'] == 0 for p in pages)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('benchmark_dir', type=Path)
    parser.add_argument('--compatibility-dir', type=Path)
    parser.add_argument('--visibility-dir', type=Path)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args()
    results = json.loads((args.benchmark_dir / 'results.json').read_text())
    report = {'cases': {}}
    for name in results['cases']:
        run = args.benchmark_dir / name
        report['cases'][name] = compare(run / 'baseline/0/benchmark.pdf',
                                       run / 'candidate/0/benchmark.pdf', 90,
                                       args.report.parent / 'differences' / name)
        print(name, report['cases'][name]['identical'], flush=True)
    if args.compatibility_dir:
        report['cases']['compatibility'] = compare(
            args.compatibility_dir / 'baseline/compilation-compatibility.pdf',
            args.compatibility_dir / 'candidate/compilation-compatibility.pdf', 144,
            args.report.parent / 'differences/compatibility')
    if args.visibility_dir:
        report['cases']['visibility'] = compare(
            args.visibility_dir / 'baseline/external-momentum-visibility.pdf',
            args.visibility_dir / 'candidate/external-momentum-visibility.pdf', 144,
            args.report.parent / 'differences/visibility')
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + '\n')
    assert all(v['identical'] for v in report['cases'].values()), 'Rendered output changed; see report/differences'


if __name__ == '__main__':
    main()
