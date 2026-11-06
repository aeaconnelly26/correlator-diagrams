#!/usr/bin/env python3
"""Recover M06 connectivity from PDF strokes; verify actual marker contact."""
import argparse
from collections import Counter
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


def plain_components(page, reader):
    matrix = (1, 0, 0, 1, 0, 0)
    stack, points, edges = [], [], []
    def transform(x, y):
        a, b, c, d, e, f = matrix
        return a*x+c*y+e, b*x+d*y+f
    for args, op in ContentStream(page.get_contents(), reader).operations:
        if op == b'q': stack.append(matrix)
        elif op == b'Q': matrix = stack.pop()
        elif op == b'cm': matrix = contact.multiply(matrix, tuple(map(float, args)))
        elif op in (b'm', b'l', b'c'):
            points.append(transform(float(args[-2]), float(args[-1])))
        elif op in (b'S', b's', b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*', b'n'):
            if op in (b'S', b's') and points:
                assert hypot(points[0][0]-points[-1][0], points[0][1]-points[-1][1]) > .05, 'Collapsed edge / self-loop'
                edges.append((points[0], points[-1]))
            points = []

    nodes, indexed = [], []
    def index(point):
        for n, old in enumerate(nodes):
            if hypot(point[0]-old[0], point[1]-old[1]) < .03: return n
        nodes.append(point)
        return len(nodes)-1
    for a, b in edges: indexed.append((index(a), index(b)))
    unseen, groups = set(range(len(nodes))), []
    while unseen:
        pending, group = [next(iter(unseen))], set()
        while pending:
            n = pending.pop()
            if n in group: continue
            group.add(n)
            pending.extend(b if a == n else a for a,b in indexed if n in (a,b))
        unseen -= group
        groups.append(group)
    assert len(groups) == 4
    groups.sort(key=lambda g: -max(nodes[n][1] for n in g))
    groups = sorted(groups[:2], key=lambda g: min(nodes[n][0] for n in g))+sorted(groups[2:], key=lambda g: min(nodes[n][0] for n in g))
    return nodes, indexed, groups


def recover(page, reader):
    nodes, indexed, groups = plain_components(page, reader)
    assert len(indexed) == 32, f"Expected four eight-edge graphs, got {len(indexed)}"
    reports = []
    for side, group in zip(['bottom','top','left','right'],groups):
        pairs = Counter(tuple(sorted((a,b))) for a,b in indexed if a in group)
        degree = Counter(n for edge in indexed if edge[0] in group for n in edge)
        assert len(group) == 8 and sum(pairs.values()) == 8
        assert sorted(degree.values()) == [1,1,1,1,3,3,3,3], 'Wrong valences / extra contact'
        assert all(c == 1 for c in pairs.values()), 'Parallel loop / duplicated edge'
        neighbors = {n:{b if a == n else a for a,b in indexed if n in (a,b)} for n in group}
        internal = {n for n in group if degree[n] == 3}
        opposite = [n for n in internal if len([m for m in neighbors[n] if degree[m] == 1]) == 2]
        assert len(opposite) == 1, 'Opposite tree vertex must carry two external legs'
        opposite = opposite[0]
        triangle = internal-{opposite}
        assert sum(pairs.get(tuple(sorted((a,b))),0) for a in triangle for b in triangle if a < b) == 3
        bridge = neighbors[opposite] & triangle
        assert len(bridge) == 1
        tip = next(iter(bridge))
        assert not any(degree[n] == 1 for n in neighbors[tip]), 'External leg attached to bridge tip'
        lengths = [hypot(nodes[a][0]-nodes[b][0],nodes[a][1]-nodes[b][1]) for a in triangle for b in triangle if a < b]
        assert max(lengths)-min(lengths) < .03, 'Default triangle is not equilateral'
        assert 35.28 < min(lengths) <= max(lengths) < 35.44, 'Reviewed compact default triangle size regressed'
        outer = {n for n in group if degree[n] == 1}
        xmin,xmax = min(nodes[n][0] for n in outer),max(nodes[n][0] for n in outer)
        ymin,ymax = min(nodes[n][1] for n in outer),max(nodes[n][1] for n in outer)
        # Logical frame +/-2.10, with the package's 0.8 coordinate baseline.
        assert abs((xmax-xmin)-4.2*.8*72/2.54) < .03, 'External x frame moved'
        assert abs((ymax-ymin)-4.2*.8*72/2.54) < .03, 'External y frame moved'
        assert all(min(abs(nodes[n][0]-xmin),abs(nodes[n][0]-xmax)) < .03 and
                   min(abs(nodes[n][1]-ymin),abs(nodes[n][1]-ymax)) < .03 for n in outer), 'External corner moved'

        for n in triangle-{tip}:
            attached = neighbors[n] & outer
            assert len(attached) == 1
            point = nodes[next(iter(attached))]
            if side in ('top','bottom'):
                assert abs(point[1]-(ymax if side == 'top' else ymin)) < .03, 'Wrong external pair'
            else:
                assert abs(point[0]-(xmin if side == 'left' else xmax)) < .03, 'Wrong external pair'
        if side in ('top','bottom'):
            assert abs(nodes[tip][0]-nodes[opposite][0]) < .03
            assert (nodes[tip][1] > nodes[opposite][1]) == (side == 'top')
        else:
            assert abs(nodes[tip][1]-nodes[opposite][1]) < .03
            assert (nodes[tip][0] > nodes[opposite][0]) == (side == 'right')
        reports.append({'side':side,'edges':8,'interaction_vertices':4,'interaction_valences':[3,3,3,3],'triangle_edges':3,'exchange_bridges':1,'cycle_rank':1,'triangle_side_lengths_pdf_pt':lengths,'outer_frame_width_pdf_pt':xmax-xmin,'outer_frame_height_pdf_pt':ymax-ymin})
    return reports



def styled_waves(page, reader):
    color, stack, curves, found = (0,0,0), [], 0, []
    for args, op in ContentStream(page.get_contents(), reader).operations:
        if op == b'q': stack.append(color)
        elif op == b'Q': color = stack.pop()
        elif op == b'RG': color = tuple(map(float,args))
        elif op == b'G': color = (float(args[0]),)*3
        elif op == b'K':
            c,m,y,k = map(float,args)
            color = (1-min(1,c+k),1-min(1,m+k),1-min(1,y+k))
        elif op == b'c': curves += 1
        elif op in (b'S',b's',b'f',b'F',b'f*',b'B',b'B*',b'b',b'b*',b'n'):
            if op in (b'S',b's') and curves and color[0] > .9 and color[1] < .1 and color[2] > .5:
                found.append(curves)
            curves = 0
    assert len(found) == 4 and min(found) >= 2, 'Styled exchanges are not four wavy paths'
    return found



def comparison_frames(page, reader):
    nodes, edges, groups = plain_components(page, reader)
    for group in groups:
        xs,ys = zip(*(nodes[n] for n in group))
        assert abs(max(xs)-min(xs)-4.2*.8*72/2.54) < .03
        assert abs(max(ys)-min(ys)-4.2*.8*72/2.54) < .03
        corners = [(x,y) for x in (min(xs),max(xs)) for y in (min(ys),max(ys))]
        assert all(any(hypot(x-nodes[n][0],y-nodes[n][1]) < .03 for n in group) for x,y in corners)
    return len(groups)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 7
    graphs = recover(reader.pages[0],reader)
    waves = styled_waves(reader.pages[2],reader)
    comparisons = sum(comparison_frames(reader.pages[i],reader) for i in [5,6])
    endpoints = contact.inspect(args.pdf)
    for page,count in [(0,0),(3,24),(4,12)]:
        assert endpoints[page]['dots'] == 16, 'Extra/missing interaction dot'
        assert endpoints[page]['triangles'] == count
        if count:
            assert min(endpoints[page]['gaps_pt']) >= -.21 and max(endpoints[page]['visible_gaps_pt']) <= .02, 'Marker misses actual vertex'
            assert all(c[0] > .9 and c[1] < .1 and c[2] > .5 for c in endpoints[page]['colors'])
    if args.report:
        args.report.write_text(json.dumps({'graphs':graphs,'shared_frame_comparison_graphs':comparisons,'styled_wavy_exchange_curve_counts':waves,'proca_contacts':24,'scalar_contacts':12,'endpoint_pages':endpoints[3:]},indent=2)+'\n')
    print('PASS M06 PDF: four equilateral eight-edge graphs with standard outer frames; eight tree/box/contact frame comparisons; four wavy exchanges; 24 Proca + 12 scalar pink white-filled contacts')


if __name__ == '__main__': main()
