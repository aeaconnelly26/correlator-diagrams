# Upper external crossing: top-edge W-circle review

2026-11-07; package checkpoint `477f850`, branch
`codex/m07b-upper-external-crossing`. Visual/geometry testing only; package code
and defaults are unchanged. This records D03, separate from the completed D02
circle-scaling fix. Only the currently supported upper external crossing is tested.

[Three-page, 18-case PDF](../../regressions/topologies/box/upper-crossing-w-clearance.pdf),
[public-macro source](../../regressions/topologies/box/upper-crossing-w-clearance.tex),
[measured results](../../regressions/topologies/box/upper-crossing-w-clearance-checks.json)
and [inspection script](../../regressions/topologies/box/inspect-upper-crossing-w-clearance.py).

Each example uses EW upper external legs (slots 1/3) and
`box-top-line={ewboson,circ=W,...}`. Remaining edges are plain. No momentum,
caps or additional circles obscure the feature being reviewed.

- Page 1: circle scales 1/.8/.6 at diagram scales .8/1, centered W and default gap.
- Page 2: crossing-gap half-width .04/.08/.12 with circle scales 1/.6 at diagram scale 1.
- Page 3: circle positions .35/.5/.65 with circle scales 1/.6, diagram scale 1 and default gap.

## Observed interference

The default geometry crowds the W-circle envelope. At diagram scale 1 and
circle scale 1, the continuous upper external EW stroke overlaps its envelope
by about 0.47 PDF pt. At diagram scale .8, the overlaps are about 0.97 pt on
the split leg and 1.31 pt on the continuous leg. The circle is painted after
these propagators; its white fill can hide pieces of their strokes, so the
result can look clipped or tangled. This is a spacing issue, not ignored circle scaling.

For centered W at diagram scale 1, circle scale .8 gives about 0.73 pt minimum
clearance; .6 gives about 1.92 pt. At diagram scale .8, circle scale .6 still
has about 1.08 pt clearance, while .8 slightly overlaps the continuous wave.
These conclusions apply to the tested default EW wavelength/amplitude and geometry.

Increasing the crossing gap only clears the split upper leg: the continuous
leg still overlaps by about 0.47 pt for a full-size circle. Moving the circle
to .35 or .65 makes it closer to one of the legs; even circle scale .6 then
shows slight overlap in the tested positions. Centered .6 is the clearest of
these tested combinations. No new default is selected by this review.

## Verification and next review

The PDF compiled successfully and all three pages were rendered and inspected.
Actual PDF paths confirm six W circles / 24 interaction dots per page, the
requested circle radii, and the expected three upper external wavy fragments
plus top internal wave per diagram. The inspection samples each cubic Bezier
at 64 intervals and includes circle/propagator stroke half-widths. Negative
clearance records overlap before the white mask; these are diagnostic findings,
not a claim that the collision has been fixed. This exploratory source is not
added to the maintained acceptance suite as an overlap-free example.

D03 remains open: review a routing/spacing change that clears a full-size top
W circle from both upper EW legs at representative scales, while preserving
the shared outer endpoints and correct crossing connectivity. Keep the circle
scaling correction from D02. The current artifact is a concrete review record;
this session implements no package geometry change.

## Later default choice

The user subsequently selected `circ scale=0.8` as the package-wide default,
including label scaling. See [verification](circ-default-verification.md).
The measurements above and PDF/preview remain historical observations at
`477f850`; their explicit circle-scale cases are still reproducible. References
to the old default scale 1 in those artifacts refer to that checkpoint. With
the new default, the centered diagram-scale-1 case has about 0.73 pt clearance;
the diagram-scale-.8 case remains very tight (about .11 pt ink-envelope overlap).
This changes circle sizing, not crossing geometry; D03 is not closed as a fully
resolved spacing review.
