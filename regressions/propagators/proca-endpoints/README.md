# M01 - Proca endpoint contract

This audit isolates the generic Proca decoration from the existing managed
bubble endpoint helper. It addresses R15, not M02 labels or new topologies.

## Target and compatibility

- Standard package dot radius: 2.15pt. Triangle tips meet the dot boundary at
  picture scales 0.72, 1.0, and 1.2, independently of arrow size.
- Keep two inward, white-filled triangles on an unsplit Proca edge. On the
  split crossed diagonal, keep one marker at each true endpoint and none at
  the crossing gap. Preserve color inheritance and `Proca` alias behavior.
- Reuse all existing topology slot maps and connectivity. No momentum or
  index system is changed.
- Automatic placement belongs to `proca`, `proca base`, `proca start`, and
  `proca end`. Generic `openarrowin/out` and the existing standalone/inserted
  bubble endpoint helper remain unchanged.
- Preserve a non-default explicit `endpoint marker distance` as the legacy
  center-distance placement. This intentional override can leave a visible
  gap; it is not an automatic-contact test.
- Low-level `proca vertex radius=...` changes the target radius for the generic
  helper; it works before or after `proca` in a line style. Its default is
  2.15pt. Managed bubble markers continue to use `bubble-vertex-radius` and
  `bubble-endpoint-marker-distance`.
- Certification covers the uniform picture scales above, standard package
  dots, and the explicit custom-radius controls. Arbitrary anisotropic/sheared
  transforms and unknown custom vertex shapes are not certified.

## Diagnostic matrix

`proca-endpoint-audit.tex` contains 144 diagrams on 24 pages:

| Pages | Cases |
| --- | --- |
| 1-3 | Raw straight, upper curve, lower curve: normal and short edges at three scales. |
| 4 | Diagonal paths with reversed endpoints at three scales. |
| 5 | Fixed 2cm path with 10pt and 12pt arrows at three scales. |
| 6 | Three-point external Proca, with actual dots at both ends. |
| 7-9 | s/t/u-tree exchanges, normal and short at three scales. |
| 10-12 | s/t/u four-legged bubbles, normal and short at three scales. |
| 13-15 | Box, crossed box, half-box bridge, normal and short at three scales. |
| 16-19 | Four triangle-contact orientations, normal and short at three scales. |
| 20-22 | Standalone bubble, sunset, inserted bubble plus exchange, at three scales/lengths. |
| 23 | Custom vertex radius in both style orders; alias, color ordering, state reset. |
| 24 | Single-endpoint styles and circ; legacy-distance and generic-arrow controls. |

Short raw edges use 6pt markers; larger-arrow controls use enough length for
both triangles. Oversized triangles on an edge too short to contain them are
not silently resized. The blue controls verify color rather than relying on
the pink examples alone. Managed cases use bare EW external legs; endcaps are omitted. The independent
crossed-box circle-placement pass is suppressed in this diagnostic harness.
Only the dedicated circ control retains its circle.

## Build and verify

From the repository root, with output kept outside the checkout:

```sh
mkdir -p /tmp/proca-endpoint-audit
TEXINPUTS="$PWD//:" pdflatex -halt-on-error -output-directory=/tmp/proca-endpoint-audit regressions/propagators/proca-endpoints/proca-endpoint-audit.tex
python3 regressions/propagators/proca-endpoints/check-endpoint-contact.py /tmp/proca-endpoint-audit/proca-endpoint-audit.pdf --baseline regressions/propagators/proca-endpoints/proca-endpoint-audit-before.pdf
```

The numerical check requires `pypdf`. It reads the actual PDF vector paths,
not the implementation's intended coordinates. It checks triangle/dot counts,
white fill, tip distance to the rendered dots, and unchanged legacy controls.
This complements visual review rather than replacing it.

The before PDF uses the package at `0dbf733`; the after PDF uses this M01
working tree. Their common TeX source declares an unused radius key only when
needed to permit compiling the new control examples against the old package.
That declaration does not alter the old marker drawing behavior.

See [results](results.md) for measured differences and the full verification record.
