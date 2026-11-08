# Deferred workflow reviews

## D01 - Systematic index-label placement review

**Source:** user's request after M03a, 2026-11-03.
**State:** acknowledged, deliberately deferred to a separate later workflow session.

Index labels currently have messy positions in the rendered diagrams. Preserving
the correct labels, logical slots, endpoints and existing controls does not imply
that their placement is visually finished. Audit and improve their positions
systematically across the package in a dedicated later session.

This is not part of M03b or the current feature-implementation sessions. Do not
retune index positions, anchors, offsets or defaults while implementing the
s-channel bubbles. Preserve working index attachment and public controls; record
placement problems without expanding the current slice to fix them.

When this later workflow is explicitly started, collect representative minimal
index examples across orientations/styles, define consistent placement rules,
inspect rendered output, and add focused regressions. Reconcile the atlas and
reference after the placement work is verified. No implementation is included
in this note.

## D02 - Crossed-box circles and per-line circle styling

**Source:** user's report during M07b, 2026-11-07.
**State:** fixed locally in the user-authorized D02 follow-up, based on
M07b checkpoint `e64cc2f`. Merge/push remains pending.

Bare Proca lines now add no circle. Explicit `circ=...`, `circ={}` and topology
circle labels still work. The manual placement pass reapplies each logical
line's resolved style in a scope, preserving scale/color/fill/label styling
without propagator endpoint decorations on the circle nodes. Explicit hiding
and fresh-call reset remain effective; topology circle-position keys are retained.

The user's exact [reproducer](reproductions/d02-cross-box-circles.tex) now
produces two W circles, each with radius 3.587 PDF pt and text scaled by .6.
The historical [observed geometry](reproductions/d02-cross-box-circles-observed.json)
records the original three circles, all radius 5.978 PDF pt. That historical
record is preserved rather than overwritten.

See [verification](d02-verification.md), the
[before/after comparison](../../regressions/topologies/cross-box/cross-box-circle-comparison.pdf)
and [three-page regression gallery](../../regressions/topologies/cross-box/cross-box-circles.pdf).
Both layouts, per-slot scales/colors, aliases, manual labels, explicit Proca
circles, hiding and consecutive-call reset are checked from actual PDF output.

## D03 - Upper external crossing versus top-edge W circle

**Source:** user's request to inspect EW upper external legs and an EW top
internal edge with `circ=W`, 2026-11-07.
**State:** demonstrated crowding; no geometry/default change made in this review.

At diagram scale 1, a default-size centered W circle overlaps the continuous
upper EW leg by about 0.47 PDF pt. Smaller centered circles help; widening the
split-leg gap alone does not clear the other leg. Off-center circles can make
the crowding worse. See the [18-case visual/geometry review](upper-crossing-w-review.md).
D03 is independent of the completed D02 scaling/unsolicited-circle fix.

The later user-selected circle default .8 improves the centered diagram-scale-1
case (about .73 pt clearance). The .8 diagram-scale case remains very tight;
D03 is still an open spacing review. See [circle-default verification](circ-default-verification.md).
