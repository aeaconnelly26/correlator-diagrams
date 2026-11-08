#!/usr/bin/env python3
"""Reject unsupported contact bubble hosts and degenerate requests explicitly."""
from pathlib import Path
import os
import subprocess
import tempfile

root = Path(__file__).resolve().parents[3]
cases = [
 ('insertion-slot=5', 'Contact bubble requires insertion-slot'),
 ('insertion-slot=0', 'Contact bubble requires insertion-slot'),
 ('insertion-slot={1,2}', 'Contact bubble requires insertion-slot'),
 ('contact-pairing=horizontal', 'Contact bubble requires contact-pairing'),
 ('contact-pairing=vertical', 'Contact bubble requires contact-pairing'),
 ('insertion-position=0', 'Contact bubble does not fit'),
 ('insertion-position=1', 'Contact bubble does not fit'),
 ('insertion-scale=0', 'Contact bubble insertion-scale must be positive'),
 ('insertion-scale=-1', 'Contact bubble insertion-scale must be positive'),
 ('insertion-scale=5', 'Contact bubble does not fit'),
 ('bubble-vertex-span=0', 'Contact bubble bubble-vertex-span must be positive'),
 ('bubble-vertex-span=-1', 'Contact bubble bubble-vertex-span must be positive'),
]
with tempfile.TemporaryDirectory(prefix='contact-bubble-errors-') as temp:
    folder = Path(temp)
    env = dict(os.environ, TEXINPUTS=str(root)+'//:')
    for n,(options, message) in enumerate(cases):
        source = folder / f'case{n}.tex'
        source.write_text(r'\documentclass{article}\usepackage{feynman-fun}\begin{document}'
                          +r'\FourPointCorr[insertion=bubble,'+options+r']\end{document}')
        result = subprocess.run(['pdflatex','-interaction=batchmode','-halt-on-error',source.name],
                                cwd=folder, env=env, capture_output=True)
        log = source.with_suffix('.log').read_text()
        assert result.returncode != 0 and message in log, (options,log[-2500:])
print(f'PASS M08a: {len(cases)} invalid contact-bubble requests produce explicit errors')
