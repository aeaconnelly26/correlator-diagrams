#!/usr/bin/env python3
"""Measure explicit circle count/size/color/text and Proca contact in PDF output."""
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
spec=importlib.util.spec_from_file_location('boxpdf',HERE.parent/'box/check-box-external-crossing.py')
boxpdf=importlib.util.module_from_spec(spec);spec.loader.exec_module(boxpdf)
species=boxpdf.species

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=Path);p.add_argument('--report',type=Path);args=p.parse_args()
 reader=PdfReader(args.pdf);assert len(reader.pages)==3
 black=(0,0,0);blue=(0,0,1);pink=(1,0,.85);green=(0,.5,0)
 expected=[
  [[(.6,black)]*2,[(1,black)]*2,[],[]],
  [[(.5,black),(.7,blue),(.6,pink),(.8,green)]]*2+[[],[]],
  [[(.6,black)]*4,[(.5,pink),(.7,black)],[(.4,pink)],[(.6,blue)]*4]]
 reports=[]
 for i,page in enumerate(reader.pages):
  centers=boxpdf.cells(page,reader);rings,dots=species.inspect_circles(page,reader)
  assert len(rings)==sum(map(len,expected[i])),f'Page {i+1}: spurious/missing rings'
  cells=[]
  for cell in range(4):
   observed=[(ring,color) for ring,color in rings if min(range(4),key=lambda n:boxpdf.distance(ring,centers[n]))==cell]
   wanted=expected[i][cell];assert len(observed)==len(wanted)
   for scale,color in wanted:
    matches=[(ring,c) for ring,c in observed if abs(ring[2]-6*scale*72/72.27)<.025 and max(abs(c[j]-color[j]) for j in (0,1,2))<.015]
    assert matches,f'Page {i+1}, cell {cell+1}: circ size/color ignored ({scale}, {color})'
    observed.remove(matches[0])
   cells.append({'explicit_circles':len(wanted),'scales':[s for s,c in wanted]})
  texts=[]
  def visit(text,cm,tm,font,size):
   if text.strip() in ('W','Z','H') and size<8:
    texts.append({'text':text.strip(),'effective_font_size':size*hypot(cm[0],cm[1])})
  page.extract_text(visitor_text=visit)
  assert len(texts)==len(rings),'Missing/duplicate circle text'
  wanted_sizes=sorted(round(6.9738*s,3) for cell in expected[i] for s,c in cell)
  observed_sizes=sorted(round(t['effective_font_size'],3) for t in texts)
  assert wanted_sizes==observed_sizes,'Circle label scale did not follow ring scale'
  reports.append({'page':i+1,'cells':cells,'text_sizes':texts})
 # The final cell explicitly makes blue rings with pink W text. Read text
 # fill operators independently of circle stroke colors and font-size checks.
 color=(0,0,0);stack=[];label_colors=[]
 for values,op in ContentStream(reader.pages[2].get_contents(),reader).operations:
  if op==b'q':stack.append(color)
  elif op==b'Q':color=stack.pop()
  elif op==b'rg':color=tuple(map(float,values))
  elif op==b'g':color=(float(values[0]),)*3
  elif op==b'k':
   c,m,y,k=map(float,values);color=tuple(1-min(1,v+k) for v in (c,m,y))
  elif op in (b'Tj',b'TJ'):
   strings=values if op==b'Tj' else values[0]
   if any(str(v)=='W' for v in strings):label_colors.append(color)
 assert label_colors[-4:]==[pink]*4,'Circle label style override ignored'
 contacts=species.contact.inspect(args.pdf)
 assert [r['triangles'] for r in contacts]==[20,12,4],'Extra endpoint decorations on circles or missing markers'
 for report in contacts:
  assert min(report['gaps_pt'])>=-.21 and max(report['visible_gaps_pt'])<=.02,'Endpoint contact regressed'
 result={'pages':reports,'marker_contacts':36,'automatic_proca_circles':0,'circle_label_scaling':True,'circle_label_color_override':True}
 if args.report:args.report.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS D02 PDF: 3 pages / 12 cases; explicit ring counts, independent radii/colors and scaled text; 36 contacting Proca tips; no automatic circles')
if __name__=='__main__':main()
