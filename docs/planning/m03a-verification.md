# M03a verification - all external t-tree bubble slots

Baseline: synchronized main at `b917ed2`. Implementation branch:
`codex/m03a-t-tree-bubbles`. R09 is complete; R10 remains M03b.
Verified checkpoint `2c3b467` is merged into main and published to GitHub.
Closeout changes only documentation; package code and PDFs match verification.

The user accepts the current index appearance temporarily. Its messy positioning
is explicitly deferred to a separate later workflow, [D01](deferred-workflows.md),
not the s-channel implementation sessions. The index checks below establish
attachment/controls, not publication-quality positioning.

This record describes the M03a checkpoint. M03b subsequently completes S-tree
external bubbles; see [current verification](m03b-verification.md) for the updated
handoff and inventory. Historical counts and scope below are retained.

## Connectivity and interface

Use the existing public interface:

```tex
\TTreeChannelCorr[
  field={},central={},leg-labels={,,,},line=plain,channel-line=plain,
  show-momenta=false,insertion=bubble,insertion-slot=2,
  bubble-top-line=plain,bubble-bottom-line=plain
]
```

Slots 1/2/3/4 are upper-left/lower-left/upper-right/lower-right. Exactly one
external edge E--H becomes E--A, two A--B arcs, then B--H. A and B are distinct
trivalent vertices. The full graph has eight propagators, four interaction
vertices, four external endpoints and one loop. The exchange and other three
legs retain their logical identities. This is not a seagull or swordfish.

The host endpoint map replaces slot-1 coordinate assumptions in geometry,
pre/post style inheritance, momentum labels/sizes/directions/visibility, and
indices. No text or slot lists are reflected. a/b remain the +90/-90 arcs along
the outer-to-tree direction. Existing bubble-local size slots 3/4 are retained;
these still share the size list with ordinary external slots 3/4.

The post segment strips external caps. Host caps stay at the true outer endpoint.
Pre/post momentum label positions default to auto: above upper legs and below
lower legs, while explicit positions win. Existing page-axis shifts remain
page-axis shifts; their default numerical values were not broadly retuned.
The exact scope is in the [contract](../../regressions/topologies/insertion/M03a-contract.md)
and [public reference](../reference.md).

## Verification

- Preserved the slot-1 baseline, then enabled and checked slot 2 (22 focused
  cases), slot 3 (32 cases), and all four slots (51 initial full-matrix cases).
  The loop-spacing review adds an explicit-offset case: 52 cases total.
- The focused public-diagram checks count actual propagator/vertex rendering
  calls, verify selected pre/post and both arc endpoints, verify that A/B are
  ordered on the intended host leg, and preserve the other legs. Collinearity
  allows 0.03pt for PGF polar/copy rounding.
- Mixed style inheritance, host momentum identity/visibility, blank labels,
  reversed host/loop directions, four bubble endpoint indices plus independent
  post indices, explicit caps on post styles (stripped), outer-only double caps,
  scale/position overrides and consecutive plain diagrams pass. Unsupported
  internal-slot/seagull-slot/s-tree controls remain unchanged.
- All **36 maintained regression/example documents pass**. The original
  **600 automatic endpoint contacts** pass unchanged. The new isolated page
  passes **16 Proca contacts** across all four placements, including white fill,
  pink color, vertex counts and visible ink contact at representative scales.
- At checkpoint `04f3913`, the original slot-1 regression was compiled before and after. Text content
  matches; maximum PDF text displacement is 0.014pt from coordinate-copy/polar
  rounding. Side-by-side renders retain connectivity, styles and tuned placement.

## Loop-spacing review

The user's screenshots exposed a separate label-side error: local arc a was
always labeled above and b below, which faces inward when those arcs swap
page sides on right-hand legs. Label placement now uses the actual arc normal,
independent of identity and clockwise/counterclockwise direction. Upper labels
sit above their arrows, lower labels below; near-vertical placements use the
appropriate left/right side. This shared bubble renderer also covers standalone
bubbles. No arc identities, propagator styles, momentum directions or geometry
are changed by this review.

Base default arrow offset is reduced from 12pt to 8pt; the existing 2pt clearance
for standard wider line styles remains. Explicit offsets/distances still work.
The current gallery intentionally differs from the pre-review slot-1 default
momentum spacing. The earlier baseline comparison above records the initial
expansion checkpoint, not a promise to retain the old spacing after this request.

The focused test now checks 34 actually rendered loop labels against their
outward normals and measures arrow clearance from the unshifted curve. It covers
all four placements, reversed directions, default spacing and an explicit 12pt
override. All 36 maintained documents and both contact checks still pass.

Reproduce the full suite, including both vector checks, with Python containing
`pypdf`:

```sh
FEYNMANFUN_PDF_PYTHON=python3 scripts/check-regressions.sh
```

Run just the new vector check on the gallery:

```sh
python3 regressions/topologies/insertion/check-t-tree-bubble-contact.py \
  regressions/topologies/insertion/t-tree-bubble-slots.pdf
```

The [machine-readable record](m03a-checks.json) pins the package hash/counts.
The [new vector report](../../regressions/topologies/insertion/t-tree-bubble-contact.json)
records actual measured gaps rather than only successful compilation.

## PDFs and inventory

The [four-page gallery](../../regressions/topologies/insertion/t-tree-bubble-slots.pdf)
has 16 examples: four plain graphs; logical momenta/mixed styles; dedicated
cap/index/position controls; and an isolated pink-Proca page. All pages were
rendered and inspected. Caps/indices appear only in examples checking them;
the topology/contact checks have no unnecessary caps or circles.

The [atlas](../diagram-inventory/inventory.pdf) now has 54 recipes on eleven
pages. I29 retains slot 1; B02-B04 add the other slots on page 6. Existing
structural/styling recipes remain; the requirement map and README/reference
are updated. Original supplied references remain unchanged.

## Remaining scope and handoff

S/u hosts, internal slot 5 and simultaneous insertions are unsupported. Seagulls
still support only t-tree slot 1. Accepted unsupported insertion keys can be
no-ops; they are not counted as capabilities. Bubble a/b follow the host direction;
`insertion-orientation` remains a seagull control. Unusually short/degenerate
host segments or large manually shifted labels/indices may need explicit tuning.

M03b is next: the corresponding s-tree slots, one placement at a time, beginning
with a frozen slot-1 contract. Use synchronized main, which includes this M03a
checkpoint. Preserve index behavior without retuning appearance; D01 is later.
