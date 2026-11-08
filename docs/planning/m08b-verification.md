# M08b contact-leg seagulls - 2026-11-08

Implemented R21 on `codex/m08b-contact-seagulls`, based on published main
`35c7959`; verified checkpoint `e57499e` is now merged and published (2026-11-08).
The feature branch is retained. See [publication record](m08b-publication.json). M08a checkpoint `d855152` and its publication handoff are
already merged/pushed; see [publication record](m08a-publication.json).
No M08b merge/push remains. Ready for the user's next task; M09a remains the next diagram-roadmap milestone.

The array-context validation fix is included; see [fix record](m08b-array-fix.md).
The original 149 cases are supplemented by 12 array/tabular/aligned cases.

## Interface and graph

```tex
\FourPointCorr[
  field={},central={},leg-labels={,,,},blob=false,
  line=plain,show-momenta=false,
  insertion=seagull,insertion-slot=1,seagull-loop-line=plain
]
```

Slots are physical corners: 1 UL, 2 LL, 3 UR, 4 LR. `FourPtCorr` is an alias.
Central/crossed quartic views share the insertion renderer; they are not extra
seagull topologies. Horizontal/vertical disconnected pairings and invalid or
multiple slots produce explicit errors. One insertion at a time.

Keep the original quartic contact C. Replace selected outer--C by outer--V,
V--C and one V--V self-loop. There are **six edges, two quartic interaction
vertices, four degree-one external nodes and one cycle**. No stem, artificial
bridge or pair of bubble vertices is introduced. The +/-2.10 outer frame and
compact coordinate scale .8 are unchanged.

The first-leg slice passed before expanding the all-slot test matrix. The
existing seagull path/marker/momentum helpers are reused through the M08a contact
host. M08a's private bubble wrapper remains available to its focused regression.
Ordinary contact, tree and bubble geometry is unchanged.

Defaults: position .40, scale .66, loop size 1.55, loop looseness 1.0. Slide 11's
upper loops face up and lower loops down, using the normal +90 on slots 1/4
and -90 on 2/3 from the outer-to-host direction. Explicit top/bottom retain
host-relative +90/-90; left/right remain page-relative. Position must be
strictly inside the selected leg; scale/loop size/looseness must be positive
and the host leg nonzero. Hidden external legs suppress the insertion while
preserving existing amputated endpoint placeholders. Hidden center vertices
hide both interaction dots.

## Source, styles and metadata

[The native source map](m08b-reference-map.json) covers all eight panels:
T1/T2 -> LR4, T3/T4 -> UR3, B1/B2 -> LL2, B3/B4 -> UL1. Each pair is the same
graph with neutral Z or directed W styling. B3 is the W variant and B4 the Z
variant. The editing tooltip is context only. Both archived originals remain
unchanged.

The focused gallery reproduces all eight species/charge-flow variants with
EW paths, explicit Z/W circles and raw filled charge arrows. These arrows
are separate from external momentum direction. The named pink samples retain
EW outer legs, an inner W circle, a pink two-ended scalar-polarization loop
without a circle and only its k momentum. Diagnostics omit caps/circles unless
they are the feature being demonstrated.

Logical styles, pre/post overrides and single/double outer caps reuse existing
helpers. Explicit pre-segment overrides retain the logical outer cap; post
segments and loop strips do not acquire outer caps. Momentum defaults remain
p1/p2 in, p3/p4 out. Global and per-contact directions, selected pre/post
visibility, blank labels, independent guide controls, loop direction, actual
concentric curves and outward label clearance are preserved. Four seagull
indices and independent post-segment indices remain attached. D01 index
appearance stays deferred.

Observed legacy limitation D04: combining raw `with arrow` and `circ` paints
both markings twice at identical coordinates. A probe against published
baseline `35c7959` reproduces the two coincident W rings on an existing s-tree
seagull, proving it predates M08b. The visible native page has 44 distinct
charge arrows (48 paints) and eight distinct species circles (12 paints).
The checker records both counts; PDF extraction repeats W for those four
loops. Visible positions and connectivity are correct. This is recorded for
later cleanup in [deferred workflows](deferred-workflows.md), with no broad
decorator rewrite in this feature slice.

## Verification and deliverables

- **149 public cases**: all four slots, central/crossed views, default/explicit
  positions, scales .72/1/1.2, frame overrides, orientations, hidden markers,
  styles, logical cap inheritance, pre/post overrides, momenta/visibility/blanks,
  direction reversal, vertex/post indices, aliases and consecutive state resets.
- **45 loop-label rectangles** clear their measured local normals;
  **410 curve samples** share the loop's concentric momentum geometry.
- **32 rejection cases** (16 requests in ordinary and array contexts) cover slots 0/5/lists, disconnected pairings, endpoint
  or out-of-range positions, nonpositive scale/loop size/looseness and zero leg.
  All fail with their intended package errors, not missing-node errors/no-ops.
- Independent PDF paths recover four six-edge graphs with two quartic vertices,
  one actual closed self-loop, no stem, correct selected corner, default .40
  placement, source-facing side, loop diameter and fixed outer frame.
- Visible-ink checks verify **20 new white-filled pink endpoint contacts**:
  eight two-ended Proca, four one-sided scalar and eight styled. Species/flow
  checks verify all eight source variants, 44 distinct filled charge arrows,
  48 actual wavy propagator paths and .8 circle sizing (accounting for fitting).
- The maintained suite passes **53 documents / 894 endpoint contacts**
  (the prior 874 plus 20 new); see [saved output](m08b-suite.txt).
- All **seven gallery pages** and **34 atlas pages** were rendered/reviewed;
  new atlas pages were inspected at reading size. The atlas has **146 recipes**:
  CS01-CS04 plain; CS11-CS14 selected source species/flow; CS21-CS24 pink samples.
- Atlas page bodies 1-29 and 31 are pixel-identical at 90dpi. Page 30 only removes
  the obsolete no-contact-seagull limitation; both diagram rows are identical.
  **All five M08a gallery pages remain pixel-identical**, despite sharing the
  contact host. Archived source checksums remain unchanged.

See the [gallery](../../regressions/topologies/insertion/contact-seagull-slots.pdf),
[atlas](../diagram-inventory/inventory.pdf), [recipes](../diagram-inventory/recipes.md),
[frozen contract](../../regressions/topologies/insertion/M08b-contract.md),
[PDF report](m08b-pdf-checks.json) and [checks/hashes](m08b-checks.json).

## Reproduction

From the repository root:

```sh
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/private/tmp regressions/topologies/insertion/contact-seagull-slots.tex
python3 regressions/topologies/insertion/check-contact-seagull-errors.py
python3 docs/diagram-inventory/build.py
```

Use a Python with `pypdf` for PDF assertions (the bundled runtime was used):

```sh
python3 regressions/topologies/insertion/check-contact-seagulls.py \
  /private/tmp/contact-seagull-slots.pdf
FEYNMANFUN_PDF_PYTHON=/absolute/path/to/pypdf-python scripts/check-regressions.sh
```

After future changes, render both outputs with `pdftoppm` and inspect actual
connectivity, marker contact, caps, charge/momentum flow and label clearance.
