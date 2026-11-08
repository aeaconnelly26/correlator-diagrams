# M07b upper external-crossing slice - 2026-11-07

Implemented R03 (P1-03 / S02-center) locally on
`codex/m07b-upper-external-crossing`, based on published `main` at `813736e`.
This checkpoint is not merged or pushed. M07b's right external pair (R04 /
S03-center) remains the next narrow slice; M07c source-routing gates follow.

## Interface and connectivity

`BoxLoopCorr[box-external-crossing=top]` and
`FourPointCorr[topology=box,box-external-crossing=top]` retain the square loop.
Logical external slots 1/2/3/4 remain UL/LL/UR/LR. Slot 1 connects UL to TR,
slot 3 connects UR to TL; lower attachments and internal slots 5-8 are unchanged.
There are eight logical edges, four trivalent interaction vertices, four outer
endpoints and one cycle. The upper crossing is not an interaction.

Slot 1 is split about the actual intersection fraction, derived from the
inner/outer spans. `box-external-crossing-gap=.04` controls its fractional
half-width. Default `none` retains prior output. Invalid geometry/gaps,
unsupported hosts and the future `right` choice are rejected explicitly.
The shared +/-2.10 outer frame and compact 0.8 coordinate baseline are retained.

The existing full-leg style/cap/marker pipeline is reused; only its physical
stroke callback is replaced for the split edge. Circle decoration is applied
once over the full logical leg, retaining line-local scale/color/position.
Legacy raw Proca overrides use one-sided fragment decorations so the cut ends
receive no tips. Caps and endpoint indices use real endpoints and new tangents.

Upper momentum guides default at fraction .23 near their outer endpoints,
with compact spans and measured gaps. New `box-external-momentum-1..4` blocks
support independent direction, label, layout, side, shifts and positions, after
legacy global controls. Visibility masks and global momentum off still apply.
Unchanged lower guides use the legacy renderer unless a block opts them into
the measured renderer. The displayed momentum samples explicitly use side
labels on the two short lower legs. D01 index appearance is deliberately deferred.

See the [frozen contract](../../regressions/topologies/box/M07b-contract.md),
[reference](../reference.md), [gallery source](../../regressions/topologies/box/box-external-crossing.tex)
and [four-page gallery](../../regressions/topologies/box/box-external-crossing.pdf).

## Evidence

- 52 focused public calls check graph slots, full-endpoint cap/index ownership,
  all 16 endpoint index values, momentum directions/visibility/reversal,
  independent shifts/layouts, legacy placement overrides, mixed styles,
  explicit dimensions, scales .72/1/1.2 and fresh-call reset.
- Four negative compilations reject unsupported host/right choice, bad gap
  and invalid geometry rather than treating a successful no-op as support.
- Independent PDF reconstruction recovers four eight-edge/one-cycle graphs,
  the unchanged loop perimeter, correct upper routing and actual gap geometry.
  Explicit rectangular dimensions and smaller scale are checked too.
- Actual PDF geometry verifies 23 marker triangles, 14 real-vertex contacts,
  no tips at artificial cut ends, four circles with radius 3.587 PDF pt
  (`circ scale=.6`), and 12 single/double cap bars following the correct
  tangent. Double-capped wavy paths meet their inner bars.
- All **47 maintained regression/example documents** pass, with the previous
  **800 endpoint contacts plus 14 new vertex contacts**. The new graph and
  rejection checker is included in `scripts/check-regressions.sh`.
  [Recorded output](m07b-regression-results.txt) and [machine-readable checks](m07b-checks.json).
- Existing five-page box regression is pixel-identical at 90dpi against a
  fresh compile using the archived `813736e` package.
- Atlas is **118 recipes / 27 pages**. P21-P24 add minimal plain/EW/Proca and
  external-momentum examples. All 26 previous page bodies are pixel-identical
  at 90dpi (footer provenance excluded). All pages were rendered and inspected;
  the new page and all four gallery pages were checked at reading size. No
  clipping, overfull boxes or unnecessary caps/circles in topology diagnostics.
- Original archived PDF/PPTX checksums still match the source manifest.

## Recorded user defect and handoff

The user's exact CrossBoxCorr example is preserved as
[D02's reproducer](reproductions/d02-cross-box-circles.tex), not advertised as
an acceptance example. Its current output has two W circles and an unwanted
empty black Proca circle. All radii are 5.978 PDF pt despite requested .6 scale;
the line-local options do not reach the separate manual circle-placement pass.
See [observed output geometry](reproductions/d02-cross-box-circles-observed.json)
and [deferred workflows](deferred-workflows.md). Crossed-box implementation and
its historical circle defaults were not changed in this upper-routing slice.

After authorized merge/push, implement R04's right-pair routing from S03-center
with its own slot/gap contract and focused checks. Keep D01, D02 and M07c source
questions explicit; do not treat them as completed by R03. The assistant handles
Git work; no manual preparation is required from the user.
