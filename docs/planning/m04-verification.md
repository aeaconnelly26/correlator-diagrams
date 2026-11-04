# M04 screenshot review - 2026-11-04

Branch: `codex/m04-seagull-expansion`. Review baseline: local checkpoint
`229526e`; published main remains `b4a6ad8`. The corrections and updated
artifacts are local, not merged or pushed. D01 index appearance stays deferred.

## Compact seagull momentum refinement

The next screenshot showed that the new concentric arrow still occupied too
much of the small loop and placed k too far away. From `841b93e`, the defaults
are refined to range **0.30-0.52** (was 0.20-0.62), radial offset **6pt**
(was 9pt), and label rectangle clearance **2pt** (was 4pt). This roughly halves
the arrow length for the standard loop while retaining the same midpoint
parameter 0.41 and local-normal rule. All eight placements inherit the same
compact proportions. Explicit range, offset and distance options still win.
The custom-override case deliberately uses the previous 9pt/4pt values.

No propagator, topology, bubble annotation or index placement changes. The
222-case/88-label/800-sample focused checks and full 39-document/656-contact
suite pass. Review and inventory PDFs are refreshed; the earlier 9pt/4pt
values below describe the preceding concentric-geometry checkpoint.

## Seagull curve/label consistency follow-up

The user's follow-up screenshot identified inconsistent k placement in the S
seagull examples. Baseline for this correction: local `9124a0b`. The earlier
helper translated a copy of the loop and selected above/below/left/right from
the whole loop axis. That was shared code, but it did not give consistent local
curve placement across rotations.

The corrected helper samples a concentric outer curve from the same center as
the loop. Radius is loop radius plus the existing 9pt offset. `auto` label
fraction now means midpoint of the selected arrow interval; explicit numeric
fractions are retained. The label follows the actual tangent-derived outward
normal at that point, with measured text-rectangle clearance. Reversing flow
changes only the arrow direction. Explicit range, offset, fraction, looseness
and label-distance controls remain available.

The seagull focused regression now covers **222 public cases**, **88 actual
label rectangles** and **800 paired curve samples** across all eight host/slot
placements, orientation choices, reversal and custom loop geometry. It also
checks automatic midpoint placement and explicit numeric fraction/looseness.
Both bubble review pages retain **identical decoded PDF drawing streams** to
`9124a0b`; bubble k/ell placement and the prior host-arrow fixes are untouched.
The loop propagator, vertices, markers, caps and index placement are untouched.

The new results supersede the original 206-case/72-label seagull counts below.
Earlier evidence is preserved in [the preceding review record](history/m04-checks-9124a0b.json).
Current hashes/results remain in m04-checks.json. The full suite remains 39
registered documents and 656 endpoint contacts; no topology was added.

## Reviewed behavior

- Auto seagull loops face inward on T trees (upper legs down, lower legs up)
  and outward on S trees (left legs left, right legs right). Explicit top,
  bottom, left and right options retain their original meanings.
- Default momentum symbol is p. Four-point external slots 1/2 enter, 3/4
  leave, including the `external-momentum-flow=default` preset. Explicit
  presets/per-leg directions remain supported. Standard visible insertion
  examples use this convention; hidden reversed-flow tests remain intentional.
- Default pre guides stay on the real segment, fractions 0.15-0.65; post
  guides use 0.25-0.75. Both default to 8pt transverse offset. Short bubble
  pieces adapt toward 12pt readable arrows, capped at 90% of segment length;
  longer seagull pieces retain compact guides. Explicit fractions/extensions
  win and reset correctly between calls.
- Auto host labels clear the full text rectangle perpendicular to the guide,
  with 2pt clearance from the arrow. This applies to bubbles and seagulls.
  Explicit anchors, label fractions, distances and page-axis shifts remain.
- Only S-tree bubble k/ell labels move to measured normal placement with 4pt
  rectangle clearance. The explicit bubble label-distance key still wins.
  T-tree bubble loop label placement, 2pt distance and 8pt base arrow offset
  remain unchanged, as requested in the second screenshot review.
- No index positions, anchors, offsets or defaults were retuned.

## Current verification

All **39 maintained documents** and **656 endpoint contacts** pass after the
final corrections. The existing seven-edge/self-loop graph and marker parser
continues to pass for all eight seagulls.

