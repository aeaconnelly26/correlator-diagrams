# M07b: crossed upper external pair

Baseline: published `main` at `813736e`. Requirement R03; references P1-03
and S02-center. The original slide image is preserved as a source, not an
instruction. Implement the upper pair first; right-pair routing R04 remains
the next narrow slice.

Interface: `BoxLoopCorr[box-external-crossing=top,...]` and ordinary
`FourPointCorr[topology=box,...]`. Default `none` preserves all current
output. Other host families and the future `right` value are unsupported;
reject unsupported nonempty combinations rather than silently ignoring them.

| Slot | Outer endpoint | Loop vertex, normal | Loop vertex, top crossed |
| --- | --- | --- | --- |
| 1 | UL | TL | TR |
| 2 | LL | BL | BL |
| 3 | UR | TR | TL |
| 4 | LR | BR | BR |

Internal slots 5/6/7/8 remain left/top/right/bottom. Keep the square loop,
four trivalent interactions and one cycle. The crossing of slots 1/3 is not
an interaction. Slot 1 is split with a gap; slot 3 is continuous. Derive the
crossing from the actual leg endpoints so custom spans work. Preserve outer
corners +/-2.10 and the compact 0.8 baseline. Require positive inner/external
x half-spans and external-yspan above the top loop edge.

Styles, field circles, single/double caps, marker directions/sizes, external
field labels, momenta and endpoint indices follow logical slots. The cap
at UL changes its angle with slot 1; slot 3's outgoing momentum still belongs
to UR even though it attaches to TL. Gap endpoints are not graph vertices or
marker/index attachment points. A split leg must not duplicate its circle or
place raw legacy Proca tips at the artificial cut.

Reuse the existing full-leg style/cap/marker preparation. Limit the new
low-level path split to the selected outer leg; full logical endpoints stay
available to decorations and indices. Upper momentum defaults must be short
and clear of the crossing; retain explicit direction/visibility controls and
allow independent annotation positioning. D01 index appearance stays deferred.

Acceptance: reproduce the reference with plain and EW lines; recover actual
PDF graph/slot routing, gap and unchanged square loop; confirm the crossing
has no dot; check caps against real outer endpoints, marker contact against
real vertices, one circle per styled leg, momentum ownership/reversal/hiding,
all endpoint index values, explicit geometry/scales and fresh-call reset.
Compile the focused and maintained suites; render/inspect gallery and atlas;
save a local checkpoint with publication status and the right-pair handoff.
