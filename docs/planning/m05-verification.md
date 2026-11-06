# M05 external swordfish verification - 2026-11-04

Implemented on `codex/m05-swordfish` from clean published main `efb5fae`.
Checkpoint `9daebf9` was fast-forwarded into main and published on 2026-11-06;
the feature branch is retained. All recorded artifact hashes matched before
merging. This publication handoff changes documentation only; package sources,
regressions and PDFs retain the verified checkpoint content.
See [machine-readable checks and hashes](m05-checks.json).

## Reference and graph

R12 is implemented from S08-L1, checked against S08-L3 and S05-L1/L3.
Slide 9 supplies annotation context. The archived originals remain unchanged;
document contents were used as references, not instructions.

For selected external endpoint E and existing tree vertex H, replace E--H by
E--A and two parallel curved A--H edges. H is the actual tree interaction,
now quartic. A and the opposite tree vertex are trivalent. Each graph has
seven propagators, three interaction dots, four external endpoints and one
independent cycle. There is no post segment, collapsed bridge, self-loop or
duplicated interaction dot. This differs from both a self-energy bubble and
the seagull's quartic self-loop. The contract was frozen before expansion:
[M05 contract](../../regressions/topologies/insertion/M05-contract.md).

## Public interface and scope

```tex
\TTreeChannelCorr[field={},show-momenta=false,
  insertion=swordfish,insertion-slot=1]
\STreeChannelCorr[field={},show-momenta=false,
  insertion=swordfish,insertion-slot=4]
```

Both macros support slots 1/2/3/4 (upper-left/lower-left/upper-right/lower-right),
one insertion at a time. E--A inherits its logical leg style and outer cap;
`insertion-pre-line` overrides its style. `bubble-top-line` and
`bubble-bottom-line` independently style the actual A--H arcs. There are no
caps on loop ends. Selected external momentum appears once on E--A, with
p1/p2 incoming and p3/p4 outgoing. Loop momentum uses the existing independent
bubble controls; `show-channel-momentum=false` hides the exchange guide.

Default position is 0.50 and scale 0.66. The fraction from E to A is
`1-(1-insertion-position)*insertion-scale/0.66`, so scale changes the loop
chord about fixed H. `swordfish-opening-angle=60` separates tangents at H;
`bubble-loop-looseness` remains effective. Tested overrides keep A strictly
inside E--H. Extreme settings that put A beyond E or collapse it onto H are
not certified. No automatic geometry clamping is claimed.

`bubble-endpoint-indices={a_A,a_H,b_A,b_H}` preserves four arc endpoint
values/ownership. `bubble-external-indices={i,j}` labels the sole E--A segment
at fractions 0.18/0.82. Existing exchange/other-leg values remain attached.
**D01 index-position appearance remains deferred.** These tests establish
value/order/attachment, not satisfactory visual index spacing.

No post segment exists: post-line, post-momentum and post-index options are
inactive. `insertion-orientation` remains seagull-only. U/contact hosts,
internal slot 5 and simultaneous insertions are unsupported. The
`external-legs=false` master switch suppresses the swordfish; legacy outer
placeholder dots are preserved. Existing bubble/seagull behavior is unchanged.

## Incremental verification

The 40-document/688-contact baseline passed before package changes. One
placement was enabled and checked before the next:

| Enabled through | Focused public cases passed |
| --- | ---: |
| T1 | 18 |
| T2 | 36 |
| T3 | 54 |
| T4 | 72 |
| S1 | 90 |
| S2 | 108 |
| S3 | 126 |
| S4 | 144 |
| Final compatibility/visibility/reset coverage | 167 |

The final source checks real drawing dispatch, seven edges/three dots/two
arcs/no post, exact shared H, selected-slot isolation, custom geometry,
scales 0.72/1/1.2, inherited/overridden mixed styles, single/double outer caps,
momentum hiding/blank labels/reversal, loop and external index values/order,
unsupported slots and consecutive-diagram reset. Hidden-external behavior
was checked against its existing placeholder-dot semantics.

An independent PDF parser recovers strokes from all eight plain examples.
Each is connected with degrees 1/1/1/1/3/3/4, one parallel-edge pair between
A and H, the correct external endpoint and the correct T/S host. It rejects
extra bridges, wrong attachments, zero-length edges and duplicate dots.
The isolated endpoint pages pass **32 Proca and 16 scalar contacts**; tips
retain pink outlines and white fill, and their visible strokes meet the dots.
Measured visible gaps are approximately -0.173 to -0.169 PDF pt, within the
maintained contact tolerance. See [PDF graph/contact results](../../regressions/topologies/insertion/swordfish-contact.json).

The final full maintained suite passes **41 documents and 736 endpoint
contacts**: 688 existing contacts plus 48 new swordfish contacts. Existing
species-circle/optical-placement, wavelength/reset and legacy-marker checks
also pass. The focused PDF was recompiled and rechecked after caption cleanup;
package/test assertions were unchanged from the full-suite run.

## Visual deliverables

- [Six-page gallery](../../regressions/topologies/insertion/swordfish-slots.pdf):
  32 examples, with full plain T/S matrices, all-eight mixed styles, and isolated
  Proca/scalar contacts. Every page was rendered and inspected.
- [Updated atlas](../diagram-inventory/inventory.pdf): **86 recipes / 19 pages**.
  Pages 17-18 contain K01-K04 and K11-K14, plain placement matrices. Page 19
  contains K21-K24, mixed EW W / pink two-ended Z loop examples. Those species
  circles are intentional; ordinary topology/endpoint pages omit decorations.
- [Recipe index](../diagram-inventory/recipes.md) and
  [reference](../reference.md) document the interface and inactive controls.

New atlas pages were inspected for clipping, caption crowding, momentum
placement and readable connectivity. Undecorated examples with both k and ell
were additionally rendered and inspected in all eight placements. The original
sixteen atlas page bodies are pixel-identical to published main `efb5fae`
above the changed baseline footer. M04 optical-circle tuning is preserved.

## Reproduce

From the repository root, with a Python environment containing `pypdf`:

```sh
mkdir -p /tmp/feynmanfun-m05-check
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-m05-check \
  regressions/topologies/insertion/swordfish-slots.tex
python3 regressions/topologies/insertion/check-swordfish.py \
  /tmp/feynmanfun-m05-check/swordfish-slots.pdf
FEYNMANFUN_PDF_PYTHON=python3 scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
pdftoppm -scale-to 1450 -png \
  /tmp/feynmanfun-m05-check/swordfish-slots.pdf \
  /tmp/feynmanfun-m05-check/page
```

The default runner compiles documents; `FEYNMANFUN_PDF_PYTHON` enables the
independent vector checks. Local verification used the bundled Python with
`pypdf` and Pillow. TeX build metadata can change PDF byte hashes on rebuild;
the checks record the exact delivered artifacts.

## Next handoff

M05 is now merged and published. Start **M06 / R08 regular tree-attached
triangles** from synchronized main: top/bottom on T trees, left/right on S
trees. Freeze their three-trivalent-vertex loop and bridge graph first; the
existing triangle-contact graph is different. D01 remains a separate later
workflow. No M06 implementation is included here.
