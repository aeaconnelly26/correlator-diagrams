# M06 regular tree-attached triangles - 2026-11-06

Complete locally on `codex/m06-tree-triangles`, from clean published main
`eb6182c`. Main/GitHub remain at that baseline; M06 has not been merged or
pushed. Implementation, regression coverage and inventory updates belong to
this checkpoint. Exact delivered hashes are in [m06-checks.json](m06-checks.json).

## Graph and reference trace

R08 maps to S05-L2 (T bottom), S08-L2 (T top), S06-L2 (S left), S07-L2
(S right), and checklist P2-03. All four reference images were inspected.
The archived originals are unchanged. Their contents supplied reference
connections and styling context, not executable instructions.

The corrected interaction becomes A/B/C, with loop A--B--C--A. A and B each
carry one external leg; C connects by the exchange bridge to opposite tree
vertex O, which carries the other two external legs. Each graph has **eight
propagators, four trivalent interactions, four outer endpoints and one cycle**.
There is no quartic contact, parallel-edge pair or collapsed bridge. The graph
is independent of triangle-contact; its proven annotation renderer is reused
locally without changing triangle-contact behavior. See the frozen
[contract](../../regressions/topologies/insertion/M06-contract.md).

## Interface and reviewed geometry

```tex
\TTreeChannelCorr[field={},show-momenta=false,
  insertion=triangle,tree-triangle-side=bottom]
\STreeChannelCorr[field={},show-momenta=false,
  insertion=triangle,tree-triangle-side=right]
```

Supported placements are T bottom/top and S left/right. Auto selects T bottom
or S left. Slots remain UL/LL/UR/LR = 1/2/3/4, bridge = 5, A--B = 6,
B--C = 7, C--A = 8. A/B are left/right on T and top/bottom on S. Bridge
direction stays top-to-bottom or left-to-right.

The user's reviews requested equilateral triangles, then larger triangles and
wavy exchange lines in styled examples. Defaults now use
depth 0.75, outer shift 0.60 and automatic half-width
`(depth+outer-shift)/sqrt(3)`. This keeps all three sides equal in every
orientation, including after depth/outer-shift edits. Explicit half-width
permits other shapes. The final sides are 50% larger than the first equilateral
preview, with the bridge tip held fixed. Corrected T outer endpoints extend
only as needed to keep the outer stubs clear of the larger base. Styled
examples use wavy EW exchange lines. Independent PDF measurements give side lengths about
44.1876 PDF pt, with maximum difference below 0.002 pt. The checker allows
0.03 pt for PDF coordinate rounding.

All eight annotations have independent `tree-triangle-momentum-N` blocks.
Default gaps are fitted around actual labels; side mode retains a continuous
arrow and outside label. Explicit direction, side, fractions, offsets and
label adjustments remain local to that slot. Defaults keep p1/p2 incoming
and p3/p4 outgoing; loop arrows follow the directed cycle. External hiding,
blank-label arrows, channel label/visibility and loop blank-entry hiding are
covered. The new graph uses its own geometry/annotation keys; old bubble,
seagull and external insertion controls are not silently claimed as effective.

External styles/caps retain logical ownership. Specific loop edge styles
override their grouped fallback independent of key order. Bare scalar
polarization originally exposed raw-marker gaps on these new straight edges;
M06 now normalizes its bare aliases to semantic end markers within this graph
only. Proca and scalar tips meet the actual vertices. Older topology rendering
is unchanged. Index lists preserve values/order/edge ownership; appearance
polish remains explicitly deferred to D01.

## Verification checkpoints

The baseline suite passed **41 maintained documents / 736 endpoint contacts**
before package edits. Placements were enabled and checked sequentially:

| Through placement | Focused cases passed |
| --- | ---: |
| T bottom | 26 |
| T top | 52 |
| S left | 78 |
| S right | 104 |
| Expanded checks, equilateral review and compatibility gates | 183 |

