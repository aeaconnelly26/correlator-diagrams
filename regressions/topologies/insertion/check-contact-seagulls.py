#!/usr/bin/env python3
"""Recover actual contact-seagull graphs, species/flow and marker contact from PDF."""
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
here = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('species_check',here/'check-species-circles.py')
species = importlib.util.module_from_spec(spec)
spec.loader.exec_module(species)
contact = species.contact


def paths(page,reader):
    state = {'matrix':(1,0,0,1,0,0),'fill':(0,0,0)}
    stack,points,ops,result = [],[],[],[]
    def transform(x,y):
        a,b,c,d,e,f = state['matrix']
        return a*x+c*y+e,b*x+d*y+f
    for args,op in ContentStream(page.get_contents(),reader).operations:
        if op == b'q': stack.append(state.copy())
        elif op == b'Q': state = stack.pop()
        elif op == b'cm': state['matrix'] = contact.multiply(state['matrix'],tuple(map(float,args)))
        elif op == b'rg': state['fill'] = tuple(map(float,args))
        elif op == b'g': state['fill'] = (float(args[0]),)*3
        elif op == b'k':
            c,m,y,k = map(float,args)
            state['fill'] = tuple(1-min(1,v+k) for v in (c,m,y))
        elif op in (b'm',b'l',b'c',b'h',b're'):
            ops.append(op)
            if op in (b'm',b'l',b'c'): points.append(transform(float(args[-2]),float(args[-1])))
        elif op in (b'S',b's',b'f',b'F',b'f*',b'B',b'B*',b'b',b'b*',b'n'):
            if points: result.append((op,ops,points,state['fill']))
            ops,points = [],[]
    return result


