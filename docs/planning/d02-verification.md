# D02 crossed-box circle fix - 2026-11-07

User-authorized follow-up on `codex/m07b-upper-external-crossing`, based on
M07b checkpoint `e64cc2f`. Both changes remain local; merge/push is pending.

## Result on the exact user example

The [original command options](reproductions/d02-cross-box-circles.tex) are
unchanged. Before the fix they produced three circles: two W rings and an
unsolicited empty black circle on the pink Proca diagonal. All ring radii
were 5.978 PDF pt despite `circ scale=.6`. After the fix there are exactly
two W rings, each radius 3.587 PDF pt, and W text is also scaled by .6.

[Before/after comparison](../../regressions/topologies/cross-box/cross-box-circle-comparison.pdf),
[three-page focused gallery](../../regressions/topologies/cross-box/cross-box-circles.pdf)
and [machine-readable checks](../../regressions/topologies/cross-box/cross-box-circles-checks.json).
The comparison embeds equal-size vector crops, generated from the archived
baseline package and corrected package. Historical defect geometry remains
preserved in `reproductions/d02-cross-box-circles-observed.json`.

## Implementation and compatibility

Bare Proca no longer implicitly requests a blank circle. Explicit `circ=Z`,
`circ={}`, circle aliases and topology circle labels still work. The manual
placement pass reapplies each logical edge's resolved style in a drawing scope,
retaining its circle scale/size/fill/draw/label style and color. Circle nodes
start fresh paths, so propagator endpoint decorations are not repeated on the
rings; rings are solid. Explicit hide-all and fresh-call reset remain supported.
Existing topology circle-position controls retain their meaning and precedence.
No endpoint, external routing, momentum or index geometry is changed.

The removed automatic blank-ring behavior is the intentional compatibility
change requested by the user. To retain that appearance, request `circ={}`
on the relevant line. A06 already does so; its explicitly requested ring now
correctly inherits pink from the line instead of being black.

## Verification

The focused gallery covers 12 public examples across both internal layouts:
exact user options at circle scales .6 and 1, bare Proca, independent scales and
colors on slots 5-8, explicit hiding, fresh-call reset, manual labels, aliases,
explicit circles on continuous/split Proca and ring/label style overrides.
Actual PDF paths check circle counts, independent radii/colors and scaled text;
all 36 Proca tips contact the real vertices with no duplicate circle-node tips.

All **49 maintained documents / 850 endpoint contacts** pass. The suite includes
both the new gallery and comparison source and runs the independent circle
checker. Full-suite results are recorded in
[d02-regression-results.txt](d02-regression-results.txt) and [d02-checks.json](d02-checks.json).

The atlas has **122 recipes / 28 pages**, adding P31-P34. All previous page
bodies are pixel-identical at 90dpi except page 7's requested color fix for
A06's explicit Proca ring; footer provenance is excluded. The new page and
changed page 7, all three focused pages and the comparison were rendered and
inspected for clipping/legibility. The archived source PDF/PPTX are unchanged.

D01 index appearance remains deferred. R04 right external-pair routing is still
the next M07b slice after authorized publication; this fix adds no new topology.