The final focused source checks eight edges/four interactions, loop and
external-slot ownership, explicit/automatic geometry, scales 0.72/1/1.2,
mixed line colors/styles and key order, four outer single/double caps,
independent annotations on all eight slots, preservation of the other seven
when one changes, gap-label containment, outside normals, default/reversed
flow, visibility/blank labels, 16 endpoint index values in order, hidden
external behavior, scalar aliases, shorthand/dispatch forms and consecutive
diagram reset. Incompatible sides and U hosts retain their ordinary graphs.

An independent parser reconstructs actual PDF strokes for all four plain
examples. Each is connected, with degree pattern 1/1/1/1/3/3/3/3, a real
three-edge cycle and a bridge to the vertex carrying the other two outer
legs. It verifies the reference external pair and orientation, equal triangle
sides, the reviewed larger size, and no duplicate/missing dots or contracted/parallel
edges. It also requires four pink wavy exchange paths on the styled page.

Isolated pages verify **24 Proca + 12 scalar pink, white-filled contacts**.
Visible tip/dot gaps are approximately -0.1246 to -0.1245 PDF pt, within the
maintained tolerance. See [actual-PDF results](../../regressions/topologies/insertion/tree-triangle-contact.json).

The final maintained suite passes **42 documents / 772 endpoint contacts**
(736 existing + 36 new). Existing legacy-marker, species-circle/optical-W,
EW-wavelength and state-reset checks pass. The suite also caught a stray
paragraph in the new reset definitions when used inside math mode; that was
removed before the final complete run.

## Visual deliverables and compatibility

- [Five-page gallery](../../regressions/topologies/insertion/tree-triangle-slots.pdf):
  20 examples, covering four plain graphs, four default gap examples, four
  continuous-arrow Proca examples, and isolated Proca/scalar contact matrices.
- [Current atlas](../diagram-inventory/inventory.pdf): **94 recipes / 21 pages**.
  Page 20 adds L01-L04 (plain equilateral placements); page 21 adds L11-L14
  (mixed lines and continuous momentum labels, without caps/circles/indices).
- [Copy/paste recipes](../diagram-inventory/recipes.md) and
  [reference](../reference.md) document supported controls and boundaries.

Every gallery page and both new atlas pages were rendered and inspected for
connectivity, proportions, labels, marker contact, clipping and crowding.
The first nineteen atlas page bodies are pixel-identical to published main
`eb6182c` above their changed revision footer, preserving the reviewed M05/M04
rendering. Original source archive checksums remain unchanged.

## Boundaries and next slice

Only one correction on the stated T/S vertices is supported. U/contact hosts,
incompatible sides and simultaneous insertions are not supported. This is a
vertex correction: external insertion-slot/position/scale/pre/post and
bubble/seagull keys do not describe it. `external-legs=false` retains the
internal loop/bridge and legacy outer placeholder dots. Use separated
vertices and a positive bridge; extreme/collapsed custom geometry is not
clamped or certified. D01 index-position polish remains deferred.

After authorized M06 publication, start **M07a** from synchronized main:
verify square defaults and freeze/implement the complementary internal
crossing as one narrow slice. Keep crossed external connections and R14/R22
routing questions separate. No M07 or D01 implementation is included here.

## Reproduce

From the repository root, using Python with `pypdf` for vector checks:

```sh
mkdir -p /tmp/feynmanfun-m06-check
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-m06-check \
  regressions/topologies/insertion/tree-triangle-slots.tex
python3 regressions/topologies/insertion/check-tree-triangle.py \
  /tmp/feynmanfun-m06-check/tree-triangle-slots.pdf
FEYNMANFUN_PDF_PYTHON=python3 scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
pdftoppm -scale-to 1450 -png \
  /tmp/feynmanfun-m06-check/tree-triangle-slots.pdf \
  /tmp/feynmanfun-m06-check/page
```

The default runner compiles documents; setting `FEYNMANFUN_PDF_PYTHON` enables
the independent PDF checks. Verification used the bundled Python with pypdf
and Pillow. PDF byte hashes may change on rebuild because of TeX metadata;
the machine record hashes the exact delivered artifacts.