def recover(page,reader):
    edges,loops = [],[]
    for op,ops,points,_ in paths(page,reader):
        if op not in (b'S',b's'): continue
        if ops == [b'm',b'l']: edges.append((points[0],points[-1],False))
        else:
            assert ops == [b'm',b'c',b'c',b'c',b'c'],ops
            assert hypot(points[0][0]-points[-1][0],points[0][1]-points[-1][1]) < .02
            edges.append((points[0],points[-1],True));loops.append(points)
    assert len(edges) == 24 and len(loops) == 4, 'Expected four six-edge graphs / closed self-loops'
    nodes,indexed = [],[]
    def index(p):
        for i,old in enumerate(nodes):
            if hypot(p[0]-old[0],p[1]-old[1]) < .03: return i
        nodes.append(p);return len(nodes)-1
    for a,b,loop in edges: indexed.append((index(a),index(b),loop))
    unseen,groups = set(range(len(nodes))),[]
    while unseen:
        pending,group = [next(iter(unseen))],set()
        while pending:
            n = pending.pop()
            if n in group: continue
            group.add(n);pending.extend(b if a==n else a for a,b,_ in indexed if n in (a,b))
        unseen -= group;groups.append(group)
    assert len(groups) == 4
    groups.sort(key=lambda g:-max(nodes[n][1] for n in g))
    groups = sorted(groups[:2],key=lambda g:min(nodes[n][0] for n in g))+sorted(groups[2:],key=lambda g:min(nodes[n][0] for n in g))
    reports = []
    for slot,group in enumerate(groups,1):
        local = [(a,b,loop) for a,b,loop in indexed if a in group]
        degree = Counter(n for a,b,_ in local for n in (a,b))
        assert len(group) == 6 and len(local) == 6
        assert sorted(degree.values()) == [1,1,1,1,4,4], 'Wrong quartic/external valences'
        self_edges = [a for a,b,loop in local if loop and a==b]
        assert len(self_edges) == 1
        insertion = self_edges[0]
        host = next(n for n in group if degree[n]==4 and n!=insertion)
        outer = [n for n in group if degree[n]==1]
        xmin,xmax = min(nodes[n][0] for n in outer),max(nodes[n][0] for n in outer)
        ymin,ymax = min(nodes[n][1] for n in outer),max(nodes[n][1] for n in outer)
        assert abs(xmax-xmin-4.2*.8*72/2.54) < .03
        assert abs(ymax-ymin-4.2*.8*72/2.54) < .03
        assert hypot(nodes[host][0]-(xmin+xmax)/2,nodes[host][1]-(ymin+ymax)/2) < .03
        target = ((xmin,ymax),(xmin,ymin),(xmax,ymax),(xmax,ymin))[slot-1]
        selected = min(outer,key=lambda n:hypot(nodes[n][0]-target[0],nodes[n][1]-target[1]))
        assert hypot(nodes[selected][0]-target[0],nodes[selected][1]-target[1]) < .03
        neighbors = {n:{b if a==n else a for a,b,loop in local if not loop and n in (a,b)} for n in group}
        assert neighbors[insertion] == {selected,host}, 'Wrong slot, extra stem or extra interaction'
        assert all(neighbors[n]=={host} for n in outer if n!=selected)
        dx,dy = nodes[host][0]-nodes[selected][0],nodes[host][1]-nodes[selected][1]
        ox,oy = nodes[insertion][0]-nodes[selected][0],nodes[insertion][1]-nodes[selected][1]
        fraction = (ox*dx+oy*dy)/(dx*dx+dy*dy)
        assert abs(fraction-.4) < .001 and abs(ox*dy-oy*dx)/hypot(dx,dy) < .03
        loop = next(p for p in loops if hypot(p[0][0]-nodes[insertion][0],p[0][1]-nodes[insertion][1]) < .03)
        fx,fy = loop[2][0]-loop[0][0],loop[2][1]-loop[0][1]
        assert (fy>0) == (slot in (1,3)), 'Loop points toward wrong vertical side'
        assert abs(fx*dx+fy*dy)/hypot(dx,dy) < .03, 'Loop is not normal to selected leg'
        diameter = hypot(fx,fy)
        assert abs(diameter-.72*1.55*.66*.8*72/2.54) < .03
        reports.append({'slot':slot,'edges':6,'interaction_valences':[4,4],'self_loops':1,'cycle_rank':1,
                        'insertion_fraction':fraction,'loop_diameter_pdf_pt':diameter,
                        'loop_side':'up' if fy>0 else 'down','outer_frame_pdf_pt':[xmax-xmin,ymax-ymin]})
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path);parser.add_argument('--report',type=Path)
    args = parser.parse_args();reader = PdfReader(args.pdf)
    assert len(reader.pages) == 7
    graphs = recover(reader.pages[0],reader)
    reports = contact.inspect(args.pdf)
    for n,count in ((3,8),(4,4),(6,8)):
        r = reports[n]
        assert r['triangles']==count and r['dots']==8,r
        assert all(g>=-.21 for g in r['gaps_pt']) and all(g<=.02 for g in r['visible_gaps_pt']),r
        assert all(c[0]>.9 and c[1]<.1 and c[2]>.9 for c in r['colors']),r
    native = paths(reader.pages[5],reader)
    charge_arrows = [p for op,ops,p,color in native if op in (b'f',b'f*',b'B',b'B*') and max(color)<.01 and
                     len(set((round(x,3),round(y,3)) for x,y in p))==3 and b'c' not in ops]
    waves = [ops.count(b'c') for op,ops,_,_ in native if op in (b'S',b's') and b'c' in ops]
    centers = [(sum(x for x,y in p)/len(p),sum(y for x,y in p)/len(p)) for p in charge_arrows]
    distinct = []
    for p in centers:
        if not any(hypot(p[0]-q[0],p[1]-q[1])<.03 for q in distinct): distinct.append(p)
    # Legacy raw with-arrow + circ repeats four decorations at identical positions.
    assert len(charge_arrows)==48 and len(distinct)==44, (len(charge_arrows),len(distinct))
    assert len(waves)==48 and min(waves)>=8, f'Lost EW waves: {waves}'
    rings,dots = species.inspect_circles(reader.pages[5],reader)
    distinct_rings = []
    for ring,color in rings:
        if not any(hypot(ring[0]-old[0],ring[1]-old[1])<.03 for old in distinct_rings): distinct_rings.append(ring)
    assert len(rings)==12 and len(distinct_rings)==8 and len(dots)==16
    text = reader.pages[5].extract_text().splitlines()
    assert sum(t.strip()=='WW' for t in text)==4 and sum(t.strip()=='Z' for t in text)==4
    pinkrings,pinkdots = species.inspect_circles(reader.pages[6],reader)
    assert len(pinkrings)==4 and len(pinkdots)==8
    assert all(abs(ring[2]-4.8*72/72.27)<.02 and max(color)==0 for ring,color in pinkrings)
    # The eight-panel native page is fitted by adjustbox; normalize to its dots.
    ratio = pinkrings[0][0][2]/pinkdots[0][2]
    assert all(abs(ring[2]/dots[0][2]-ratio)<.01 and max(color)==0 for ring,color in rings)
    result = {'graphs':graphs,'proca':reports[3],'scalar':reports[4],'pink_styled':reports[6],
              'native_species':{'W_loops':4,'Z_loops':4,'distinct_charge_arrows':len(distinct),'raw_arrow_paints':len(charge_arrows),'distinct_species_circles':len(distinct_rings),'raw_circle_paints':len(rings),'legacy_coincident_overpaint':True,'wave_paths':len(waves),'curves_per_wave_path':waves},'styled_W_circles':4}
    if args.report: args.report.write_text(json.dumps(result,indent=2)+'\n')
    print('PASS M08b: four six-edge graphs; two quartic vertices, one direct self-loop, fixed corners and source-facing sides')
    print('PASS M08b: 20 white-filled pink contacts; eight Z/W source variants, 44 distinct charge arrows, 48 wavy propagators and default .8 circles')


if __name__=='__main__': main()
