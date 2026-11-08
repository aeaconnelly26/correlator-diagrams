# Crossed-vertex checkpoint - 2026-11-08

Current branch: `codex/crossed-vertex`, based on published main `bfb23ac`.
Implemented and verified locally; merge/push pending. Main and GitHub were not
changed by this session. M08b remains published. The next numbered roadmap
slice is M09a after this branch is integrated, unless the user selects another task.

## Implemented result

Exactly the two user-requested half-moon layouts, from IMG_0135/IMG_0136:
`CrossedVertexCorr[crossed-vertex-orientation=right/left]`. The two W edges lie
on the full opposite-corner diagonal through the central quartic vertex. The
curved edge joins the two cubic vertices. Its external crossover is a gap,
never a fourth interaction. The handwritten plus/minus-one labels are omitted.

This extends the existing triangle-contact graph. The
[contract](contract.md) records fixed external/internal slots and the difference
from the unimplemented angular M07c proposal. The R14/R22 fixed-slot graphs
are now available in the user-selected embedding; no extra loop family or
top/bottom variants are claimed. D01 index appearance remains deferred.

## Reproduce

```sh
mkdir -p /tmp/feynmanfun-crossed-vertex-review
TEXINPUTS="$PWD//:" pdflatex -interaction=nonstopmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-crossed-vertex-review \
  regressions/topologies/crossed-vertex/crossed-vertex-regression.tex
# Use a Python environment with pypdf:
python3 regressions/topologies/crossed-vertex/check-crossed-vertex.py \
  /tmp/feynmanfun-crossed-vertex-review/crossed-vertex-regression.pdf
python3 docs/diagram-inventory/build.py
FEYNMANFUN_PDF_PYTHON=/path/to/python-with-pypdf scripts/check-regressions.sh
```

The bundled Python used for this checkpoint is recorded in `run.json`.

## Verification evidence

- All **54 maintained documents** compile; the registered PDF checks pass.
  Previous 894 real endpoint contacts remain passing; the new gallery adds
  **34**, for **928**. Full stdout is saved in `regressions.txt`.
- `checks.json` recovers both actual PDF graphs: seven logical edges, one
  cycle, valences 4/3/3, quartic external pairs 2/3 and 1/4, and the correct
  interrupted external leg. The circle is one continuous semicircle. No
  interaction dot is present at the crossover. Tests also recover scale/span
  variants and unequal outer frames, with collinear inner/outer W segments.
- Four actual W-circle centers lie at their straight segment midpoints and
  inherit the .8 ring size. The Proca half-moons have no circles. Minimal
  topology/marker examples have no unnecessary momenta, circles or caps.
- All seven public momentum controls are exercised independently in each
  layout: a one-slot offset changes exactly one actual arrow stroke; label-only
  movement leaves all arrow strokes unchanged; hiding all momenta leaves only
  the eight visible propagator strokes. Twenty temporary PDF pages support
  these comparisons. Gallery cases also exercise reversed curved momentum,
  gap/side labels, explicit range/fraction, and default p1/p2-in, p3/p4-out flow.
- The nine-page gallery contains 28 diagrams, including a consecutive ordinary
  triangle-contact reset case. It covers one/two-ended tips, marker sizes,
  single/double outer caps, split EW/Proca legs, explicit external circles,
  endpoint indices, array alignment, representative scales and custom spans.
  Index appearance is preserved rather than retuned. Slot 6 indices follow
  the curve. No unknown-key, overfull or underfull warnings occurred.
- Eight invalid requests (ordinary text and math arrays) fail explicitly.
  The validation does not introduce alignment-tab `&&` expressions.
- The atlas has **150 recipes / 36 pages**, with stable CV01/CV02 plain and
  CV11/CV12 styled recipes on pages 35/36. All pages were rendered and reviewed;
  both new pages and the gallery were inspected at reading size. The previous
  34 atlas page bodies are pixel-identical at 90 dpi after excluding the
  provenance footer; see `atlas-pixel-check.json`.
- Existing four triangle-contact orientations, working APIs, and the .8
  coordinate baseline remain unchanged visually. Their automatic internal
  label fraction still resolves to .50; only new curved-edge defaults use
  shoulder positions. The local thesis source, PDF, and package snapshot under
  ignored `output/` were not edited.

Saved deliverables: [gallery](gallery.pdf), [current atlas](../../diagram-inventory/inventory.pdf),
[recipes](../../diagram-inventory/recipes.md), and [public controls](../../reference.md#crossed-vertex-correction-two-half-moon-layouts).
Hashes of tested sources and PDF outputs are recorded in `run.json`.