`insertion-momentum-review.tex` adds **84 public-diagram cases**. It observes
actual arrow-helper directions across contact, s/t/u tree and loop channels,
box/crossed box, half-box, flat contact and all four triangle-contact layouts.
It tests all 16 bubble/seagull placements at scales 0.72/1/1.2, mixed host
styles and longer labels. **130 actual text rectangles** clear their host
arrows; short bubble arrows meet the readable target or the available-length
cap, while long guides remain compact. **32 rendered loops** satisfy the
requested inward/outward sign. Explicit all-in flow, default reset, orientation,
pre/post ranges, extended guides and fixed anchors remain usable.

The S-bubble focused source now has **64 cases and 38 emitted loop-label
checks**, measuring rectangle clearance as well as actual arrow offset and
outward label side. A 3pt explicit label-distance control proves that the new
4pt default does not override an explicit value. Existing T-bubble loop-spacing
checks still use the unchanged 8pt base offset and previous label placement.

Rendered/inspected all four pages of the new momentum review and refreshed
insertion galleries; the new review shows every s/t bubble/seagull placement
with standard external flow and no caps/circles/indices. The atlas now has
**70 recipes on 15 pages**, adding H01-H04 as annotation examples. Structural
seagull matrices show the corrected auto sides. These add recipes, not topologies.

The original 14-page baseline-identity result below belongs to `229526e`.
The reviewed defaults intentionally change that output; it is no longer a
current identity requirement. Initial hashes/results are preserved in
[the initial checkpoint record](history/m04-checks-229526e.json).
Current hashes/results are in [m04-checks.json](m04-checks.json).

Reproduce the review with:

```sh
mkdir -p /tmp/feynmanfun-m04-review
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-m04-review \
  regressions/topologies/insertion/insertion-momentum-review.tex
FEYNMANFUN_PDF_PYTHON=python3 sh scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
```

# Historical M04 implementation verification - 2026-11-03

The original implementation record follows. Its defaults/counts describe
checkpoint `229526e`; the screenshot-review contract above supersedes them.


Date: 2026-11-03. Branch: `codex/m04-seagull-expansion`.
Baseline: synchronized main `b4a6ad8`, including published M03a/M03b.
M04 is complete locally; its merge/push remains pending. Main/GitHub retain
`b4a6ad8`. No manual Git preparation is needed from the user.

## Connectivity and public interface

```tex
\STreeChannelCorr[
  field={},central={},leg-labels={,,,},show-momenta=false,
  line=plain,channel-line=plain,
  insertion=seagull,insertion-slot=4,seagull-loop-line=plain
]
```

The same interface works with `\TTreeChannelCorr`. Slots 1/2/3/4 mean
upper-left/lower-left/upper-right/lower-right. On a T tree, slots 1/3 attach
to the upper tree vertex, 2/4 to the lower. On an S tree, slots 1/2 attach
to the left tree vertex, 3/4 to the right. Exchange remains slot 5.

The selected E--H becomes E--V, V--H, plus one closed V--V self-loop.
There are seven propagator edges, four external endpoints, two trivalent
tree vertices, one quartic insertion vertex and one loop. Both loop ends
meet V. This is distinct from two-vertex self-energy bubbles, a stemmed
loop, or a swordfish sharing the tree interaction vertex.

R11 sources: PDF P2-05/P3-03; S05-C1/R1, S08-C1/R1, S06-C1/C2,
S07-C1/C2, and the repeated species variants on slides 20/21. The unchanged
[source coverage](source-coverage.md) retains every panel mapping.
See the frozen [contract](../../regressions/topologies/insertion/M04-contract.md).

The implementation reuses host-relative aliases and the existing loop, marker,
style, momentum and index machinery. Historical private helper names containing
`slotone` are retained internally. Public keys and the original T1 output stay
compatible. S seagulls use the existing S-insertion exchange momentum defaults.

## Controls and boundaries

- Pre/post host styles and arrow sizes follow the selected logical external
  slot. Explicit pre/post line overrides win. Single/double caps remain only
  on the true outer endpoints; post-segment cap tokens are stripped.
- `auto`/`bottom` select -90 degrees from the outer-to-host direction; `top`
  selects +90. `left`/`right` select absolute page angles 180/0. These retain
  the prototype's meaning. New right-side placements do not reflect text.
- The loop momentum keeps its independent label, direction, range, offset,
  label fraction and distance controls. Label side now follows the physical
  loop normal across all placements and reversal. Its default offset remains
  9pt; the closer bubble defaults are unaffected.
- Logical host momentum hiding suppresses both pre/post annotations while
  retaining the loop. Blank host labels retain arrows. Loop direction `none`
  suppresses the loop momentum. Proca and one-sided scalar markers retain
  white fill and inherited color. Loop marker/arrow sizing remains local slot
  3, shared with the existing external-slot-3 size-list entry.
