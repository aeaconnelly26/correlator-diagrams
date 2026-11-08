#!/usr/bin/env python3
"""Verify actual upper-crossed box PDF connectivity, markers, circles and caps."""
import argparse
from collections import Counter
import importlib.util
import json
import os
import subprocess
import tempfile
from math import hypot
from pathlib import Path
import sys
from pypdf import PdfReader
from pypdf.generic import ContentStream
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('species', HERE.parent/'insertion/check-species-circles.py')
species = importlib.util.module_from_spec(spec); spec.loader.exec_module(species)

def distance(a,b): return hypot(a[0]-b[0],a[1]-b[1])
def strokes(page,reader):
    matrix=(1,0,0,1,0,0); stack=[]; points=[]; curves=0; result=[]
    def transform(x,y):
        a,b,c,d,e,f=matrix; return a*x+c*y+e,b*x+d*y+f
    for args,op in ContentStream(page.get_contents(),reader).operations:
        if op==b'q': stack.append(matrix)
        elif op==b'Q': matrix=stack.pop()
        elif op==b'cm': matrix=species.contact.multiply(matrix,tuple(map(float,args)))
        elif op in (b'm',b'l',b'c'):
            points.append(transform(*map(float,args[-2:])))
            if op==b'c': curves+=1
        elif op in (b'S',b's',b'f',b'F',b'f*',b'B',b'B*',b'b',b'b*',b'n'):
            if op in (b'S',b's') and points: result.append((points[0],points[-1],curves))
            points=[]; curves=0
    return result

def cells(page,reader):
    dots=species.inspect_circles(page,reader)[1]; assert len(dots)==16
    # Four separated gallery cells; physical graph components cannot be used:
    # the split external leg deliberately leaves its outer fragment disconnected.
    ys=sorted(d[1] for d in dots); ymid=(ys[7]+ys[8])/2
    centers=[]
    for row in ([d for d in dots if d[1]>ymid],[d for d in dots if d[1]<ymid]):
        xs=sorted(d[0] for d in row); xmid=(xs[3]+xs[4])/2
        for group in ([d for d in row if d[0]<xmid],[d for d in row if d[0]>xmid]):
            centers.append((sum(d[0] for d in group)/4,sum(d[1] for d in group)/4))
    return centers

def reconstruct(page,reader):
    paths=strokes(page,reader); assert len(paths)==36 and all(n==0 for _,_,n in paths)
    centers=cells(page,reader); reports=[]
    for cell,(cx,cy) in enumerate(centers):
        edges=[(a,b) for a,b,_ in paths if min(range(4),key=lambda n:distance(a,centers[n]))==cell]
        nodes=[]
        def index(p):
            for i,q in enumerate(nodes):
                if distance(p,q)<.03:return i
            nodes.append(p);return len(nodes)-1
        indexed=[(index(a),index(b)) for a,b in edges]
        degree=Counter(n for edge in indexed for n in edge)
        assert len(nodes)==10 and len(indexed)==9 and sorted(degree.values())==[1]*6+[3]*4
        internal={n for n in degree if degree[n]==3}
        xmin,xmax=min(nodes[n][0] for n in internal),max(nodes[n][0] for n in internal)
        ymin,ymax=min(nodes[n][1] for n in internal),max(nodes[n][1] for n in internal)
        corner={name:min(internal,key=lambda n:distance(nodes[n],(x,y))) for name,x,y in
                [('TL',xmin,ymax),('TR',xmax,ymax),('BL',xmin,ymin),('BR',xmax,ymin)]}
        key=lambda a,b:tuple(sorted((a,b)))
        perimeter={key(corner[a],corner[b]) for a,b in [('TL','TR'),('TR','BR'),('BR','BL'),('BL','TL')]}
        assert {key(a,b) for a,b in indexed if a in internal and b in internal}==perimeter
        loose=set(degree)-internal
        gaps={n for n in loose if xmin<nodes[n][0]<xmax and nodes[n][1]>ymax}
        assert len(gaps)==2
        outer=loose-gaps
        oxmin,oxmax=min(nodes[n][0] for n in outer),max(nodes[n][0] for n in outer)
        oymin,oymax=min(nodes[n][1] for n in outer),max(nodes[n][1] for n in outer)
        outercorner={name:min(outer,key=lambda n:distance(nodes[n],(x,y))) for name,x,y in
                    [('UL',oxmin,oymax),('UR',oxmax,oymax),('LL',oxmin,oymin),('LR',oxmax,oymin)]}
        expected_outer=4.2*.8*[1,1,1,.8][cell]*72/2.54
        assert abs(oxmax-oxmin-expected_outer)<.03 and abs(oymax-oymin-expected_outer)<.03
        unbroken={key(a,b) for a,b in indexed if a not in gaps and b not in gaps}
        expected=perimeter|{key(outercorner[a],corner[b]) for a,b in [('UR','TL'),('LL','BL'),('LR','BR')]}
        assert unbroken==expected,'Continuous upper or lower leg has wrong vertex'
        ends=[]
        for n in gaps:
            ends.extend(b if a==n else a for a,b in indexed if n in (a,b))
        assert set(ends)=={outercorner['UL'],corner['TR']},'Split leg lost logical slot 1'
        start,end=nodes[outercorner['UL']],nodes[corner['TR']]
        t=(cx-start[0])/(end[0]-start[0]); gap=[.04,.07,.04,.04][cell]
        for f in (t-gap,t+gap):
            point=tuple(start[i]+f*(end[i]-start[i]) for i in (0,1))
            assert min(distance(nodes[n],point) for n in gaps)<.03
        cross=tuple(start[i]+t*(end[i]-start[i]) for i in (0,1))
        assert cross[1]>ymax and min(distance(cross,nodes[n]) for n in internal)>1
        logical=list(unbroken)+[tuple(ends)]; valences=Counter(n for edge in logical for n in edge)
        assert len(logical)==8 and len(logical)-len(valences)+1==1
        assert sorted(valences.values())==[1]*4+[3]*4
        reports.append({'logical_edges':8,'vertices':4,'cycle_rank':1,'gap_half_fraction':gap,'crossing_is_vertex':False})
    return reports

