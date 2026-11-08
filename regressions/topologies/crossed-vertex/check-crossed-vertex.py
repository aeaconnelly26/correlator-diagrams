#!/usr/bin/env python3
"""Check rendered half-moon graphs, actual marker contact and style isolation."""
import argparse
from collections import Counter
import importlib.util
import json
from math import hypot
import os
from pathlib import Path
import subprocess
import sys
import tempfile

from pypdf import PdfReader

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location('seagulls', HERE.parent/'insertion/check-contact-seagulls.py')
helpers = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helpers)


def distance(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])


def graphs(page, reader, scales=(1, 1), frames=((2.1, 2.1), (2.1, 2.1)), gaps=(.04, .04), row=None):
    paths = [(ops, p) for op, ops, p, _ in helpers.paths(page, reader) if op in (b'S', b's')]
    dots = helpers.species.inspect_circles(page, reader)[1]
    if row:
        ys = sorted(d[1] for d in dots)
        mid = (ys[5]+ys[6])/2
        select = lambda p:(p[1] > mid) == (row == 'top')
        dots = [d for d in dots if select(d)]
        paths = [(ops,p) for ops,p in paths if select(p[0])]
    assert len(dots) == 6 and len(paths) == 16, (len(dots), len(paths))
    ordered = sorted(dots, key=lambda d:d[0])
    centers = [sorted(group, key=lambda d:d[0])[1][:2] for group in (ordered[:3], ordered[3:])]
    reports = []
    for cell, q in enumerate(centers):
        local = [(ops, p) for ops, p in paths if min(range(2), key=lambda i:distance(p[0], centers[i])) == cell]
        assert len(local) == 8
        arcs = [p for ops, p in local if b'c' in ops]
        assert len(arcs) == 1 and len(arcs[0]) == 3, 'Half-moon must be one continuous two-cubic semicircle'
        arc = arcs[0]
        radius = distance(arc[0], q)
        assert abs(radius-distance(arc[-1], q)) < .03
        assert abs(radius-distance(arc[1], q)) < .03
        assert distance(tuple((arc[0][i]+arc[-1][i])/2 for i in (0,1)), q) < .03
        assert arc[1][1] > q[1] and (arc[1][0] > q[0]) == (cell == 0)
        nodes = []
        def index(p):
            for i, old in enumerate(nodes):
                if distance(p, old) < .03: return i
            nodes.append(p)
            return len(nodes)-1
        edges = [(index(p[0]), index(p[-1])) for _, p in local]
        degree = Counter(n for edge in edges for n in edge)
        assert sorted(degree.values()) == [1]*6 + [3,3,4]
        quartic = next(n for n in degree if degree[n] == 4)
        assert distance(nodes[quartic], q) < .03
        loose = [n for n in degree if degree[n] == 1]
        outer = sorted(loose, key=lambda n:distance(nodes[n], q), reverse=True)[:4]
        cuts = set(loose)-set(outer)
        assert len(cuts) == 2
        xmin, xmax = min(nodes[n][0] for n in outer), max(nodes[n][0] for n in outer)
        ymin, ymax = min(nodes[n][1] for n in outer), max(nodes[n][1] for n in outer)
        unit = .8*72/2.54*scales[cell]
        assert abs(xmax-xmin-2*frames[cell][0]*unit) < .04
        assert abs(ymax-ymin-2*frames[cell][1]*unit) < .04
        corners = [min(outer, key=lambda n:distance(nodes[n], p)) for p in ((xmin,ymax),(xmin,ymin),(xmax,ymax),(xmax,ymin))]
        neighbors = [b if a == n else a for n in cuts for a,b in edges if n in (a,b)]
        crossed_slot = 3 if cell == 0 else 1
        assert set(neighbors) == {quartic, corners[crossed_slot-1]}
        for cut in cuts:
            assert abs(abs(distance(nodes[cut],q)-radius)-gaps[cell]*distance(nodes[corners[crossed_slot-1]],q)) < .04
        logical = [(a,b) for a,b in edges if not ({a,b} & cuts)] + [tuple(neighbors)]
        valence = Counter(n for edge in logical for n in edge)
        assert len(logical) == 7 and sorted(valence.values()) == [1]*4+[3,3,4]
        assert len(logical)-len(valence)+1 == 1
        pair = [i+1 for i,n in enumerate(corners) if any({a,b} == {n,quartic} for a,b in logical)]
        assert pair == ([2,3] if cell == 0 else [1,4]), pair
        # Independent collinearity test against the actual fixed outer corners.
        cubic_slots = (1,4) if cell == 0 else (2,3)
        for slot in cubic_slots:
            endpoint = corners[slot-1]
            cubic = next(b if a == endpoint else a for a,b in logical if endpoint in (a,b))
            vx,vy = nodes[endpoint][0]-q[0], nodes[endpoint][1]-q[1]
            ax,ay = nodes[cubic][0]-q[0], nodes[cubic][1]-q[1]
            assert abs(ax*vy-ay*vx)/hypot(vx,vy) < .03, 'W edge kinked away from outer diagonal'
        reports.append({'orientation':'right' if cell == 0 else 'left','logical_edges':7,
                        'interaction_valences':[4,3,3],'cycle_rank':1,'quartic_external_pair':pair,
                        'crossed_external_slot':crossed_slot,'crossing_is_vertex':False,
                        'half_moon_radius_pdf_pt':radius,'outer_frame_pdf_pt':[xmax-xmin,ymax-ymin]})
    return reports


