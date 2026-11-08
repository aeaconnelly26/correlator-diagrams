#!/usr/bin/env python3
"""Recover contact-bubble connectivity, outer frame and Proca contact from PDF."""
import argparse
from collections import Counter
import importlib.util
import json
from math import hypot
from pathlib import Path
import sys
from pypdf import PdfReader

sys.dont_write_bytecode = True
here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('triangle_check', here / 'check-tree-triangle.py')
triangle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(triangle)
spec = importlib.util.spec_from_file_location('species_check', here / 'check-species-circles.py')
species = importlib.util.module_from_spec(spec)
spec.loader.exec_module(species)


def recover(page, reader):
    nodes, edges, groups = triangle.plain_components(page, reader)
    assert len(edges) == 28, f'Expected four seven-edge graphs, got {len(edges)}'
    reports = []
    for slot, group in enumerate(groups, 1):
        local = [(a,b) for a,b in edges if a in group]
        degree = Counter(n for edge in local for n in edge)
        pairs = Counter(tuple(sorted(edge)) for edge in local)
        assert len(group) == 7 and len(local) == 7
        assert sorted(degree.values()) == [1,1,1,1,3,3,4], 'Wrong interaction valences'
        host = next(n for n in group if degree[n] == 4)
        bubble = [n for n in group if degree[n] == 3]
        assert pairs[tuple(sorted(bubble))] == 2, 'Bubble must have two parallel propagators'
        outer = [n for n in group if degree[n] == 1]
        xmin,xmax = min(nodes[n][0] for n in outer),max(nodes[n][0] for n in outer)
        ymin,ymax = min(nodes[n][1] for n in outer),max(nodes[n][1] for n in outer)
        assert abs(xmax-xmin-4.2*.8*72/2.54) < .03
        assert abs(ymax-ymin-4.2*.8*72/2.54) < .03
        assert hypot(nodes[host][0]-(xmin+xmax)/2,nodes[host][1]-(ymin+ymax)/2) < .03
        target = ((xmin,ymax),(xmin,ymin),(xmax,ymax),(xmax,ymin))[slot-1]
        selected = min(outer, key=lambda n:hypot(nodes[n][0]-target[0], nodes[n][1]-target[1]))
        assert hypot(nodes[selected][0]-target[0], nodes[selected][1]-target[1]) < .03
        neighbors = {n:{b if a == n else a for a,b in local if n in (a,b)} for n in group}
        assert len(neighbors[selected] & set(bubble)) == 1, 'Wrong selected external corner'
        a = next(iter(neighbors[selected]))
        b = next(n for n in bubble if n != a)
        assert host in neighbors[b] and selected not in neighbors[b]
        assert all(host in neighbors[n] for n in outer if n != selected), 'Unselected legs moved'
        dx,dy = nodes[host][0]-nodes[selected][0], nodes[host][1]-nodes[selected][1]
        fractions = []
        for n in (a,b):
            ox,oy = nodes[n][0]-nodes[selected][0],nodes[n][1]-nodes[selected][1]
            assert abs(ox*dy-oy*dx)/hypot(dx,dy) < .03, 'Bubble vertices off selected leg'
            fractions.append((ox*dx+oy*dy)/(dx*dx+dy*dy))
        assert 0 < fractions[0] < .5 < fractions[1] < 1
        assert abs(sum(fractions)-1) < .001
        reports.append({'slot':slot,'edges':7,'interaction_valences':[4,3,3], 'parallel_bubble_edges':2,
                        'cycle_rank':len(local)-len(group)+1,'insertion_fractions':fractions,
                        'outer_frame_pdf_pt':[xmax-xmin,ymax-ymin]})
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 5
    graphs = recover(reader.pages[0],reader)
    endpoints = triangle.contact.inspect(args.pdf)[3]
    assert endpoints['triangles'] == 16 and endpoints['dots'] == 12, endpoints
    assert all(g >= -.21 for g in endpoints['gaps_pt']), endpoints
    assert all(g <= .02 for g in endpoints['visible_gaps_pt']), endpoints
    assert all(c[0] > .9 and c[1] < .1 and c[2] > .9 for c in endpoints['colors'])
    styled = triangle.contact.inspect(args.pdf)[4]
    assert styled['triangles'] == 8 and styled['dots'] == 12
    assert all(g >= -.21 for g in styled['gaps_pt'])
    assert all(g <= .02 for g in styled['visible_gaps_pt'])
    assert all(c[0] > .9 and c[1] < .1 and c[2] > .9 for c in styled['colors'])
    rings, dots = species.inspect_circles(reader.pages[4], reader)
    assert len(rings) == 8 and len(dots) == 12
    assert all(abs(ring[2]-4.8*72/72.27) < .02 and max(color) == 0 for ring,color in rings), 'Default circle size/color changed'
    assert sum(line.strip() == 'W' for line in reader.pages[4].extract_text().splitlines()) == 8
    result = {'graphs':graphs,'proca_endpoint_page':endpoints, 'styled_endpoint_page':styled, 'styled_W_circles':len(rings), 'default_circle_radius_pdf_pt':rings[0][0][2]}
    if args.report: args.report.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS M08a: four seven-edge contact graphs; quartic host + two cubic vertices; fixed corners')
    print('PASS M08a: 24 white-filled pink endpoint contacts; eight default-size black W circles and no pink circles')


if __name__ == '__main__': main()
