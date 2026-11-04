# M02 triangle-contact annotation contract

Baseline: `6657735`. Branch: `codex/m02-triangle-contact-annotations`.
Requirement R06; preserve the four R07 graphs. No new connectivity or insertions.

Slots 1-4 remain upper-left, lower-left, upper-right, lower-right external
legs. Slots 5-7 follow the existing internal directed endpoints for each
orientation (see the reference); arrow reversal never renumbers them.

Public additions: `triangle-contact-momentum-1={...}` through
`triangle-contact-momentum-7={...}`. Each accepts `start`, `end`, `offset`,
`label-fraction`, `label-gap`, `label-offset`, `label-xshift`, `label-yshift`,
`label-anchor`, and `side=outside|inside|left|right`. Fractions use the directed
edge endpoints, offset dimensions use TeX units, and label shifts affect only
the label. `side` controls the perpendicular side of the arrow and label.
Default label offset is 6pt outside external arrows and 0pt on internal arrows;
the external clearance avoids crowding on short legs. An explicit zero restores
inline external labels. Very long labels can still require manual tuning.

Existing grouped external/internal options remain fallbacks. Explicit grouped
ranges/fractions must take effect on every selected slot. Existing tuned ranges
remain the defaults via `auto`; per-slot values take precedence regardless of
key order. Unspecified per-slot fields inherit the group. Each macro call resets
its overrides. Existing direction, visibility, style, index, and momentum-off
controls retain their logical slots. Blank external labels keep a continuous
unlabeled arrow; blank internal entries keep their existing omission behavior.

Acceptance: all four orientations, unequal spans, mixed EW/Proca lines,
individual changes to each of seven slots, reversed directions, grouped keys,
hidden/blank momenta, and consecutive diagrams. Check emitted coordinates and
label anchors, outside half-planes, unaffected slots, existing regressions,
and all pages of a minimal rendered gallery. No unnecessary caps/circs.
