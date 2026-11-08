# Circle default scale 0.8 - 2026-11-07

User-authorized package-wide default change on
`codex/m07b-upper-external-crossing`, based on review checkpoint `a90e6f0`.
The implementation sets the initial ring diameter to 9.6pt and label scale to
0.8. Nothing changes outer endpoints, coordinate scale, propagator paths,
momentum directions or index placement. Merge/push remains pending.

The `circ scale` key still uses its existing 12pt reference. Explicit .8 is
identical to the new default; explicit 1 restores the former 12pt diameter
and full-size label. Explicit .6 stays 7.2pt with label scale .6. Explicit
`circ size` and `circ label scale` remain independent controls. This avoids
shrinking recipes that already chose a scale.

[Two-page focused gallery](../../regressions/propagators/circ/circ-default-scale.pdf),
[source](../../regressions/propagators/circ/circ-default-scale.tex) and
[actual PDF measurements](../../regressions/propagators/circ/circ-default-scale-checks.json).

The focused PDF checks 11 circles and their labels across raw propagators,
ordinary boxes, internal crossed boxes and S-tree exchange lines. All defaults
measure radius 4.782 PDF pt (9.6 TeX pt diameter), and label sizes agree with
scale .8. Explicit .6/.8/1 and a subsequent unset call verify override semantics
and reset. The pink stem circle retains its line color. Both pages were
rendered and inspected at reading size.

All **50 maintained documents / 850 endpoint contacts** pass. The focused
source and independent PDF checker are part of the maintained suite. All 29
atlas pages were rendered and visually reviewed; the new page was checked at
reading size. Full results are recorded in `circ-default-regression-results.txt` and
`circ-default-checks.json`. The atlas is rebuilt at **126 recipes / 29 pages**,
adding P41-P44 for the new default, explicit former size and cross-family
examples. Existing recipes with unset circle sizes intentionally change;
explicit scales remain unchanged.

D03 upper-crossing clearance remains a separate geometry review. The new
centered .8 circle clears the continuous upper leg by about .73 PDF pt at
diagram scale 1 in the previously measured case. At diagram scale .8 it remains
very tight. The older 18-case review remains a checkpoint-specific record;
this default change is not a claim that all possible style/scale collisions
are resolved.
