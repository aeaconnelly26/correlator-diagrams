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
\usepackage{amsmath,xcolor,graphicx,adjustbox,fancyhdr,pdfpages}
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
    chunks = [head]
    recipes = ['# Current diagram recipes', '',
               'Generated from `catalog.json`. These are existing capabilities, not proposed APIs.', '',
               'Baseline: `' + catalog['baseline'] + '`, audited 2026-11-03. Atlas: [PDF](inventory.pdf).', '',
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
    preview = catalog.get('branch_preview')
    if preview:
        chunks.append('\\includepdf[pages=-]{seagull-branch-examples.pdf}\n')
        recipes += ['## Unmerged branch: seagull examples', '',
                    '**Branch-only:** `' + preview['branch'] + '` at `' + preview['revision'] + '`.', '',
                    'These recipes require that revision. They are not supported by the current checkout.', '',
                    'See [branch integration](../planning/branch-integration.md) before using them.', '']
        for entry in preview['entries']:
            call = '\\' + entry['macro'] + '[\n  ' + ',\n  '.join(entry['options']) + '\n]'
            recipes += ['### ' + entry['id'] + ' - ' + entry['title'], '',
                        entry['description'], '', '**Limit:** ' + entry['limitation'], '',
                        '```tex', call, '```', '']
    chunks.append('\\end{document}\n')
    (HERE / 'inventory.tex').write_text(''.join(chunks))
    (HERE / 'recipes.md').write_text('\n'.join(recipes))
    if preview:
        # Build this page in isolation: its macros must not accidentally load
        # the current checkout's package. The complete atlas embeds the PDF.
        branch_head = head.replace('baseline ' + tex(catalog['baseline']),
                                   'unmerged seagull branch ' + preview['revision'][:7])
        branch_chunks = [branch_head, '\\setcounter{page}{8}\n',
            '\\atlaspage{08 / UNMERGED BRANCH}{Seagull insertion examples}{'
            'Rendered from ' + tex(preview['branch']) + ' at ' + preview['revision'][:7] +
            '. Not yet merged into main or the current checkout. Only t-tree external slot 1 is supported.}\n']
        for i, entry in enumerate(preview['entries']):
            call = '\\' + entry['macro'] + '[' + ','.join(entry['options']) + ']'
            branch_chunks.append('\\atlascell{' + tex(entry['id'] + '  ' + entry['title']) +
                '}{\\' + entry['macro'] + '}{' + call + '}{' + tex(entry['description']) +
                '}{' + tex(entry['limitation']) + '}' + ('\\hfill\n' if i == 0 else '\\par\n'))
        branch_chunks.append('\\end{document}\n')
        (HERE / 'seagull-branch-examples.tex').write_text(''.join(branch_chunks))


def compile_branch_preview(preview):
    with tempfile.TemporaryDirectory(prefix='feynmanfun-branch-atlas-') as tmp:
        source = subprocess.check_output(
            ['git', 'show', preview['revision'] + ':feynman-fun.sty'], cwd=ROOT)
        (Path(tmp) / 'feynman-fun.sty').write_bytes(source)
        env = os.environ.copy()
        env['TEXINPUTS'] = tmp + '//:' + str(ROOT) + '//:' + env.get('TEXINPUTS', '')
        result = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
            '-output-directory=' + tmp, str(HERE / 'seagull-branch-examples.tex')],
            cwd=tmp, env=env, capture_output=True, text=True)
        if result.returncode:
            raise RuntimeError(result.stdout[-6000:])
        shutil.copyfile(Path(tmp) / 'seagull-branch-examples.pdf', HERE / 'seagull-branch-examples.pdf')


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
    if catalog.get('branch_preview'):
        compile_branch_preview(catalog['branch_preview'])
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
    extra = len(catalog.get('branch_preview', {}).get('entries', []))
    print(f'Built {len(ids)} current examples plus {extra} unmerged-branch examples: {HERE / "inventory.pdf"}')


if __name__ == '__main__':
    main()
