#!/usr/bin/env python3
"""Measure inclusive helper time separately from uninstrumented benchmarks."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('benchmark', HERE / 'benchmark-compilation.py')
benchmark = importlib.util.module_from_spec(spec)
spec.loader.exec_module(benchmark)
HELPERS = [
    'configurestyles', 'preparelists', 'resetchanneldefaults', 'resetloopchanneldefaults',
    'resetboxdefaults', 'resetcrossboxdefaults', 'resethalfboxdefaults',
    'resetflatcontactdefaults', 'resettrianglecontactdefaults', 'resetinsertedbubbledefaults',
    'resetseagullinsertiondefaults', 'resetinsertiondefaults', 'resolvechanneldefaults',
    'resolveloopchanneldefaults', 'getlistitemorblank', 'selectmomentumslot',
    'stripendcapstyles', 'scalarstyletoend', 'semanticstyleinternal',
    'drawmomentumrangeoffset', 'drawmomentumrangeoffsetout',
]


def instrumentation():
    lines = [r'\makeatletter']
    for n in HELPERS:
        lines += [r'\newcount\profile' + n + 'Ticks',
                  r'\newcount\profile' + n + 'Calls',
                  r'\pretocmd{\corr@' + n + r'}{\edef\profile' + n
                  + r'Start{\number\pdfelapsedtime}\global\advance\profile' + n
                  + r'Calls by 1}{}{\errmessage{profile prefix failed}}',
                  r'\apptocmd{\corr@' + n + r'}{\global\advance\profile' + n
                  + r'Ticks by \numexpr\pdfelapsedtime-\profile' + n
                  + r'Start\relax}{}{\errmessage{profile suffix failed}}']
    lines += [r'\AtEndDocument{' + ''.join(
        r'\typeout{PROFILE ' + n + r' \the\profile' + n + r'Calls\space \the\profile'
        + n + 'Ticks}' for n in HELPERS) + '}', r'\makeatother']
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--package-dir', type=Path, default=benchmark.ROOT)
    parser.add_argument('--output-dir', type=Path, required=True)
    parser.add_argument('--cases', nargs='+', default=['mixed', 'indexed'])
    args = parser.parse_args()
    output = args.output_dir.resolve()
    if (output / 'profile.json').exists():
        parser.error('output-dir already contains a profile')
    output.mkdir(parents=True, exist_ok=True)
    env = dict(os.environ, TEXINPUTS=f'{args.package_dir.resolve()}:')
    report = {
        'method': 'Inclusive pdfelapsedtime ticks (1/65536 second); instrumented, not benchmark timing. Nested helper times must not be added together.',
        'engine': subprocess.check_output(['pdflatex', '--version'], text=True).splitlines()[0],
        'package_sha256': hashlib.sha256((args.package_dir / 'feynman-fun.sty').read_bytes()).hexdigest(),
        'cases': {},
    }
    for name in args.cases:
        source, _ = benchmark.workloads()[name]
        source = source.replace(r'\begin{document}', instrumentation() + r'\begin{document}', 1)
        run = output / name
        run.mkdir(exist_ok=True)
        (run / 'profile.tex').write_text(source)
        command = ['pdflatex', '-interaction=batchmode', '-halt-on-error', 'profile.tex']
        result = subprocess.run(command, cwd=run, env=env, capture_output=True, text=True)
        log = (run / 'profile.log').read_text()
        if result.returncode:
            raise RuntimeError(log[-5000:])
        rows = re.findall(r'^PROFILE (\w+) (\d+) (\d+)$', log, re.M)
        assert len(rows) == len(HELPERS)
        report['cases'][name] = {n: {'calls': int(c), 'ticks': int(t), 'seconds': int(t) / 65536}
                                for n, c, t in rows}
        print(name, report['cases'][name]['configurestyles'], flush=True)
    (output / 'profile.json').write_text(json.dumps(report, indent=2) + '\n')


if __name__ == '__main__':
    main()
