# M06 regular tree-attached triangles - 2026-11-06

Verified checkpoint `629356d`, implemented on `codex/m06-tree-triangles`
from `eb6182c`, is now merged and published on main (2026-11-06). The feature
branch is retained. Publication used a fast-forward; the tested package and
PDFs are unchanged. See [publication record](m06-publication.json). Exact delivered hashes are in [m06-checks.json](m06-checks.json).
The subsequent [compact scale review](scale-baseline-verification.md) applies
the 0.8 coordinate baseline throughout and refreshes the PDFs. The later
[S-exchange review](s-tree-span-verification.md) lengthens ordinary S exchanges
while leaving all seven triangle gallery pages pixel-identical. The
[endcap fix](insertion-endcaps-verification.md) preserves logical caps across
outer segment overrides and adds four cap-only atlas recipes.

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
preview. The final shared-frame review sets ordinary trees, boxes and
triangle-contact outer endpoints to +/-2.10 on both axes. That fits the large
triangle while retaining its exchange stem. Explicit custom spans are honored;
T triangles translate inward only if an explicitly tighter frame requires it.
Styled examples retain wavy EW exchange lines. Independent PDF measurements give side lengths about
35.356 PDF pt at the compact baseline (44.1876 before rebasing), with maximum difference below 0.002 pt. The checker allows
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
| Expanded checks and equilateral/size review at 2506354 | 183 |
| Endpoint alignment, exact default/custom outer frames | 191 |

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
Visible tip/dot gaps are approximately -0.1763 to -0.1741 PDF pt, within the
maintained tolerance. See [actual-PDF results](../../regressions/topologies/insertion/tree-triangle-contact.json).

The final maintained suite passes **45 documents / 772 endpoint contacts**
(736 existing + 36 new). Existing legacy-marker, species-circle/optical-W,
EW-wavelength and state-reset checks pass. The suite also caught a stray
paragraph in the new reset definitions when used inside math mode; that was
removed before the final complete run.

## Visual deliverables and compatibility

- [Seven-page gallery](../../regressions/topologies/insertion/tree-triangle-slots.pdf):
  28 examples, covering four plain graphs, four default gap examples, four
  continuous-arrow Proca examples, and isolated Proca/scalar contact matrices.
- [Current atlas](../diagram-inventory/inventory.pdf): **106 recipes / 24 pages**.
  Page 20 adds L01-L04 (plain equilateral placements); page 21 adds L11-L14
  (mixed lines and continuous momentum labels, without caps/circles/indices).
- [Copy/paste recipes](../diagram-inventory/recipes.md) and
  [reference](../reference.md) document supported controls and boundaries.

Every gallery page and all atlas pages were rendered and inspected for
connectivity, proportions, labels, marker contact, clipping and crowding.
The cross-family span change intentionally updates earlier default diagrams;
the previous first-nineteen-pages identity claim applied to checkpoint 2506354.
Box/cross-box inner geometry and all graph connections remain unchanged.
Original source archive checksums remain unchanged.

## Endpoint-alignment and shared-frame review

Checkpoint `2506354` enlarged selected T endpoints to fit the triangle. The user
clarified that spans could change, provided they changed consistently across
ordinary/corrected trees, box, crossed box and triangle-contact. The final
solution adopts the existing box frame, +/-2.10 on both axes, as the common
default, with global span keys and explicit family overrides honored.

All 191 triangle cases assert their requested outer corners. Another 188
public cases check common/default/custom frames across trees, all supported
external bubble/seagull/swordfish slots, regular triangles, channel loops,
box/crossed box and four triangle-contact orientations. Family overrides are
checked in both key orders, followed by fresh defaults. Independent PDF paths
measure the common 4.2 by 4.2-unit logical frame (95.2441pt square
at the compact baseline, nominal before PGF rounding) in four regular
triangle graphs and eight additional tree/box/contact comparisons, while
retaining equilateral triangles (approximately 35.356pt sides at the
compact baseline) and wavy styled exchanges.

Styled seagull W-circle positions were retuned to preserve their measured
optical centering on the longer legs. The existing 40-circle / 32-contact check
passes. A near-zero `veclen` calculation in the M02 test harness overflowed;
its replacement component bound is stricter than the original Euclidean
0.01pt criterion. Package annotation logic was unchanged. See
[shared-frame verification](four-leg-frame-verification.md).
The initial M06 record is preserved in [history](history/m06-checks-2506354.json),
and the pre-rebase shared-frame checkpoint in
[ad9592b history](history/m06-checks-ad9592b.json). The compact-scale checkpoint
is preserved in [97ecd10 history](history/m06-checks-97ecd10.json), and the pre-endcap-fix
record in [b1d84eb history](history/m06-checks-b1d84eb.json).

## Boundaries and next slice

Only one correction on the stated T/S vertices is supported. U/contact hosts,
incompatible sides and simultaneous insertions are not supported. This is a
vertex correction: external insertion-slot/position/scale/pre/post and
bubble/seagull keys do not describe it. `external-legs=false` retains the
internal loop/bridge and legacy outer placeholder dots. Use separated
vertices and a positive bridge; extreme/collapsed custom geometry is not
clamped or certified. D01 index-position polish remains deferred.

M06 is published. Start **M07a** next from synchronized main:
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
