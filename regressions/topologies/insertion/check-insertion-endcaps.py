#!/usr/bin/env python3
"""Verify actual double-bar caps and wave contact on the insertion gallery."""
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
spec = importlib.util.spec_from_file_location('contact', source)
contact = importlib.util.module_from_spec(spec)
spec.loader.exec_module(contact)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 1
    matrix, stack, points, curves, bars, waves = (1,0,0,1,0,0), [], [], 0, [], []
    for values, op in ContentStream(reader.pages[0].get_contents(), reader).operations:
        if op == b'q': stack.append(matrix)
        elif op == b'Q': matrix = stack.pop()
        elif op == b'cm': matrix = contact.multiply(matrix, tuple(map(float, values)))
        elif op in (b'm', b'l', b'c'):
            x,y = map(float, values[-2:]); a,b,c,d,e,f = matrix
            points.append((a*x+c*y+e, b*x+d*y+f))
            if op == b'c': curves += 1
        elif op in (b'S',b's',b'f',b'F',b'f*',b'B',b'B*',b'b',b'b*',b'n'):
            if op in (b'S',b's') and len(points) >= 2:
                length = hypot(points[-1][0]-points[0][0], points[-1][1]-points[0][1])
                if not curves and len(points) == 2 and 2 < length < 14:
                    bars.append({'center': tuple((points[0][j]+points[1][j])/2 for j in (0,1)),
                                 'axis': tuple((points[1][j]-points[0][j])/length for j in (0,1))})
                elif curves and length > 5:
                    waves.extend([points[0], points[-1]])
            points, curves = [], 0
    assert len(bars) == 32, f'Expected eight cap bars per diagram, got {len(bars)}'
    remaining, caps, errors = set(range(32)), [], []
    while remaining:
        n = min(remaining); remaining.remove(n); first = bars[n]
        distance = lambda m: hypot(*(bars[m]['center'][j]-first['center'][j] for j in (0,1)))
        other = min(remaining, key=distance)
        assert 1 < distance(other) < 3, 'Cap bars are not paired'
        remaining.remove(other); second = bars[other]
        assert abs(sum(a*b for a,b in zip(first['axis'],second['axis']))) > .999, 'Cap bars not parallel'
        delta = tuple(second['center'][j]-first['center'][j] for j in (0,1))
        assert abs(sum(a*b for a,b in zip(delta,first['axis']))) < .03, 'Cap pair is not transverse to its leg'
        matches = [min(hypot(bar['center'][0]-x,bar['center'][1]-y) for x,y in waves)
                   for bar in (first,second)]
        assert min(matches) < .03 and max(matches) > 1, 'Wave does not end at exactly one inner cap bar'
        errors.append(min(matches)); caps.append((first if matches[0] > matches[1] else second)['center'])
    caps.sort(key=lambda p:-p[1])
    for row in (caps[:8],caps[8:]):
        row.sort()
        for group in (row[:4],row[4:]):
            xs,ys = zip(*group)
            assert abs(max(xs)-min(xs)-4.2*.8*72/2.54) < .03
            assert abs(max(ys)-min(ys)-4.2*.8*72/2.54) < .03
            assert all(any(hypot(x-u,y-v)<.03 for u,v in group)
                       for x in (min(xs),max(xs)) for y in (min(ys),max(ys))), 'A cap is on an internal endpoint'
    report = {'diagrams':4,'double_caps':16,'cap_bars':32,
              'maximum_wave_inner_bar_error_pdf_pt':max(errors)}
    if args.report: args.report.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS insertion caps PDF: 16 double caps / 32 bars at outer corners; waves end on inner bars')


if __name__ == '__main__': main()
