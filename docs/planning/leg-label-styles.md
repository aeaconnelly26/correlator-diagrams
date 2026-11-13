# Nested external leg-label styles

Requested 2026-11-13 on `codex/three-point-field-labels`, following checkpoint
`6ab45df`. The user selected `label-style={...}` inside each `leg-styles` entry
so label adjustments stay next to their leg's propagator style. This implements
the external-label part of [D05](deferred-workflows.md); the broader common
momentum/index naming review remains deferred.

## Interface and ownership

```tex
leg-labels={Z_\alpha,{W^+}_\gamma,{W^-}_\beta},
leg-styles={
  {ewboson,endcapp,label-style={xshift=-2pt,yshift=3pt}},
  {ewboson,endcap,label-style={xshift=5pt,yshift=3pt}},
  {endcap,spol,label-style={yshift=-3pt}}
}
```

Nested options style the external label's TikZ node; the remaining items style
the propagator. Label text still comes from `leg-labels` or `field`/`indices`.
The parser extracts metadata once per logical leg before propagator style
resolution. Ordinary style items retain their tokens and order, including
braced comma values. Styles without the nested key skip key/value parsing.
All propagator consumers use the cleaned style accessor, including box,
half-box, loop-channel defaults and insertion hosts.

The shared label renderer applies the node options after each topology's base
placement. Logical slots follow external-label order through rotations,
crossing gaps and insertion/split segments. Positive x moves right; positive y
moves up. Shifts use physical dimensions independent of diagram scale. Actual
node bounds determine the picture extent, including for PDF export/caching.
Bare path `xshift`/`yshift`, momentum annotations, endpoint indices and geometry
retain their existing behavior. Default label positions are unchanged.

`\corrset{leg-styles={...}}` supplies defaults. A per-call list replaces that
list locally. Within one leg, the last `label-style` wins; an explicit `{}` is
an empty node style. An explicit nested style replaces the complete legacy
`three-point-field-label-N-style` for that slot. When it is absent, the legacy
style still applies. No new long per-topology key names are introduced.

Sunset's first two entries style its left/right external label nodes. Its
existing segment appearance controls remain `sunset-...-line`; this follow-up
does not change sunset's propagator-slot model.

## Verification

The five-page [gallery](../../regressions/labels/leg-label-styles.pdf) has
**517 passing node/endpoint/style/reset checks**. Its 17 topology/layout pairs
cover all four three-point orientations; two-point and four-point contact;
loop channel; box; both crossed-box layouts; half-box; flat and triangle
contact; bubble/seagull insertions; bubble; and sunset external labels.
Actual transformed node centers move by the requested x/y amounts at scale .8,
while their leg endpoints stay fixed. Fresh calls restore prior placement.

Additional checks cover global/local replacement, missing/empty slots,
explicit empty nested styles, legacy precedence, duplicate keys, verbatim
braced path options, and unexpanded node options (`font=\small` and an
execution counter). The final page renders the user's all-in vertex with
`q_1,q_3,q_2`, 10pt/empty/empty propagator arrow sizes and outward momentum
layout. The rendered gallery and the isolated requested example were inspected.

The two-page earlier legacy-key gallery still passes its **48 assertions**
and is pixel-identical to its saved baseline at 144 dpi. The user's requested
example with nested styles is pixel-identical at 200 dpi to the same example
with equivalent legacy offsets.

The existing optional local cache adapter was exercised with the new syntax:
a cold build creates one external PDF, a warm build leaves its bytes and mtime
unchanged, and editing one nested `xshift` creates one new external PDF. That
adapter remains an optional ignored artifact; TikZ externalization by itself
does not track edits to these macro arguments.

Reproduce the focused checks with:

```sh
mkdir -p /tmp/feynmanfun-leg-labels
TEXINPUTS="$PWD:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-leg-labels \
  regressions/labels/leg-label-styles.tex
```

The new document is registered in `scripts/check-regressions.sh`. The maintained
suite passes all **57 documents**, registered PDF checks and **928 endpoint
contacts**. The final focused source also passes after adding the copy/paste
acceptance example and the braced-comma preservation check. Suite output and
source/output hashes are recorded in `leg-label-styles-checks.json`.
Historical evidence for the original three-point controls is retained in its
own checkpoint record. The atlas stays at 150 recipes / 36 pages; this is an
annotation interface change, with no new graph or default recipe geometry.

Local checkpoint only; performance checkpoint `9884f9b` and the label follow-ups
are unmerged/unpushed. Published main remains `7069f39`.
