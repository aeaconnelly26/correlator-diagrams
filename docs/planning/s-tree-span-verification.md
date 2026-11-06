# Longer ordinary S exchanges - 2026-11-06

Historical S-span checkpoint `b1d84eb`, a user-directed follow-up to `97ecd10` on `codex/m06-tree-triangles`.
Ordinary S trees and their external bubble/seagull/swordfish variants now use
`channel-vertex-xspan=1.05` by default, up from 0.78. The exchange length is
2.10 logical units instead of 1.56, approximately **35% longer**. It measures
about **47.625 PDF pt** at the compact unit scale.

S regular-triangle corrections retain their previous 0.78 half-span and
bridge geometry. T/U trees, four-legged loop bubbles and the shared outer
corners (+/-2.10 on both axes) retain their geometry. The package-wide 0.8
coordinate baseline remains in effect.

An explicit `channel-vertex-xspan` overrides either default. In particular,
`channel-vertex-xspan=0.78` recovers the former ordinary S layout. The explicit
setting resets between diagrams, even when its value equals the old default.
The new default is resolved after topology and insertion options, so a
triangle correction is identified before the span is selected.

The styled S-seagull sample uses `circ position=0.57513` (previously 0.57159)
to retain optical W centering on the reshaped inner host segment. T samples
remain at 0.57332, and bubble-host W circles remain at 0.5. This changes the
documentation recipe, not the default circle API.

Verification:

- **46 focused public cases** observe the emitted interaction vertices and
  outer corners: ordinary S trees, every external slot of bubble/seagull/
  swordfish insertions, explicit spans 0.78/0.91, both triangle sides,
  triangle overrides, dispatch, T/U controls and fresh-call reset.
- Actual PDF paths in the plain comparison page measure five ordinary or
  externally corrected exchanges at 47.6254pt, with the triangle bridge
  retained at 18.3706pt.
- **All seven triangle-gallery pages are pixel-identical** to `97ecd10` at
  1100px, including all four triangle orientations, annotations and styles.
- Atlas body changes are limited to pages **3, 12, 14, 15, 16, 18, 19**, which
  show ordinary S trees and external corrections. The other sixteen page
  bodies are pixel-identical at 1100px; footer provenance is excluded.
- The focused plain page, seven changed atlas pages and all four species
  pages were rendered and inspected for layout, connectivity and spacing.
- The maintained suite passes **44 documents / 772 endpoint contacts**.
  Existing momentum, cap, index-ownership, mixed-style and reset checks pass.
  The species checker retains its strict optical-centering/contact tolerances;
  minimum circle/vertex ink clearance remains above 3.14 PDF pt.

The [plain comparison](../../regressions/topologies/channel/s-tree-span-regression.pdf)
contains no caps, circles, field labels or momentum guides. The
[atlas](../diagram-inventory/inventory.pdf) and
[styled insertion gallery](../../regressions/topologies/insertion/insertion-species-samples.pdf)
are rebuilt. Current measurements and hashes are in
[s-tree-span-checks.json](s-tree-span-checks.json). The pre-review M06 record is
preserved in [history](history/m06-checks-97ecd10.json).

The earlier scale-equivalence script now accepts explicit pre/post-scale Git
refs and defaults to `ad9592b` / `97ecd10`. This keeps that historical
scale-only proof reproducible after the intentional S geometry change.
D01 index-position cleanup remains deferred. M07a is still the next feature
slice after authorized M06 publication; no merge/push is performed here.

Reproduce from the repository root:

```sh
mkdir -p /tmp/feynmanfun-s-span
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-s-span \
  regressions/topologies/channel/s-tree-span-regression.tex
FEYNMANFUN_PDF_PYTHON=/path/to/python scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
```
