#!/usr/bin/env python3
"""Recover reference traces and public-output external attachments from PDF paths."""
import argparse,importlib.util,json,sys
from collections import Counter
from math import hypot
from pathlib import Path
sys.dont_write_bytecode=True
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('boxes',ROOT/'regressions/topologies/box/check-box-external-crossing.py')
boxes=importlib.util.module_from_spec(spec);spec.loader.exec_module(boxes)

def recover(page,reader,expected_pairs,split):
 paths=boxes.strokes(page,reader);nodes=[];edges=[]
 def index(p):
  for i,q in enumerate(nodes):
   if hypot(p[0]-q[0],p[1]-q[1])<.03:return i
  nodes.append(p);return len(nodes)-1
 for a,b,_ in paths:edges.append((index(a),index(b)))
 unseen=set(range(len(nodes)));groups=[]
 while unseen:
  pending=[next(iter(unseen))];group=set()
  while pending:
   n=pending.pop()
   if n in group:continue
   group.add(n);pending.extend(b if a==n else a for a,b in edges if n in (a,b))
  unseen-=group;groups.append(group)
 large=[g for g in groups if len(g)>=7];small=[g for g in groups if len(g)<7]
 assert len(large)==len(expected_pairs)
 for group in small:
  assert split and len(group)==2
  owner=min(large,key=lambda g:min(boxes.distance(nodes[a],nodes[b]) for a in g for b in group));owner.update(group)
 large.sort(key=lambda g:-max(nodes[n][1] for n in g))
 if len(large)==4:large=sorted(large[:2],key=lambda g:min(nodes[n][0] for n in g))+sorted(large[2:],key=lambda g:min(nodes[n][0] for n in g))
 reports=[]
 for group,wanted_pair in zip(large,expected_pairs):
  physical=[(a,b) for a,b in edges if a in group];degree=Counter(n for e in physical for n in e)
  inner={n for n in group if degree[n]>=3};assert len(inner)==3
  xmin,xmax=min(nodes[n][0] for n in group),max(nodes[n][0] for n in group)
  ymin,ymax=min(nodes[n][1] for n in group),max(nodes[n][1] for n in group)
  corners=[(xmin,ymax),(xmin,ymin),(xmax,ymax),(xmax,ymin)]
  outer={slot:min(group,key=lambda n:boxes.distance(nodes[n],point)) for slot,point in enumerate(corners,1)}
  assert all(boxes.distance(nodes[outer[s]],point)<.03 for s,point in enumerate(corners,1))
  assert abs(xmax-xmin-4.2*.8*72/2.54)<.03 and abs(ymax-ymin-4.2*.8*72/2.54)<.03
  gap=group-inner-set(outer.values());assert len(gap)==(2 if split else 0)
  logical=[(a,b) for a,b in physical if a not in gap and b not in gap]
  if gap:
   joined=[b if a==n else a for n in gap for a,b in physical if n in (a,b)]
   assert len(joined)==2;logical.append(tuple(joined))
  degree=Counter(n for e in logical for n in e)
  assert len(logical)==7 and sorted(degree.values())==[1]*4+[3,3,4]
  assert len(logical)-len(degree)+1==1
  quartic=next(n for n in inner if degree[n]==4)
  pair=sorted(s for s,n in outer.items() if any(set(e)=={n,quartic} for e in logical));assert pair==wanted_pair,(pair,wanted_pair)
  assert sum(a in inner and b in inner for a,b in logical)==3
  dots=boxes.species.inspect_circles(page,reader)[1]
  assert all(any(boxes.distance(nodes[n],dot)<.03 for dot in dots) for n in inner)
  cubic=inner-{quartic};ix=[nodes[n][0] for n in inner];iy=[nodes[n][1] for n in inner]
  assert abs(max(ix)-min(ix)-(max(iy)-min(iy)))<.03,'Square span override ignored'
  reports.append({'quartic_external_pair':pair,'single_external_pair':sorted(set(range(1,5))-set(pair)),'logical_edges':7,'interaction_valences':[3,3,4],'cycle_rank':1,'gap_is_vertex':False,'cubic_midpoint':[sum(nodes[n][i] for n in cubic)/2 for i in (0,1)]})
 return reports

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('pdf',type=Path);p.add_argument('--report',type=Path);args=p.parse_args();r=PdfReader(args.pdf);assert len(r.pages)==3
 target=recover(r.pages[0],r,[[1,4],[2,3]],True)
 existing=recover(r.pages[1],r,[[1,3],[2,4],[1,2],[3,4]],False)
 styled=recover(r.pages[2],r,[[1,3],[2,4]],False)
 rings=boxes.species.inspect_circles(r.pages[2],r)[0];assert len(rings)==2
 for ring,color in rings:
  assert abs(ring[2]-4.8*72/72.27)<.03
  assert min(boxes.distance(ring,s['cubic_midpoint']) for s in styled)<.03,'Z circle is not between cubic vertices'
 assert not any(t['quartic_external_pair']==e['quartic_external_pair'] for t in target for e in existing)
 report={'target_traces':target,'existing_public_outputs':existing,'existing_styling_outputs':styled,'target_supported_with_fixed_external_slots':False,'new_loop_topology_required':False,'missing_capability':'Opposite quartic external pairs 1/4 and 2/3 on triangle contact','styled_circles':2}
 if args.report:args.report.write_text(json.dumps(report,indent=2)+'\n')
 print('PASS M07c PDF: two 7-edge source traces; four distinct adjacent-pair public graphs; two styled Z-edge recipes. Opposite-pair routing is absent.')
if __name__=='__main__':main()
