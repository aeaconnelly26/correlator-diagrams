# M02 triangle-contact annotation contract

Baseline: `6657735`. Branch: `codex/m02-triangle-contact-annotations`.
Requirement R06; preserve the four R07 graphs. No new connectivity or insertions.

Slots 1-4 remain upper-left, lower-left, upper-right, lower-right external
legs. Slots 5-7 follow the existing internal directed endpoints for each
orientation (see the reference); arrow reversal never renumbers them.

Public additions: `triangle-contact-momentum-1={...}` through
`triangle-contact-momentum-7={...}`. Each accepts `start`, `end`, `offset`,
`label-fraction`, `label-gap`, `label-offset`, `label-xshift`, `label-yshift`,
`label-anchor`, `layout=gap|side`, and `side=outside|inside|left|right`. Fractions use the directed
edge endpoints, offset dimensions use TeX units, and label shifts affect only
the label. `side` controls the perpendicular side of the arrow and label.
Reviewed defaults: gap labels sit on the arrow line with a break fitted to the
actual rendered node. External auto arrows are compact (at most 24pt in diagram
units). Quartic-side label/range centers are at fraction 0.30 from the outer end,
other external centers at 0.50; this follows orientation. Internal default ranges
remain unchanged. Side layout uses one continuous arrow and an outward label,
with an automatic boundary anchor and 3pt clearance. Set the layout globally
with `triangle-contact-momentum-layout`, or independently in any slot. Manual
off-axis labels never leave an empty gap behind. Very long labels can still
require tuning, a smaller font, or side layout.

Existing grouped external/internal options remain fallbacks. Explicit grouped
ranges/fractions must take effect on every selected slot. Per-slot values take precedence regardless of
key order. Unspecified per-slot fields inherit the group. Each macro call resets
its overrides. Existing direction, visibility, style, index, and momentum-off
controls retain their logical slots. Blank external labels keep a continuous
unlabeled arrow; blank internal entries keep their existing omission behavior.

Acceptance: all four orientations, unequal spans, mixed EW/Proca lines,
individual changes to each of seven slots, reversed directions, grouped keys,
hidden/blank momenta, and consecutive diagrams. Check emitted coordinates and
label anchors, outside half-planes, unaffected slots, existing regressions,
and all pages of a minimal rendered gallery. No unnecessary caps/circs.
Review checks also require actual node centers inside default gaps, compact
default arrows/breaks, correct quartic-slot placement, a single stroke in side
mode, and per-slot mixing of layouts without moving other annotations.