def rejected_options():
    cases = [('crossed-vertex-orientation=top', "Choice 'top' unknown"),
             ('crossed-vertex-crossing-gap=.9', 'Invalid crossed vertex'),
             ('triangle-contact-xspan=-1', 'Invalid crossed vertex'),
             ('triangle-contact-external-xspan=.5', 'Invalid crossed vertex')]
    with tempfile.TemporaryDirectory(prefix='feynmanfun-cv-errors-') as folder:
        build = Path(folder)
        for i,(options, expected) in enumerate(cases):
            for array in (False,True):
                body = r'\CrossedVertexCorr['+options+']'
                if array: body = r'\[\begin{array}{c}'+body+r'\end{array}\]'
                source = build/f'bad-{i}-{int(array)}.tex'
                source.write_text(r'\documentclass{article}\usepackage{feynman-fun}\begin{document}'+body+r'\end{document}')
                result = subprocess.run(['pdflatex','-interaction=batchmode','-halt-on-error',source.name],cwd=build,
                                        env=dict(os.environ,TEXINPUTS=str(ROOT)+'//:'),stdout=subprocess.DEVNULL)
                log = source.with_suffix('.log').read_text().replace('\n','')
                assert result.returncode != 0 and expected in log, (options, log[-1000:])
    return len(cases)*2


def annotation_isolation():
    """Compare actual PDF strokes after changing one public momentum control."""
    base = 'field={},leg-labels={,,,},central={},blob=false,external-vertices=false,center-vertex=true,line=plain,triangle-contact-momentum-layout=side,triangle-contact-internal-momenta={a,b,c}'
    cases = [''] + [f'triangle-contact-momentum-{slot}={{offset=16pt}}' for slot in range(1,8)]
    cases += ['triangle-contact-momentum-6={label-offset=10pt,label-xshift=2pt}',
              'triangle-contact-internal-momentum-directions={none,none,none},external-momentum-hide={1,2,3,4}']
    reports = []
    with tempfile.TemporaryDirectory(prefix='feynmanfun-cv-momenta-') as folder:
        build = Path(folder)
        for orientation in ('right','left'):
            source = build/f'{orientation}.tex'
            source.write_text(r'\documentclass{article}\usepackage{feynman-fun}\begin{document}' + '\n'.join(
                (r'\newpage' if i else '') + r'\[\CrossedVertexCorr['+base+',crossed-vertex-orientation='+orientation+','+options+r']\]'
                for i, options in enumerate(cases)) + r'\end{document}')
            subprocess.run(['pdflatex','-interaction=batchmode','-halt-on-error',source.name],cwd=build,
                           env=dict(os.environ,TEXINPUTS=str(ROOT)+'//:'),stdout=subprocess.DEVNULL,check=True)
            reader = PdfReader(source.with_suffix('.pdf'))
            def signature(page):
                dots = helpers.species.inspect_circles(page,reader)[1]
                q = sorted(dots,key=lambda d:d[0])[1]
                return [(ops,[(x-q[0],y-q[1]) for x,y in p]) for op,ops,p,_ in helpers.paths(page,reader) if op in (b'S',b's')]
            baseline = signature(reader.pages[0])
            assert len(baseline) == 15
            def equal(a,b):
                return a[0] == b[0] and len(a[1]) == len(b[1]) and all(distance(p,q)<.035 for p,q in zip(a[1],b[1]))
            for slot in range(1,8):
                current = signature(reader.pages[slot])
                unmatched = [p for p in current if not any(equal(p,q) for q in baseline)]
                assert len(current) == len(baseline) and len(unmatched) == 1, (orientation,slot,len(unmatched))
            shifted = signature(reader.pages[8])
            assert len(shifted) == 15 and all(any(equal(p,q) for q in baseline) for p in shifted), 'Label-only movement changed an arrow'
            assert len(signature(reader.pages[9])) == 8, 'Hidden momenta left strokes behind'
            reports.append({'orientation':orientation,'independent_momentum_slots':7,'label_only_strokes_unchanged':True,'all_momenta_hidden':True})
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path)
    parser.add_argument('--report',type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 9
    topology = graphs(reader.pages[0],reader)
    graphs(reader.pages[4],reader, scales=(.72,1.2),row='top')
    graphs(reader.pages[4],reader,row='bottom')
    graphs(reader.pages[7],reader,frames=((2.4,1.9),(1.9,2.4)),gaps=(.04,.06),row='bottom')
    contacts = helpers.contact.inspect(args.pdf)
    for page,count,dots in ((2,4,6),(3,12,6),(6,16,12),(8,10,12)):
        r = contacts[page-1]
        assert r['triangles'] == count and r['dots'] == dots, r
        touching = [(g,v) for g,v in zip(r['gaps_pt'],r['visible_gaps_pt']) if g < 1]
        assert len(touching) == (8 if page == 6 else count), r
        assert min(g for g,v in touching) >= -.21 and max(v for g,v in touching) <= .02, r
    rings,dots = helpers.species.inspect_circles(reader.pages[1],reader)
    assert len(rings) == 4 and len(dots) == 6
    for ring,color in rings:
        assert abs(ring[2]-4.8*72/72.27) < .03
        nearest = sorted(dots,key=lambda d:distance(ring,d))[:2]
        midpoint = tuple((nearest[0][i]+nearest[1][i])/2 for i in (0,1))
        assert distance(ring,midpoint) < .04, 'W circle does not follow its actual diagonal segment'
    # All fourteen indexed ends survive, including f/F on the semicircle.
    text = reader.pages[8].extract_text()
    assert all(letter in text for letter in 'abcdefgABCDEFG')
    report = {'graphs':topology,'new_marker_contacts':34,'styled_W_circles':4,
              'rejected_options':rejected_options(),'annotation_isolation':annotation_isolation(),'pages':9}
    if args.report: args.report.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS crossed vertex: both 7-edge/4-3-3 graphs; aligned diagonals; 34 marker contacts; W circles; 8 invalid cases')


if __name__ == '__main__':
    main()
