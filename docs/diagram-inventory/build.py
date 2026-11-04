#!/usr/bin/env python3
"""Rebuild the documentation atlas using only existing public package macros."""
import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def tex(text):
    return ''.join({'&': r'\&', '%': r'\%', '_': r'\_', '#': r'\#',
                    '{': r'\{', '}': r'\}'}.get(c, c) for c in text)


def render_sources(catalog):
    head = r'''% Generated from catalog.json by build.py; uses the public package macros.
\documentclass[10pt,letterpaper]{article}
\usepackage[margin=0.62in]{geometry}
\usepackage{amsmath,xcolor,graphicx,adjustbox,fancyhdr}
\usepackage{feynman-fun}
\definecolor{atlasink}{HTML}{20394B}
\pagestyle{fancy}\fancyhf{}
\fancyfoot[L]{\scriptsize Feynman Fun | baseline 0dbf733 | 2026-11-03}
\fancyfoot[R]{\scriptsize\thepage}
\renewcommand{\headrulewidth}{0pt}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\newcommand{\atlaspage}[3]{%
  {\sffamily\color{atlasink}\small CURRENT CAPABILITIES / #1\par}
  \vspace{5pt}{\sffamily\bfseries\Large #2\par}
  \vspace{5pt}{\small #3\par}\vspace{13pt}}
\newcommand{\atlascell}[5]{%
  \begin{minipage}[t][2.38in][t]{0.475\linewidth}
  {\sffamily\bfseries\color{atlasink}#1\par}
  \vspace{3pt}{\ttfamily\footnotesize\detokenize{#2}\par}
  \vspace{4pt}\begin{minipage}[c][1.57in][c]{\linewidth}\centering
  \begin{adjustbox}{max width=\linewidth,max totalheight=1.52in}#3\end{adjustbox}
  \end{minipage}\par
  {\footnotesize #4\par}\vspace{2pt}
  {\scriptsize\color{black!65}#5\par}
  \end{minipage}}
\begin{document}
'''
    head = head.replace('baseline 0dbf733', 'baseline ' + tex(catalog['baseline']))
    head = head.replace('2026-11-03', tex(catalog['date']))
    chunks = [head]
    recipes = ['# Current diagram recipes', '',
               'Generated from `catalog.json`. These are existing capabilities, not proposed APIs.', '',
               'Baseline: `' + catalog['baseline'] + '`, audited ' + catalog['date'] + '. Atlas: [PDF](inventory.pdf).', '',
               'Use `\\usepackage{feynman-fun}`. Paste a recipe inside `\\[ ... \\]`.', '',
               'The main atlas hides annotations. The appendix demonstrates selected annotation and style features.', '']
    for pi, page in enumerate(catalog['pages']):
        if pi:
            chunks.append(r'\newpage' + '\n')
        chunks.append('\\atlaspage{' + tex(page['section']) + '}{' + tex(page['title']) + '}{' + tex(page['subtitle']) + '}\n')
        recipes += ['## ' + page['title'], '']
        for i, entry in enumerate(page['entries']):
            options = [o for o in catalog['base_options']
                       if o not in entry.get('omit_base_options', [])] + entry['options']
            call = '\\' + entry['macro'] + '[\n  ' + ',\n  '.join(options) + '\n]'
            chunks.append('\\atlascell{' + tex(entry['id'] + '  ' + entry['title']) + '}{\\' + entry['macro'] + '}{%\n' + call + '\n}{' + tex(entry['description']) + '}{' + tex(entry['limitation']) + '}')
            if i % 2 == 0 and i + 1 < len(page['entries']):
                chunks.append(r'\hfill' + '\n')
            else:
                chunks.append('\\par\\vspace{4pt}\n')
            recipes += ['### ' + entry['id'] + ' - ' + entry['title'], '',
                        entry['description'], '', '**Limit:** ' + entry['limitation'], '',
                        '```tex', call, '```', '']
    chunks.append('\\end{document}\n')
    (HERE / 'inventory.tex').write_text(''.join(chunks))
    (HERE / 'recipes.md').write_text('\n'.join(recipes))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sources-only', action='store_true')
    args = parser.parse_args()
    catalog = json.loads((HERE / 'catalog.json').read_text())
    ids = [e['id'] for p in catalog['pages'] for e in p['entries']]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate inventory ID')
    render_sources(catalog)
    if args.sources_only:
        return
    env = os.environ.copy()
    env['TEXINPUTS'] = str(ROOT) + '//:' + env.get('TEXINPUTS', '')
    with tempfile.TemporaryDirectory(prefix='feynmanfun-atlas-') as tmp:
        cmd = ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
               '-output-directory=' + tmp, 'inventory.tex']
        for _ in range(2):
            result = subprocess.run(cmd, cwd=HERE, env=env, capture_output=True, text=True)
            if result.returncode:
                raise RuntimeError(result.stdout[-6000:])
        log = (Path(tmp) / 'inventory.log').read_text()
        issues = [line for line in log.splitlines() if 'Overfull' in line or 'Underfull' in line]
        if issues:
            print('\n'.join(issues))
        shutil.copyfile(Path(tmp) / 'inventory.pdf', HERE / 'inventory.pdf')
    print(f'Built {len(ids)} current examples on {len(catalog["pages"])} pages: {HERE / "inventory.pdf"}')


if __name__ == '__main__':
    main()
