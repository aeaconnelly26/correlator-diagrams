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


def inspect_circles(page, reader, *, include_triangles=False):
    state = {'ctm': (1, 0, 0, 1, 0, 0), 'fill': (0, 0, 0),
             'stroke': (0, 0, 0), 'width': 1.0}
    stack, points, circles, dots = [], [], [], []
    curves = 0
    triangles = []

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
            if curves == 0 and points and min(state['fill']) > .99 and max(state['stroke']) > .1:
                unique = []
                for point in points:
                    if not any(hypot(point[0]-other[0], point[1]-other[1]) < .001 for other in unique):
                        unique.append(point)
                if len(unique) == 3:
                    triangles.append((unique, state['width']*hypot(*state['ctm'][:2])/2))
            points, curves = [], 0
    return (circles, dots, triangles) if include_triangles else (circles, dots)


def optical_gaps(ring, dots, triangles):
    """Measure free space between the triangle ink and the tree-dot ink."""
    x, y, radius, outline = ring
    first, last = min(((u, v) for n, u in enumerate(dots) for v in dots[n+1:]),
                      key=lambda pair: hypot(x-(pair[0][0]+pair[1][0])/2,
                                             y-(pair[0][1]+pair[1][1])/2))

    def attached(dot):
        return [(points, width) for points, width in triangles
                if min(abs(hypot(px-dot[0], py-dot[1])-dot[2]) for px, py in points) < .6]

    if not attached(first):
        first, last = last, first
    arrows = attached(first)
    assert len(arrows) == 2 and not attached(last), 'Cannot identify the seagull and tree endpoints'
    length = hypot(last[0]-first[0], last[1]-first[1])
    axis = ((last[0]-first[0])/length, (last[1]-first[1])/length)
    arrow_edge = max((px-first[0])*axis[0]+(py-first[1])*axis[1]+width
                     for points, width in arrows for px, py in points)
    dot_edge = length-last[2]-last[3]
    center = (x-first[0])*axis[0]+(y-first[1])*axis[1]
    normal_error = abs((x-first[0])*axis[1]-(y-first[1])*axis[0])
    assert normal_error < .03, 'W circle left the host segment axis'
    return center-radius-outline-arrow_edge, dot_edge-center-radius-outline



def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 4, 'Expected the complete sixteen-example species gallery'
    endpoint_reports = contact.inspect(args.pdf)
    reports = []
    for i, page in enumerate(reader.pages):
        circles, dots, triangles = inspect_circles(page, reader, include_triangles=True)
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
        # Seagulls have an extended pink arrow footprint on the inner host
        # side. Center in the remaining visible gap; bubble hosts retain .5.
        if i in (0, 2):
            visible_gaps = [optical_gaps(ring, dots, triangles) for ring in black]
            assert len(visible_gaps) == 4 and min(min(pair) for pair in visible_gaps) > 0
            centered_errors = [abs(left-right)/2 for left, right in visible_gaps]
            assert max(centered_errors) < .05, f'Page {i+1}: W has unequal visible gaps'
            centering_reference = 'visible arrow-to-tree gap'
        else:
            midpoint_errors = [min(hypot(x-(u[0]+v[0])/2, y-(u[1]+v[1])/2)
                                   for n, u in enumerate(dots) for v in dots[n+1:])
                               for x, y, _, _ in black]
            centered_errors = [error for error in midpoint_errors if error < .03]
            assert len(centered_errors) == 4, f'Page {i+1}: inner bubble-host W left its midpoint'
            centering_reference = 'vertex-to-vertex midpoint'
            visible_gaps = []
        gaps = [hypot(x-u, y-v)-r-s-o-p
                for (x, y, r, o), color in circles for u, v, s, p in dots]
        assert min(gaps) > .2, f'Page {i+1}: species circle crowds an interaction vertex'
        endpoints = endpoint_reports[i]
        assert endpoints['triangles'] == 8, f'Page {i+1}: expected two endpoint arrows on each pink loop'
        assert min(endpoints['gaps_pt']) >= -.21 and max(endpoints['visible_gaps_pt']) <= .02, \
            f'Page {i+1}: pink endpoint arrows miss their interaction vertices'
        reports.append({'page': i+1, 'pink_endpoint_arrows': endpoints['triangles'],
                        'maximum_visible_endpoint_ink_gap_pdf_pt': max(endpoints['visible_gaps_pt']), 'ew_circles': len(circles), 'pink_stem_circles': len(pink),
                        'black_w_circles': len(black), 'centered_inner_w_circles': len(centered_errors),
                        'inner_w_centering_reference': centering_reference,
                        'maximum_inner_w_centering_error_pdf_pt': max(centered_errors),
                        'visible_arrow_circle_tree_gaps_pdf_pt': visible_gaps,
                        'minimum_circle_vertex_ink_clearance_pdf_pt': min(gaps)})
    if args.report:
        args.report.write_text(json.dumps(reports, indent=2)+'\n')
    minimum = min(r['minimum_circle_vertex_ink_clearance_pdf_pt'] for r in reports)
    print(f'PASS: 40 EW circles (16 pink Z stems, 24 black W); 32 contacting pink endpoint arrows; 8 optically centered seagull W circles; 8 midpoint bubble-host W circles; circle/vertex clearance {minimum:.3f} PDF pt')


if __name__ == '__main__':
    main()
