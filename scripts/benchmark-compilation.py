#!/usr/bin/env python3
"""Serial, repeatable pdfLaTeX workloads; keep PDFs for baseline comparisons."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import statistics
import subprocess
import time

ROOT = Path(__file__).resolve().parent.parent


def document(body='', package=True, preamble=''):
    return (r'\documentclass{article}' + '\n'
            + (r'\usepackage{amsmath,feynman-fun}' if package else '') + '\n'
            + preamble + '\n' + r'\begin{document}' + '\n'
            + (body or 'Loading benchmark.') + '\n' + r'\end{document}' + '\n')


def repeat(call, n):
    return '\n'.join(r'\[' + call + r'\]' for _ in range(n))


def workloads():
    decorated = r'line={ewboson,endcapp},momentum-labels={q_1,q_2,q_3,q_4}'
    mixed = [
        r'\BoxLoopCorr[' + decorated + r',box-top-line={ewboson,circ=W}]',
        r'\CrossedVertexCorr[' + decorated + r',triangle-contact-internal-lines={ewboson,{proca,pink},ewboson}]',
        r'\TTreeChannelCorr[insertion=bubble,insertion-slot=1,' + decorated + ']',
        r'\STreeChannelCorr[insertion=seagull,insertion-slot=3,' + decorated + ']',
        r'\TTreeChannelCorr[insertion=triangle,' + decorated + ']',
    ]
    return {
        'empty': (document(package=False), 0),
        'load': (document(), 0),
        'single': (document(repeat(r'\FourPointCorr[show-momenta=false,line=plain]', 1)), 1),
        'simple': (document(repeat(r'\FourPointCorr[show-momenta=false,line=plain]', 40)), 40),
        'three-point': (document(repeat(r'\ThreePointCorr', 20)), 20),
        'mixed': (document('\n'.join(repeat(c, 4) for c in mixed)), 20),
        'indexed': (document(repeat(
            r'\BoxLoopCorr[show-momenta=false,line=plain,'
            r'box-propagator-left-indices={a,b,c,d,e,f,g,h},'
            r'box-propagator-right-indices={i,j,k,l,m,n,o,p}]', 20)), 20),
        'atlas': ((ROOT / 'docs/diagram-inventory/inventory.tex').read_text(), 150),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-dir', type=Path, default=ROOT)
    parser.add_argument('--baseline-dir', type=Path,
                        help='Alternate baseline/candidate order for paired comparisons')
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--repeats', type=int, default=5)
    parser.add_argument('--warmups', type=int, default=1)
    parser.add_argument('--cases', nargs='+')
    args = parser.parse_args()
    if args.repeats < 1 or args.warmups < 0:
        parser.error('repeats must be positive; warmups must be nonnegative')
    package_dir = args.package_dir.resolve()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=True)
    if (output / 'results.json').exists():
        parser.error('output-dir already contains results; choose a fresh directory')
    variants = {'candidate': package_dir}
    if args.baseline_dir:
        variants = {'baseline': args.baseline_dir.resolve(), **variants}
    # Give both variants an identical, flat lookup environment. Recursively
    # searching a working repo versus a one-file baseline distorts load timings.
    isolated = {}
    for name, path in variants.items():
        isolated[name] = output / 'packages' / name
        isolated[name].mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path / 'feynman-fun.sty', isolated[name] / 'feynman-fun.sty')
    engine = subprocess.check_output(['pdflatex', '--version'], text=True).splitlines()[0]
    revision = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip()
    report = {
        'engine': engine, 'platform': platform.platform(), 'revision': revision,
        'packages': {name: {'directory': str(path), 'sha256': hashlib.sha256(
            (path / 'feynman-fun.sty').read_bytes()).hexdigest()} for name, path in variants.items()},
        'warmups': args.warmups, 'repeats': args.repeats, 'cases': {},
        'method': 'Serial fresh-output-directory runs; warmups excluded; one pdflatex pass per run; alternate variant order each repetition.',
    }
    cases = workloads()
    for name in args.cases or cases:
        source, count = cases[name]
        samples = {variant: [] for variant in variants}
        for i in range(args.warmups + args.repeats):
            order = list(variants) if i % 2 == 0 else list(reversed(variants))
            for variant in order:
                run = output / name / variant / str(i)
                run.mkdir(parents=True, exist_ok=True)
                (run / 'benchmark.tex').write_text(source)
                env = dict(os.environ, TEXINPUTS=f'{isolated[variant]}:')
                command = ['pdflatex', '-interaction=batchmode', '-halt-on-error', 'benchmark.tex']
                before = resource.getrusage(resource.RUSAGE_CHILDREN)
                start = time.perf_counter()
                result = subprocess.run(command, cwd=run, env=env, capture_output=True, text=True)
                wall = time.perf_counter() - start
                after = resource.getrusage(resource.RUSAGE_CHILDREN)
                if result.returncode:
                    raise RuntimeError((run / 'benchmark.log').read_text()[-5000:])
                samples[variant].append({'wall_seconds': wall, 'user_seconds': after.ru_utime - before.ru_utime,
                                         'system_seconds': after.ru_stime - before.ru_stime,
                                         'warmup': i < args.warmups})
                print(f'{name} {variant} {i}: {wall:.3f}s' + (' warmup' if i < args.warmups else ''), flush=True)
        report['cases'][name] = {
            'diagrams': count, 'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
            'command': command, 'variants': {},
        }
        for variant, runs in samples.items():
            measured = runs[args.warmups:]
            report['cases'][name]['variants'][variant] = {
                'samples': runs,
                'median_wall_seconds': statistics.median(s['wall_seconds'] for s in measured),
                'min_wall_seconds': min(s['wall_seconds'] for s in measured),
                'max_wall_seconds': max(s['wall_seconds'] for s in measured),
                'median_user_seconds': statistics.median(s['user_seconds'] for s in measured),
            }
        (output / 'results.json').write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()
