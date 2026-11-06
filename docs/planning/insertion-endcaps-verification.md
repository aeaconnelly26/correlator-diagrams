# Insertion outer-endcap fix - 2026-11-06

User-reported T-channel defect, reproduced on `b1d84eb`. An external leg
requested `endcapp`, but an explicit `insertion-pre-line=ewboson` replaced
the selected outer segment's entire style and dropped its cap. The focused
test rejects the old package with **three outer caps instead of four**.

Bubble, seagull and swordfish insertions now preserve cap metadata from their
logical external leg when overriding the outer segment appearance. This
shared path covers all four external slots on both T and S trees. Only caps
are inherited: circles, species labels and polarization styles are not
copied into the explicit override. Explicit segment cap settings take
precedence; they do not accumulate a duplicate logical cap. The inner post
segment and loop handling are unchanged.

```tex
\TTreeChannelCorr[
  line={ewboson,endcapp},
  insertion=bubble,insertion-slot=3,
  insertion-pre-line=ewboson,
  insertion-post-line={ewboson,circ=W}
]
```

This now retains all four external double caps. A cap does not need to be
repeated inside `insertion-pre-line`. Omit it from the logical leg style
when that leg should be uncapped; a cap explicitly requested on the segment
still applies.

Verification covers **241 public cases**: S/T trees, bubble/seagull/swordfish,
all four slots, scales 0.72/1/1.2, single/double caps, separate pre/post line
styles, explicit segment precedence, per-leg styles, and fresh uncapped
reset. Caps are checked against actual external-node coordinates; the
tests reject caps accidentally drawn on insertion vertices.

The independent PDF checker finds **16 double caps / 32 bars** across four
examples, verifies both bars are parallel and correctly paired, places the
outer bars at the four outer corners, and requires the wavy propagator to
meet exactly the inner bar. It checks the emitted PDF geometry, not only
helper calls. The new regression and PDF check are registered in the
maintained suite: **45 documents / 772 Proca/scalar endpoint contacts** pass,
in addition to these endcap checks. Existing geometry, momentum, styles,
circles, indices and reset checks retain their tolerances.

The [focused PDF](../../regressions/topologies/insertion/insertion-endcaps.pdf)
and new atlas page 24 (N01-N04) show only the caps under test. No independent
circles, field labels, indices or momentum guides are added. The atlas now
contains **106 recipes / 24 pages**; the original 23 page bodies are
pixel-identical at 1100px to `b1d84eb`, excluding footer provenance. Both
newly authored pages were rendered and inspected.

Measurements and file hashes are in
[insertion-endcaps-checks.json](insertion-endcaps-checks.json). The pre-fix
M06 record is preserved in [history](history/m06-checks-b1d84eb.json).
The compact 0.8 scale, longer ordinary S exchange, unchanged regular
triangles and deferred D01 index-position work remain in effect. The work
stays local on `codex/m06-tree-triangles`; no merge/push is performed here.

Reproduce from the repository root with Python providing `pypdf`:

```sh
mkdir -p /tmp/feynmanfun-insertion-caps
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-insertion-caps \
  regressions/topologies/insertion/insertion-endcaps.tex
/path/to/python regressions/topologies/insertion/check-insertion-endcaps.py \
  /tmp/feynmanfun-insertion-caps/insertion-endcaps.pdf
FEYNMANFUN_PDF_PYTHON=/path/to/python scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
```
