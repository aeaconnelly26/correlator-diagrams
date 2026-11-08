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
**State:** code-path cause confirmed; preserve compatibility during the upper
external-routing slice and fix in a dedicated narrow follow-up.

CrossBoxCorr currently adds empty black circles to Proca diagonals automatically.
`cross-box-circs=false` suppresses these (and explicit crossed-box circles).
Circle options inside `box-line` or a specific crossed-box line are applied only
inside the propagator's drawing scope; the separate manual circle-placement
pass consequently loses `circ scale`, color, and other line-local settings.
This is distinct from ordinary BoxLoopCorr's inline circle decoration. The new
M07b external routing must preserve inline circle scaling and ownership.

Follow-up acceptance: remove automatic circles unless explicitly requested,
with a documented compatibility decision; carry each logical line's circle
scale/color/fill/label style to the manual circle pass; verify both internal
layouts, specific-slot overrides, split diagonals, hidden circles and consecutive
calls. Inspect actual circle diameters/colors and label sizes in a focused PDF.

Exact user example: [reproducer](reproductions/d02-cross-box-circles.tex).
The compiled output has two W rings plus an empty black ring on the Proca up
diagonal. All three radii measure 5.978 PDF pt despite the requested 0.6 scale;
the expected scaled radius is 3.587 PDF pt. See
[observed geometry](reproductions/d02-cross-box-circles-observed.json).
