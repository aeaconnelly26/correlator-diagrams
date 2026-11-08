#!/usr/bin/env python3
"""Verify default circle radii and label scaling across public interfaces."""
import argparse,importlib.util,json,sys
from math import hypot
from pathlib import Path
sys.dont_write_bytecode=True
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('species',ROOT/'regressions/topologies/insertion/check-species-circles.py')
species=importlib.util.module_from_spec(spec);spec.loader.exec_module(species)
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=Path);p.add_argument('--report',type=Path);args=p.parse_args()
 r=PdfReader(args.pdf);assert len(r.pages)==2;reports=[]
 for i,page in enumerate(r.pages):
  rings,dots=species.inspect_circles(page,r)
  assert len(rings)==[7,4][i]
  if i==0:
   wanted=[.8]*7
   assert sum(color[0]>.9 and color[1]<.1 and color[2]>.5 for _,color in rings)==1,'Stem circle color changed'
  else:
   rings.sort(key=lambda c:-c[0][1]);rings=sorted(rings[:2],key=lambda c:c[0][0])+sorted(rings[2:],key=lambda c:c[0][0]);wanted=[.8,1,.6,.8]
  for (ring,color),scale in zip(rings,wanted):assert abs(ring[2]-6*scale*72/72.27)<.03,'Default, explicit override or reset failed'
  fonts=[]
  def visit(text,cm,tm,font,size):
   if text.strip() in ('W','Z') and size<8:fonts.append(size*hypot(cm[0],cm[1]))
  page.extract_text(visitor_text=visit)
  assert len(fonts)==len(wanted)
  assert sorted(round(n,3) for n in fonts)==sorted(round(6.9738*s,3) for s in wanted),'Circle label scale disagrees with ring'
  reports.append({'page':i+1,'circles':len(rings),'radii_pdf_pt':[a[2] for a,c in rings],'label_font_sizes_pdf_pt':fonts})
 result={'default_scale':.8,'default_diameter_tex_pt':9.6,'default_radius_pdf_pt':4.8*72/72.27,'pages':reports,'explicit_scales_preserved':[.6,.8,1],'fresh_call_reset':True}
 if args.report:args.report.write_text(json.dumps(result,indent=2)+'\n')
 print('PASS circle default: 11 actual PDF circles and labels; raw/box/crossed-box/tree default 0.8, explicit 0.6/0.8/1 and fresh-call reset')
if __name__=='__main__':main()
