# Three-point external field-label placement

Requested 2026-11-13 for `Z_\alpha`, `W^+_\gamma`, and `W^-_\beta` in the
user's all-in three-point vertex. Implemented on `codex/three-point-field-labels`,
based on local performance checkpoint `9884f9b`. This is an external field-label
follow-up; D01 internal/endpoint index appearance remains deferred.

## Public controls

```tex
three-point-field-label-1-style={xshift=-2pt,yshift=3pt},
three-point-field-label-2-style={xshift=5pt,yshift=3pt},
three-point-field-label-3-style={yshift=-3pt}
```

These are TikZ node styles applied after each orientation's existing coordinate
placement. Slots follow `leg-labels`, including after rotations. Positive x is
right and positive y is up; shifts use physical points independent of diagram
scale. Empty styles retain the old placement. Global styles can be supplied
through `corrset`; per-call replacements remain local to the diagram.

The labels retain their true node bounds, so moving a label updates the picture
extent used by PDF export/caching. No text-width or invisible-box workaround is
used. Propagator geometry, momentum-label placement, flow and indices are unchanged.

## Verification

The two-page [focused gallery](../../regressions/topologies/three-point/three-point-field-labels.pdf)
compiles with **48 assertions on actual node centers**. Four orientations each
check all three x/y displacements and a fresh call with the global defaults
restored. The user's unmodified example has byte-identical PDF drawing content
before/after this change. The adjusted default-orientation example was rendered
and visually inspected. The original atlas and recipes are unchanged because
no defaults or topology were changed.

Reproduce the focused checks with:

```sh
mkdir -p /tmp/feynmanfun-field-labels
TEXINPUTS="$PWD:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-field-labels \
  regressions/topologies/three-point/three-point-field-labels.tex
```

The new document is registered in `scripts/check-regressions.sh`. Source and
evidence hashes are recorded in `three-point-field-labels-checks.json`.

The complete maintained suite passes: **56 documents**, all registered PDF checks,
and **928 endpoint contacts**. The atlas stays at 150 recipes / 36 pages. This
branch includes performance checkpoint `9884f9b`; neither it nor this field-label
follow-up has been merged or pushed. Published main remains `7069f39`.
