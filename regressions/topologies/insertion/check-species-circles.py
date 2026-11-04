#!/usr/bin/env python3
"""Check species-circle placement, stem colors and clearance from interaction dots."""
import argparse
import importlib.util
import json
from math import hypot
from pathlib import Path
import sys

from pypdf import PdfReader
from pypdf.generic import ContentStream

sys.dont_write_bytecode = True
source = Path(__file__).resolve().parents[2] / 'propagators/proca-endpoints/check-endpoint-contact.py'
spec = importlib.util.spec_from_file_location('endpoint_contact', source)
contact = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contact)


def inspect_circles(page, reader):
    state = {'ctm': (1, 0, 0, 1, 0, 0), 'fill': (0, 0, 0),
             'stroke': (0, 0, 0), 'width': 1.0}
    stack, points, circles, dots = [], [], [], []
    curves = 0

    def transform(x, y):
        a, b, c, d, e, f = state['ctm']
        return (a*x+c*y+e, b*x+d*y+f)

    for args, op in ContentStream(page.get_contents(), reader).operations:
        if op == b'q':
            stack.append(state.copy())
        elif op == b'Q':
            state = stack.pop()
        elif op == b'cm':
            state['ctm'] = contact.multiply(state['ctm'], tuple(map(float, args)))
        elif op == b'w':
            state['width'] = float(args[0])
        elif op in (b'rg', b'RG'):
            state['fill' if op == b'rg' else 'stroke'] = tuple(map(float, args))
        elif op in (b'g', b'G'):
            state['fill' if op == b'g' else 'stroke'] = (float(args[0]),)*3
        elif op in (b'k', b'K'):
            c, m, y, k = map(float, args)
            state['fill' if op == b'k' else 'stroke'] = tuple(
                1-min(1, v+k) for v in (c, m, y))
        elif op in (b'm', b'l'):
            points.append(transform(*map(float, args)))
        elif op == b'c':
            curves += 1
            points.extend(transform(float(args[j]), float(args[j+1])) for j in (0, 2, 4))
        elif op in (b'S', b's', b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*', b'n'):
            if curves == 4 and points and op in (b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*'):
                xs, ys = zip(*points)
                width, height = max(xs)-min(xs), max(ys)-min(ys)
                if abs(width-height) < .02 and 1 < width < 15:
                    ring = ((max(xs)+min(xs))/2, (max(ys)+min(ys))/2, width/2,
                            state['width']*hypot(*state['ctm'][:2])/2)
                    if min(state['fill']) > .99:
                        circles.append((ring, state['stroke']))
                    elif max(state['fill']) < .01:
                        dots.append(ring)
            points, curves = [], 0
    return circles, dots


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 4, 'Expected the complete sixteen-example species gallery'
    reports = []
    for i, page in enumerate(reader.pages):
        circles, dots = inspect_circles(page, reader)
        assert len(circles) == [8, 12, 8, 12][i], f'Page {i+1}: missing/extra species circles'
        assert len(dots) == [12, 16, 12, 16][i], f'Page {i+1}: wrong interaction vertex count'
        pink = [ring for ring, color in circles if color[0] > .9 and color[1] < .1 and color[2] > .5]
        black = [ring for ring, color in circles if max(color) < .01]
        assert len(pink) == 4, f'Page {i+1}: expected one pink Z circle per central stem'
        assert len(pink)+len(black) == len(circles), 'Unexpected circle color'
        # Pink circles must sit halfway between two tree vertices, along the
        # horizontal S exchange or vertical T exchange; loops have no circles.
        for x, y, _, _ in pink:
            candidates = [(u, v) for u in dots for v in dots if u != v
                          and abs(u[0]-v[0] if i < 2 else u[1]-v[1]) < .03]
            assert any(hypot(x-(u[0]+v[0])/2, y-(u[1]+v[1])/2) < .03
                       for u, v in candidates), 'Pink Z circle left its central stem'
        gaps = [hypot(x-u, y-v)-r-s-o-p
                for (x, y, r, o), color in circles for u, v, s, p in dots]
        assert min(gaps) > .2, f'Page {i+1}: species circle crowds an interaction vertex'
        reports.append({'page': i+1, 'ew_circles': len(circles), 'pink_stem_circles': len(pink),
                        'black_w_circles': len(black),
                        'minimum_circle_vertex_ink_clearance_pdf_pt': min(gaps)})
    if args.report:
        args.report.write_text(json.dumps(reports, indent=2)+'\n')
    minimum = min(r['minimum_circle_vertex_ink_clearance_pdf_pt'] for r in reports)
    print(f'PASS: 40 EW species circles (16 pink Z stems, 24 black W); minimum circle/vertex ink clearance {minimum:.3f} PDF pt')


if __name__ == '__main__':
    main()
