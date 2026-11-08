# M08b alignment compatibility fix - 2026-11-08

Follow-up to local checkpoint `59c171f`, prompted by a reported Overleaf slowdown.
The small standalone size check succeeded but did not cover the user's math-array
layout. Downloading the actual project for local diagnosis reproduced a fatal
parser error at its first contact seagull inside `array`:

```text
Runaway argument?
Forbidden control sequence found while scanning use of \pgfmath@parse@next.
```

A minimal one-seagull array reproduces the same error. The two new seagull
geometry checks contained literal `&&` tokens in PGF math expressions. Their
ampersands conflict with TeX alignment processing. The default Overleaf error
recovery mode can turn the failure into a prolonged compile. This was an M08b
validation bug; insertion size and diagram geometry were not responsible.

Replace the checks by the equivalent alignment-safe expressions:

```tex
min(position,1-position)>0
min(scale,loop-size,loop-looseness,leg-length)>0
```

The same strict bounds and positive-geometry errors remain. No public option,
geometry, styling, marker or momentum default changes.

Evidence:

- Original minimal array: fails; corrected minimal array: passes.
- The downloaded project uses the exact package from `59c171f`. Its unmodified
  document fails with that package; replacing only the package with the fix
  compiles all nine pages in about 8.5 seconds locally (one pdfLaTeX pass).
- Twelve valid seagull cases cover all four slots in `array`, `tabular` and
  `aligned`; the new maintained alignment regression catches the original bug.
- The 16 invalid requests are tested in both ordinary and array contexts:
  32 intended package errors, without accidental parser/alignment failures.
- The maintained suite now passes 53 documents / 894 endpoint contacts.
  See [suite output](m08b-suite.txt) and [current checks](m08b-checks.json).

The actual user project is kept only in temporary diagnostic files; it is not
added to this repository or published. Its Overleaf source was not edited.
The corrected package must replace the older package in that Overleaf project.

This fix is included in verified M08b checkpoint `e57499e`, now merged and
published on main (2026-11-08). The source branch is retained; see
[publication record](m08b-publication.json). The atlas has the same 146 recipes / 34 pages,
and its saved PDFs remain unchanged because this only repairs compile-context
compatibility. The next diagram-roadmap milestone remains M09a; no M08b integration remains.
