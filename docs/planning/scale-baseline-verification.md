# Compact diagram scale - 2026-11-06

User-directed follow-up to `ad9592b` on `codex/m06-tree-triangles`.
The package-wide coordinate baseline is now **0.8 times the former size**.
M06 and this review remain local; merge/push is pending.

| Public scale | Equivalent former scale |
| --- | --- |
| 0.8 | 0.64 |
| 1.0 | 0.8 |
| 1.25 | 1.0 |

All five drawing entry points apply the same factor exactly once. Their
aliases and preset wrappers inherit it. Sunset's existing default scale 1.2
and the thesis vertex's 0.75 also shrink by 20%. Logical dimensions, shared
outer corners (+/-2.10), large equilateral triangle proportions and option
values are preserved. At unit scale the shared frame is nominally 3.36 cm
square; PDF coordinates measure about 95.256 pt after PGF rounding. Regular
triangle sides measure about 35.356 pt and remain equilateral.

This deliberately reproduces the existing `scale=0.8` behavior. It uses TikZ
coordinate scaling: fonts, circles, stroke widths and arrowhead sizing retain
their existing rules. Raw user-created TikZ pictures and standalone propagator
commands keep their own scale.

Verification covers:

- **135 public cases across all 27 commands/aliases**: actual picture
  transforms, omitted scale, explicit 0.8/1/1.25, preset defaults, consecutive
  reset and isolation from the next raw TikZ picture.
- **All 23 atlas pages / 102 recipes** compared with package `ad9592b` at
  0.8 times each recipe's scale, including explicit overrides. Before/after
  renders are pixel-identical at 1000px. The committed comparison script
  reproduces this evidence; the report records pixel hashes and both package
  hashes. Page text/provenance is held equal between comparison builds.
- **191 triangle + 188 shared-frame cases**, with actual PDF checks for
  twelve common frames, four equilateral graphs and four wavy exchanges.
  The size assertions now expect the authorized compact physical baseline;
  contact tolerances are unchanged.
- **43 maintained documents / 772 endpoint contacts**, including mixed
  styles, reversed directions, legacy overrides, caps, labels and reset.
- **40 species circles**, 32 contacting pink loop arrows, eight optically
  centered seagull W circles and eight midpoint bubble-host W circles. Existing
  positions need no retuning: maximum W centering error is below 0.015 PDF pt,
  and minimum circle/vertex clearance is about 3.545 PDF pt.

The first complete run compiled all 43 documents but exposed a historical-size
assumption in the legacy marker comparison. Its two managed legacy examples
now use `scale=1.25`, matching their archived raw-TikZ controls at physical
scale 1.0. The raw controls, archived PDF, numerical comparator and endpoint
tolerances are unchanged. This verifies the old override behavior at equal
physical scale; ordinary managed examples exercise the new baseline.

The atlas, seven-page triangle gallery and four-page species gallery were
rebuilt, rendered and inspected. The final atlas includes the new scale note.
No additional graph capability or D01 index-position adjustment is included.
The pre-rebase M06 machine record is preserved in
[history](history/m06-checks-ad9592b.json); current measurements and hashes are
in [m06-checks.json](m06-checks.json) and
[scale-baseline-checks.json](scale-baseline-checks.json).

Reproduce from the repository root with Python providing `pypdf` and Pillow:

```sh
FEYNMANFUN_PDF_PYTHON=/path/to/python scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
/path/to/python regressions/scale/check-baseline-equivalence.py \
  --baseline-ref ad9592b --report regressions/scale/baseline-equivalence.json
```

The comparison script requires the local pre-rebase Git commit, `pdflatex`
and `pdftoppm`. It builds in temporary directories and leaves package sources
unchanged. M07a remains the next feature slice after authorized publication.
