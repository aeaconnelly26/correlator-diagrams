#!/usr/bin/env python3
"""Require explicit failures for invalid external contact-seagull requests."""
import os
from pathlib import Path
import subprocess
import tempfile

root = Path(__file__).resolve().parents[3]
cases = [(key,'Contact seagull requires insertion-slot') for key in
         ('insertion-slot=0','insertion-slot=5','insertion-slot={1,2}')]
cases += [(key,'Contact seagull requires contact-pairing') for key in
          ('contact-pairing=horizontal','contact-pairing=vertical')]
cases += [(f'insertion-position={value}','Contact seagull position must be strictly') for value in (0,1,-.1,1.1)]
cases += [(f'{key}={value}','Contact seagull requires positive geometry') for key in
          ('insertion-scale','seagull-loop-size','seagull-loop-looseness') for value in (0,-1)]
cases += [('fourpoint-xspan=0,fourpoint-yspan=0','Contact seagull requires positive geometry')]
with tempfile.TemporaryDirectory(prefix='contact-seagull-errors-') as temp:
    folder = Path(temp)
    env = dict(os.environ,TEXINPUTS=str(root)+'//:')
    for i,(options,message) in enumerate(cases):
        source = folder/f'case{i}.tex'
        source.write_text(r'\documentclass{article}\usepackage{feynman-fun}\begin{document}'
                          +r'\FourPointCorr[insertion=seagull,'+options+r']\end{document}')
        result = subprocess.run(['pdflatex','-interaction=batchmode','-halt-on-error',source.name],
                                cwd=folder,env=env,capture_output=True)
        log = source.with_suffix('.log').read_text()
        assert result.returncode != 0 and message in log,(options,log[-2000:])
print(f'PASS M08b: {len(cases)} invalid contact-seagull requests produce explicit errors')