- `seagull-vertex-indices` retains its original four logical values/order.
  Index anchors, offsets and defaults were not changed. Their messy appearance
  remains [D01](deferred-workflows.md), a separate later workflow.
- `insertion-post-indices` remains bubble-only. `insertion-style` is stored but
  currently not consumed; use pre/post/loop line keys. Short/custom host spans
  can need existing annotation controls. Do not infer support from compilation.
- One insertion at a time. U-tree, contact hosts and internal slot 5 remain
  unsupported. Swordfish, internal corrections and stemmed tadpoles are future work.

## Verification results

The final maintained suite passes **all 38 regression/example documents**.
Its endpoint checks cover **656 contacts**: 600 existing, 16 T bubbles,
16 S bubbles and 24 M04 seagull Proca/scalar tips.

The focused `seagull-slots.tex` verifies **206 complete public-diagram cases**:
actual seven-edge topology and endpoint degrees, selected-host aliases and
position, inherited/overridden styles, all logical momentum labels and hiding,
blank/reversed flow, all five orientation choices, single/double outer caps,
index values/order, scales 0.72/1/1.2, explicit spans/position/loop geometry,
marker selection/sizing and consecutive ordinary diagrams. Generic
`FourPointCorr` dispatch and unsupported U/contact/internal controls are included.
Coordinate-copy checks allow 0.03 TeX pt for PGF rounding.

Each placement was enabled only after passing the preceding slice. Stage counts:
T1 24, T1-T2 48, T1-T3 72, T1-T4 96; then S1 120, S2 144, S3 168, S4 192.
The final geometry/dispatcher/unsupported-host checks bring the total to 206.
**72 emitted loop labels** are measured to lie outward of their actual arrows,
including both flow directions and every orientation.

An independent PDF parser extracts all stroked paths on the first two gallery
pages. It verifies eight actual diagrams, each with seven edges, degree vector
`1,1,1,1,3,3,4`, and one closed four-cubic self-loop at the quartic point.
This does not rely on TeX helper invocation counts. The isolated Proca/scalar
pages independently verify 16/8 tips, 24 visible dots on each page, pink color,
white fill, visible ink contact and absence of buried/extra markers.

Fourteen compatibility pages have identical decoded PDF drawing streams to
`b4a6ad8`: eight original T1 variants (plain, momentum, Proca, top/left/right,
indices, mixed caps/scalar) and six ordinary tree/bubble controls across s/t/u.
The existing bubble regressions' former unsupported-seagull examples now target
unsupported internal slot 5; their existing visible galleries are unchanged.

## Visual outputs

- Focused gallery: **six pages / 32 examples**. Plain T and S placement matrices;
  representative momentum/mixed lines; dedicated cap/index/orientation controls;
  isolated Proca and one-sided scalar marker matrices. Caps and indices are
  confined to their own checks; no unnecessary circles are added.
- Atlas: **14 pages / 66 reproducible public recipes**. G01-G04 show T seagulls;
  G11-G14 show S seagulls. G01 intentionally repeats U01 to display the full
  matrix; neither aliases nor styles are counted as distinct graph topologies.
- Rendered and inspected every gallery page and all atlas pages, with readable
  reviews of changed pages 6/8 and new pages 13/14. No clipping or crowding in
  the new plain topology pages. The dedicated index panel records D01 honestly.
- Atlas pages 1-5, 7 and 9-11 are pixel-identical above the intentionally updated
  baseline footer to the prior rendering. Existing plain bubble recipes remain.

## Reproduce

From the repository root, using a Python interpreter with pypdf for vector checks:

```sh
mkdir -p /tmp/feynmanfun-m04-check
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-m04-check \
  regressions/topologies/insertion/seagull-slots.tex
python3 regressions/topologies/insertion/check-seagull-contact.py \
  /tmp/feynmanfun-m04-check/seagull-slots.pdf
FEYNMANFUN_PDF_PYTHON=python3 sh scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
```

Gallery: `regressions/topologies/insertion/seagull-slots.pdf`.
Independent numerical report: `regressions/topologies/insertion/seagull-contact.json`.
Machine-readable results/hashes: [m04-checks.json](m04-checks.json).

Next: integrate/publish M04 when authorized, then **M05 external swordfish**.
Freeze the shared interaction vertex and two-edge loop before implementing the
first placement. Keep D01 deferred beyond the current feature sessions.
