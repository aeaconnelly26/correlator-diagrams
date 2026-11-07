#!/usr/bin/env python3
"""Reconstruct both crossed-box graphs and check real endpoint marker contact."""
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
HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


graph = module('triangle_graph', HERE.parent / 'insertion/check-tree-triangle.py')
species = module('species', HERE.parent / 'insertion/check-species-circles.py')


def reconstruct(page, reader):
    nodes, paths, groups = graph.plain_components(page, reader)
    dots = species.inspect_circles(page, reader)[1]
    assert len(paths) == 36 and len(dots) == 16
    reports = []
    for layout, gap, group in zip(['left-right','top-bottom']*2, [.045,.045,.08,.08], groups):
        edges = [(a,b) for a,b in paths if a in group]
        degree = Counter(n for edge in edges for n in edge)
        assert len(group) == 10 and len(edges) == 9
        assert sorted(degree.values()) == [1]*6+[3]*4
        internal = {n for n in group if degree[n] == 3}
        xmin,xmax = min(nodes[n][0] for n in internal),max(nodes[n][0] for n in internal)
        ymin,ymax = min(nodes[n][1] for n in internal),max(nodes[n][1] for n in internal)
        assert abs(xmax-xmin-(ymax-ymin)) < .03, 'Default box is not square'
        assert abs(xmax-xmin-2*1.34*.8*72/2.54) < .03, 'Inner span changed'
        corners = {name:min(internal,key=lambda n:hypot(nodes[n][0]-x,nodes[n][1]-y))
                   for name,x,y in [('TL',xmin,ymax),('TR',xmax,ymax),('BL',xmin,ymin),('BR',xmax,ymin)]}
        assert len(set(corners.values())) == 4
        assert all(any(hypot(nodes[n][0]-x,nodes[n][1]-y)<.03 for x,y,*_ in dots)
                   for n in internal), 'Interaction dot missing / misplaced'
        loose = {n for n in group if degree[n] == 1}
        gap_nodes = {n for n in loose if xmin < nodes[n][0] < xmax and ymin < nodes[n][1] < ymax}
        assert len(gap_nodes) == 2, 'Gap has become an interaction or vanished'
        outer = loose-gap_nodes
        xs,ys = zip(*(nodes[n] for n in outer))
        assert abs(max(xs)-min(xs)-4.2*.8*72/2.54) < .03
        assert abs(max(ys)-min(ys)-4.2*.8*72/2.54) < .03
        assert all(any(hypot(nodes[n][0]-x,nodes[n][1]-y)<.03 for n in outer)
                   for x in (min(xs),max(xs)) for y in (min(ys),max(ys)))
        key = lambda a,b: tuple(sorted((a,b)))
        physical_internal = {key(a,b) for a,b in edges if a in internal and b in internal}
        fixed_names = [('BL','TL'),('TR','BR')] if layout == 'left-right' else [('TL','TR'),('BL','BR')]
        expected = {key(corners[a],corners[b]) for a,b in fixed_names+[('BL','TR')]}
        assert physical_internal == expected, 'Wrong fixed edges or continuous diagonal'
        joined = []
        for n in gap_nodes:
            neighbors = [b if a == n else a for a,b in edges if n in (a,b)]
            assert len(neighbors) == 1 and neighbors[0] in internal
            joined.append(neighbors[0])
        assert set(joined) == {corners['TL'],corners['BR']}, 'Split diagonal has wrong endpoints'
        start,end = nodes[corners['TL']],nodes[corners['BR']]
        for fraction in (.5-gap,.5+gap):
            expected_point = tuple(start[i]+fraction*(end[i]-start[i]) for i in (0,1))
            assert min(hypot(nodes[n][0]-expected_point[0],nodes[n][1]-expected_point[1]) for n in gap_nodes) < .03
        logical = [(a,b) for a,b in edges if a not in gap_nodes and b not in gap_nodes]+[tuple(joined)]
        valences = Counter(n for edge in logical for n in edge)
        assert len(logical) == 8 and sorted(valences.values()) == [1]*4+[3]*4
        assert len(logical)-len(valences)+1 == 1, 'Wrong cycle rank'
        reports.append({'layout':layout,'logical_edges':8,'interaction_vertices':4,
                        'interaction_valences':[3]*4,'cycle_rank':1,
                        'inner_square_pdf_pt':xmax-xmin,'gap_fraction_half_width':gap,
                        'crossing_is_interaction':False})
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 4
    graphs = reconstruct(reader.pages[0],reader)
    contacts = graph.contact.inspect(args.pdf)
    assert contacts[2]['dots'] == 16 and contacts[2]['triangles'] == 24, 'Missing or spurious gap-end marker'
    assert min(contacts[2]['gaps_pt']) >= -.21 and max(contacts[2]['visible_gaps_pt']) <= .02
    assert all(c[0] > .9 and c[1] < .1 and c[2] > .5 for c in contacts[2]['colors'])
    assert contacts[3]['triangles'] == 4 and max(contacts[3]['visible_gaps_pt']) <= .02
    assert len(species.inspect_circles(reader.pages[3],reader)[0]) == 4, 'Circle controls added/lost a marker'
    waves, curves, points = [], 0, []
    for values,op in ContentStream(reader.pages[3].get_contents(),reader).operations:
        if op in (b'm',b'l',b'c'):
            points.append(tuple(map(float,values[-2:])))
            if op == b'c': curves += 1
        elif op in (b'S',b's',b'f',b'F',b'f*',b'B',b'B*',b'b',b'b*',b'n'):
            if op in (b'S',b's') and curves and len(points)>1 and hypot(points[0][0]-points[-1][0],points[0][1]-points[-1][1])>5:
                waves.append(curves)
            points,curves = [],0
    assert len(waves) == 10 and min(waves)>=2, 'Mixed EW or capped external paths stopped being wavy'
    report = {'graphs':graphs,'proca_contacts':16,'scalar_contacts':8,
              'mixed_proca_contacts':4,'endpoint_report':contacts[2:],'explicit_circles':4,
              'wavy_paths':len(waves),'wavy_path_curve_counts':waves}
    if args.report: args.report.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS M07a PDF: four eight-edge square crossed graphs, no central interaction; 16 Proca + 8 scalar + 4 mixed contacting tips; four explicit circles')


if __name__ == '__main__': main()
