#!/usr/bin/env python3
"""Verify actual plain seagull graphs and colored endpoint ink in the M04 PDF."""
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


def plain_graph(page, reader):
    """Recover edges from stroked PDF paths, independently of TeX helper calls."""
    matrix = (1, 0, 0, 1, 0, 0)
    stack, ops, points, edges = [], [], [], []

    def transform(x, y):
        a, b, c, d, e, f = matrix
        return (a*x+c*y+e, b*x+d*y+f)

    for args, op in ContentStream(page.get_contents(), reader).operations:
        if op == b'q':
            stack.append(matrix)
        elif op == b'Q':
            matrix = stack.pop()
        elif op == b'cm':
            matrix = contact.multiply(matrix, tuple(float(n) for n in args))
        elif op in (b'm', b'l', b'c', b'h', b're'):
            ops.append(op)
            if op in (b'm', b'l', b'c'):
                points.append(transform(float(args[-2]), float(args[-1])))
        elif op in (b'S', b's', b'f', b'F', b'f*', b'B', b'B*', b'b', b'b*', b'n'):
            if op in (b'S', b's'):
                if ops == [b'm', b'l']:
                    edges.append((points[0], points[-1], False))
                elif ops == [b'm', b'c', b'c', b'c', b'c']:
                    assert hypot(points[0][0]-points[-1][0], points[0][1]-points[-1][1]) < .02, 'Self-loop is open'
                    edges.append((points[0], points[-1], True))
                else:
                    raise AssertionError(f'Unexpected stroked path on plain topology page: {ops}')
            ops, points = [], []

    nodes, indexed, degrees = [], [], []
    def node_index(point):
        for i, other in enumerate(nodes):
            if hypot(point[0]-other[0], point[1]-other[1]) < .05:
                return i
        nodes.append(point)
        degrees.append(0)
        return len(nodes)-1

    for first, last, loop in edges:
        a, b = node_index(first), node_index(last)
        assert loop == (a == b), 'Self-loop/straight-edge identity mismatch'
        indexed.append((a, b, loop))
        degrees[a] += 1
        degrees[b] += 1
    assert len(edges) == 28, f'Expected 7 actual edges in each of 4 diagrams, got {len(edges)}'
    unseen, components = set(range(len(nodes))), []
    while unseen:
        pending, component = [next(iter(unseen))], set()
        while pending:
            n = pending.pop()
            if n in component:
                continue
            component.add(n)
            pending.extend(b if a == n else a for a, b, _ in indexed if a == n or b == n)
        unseen -= component
        component_edges = [edge for edge in indexed if edge[0] in component]
        assert sorted(degrees[n] for n in component) == [1, 1, 1, 1, 3, 3, 4], 'Wrong external/tree/quartic valence'
        assert len(component_edges) == 7
        assert sum(loop for _, _, loop in component_edges) == 1
        components.append({'edges': 7, 'external_endpoints': 4, 'trivalent_vertices': 2, 'quartic_vertices': 1, 'self_loops': 1})
    assert len(components) == 4
    return components


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf', type=Path)
    parser.add_argument('--report', type=Path)
    args = parser.parse_args()
    reader = PdfReader(args.pdf)
    assert len(reader.pages) == 6, 'Expected the complete six-page M04 gallery'
    graphs = [plain_graph(page, reader) for page in reader.pages[:2]]
    reports = contact.inspect(args.pdf)
    for page, triangles in ((4, 16), (5, 8)):
        report = reports[page]
        assert report['triangles'] == triangles and report['dots'] == 24, report
        assert all(g >= -.21 for g in report['gaps_pt']), report
        assert all(g <= .02 for g in report['visible_gaps_pt']), report
        assert all(c[0] > .9 and c[1] < .1 and c[2] > .9 for c in report['colors']), report
    for report in reports[:2]:
        assert report['dots'] == 12 and report['triangles'] == 0, report
    if args.report:
        args.report.write_text(json.dumps({'plain_graphs': graphs, 'proca': reports[4], 'scalar': reports[5]}, indent=2) + '\n')
    print('PASS M04: 8 actual PDF graphs, each 7 edges / one quartic self-loop; 24 pink, white-filled endpoint tips contact visible vertices')


if __name__ == '__main__':
    main()
