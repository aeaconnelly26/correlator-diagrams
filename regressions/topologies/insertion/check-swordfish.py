#!/usr/bin/env python3
"""Recover swordfish connectivity from PDF strokes and check endpoint ink."""
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


def graphs(page, reader, channel):
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
                assert hypot(points[0][0]-points[-1][0], points[0][1]-points[-1][1]) > .05, 'Zero-length edge or self-loop'
                edges.append((points[0], points[-1]))
            points = []
    assert len(edges) == 28, 'Expected four seven-edge graphs'
    nodes, indexed = [], []
    def index(point):
        for n, old in enumerate(nodes):
            if hypot(point[0]-old[0], point[1]-old[1]) < .03: return n
        nodes.append(point)
        return len(nodes)-1
    for a, b in edges: indexed.append((index(a), index(b)))
    unseen, components = set(range(len(nodes))), []
    while unseen:
        pending, group = [next(iter(unseen))], set()
        while pending:
            n = pending.pop()
            if n in group: continue
            group.add(n)
            pending.extend(b if a == n else a for a, b in indexed if n in (a, b))
        unseen -= group
        components.append(group)
    assert len(components) == 4
    components.sort(key=lambda g: -max(nodes[n][1] for n in g))
    components = sorted(components[:2], key=lambda g: min(nodes[n][0] for n in g))+sorted(components[2:], key=lambda g: min(nodes[n][0] for n in g))
    reports = []
    for slot, group in enumerate(components, 1):
        pairs = Counter(tuple(sorted((a, b))) for a, b in indexed if a in group)
        degree = Counter(n for pair in indexed if pair[0] in group for n in pair)
        assert len(group) == 7 and sum(pairs.values()) == 7
        assert sorted(degree.values()) == [1, 1, 1, 1, 3, 3, 4], 'Wrong valences / fake bridge'
        loops = [pair for pair, count in pairs.items() if count == 2]
        assert len(loops) == 1 and all(c <= 2 for c in pairs.values()), 'Expected exactly one parallel-edge pair'
        a, host = sorted(loops[0], key=lambda n: degree[n])
        assert degree[a] == 3 and degree[host] == 4
        opposite = next(n for n in group if degree[n] == 3 and n != a)
        assert pairs[tuple(sorted((host, opposite)))] == 1, 'Exchange does not meet shared host'
        external = [n for n in group if degree[n] == 1]
        selected = next(n for n in external if tuple(sorted((n, a))) in pairs)
        x = min(nodes[n][0] for n in external) if slot in (1, 2) else max(nodes[n][0] for n in external)
        y = max(nodes[n][1] for n in external) if slot in (1, 3) else min(nodes[n][1] for n in external)
        assert hypot(nodes[selected][0]-x, nodes[selected][1]-y) < .03, 'Wrong logical external slot'
        if channel == 'T':
            assert abs(nodes[host][0]-nodes[opposite][0]) < .03
            assert (nodes[host][1] > nodes[opposite][1]) == (slot in (1, 3))
        else:
            assert abs(nodes[host][1]-nodes[opposite][1]) < .03
            assert (nodes[host][0] < nodes[opposite][0]) == (slot in (1, 2))
        reports.append({'channel': channel, 'slot': slot, 'edges': 7, 'vertices': 3,
                        'parallel_edges': 2, 'shared_vertex_valence': 4, 'cycle_rank': 1})
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 6
    reports = graphs(reader.pages[0], reader, 'T')+graphs(reader.pages[1], reader, 'S')
    endpoint = contact.inspect(args.pdf)
    for i, count in [(0, 0), (1, 0), (4, 32), (5, 16)]:
        assert endpoint[i]['dots'] == (12 if i < 2 else 24), 'Duplicate/missing interaction dot'
        assert endpoint[i]['triangles'] == count
        if count:
            assert min(endpoint[i]['gaps_pt']) >= -.21 and max(endpoint[i]['visible_gaps_pt']) <= .02, 'Marker misses vertex'
            assert all(c[0] > .9 and c[1] < .1 and c[2] > .5 for c in endpoint[i]['colors'])
    if args.report:
        args.report.write_text(json.dumps({'graphs': reports, 'proca_contacts': 32, 'scalar_contacts': 16,
                                          'endpoint_pages': endpoint[4:]}, indent=2)+'\n')
    print('PASS M05 PDF: eight seven-edge shared-quartic graphs; 32 Proca and 16 scalar white-filled pink contacts')


if __name__ == '__main__': main()
