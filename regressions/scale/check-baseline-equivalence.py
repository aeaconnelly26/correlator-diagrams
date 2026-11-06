#!/usr/bin/env python3
"""Compare the compact-scale checkpoint with its pre-rebase package."""
import argparse
from decimal import Decimal
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile

from PIL import Image

ROOT = Path(__file__).resolve().parents[2]


def digest(data):
    return hashlib.sha256(data).hexdigest()


def run(command, directory, env=None):
    result = subprocess.run(command, cwd=directory, env=env,
                            capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(f'{command[0]} failed:\n{result.stdout[-6000:]}\n{result.stderr[-2000:]}')
    return result.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-ref', default='ad9592b')
    parser.add_argument('--current-ref', default='97ecd10',
                        help='Post-rebase checkpoint; later geometry reviews intentionally differ')
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    old_package = run(['git', 'show', f'{args.baseline_ref}:feynman-fun.sty'], ROOT)
    new_package = run(['git', 'show', f'{args.current_ref}:feynman-fun.sty'], ROOT)
    new_source = (ROOT / 'docs/diagram-inventory/inventory.tex').read_text()
    old_source, count = re.subn(
        r'(?m)^([ \t]*)scale=([\d.]+)',
        lambda m: m[1] + 'scale=' + str(Decimal(m[2]) * Decimal('0.8')),
        new_source)
    assert count > 0, 'No public scale settings found in generated atlas'
    reports = []
    with tempfile.TemporaryDirectory(prefix='feynmanfun-scale-') as temporary:
        stages = []
        for name, package, source in [('before', old_package, old_source),
                                      ('after', new_package, new_source)]:
            stage = Path(temporary) / name
            stage.mkdir()
            (stage / 'feynman-fun.sty').write_text(package)
            (stage / 'inventory.tex').write_text(source)
            env = os.environ.copy()
            env['TEXINPUTS'] = f'{stage}:{ROOT}//:'
            for _ in range(2):
                run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', 'inventory.tex'], stage, env)
            run(['pdftoppm', '-scale-to', '1000', '-png', 'inventory.pdf', 'page'], stage)
            stages.append(sorted(stage.glob('page-*.png')))
        assert len(stages[0]) == len(stages[1]) > 0, 'Page count changed'
        for page, (old, new) in enumerate(zip(*stages), 1):
            with Image.open(old) as a, Image.open(new) as b:
                assert a.size == b.size and a.convert('RGB').tobytes() == b.convert('RGB').tobytes(), f'Page {page} changed'
                reports.append({'page': page, 'pixel_identical': True,
                                'size_px': list(a.size),
                                'rgb_sha256': digest(a.convert('RGB').tobytes())})
    report = {'baseline_ref': args.baseline_ref, 'current_ref': args.current_ref, 'coordinate_factor': 0.8,
              'rebased_scale_settings': count, 'identical_pages': len(reports),
              'old_package_sha256': digest(old_package.encode()),
              'new_package_sha256': digest(new_package.encode()),
              'current_atlas_source_sha256': digest(new_source.encode()),
              'pages': reports}
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + '\n')
    print(f'PASS scale equivalence: all {len(reports)} atlas pages pixel-identical at 1000px; {count} public scale settings rebased by 0.8')


if __name__ == '__main__':
    main()
