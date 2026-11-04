#!/usr/bin/env python3
"""Check actual rendered triangle contact, counts, fill, and legacy controls."""
import argparse
import json
from math import hypot
from pathlib import Path

from pypdf import PdfReader
from pypdf.generic import ContentStream

# Graph endpoint counts, not counts of helper invocations. Six diagrams/page.
EXPECTED_TRIANGLES = [12] * 5 + [36] + [12] * 3 + [24] * 3 + [48, 48, 12] + [36] * 4 + [24, 36, 36, 12, 9, 12, 24]
EXPECTED_DOTS = [12] * 5 + [24] + [12] * 6 + [24, 24, 12] + [18] * 4 + [12, 12, 24, 12, 12, 12, 18]


def multiply(t, u):
    a, b, c, d, e, f = t
    g, h, i, j, k, l = u
    return (a*g+c*h, b*g+d*h, a*i+c*j, b*i+d*j, a*k+c*l+e, b*k+d*l+f)


def inspect(pdf):
    reader = PdfReader(pdf)
    reports = []
    for page_number, page in enumerate(reader.pages, 1):
        state = {'ctm': (1, 0, 0, 1, 0, 0), 'stroke': (0, 0, 0), 'fill': (0, 0, 0), 'width': 1.0}
        stack, points, triangles, dots = [], [], [], []
        curved = False

        def transform(x, y):
            a, b, c, d, e, f = state['ctm']
            return (a*x+c*y+e, b*x+d*y+f)

        for args, op in ContentStream(page.get_contents(), reader).operations:
            numbers = [float(n) for n in args] if op in (
                b'cm', b'm', b'l', b'c', b'RG', b'rg', b'G', b'g', b'k', b'K', b'w') else []
            if op == b'q':
                stack.append(state.copy())
            elif op == b'Q':
                state = stack.pop()
            elif op == b'cm':
                state['ctm'] = multiply(state['ctm'], numbers)
            elif op == b'w':
                state['width'] = numbers[0]
            elif op in (b'k', b'K'):
                c, m, y, k = numbers
                state['stroke' if op == b'K' else 'fill'] = (
                    1-min(1, c+k), 1-min(1, m+k), 1-min(1, y+k))
            elif op in (b'RG', b'rg'):
                state['stroke' if op == b'RG' else 'fill'] = tuple(numbers)
            elif op in (b'G', b'g'):
                state['stroke' if op == b'G' else 'fill'] = (numbers[0],)*3
            elif op in (b'm', b'l'):
                points.append(transform(*numbers))
            elif op == b'c':
                curved = True
                points.extend(transform(numbers[i], numbers[i+1]) for i in (0, 2, 4))
            elif op in (b'S', b's', b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*', b'n'):
                unique = []
                for p in points:
                    if not any(hypot(p[0]-q[0], p[1]-q[1]) < 0.001 for q in unique):
                        unique.append(p)
                if not curved and len(unique) == 3 and max(state['stroke']) > 0.1:
                    if min(state['fill']) < 0.99:
                        raise ValueError(f'Page {page_number}: triangle lost white fill')
                    half_outline = state['width'] * hypot(*state['ctm'][:2]) / 2
                    triangles.append((unique, state['stroke'], half_outline))
                if curved and points and op in (b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*') and max(state['fill']) < 0.1:
                    xs, ys = zip(*points)
                    width, height = max(xs)-min(xs), max(ys)-min(ys)
                    if abs(width-height) < 0.01 and 1 < width < 15:
                        half_outline = state['width'] * hypot(*state['ctm'][:2]) / 2
                        dots.append(((min(xs)+max(xs))/2, (min(ys)+max(ys))/2, width/2, half_outline))
                points, curved = [], False

        gaps, visible_gaps = [], []
        for vertices, color, triangle_outline in triangles:
            # The tip is the triangle vertex nearest a dot boundary. Other
            # corners stay further inside the edge in these isolated cases.
            distances = [(hypot(px-x, py-y)-radius, triangle_outline+dot_outline)
                         for px, py in vertices for x, y, radius, dot_outline in dots]
            gap, outlines = min(distances, key=lambda pair: abs(pair[0]))
            gaps.append(gap)
            visible_gaps.append(gap-outlines)
        reports.append({'page': page_number, 'triangles': len(triangles), 'dots': len(dots),
                        'gaps_pt': gaps, 'visible_gaps_pt': visible_gaps,
                        'colors': [c for _, c, _ in triangles]})
    return reports


def validate(reports, baseline=None):
    if len(reports) != len(EXPECTED_TRIANGLES):
        raise ValueError('Expected the complete 26-page integrated diagnostic')
    for i, report in enumerate(reports):
        if (report['triangles'], report['dots']) != (EXPECTED_TRIANGLES[i], EXPECTED_DOTS[i]):
            raise ValueError(f'Page {i+1}: unexpected triangle/dot count: {report}')
        # Last page's lower row deliberately exercises the legacy distance
        # and generic add-on; it must match baseline, not automatic contact.
        count = 4 if i == 23 else 8 if i == 24 else len(report['gaps_pt'])
        automatic = report['gaps_pt'][:count]
        visible = report['visible_gaps_pt'][:count]
        # Measure both visible stroke outlines from PDF w/cm operators.
        # Managed markers deliberately retain a 0.25pt tip clearance; accepting
        # a real ink gap is still a failure. Reject deeply buried tips too.
        if any(gap < -0.21 for gap in automatic) or any(gap > 0.02 for gap in visible):
            raise ValueError(f'Page {i+1}: visible endpoint gap/overlap: {automatic}; ink gaps: {visible}')
    colors = reports[22]['colors']
    if not all(c[2] > c[0] and c[2] > c[1] for c in colors[6:10]):
        raise ValueError('Blue style-order controls lost their inherited color')
    if baseline:
        if len(baseline) != 24:
            raise ValueError('Expected the archived 24-page pre-M01 baseline')
        old, new = baseline[23]['gaps_pt'][4:], reports[23]['gaps_pt'][4:]
        if len(old) != 5 or any(abs(a-b) > 0.001 for a, b in zip(old, new)):
            raise ValueError('Explicit legacy-distance / generic-arrow placement changed')
        managed_legacy = reports[24]['gaps_pt'][8:]
        if any(abs(a-b) > 0.001 for a, b in zip(old[:4], managed_legacy)):
            raise ValueError('Managed legacy override does not match the raw legacy control')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--baseline', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reports = inspect(args.pdf)
    baseline = inspect(args.baseline) if args.baseline else None
    validate(reports, baseline)
    if args.report:
        args.report.write_text(json.dumps(reports, indent=2)+'\n')
    gaps = [g for i, r in enumerate(reports) for g in r['gaps_pt'][:(4 if i == 23 else 8 if i == 24 else len(r['gaps_pt']))]]
    visible = [g for i, r in enumerate(reports) for g in r['visible_gaps_pt'][:(4 if i == 23 else 8 if i == 24 else len(r['gaps_pt']))]]
    print(f'PASS: {len(reports)} pages; {sum(r["triangles"] for r in reports)} endpoint triangles; '
          f'{len(gaps)} automatic contacts; maximum circle-path gap {max(gaps):.4f} PDF pt; '
          f'maximum visible ink gap {max(visible):.4f} PDF pt')
    if baseline:
        print('PASS: raw and managed legacy overrides and the generic open-arrow add-on retain baseline placement')


if __name__ == '__main__':
    main()
