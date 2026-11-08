#!/usr/bin/env python3
"""Measure EW external-stroke intrusion into the top internal circle envelope.

Negative clearance is an observation of crowding, not a failed topology test.
The circle's white fill may mask a propagator drawn earlier in the PDF.
"""
import argparse
import importlib.util
import json
from math import hypot
from pathlib import Path
import sys
sys.dont_write_bytecode=True
from pypdf import PdfReader
from pypdf.generic import ContentStream
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('boxes',HERE/'check-box-external-crossing.py')
boxes=importlib.util.module_from_spec(spec);spec.loader.exec_module(boxes)

def paths(page,reader):
 matrix=(1,0,0,1,0,0);stack=[];width=1;points=[];curves=0;result=[];last=None
 def transform(x,y):
  a,b,c,d,e,f=matrix;return a*x+c*y+e,b*x+d*y+f
 for args,op in ContentStream(page.get_contents(),reader).operations:
  if op==b'q':stack.append((matrix,width))
  elif op==b'Q':matrix,width=stack.pop()
  elif op==b'cm':matrix=boxes.species.contact.multiply(matrix,tuple(map(float,args)))
  elif op==b'w':width=float(args[0])
  elif op in (b'm',b'l'):
   last=transform(*map(float,args));points.append(last)
  elif op==b'c':
   controls=[last]+[transform(float(args[i]),float(args[i+1])) for i in (0,2,4)]
   for j in range(1,65):
    t=j/64;weights=((1-t)**3,3*(1-t)**2*t,3*(1-t)*t*t,t**3)
    points.append(tuple(sum(w*p[i] for w,p in zip(weights,controls)) for i in (0,1)))
   last=controls[-1];curves+=1
  elif op in (b'S',b's',b'f',b'F',b'f*',b'B',b'B*',b'b',b'b*',b'n'):
   if op in (b'S',b's') and points:
    result.append((points,curves,width*hypot(matrix[0],matrix[1])/2))
   points=[];curves=0;last=None
 return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=Path);p.add_argument('--report',type=Path);args=p.parse_args()
 reader=PdfReader(args.pdf);assert len(reader.pages)==3;report=[]
 settings=[[(scale,circ,.04,.5) for circ in (1,.8,.6) for scale in (.8,1)],[(1,circ,gap,.5) for gap in (.04,.08,.12) for circ in (1,.6)],[(1,circ,.04,pos) for pos in (.35,.5,.65) for circ in (1,.6)]]
 for page_number,page in enumerate(reader.pages,1):
  rings,dots=boxes.species.inspect_circles(page,reader);assert len(rings)==6 and len(dots)==24
  rings.sort(key=lambda r:-r[0][1]);rings=sum((sorted(rings[i:i+2],key=lambda r:r[0][0]) for i in range(0,6,2)),[])
  centers=[]
  for ring,color in rings:
   nearest=sorted(dots,key=lambda d:boxes.distance(ring,d))[:4]
   centers.append(tuple(sum(d[i] for d in nearest)/4 for i in (0,1)))
  strokes=paths(page,reader);assert len(strokes)==54
  for cell,((ring,color),(scale,circ,gap,position)) in enumerate(zip(rings,settings[page_number-1])):
   selected=[p for p in strokes if min(range(6),key=lambda n:boxes.distance(tuple((p[0][0][i]+p[0][-1][i])/2 for i in (0,1)),centers[n]))==cell]
   assert len(selected)==9 and [i for i,p in enumerate(selected) if p[1]]==[0,1,3,6]
   assert abs(ring[2]-6*circ*72/72.27)<.03
   leg_clearances=[]
   for indices in [(0,1),(3,)]:
    clearance=min(boxes.distance(point,ring)-ring[2]-ring[3]-selected[i][2] for i in indices for point in selected[i][0])
    leg_clearances.append(clearance)
   report.append(dict(page=page_number,cell=cell+1,diagram_scale=scale,circle_scale=circ,crossing_gap=gap,circle_position=position,split_leg_ink_clearance_pdf_pt=leg_clearances[0],continuous_leg_ink_clearance_pdf_pt=leg_clearances[1],minimum_ink_clearance_pdf_pt=min(leg_clearances),overlap_before_white_mask=min(leg_clearances)<0))
 result={'examples':report,'pages':3,'cases':18,'method':'64 samples per cubic Bezier, actual PDF strokes, circle radius and stroke outlines; negative means ink-envelope overlap before white circle mask','package_changes':False}
 if args.report:args.report.write_text(json.dumps(result,indent=2)+'\n')
 for r in report:print(f"p{r['page']}/{r['cell']}: scale={r['diagram_scale']} circ={r['circle_scale']} gap={r['crossing_gap']} pos={r['circle_position']}: split {r['split_leg_ink_clearance_pdf_pt']:.2f}pt; continuous {r['continuous_leg_ink_clearance_pdf_pt']:.2f}pt")
if __name__=='__main__':main()
