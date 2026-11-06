# Shared four-leg endpoint frame - 2026-11-06

User-directed M06 review follow-up on `codex/m06-tree-triangles`, after
checkpoint `2506354`. Still local; main/GitHub remain at `eb6182c`.

The user clarified that spans may grow if the change is consistent across
ordinary/corrected T channels, box, crossed box and triangle-contact. The
shared default adopts the existing box/crossed-box outer frame: **+/-2.10 on
both axes**. This also applies to ordinary contact pairings, s/t/u trees and
channel loops, and the supported tree insertions. Inner box dimensions,
crossing connectivity, triangle-contact vertices and the larger equilateral
regular triangle retain their existing values. Half-box and flat-contact
identity stubs keep their specialized layouts.

## Interface and precedence

`fourpoint-xspan` and `fourpoint-yspan` now control the outer endpoints across
these families. Box/crossed-box external spans and triangle-contact external
spans inherit these values by default. An explicitly supplied family-specific
external span overrides only that axis, in either key order. Defaults reset
on the next diagram.

```tex
\TTreeChannelCorr[fourpoint-xspan=2.4,fourpoint-yspan=1.8]
\BoxLoopCorr[fourpoint-xspan=2.4,fourpoint-yspan=1.8]
\CrossBoxCorr[fourpoint-xspan=2.4,fourpoint-yspan=1.8]
\TriangleContactCorr[fourpoint-xspan=2.4,fourpoint-yspan=1.8]
```

The default frame fits the larger regular T triangle without shortening its
stem. If an explicit tighter T frame needs it, the three loop vertices can
translate inward together to leave 0.28 axial clearance beyond the base.
Endpoints remain fixed at the requested corners; side lengths do not shrink.
Extreme explicit geometry can still collapse a bridge and is not certified.

## Checks and evidence

- **191 regular-triangle public cases** verify exact outer corners, including
  explicit wide/tight spans, equilateral shape, styles, annotations, caps,
  index ownership and reset. The initial `2506354` package fails the new corner
  check at `corrLL`, demonstrating that the test rejects the reported defect.
- **188 additional public cases** cover the shared frame on trees, all supported
  external bubble/seagull/swordfish placements, regular triangles, channel
  loops, contact pairings, box/crossed box and four triangle-contact orientations.
  Default and custom frames, family overrides in both key orders and fresh-call
  reset are checked through the public interfaces.
- Actual PDF strokes verify **twelve common-frame diagrams**: four regular
  triangles, then eight plain tree/box/contact comparison examples. Each
  default frame measures **119.0551 PDF pt square**, with outer endpoints at
  all four corners. The regular loop sides remain about 44.188pt and equal.
- The four styled exchanges remain wavy. All **24 Proca + 12 scalar** endpoint
  contacts retain pink outlines and white fill. The existing species checker
  also verifies all 40 circles and 32 loop endpoints.

Styled seagull W circles were retuned for the longer default legs using the
existing `circ position` option: **0.57332 (T)** and **0.57159 (S)**. These values
preserve equal visible gaps between the triangle marker, W circle and tree dot.
Bubble-host W circles retain 0.5. See the updated
[species measurements](../../regressions/topologies/insertion/species-circles.json).

The M02 annotation harness exposed PGF reciprocal overflow while computing a
near-zero Euclidean gap-center error. It now uses a maximum component error
bound of 0.007pt, which implies Euclidean error below the original 0.01pt
tolerance. The assertions are stricter; package annotation behavior was not
changed to accommodate the test.

The final maintained suite is recorded in [M06 verification](m06-verification.md)
and [checks/hashes](m06-checks.json). The prior M06 machine record is preserved
in [history](history/m06-checks-2506354.json).

## PDFs and visual review

The current [atlas](../diagram-inventory/inventory.pdf) has **102 recipes on
23 pages**. Pages 22-23 repeat existing structures to demonstrate endpoint
alignment; these are comparison recipes, not new graph topologies. All atlas
pages were rendered and inspected after the shared-default change, including
the updated triangle-contact annotations and insertion styles.

The [seven-page gallery](../../regressions/topologies/insertion/tree-triangle-slots.pdf)
contains 28 examples, including eight plain frame comparisons on its final
two pages. All pages were inspected. Older milestone PDFs/checkpoints preserve
their revision-specific geometry; the current atlas reflects the new defaults.
The initial claim that nineteen atlas pages were pixel-identical applies to
`2506354`, before this authorized cross-family default change.

Reproduce with the M06 commands in its verification record. The included
`four-leg-frame-checks.tex` is a test helper, not a standalone document.
No topology, M07 crossing feature or D01 index-position cleanup is added here.