def rejected_options():
    cases=[('topology=cross-box,box-external-crossing=top','requires topology=box'),
           ('topology=box,box-external-crossing=right',"Choice 'right' unknown"),
           ('topology=box,box-external-crossing=top,box-external-crossing-gap=.8','Invalid box external crossing gap'),
           ('topology=box,box-external-crossing=top,fourpoint-yspan=1','require positive x spans')]
    root=HERE.parents[2]
    with tempfile.TemporaryDirectory(prefix='feynmanfun-crossing-options-') as folder:
        build=Path(folder)
        for index,(options,expected) in enumerate(cases):
            tex=build/f'reject-{index}.tex'
            tex.write_text(r'\documentclass{article}\usepackage{feynman-fun}\begin{document}\FourPointCorr['+options+r']\end{document}')
            env=dict(os.environ,TEXINPUTS=str(root)+'//:'+os.environ.get('TEXINPUTS',''))
            result=subprocess.run(['pdflatex','-interaction=batchmode','-halt-on-error',tex.name],cwd=build,env=env,stdout=subprocess.DEVNULL)
            log=tex.with_suffix('.log').read_text()
            assert result.returncode!=0 and expected in log.replace('\n',' '),f'Invalid combination not rejected with expected diagnostic {expected}: {options}'
    return len(cases)

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('pdf',type=Path);parser.add_argument('--report',type=Path);args=parser.parse_args()
    reader=PdfReader(args.pdf);assert len(reader.pages)==4
    graphs=reconstruct(reader.pages[0],reader)
    contact=species.contact.inspect(args.pdf)[2]
    assert contact['triangles']==23,'Extra/missing tips, including artificial cut ends'
    touching=[(a,b) for a,b in zip(contact['gaps_pt'],contact['visible_gaps_pt']) if a<1]
    assert len(touching)==14,'Wrong real-vertex contact count'
    assert min(a for a,b in touching)>=-.21 and max(b for a,b in touching)<=.02
    rings=species.inspect_circles(reader.pages[3],reader)[0]
    assert len(rings)==4,'Split edge duplicated/lost circle'
    assert all(abs(ring[2]-3.6*72/72.27)<.03 for ring,color in rings),'circ scale=.6 ignored'
    centers=cells(reader.pages[3],reader);paths=strokes(reader.pages[3],reader)
    caps=[]
    for cell,expected in [(0,4),(1,8)]:
        selected=[(a,b,n) for a,b,n in paths if min(range(4),key=lambda i:distance(a,centers[i]))==cell]
        bars=[(a,b) for a,b,n in selected if n==0 and distance(a,b)<10]
        assert len(bars)==expected
        cx,cy=centers[cell]; unit=.8*72/2.54
        outer=[(cx-2.1*unit,cy+2.1*unit),(cx-2.1*unit,cy-2.1*unit),(cx+2.1*unit,cy+2.1*unit),(cx+2.1*unit,cy-2.1*unit)]
        host=[(cx+1.34*unit,cy+1.34*unit),(cx-1.34*unit,cy-1.34*unit),(cx-1.34*unit,cy+1.34*unit),(cx+1.34*unit,cy-1.34*unit)]
        for endpoint,vertex in zip(outer,host):
            midpoint=lambda bar:tuple((bar[0][i]+bar[1][i])/2 for i in (0,1))
            bar=min(bars,key=lambda bar:distance(midpoint(bar),endpoint));assert distance(midpoint(bar),endpoint)<.03
            dx,dy=vertex[0]-endpoint[0],vertex[1]-endpoint[1]
            assert abs((bar[1][0]-bar[0][0])*dx+(bar[1][1]-bar[0][1])*dy)<.1,'Cap tangent follows old host'
            if cell==1:
                norm=hypot(dx,dy);inner=tuple(endpoint[i]+3*.8*72/72.27*(dx,dy)[i]/norm for i in (0,1))
                assert min(distance(midpoint(bar),inner) for bar in bars)<.03
                assert min(distance(point,inner) for a,b,n in selected if n for point in (a,b))<.08,'Wave missed inner cap'
        caps.append({'bars':expected,'outer_endpoints':4})
    report={'rejected_option_cases':rejected_options(),'graphs':graphs,'marker_triangles':23,'real_vertex_contacts':14,'scaled_circles':4,'caps':caps}
    if args.report:args.report.write_text(json.dumps(report,indent=2)+'\n')
    print('PASS M07b PDF: four routed square/perimeter graphs; 23 tips, 14 contacts, four scaled circles; 12 cap bars with correct tangent/contact')
if __name__=='__main__':main()
