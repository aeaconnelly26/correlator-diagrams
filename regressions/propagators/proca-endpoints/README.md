# Integrated Proca endpoint contract

This R15 audit combines M01's raw Proca fix with the seagull branch's managed
straight/curved marker helpers. It does not implement M02 labels or new hosts.
See [integration verification](../../../docs/planning/integration-verification.md).

## Placement and compatibility

- Raw Proca triangles anchor their actual tips at the scaled 2.15pt standard
  dot radius, independently of arrow size. Per-line `proca vertex radius=...`
  targets another circular radius in either style order.
- Ordinary managed straight/curved markers retain the semantic vertex radius
  and default 0.25pt tip clearance. Dot and triangle outlines still visibly
  touch; measure both stroke widths rather than only the circle path.
- Explicit per-line M01 radius or legacy-distance options remain effective
  on managed straight Proca edges. These select the requested raw geometry
  without also queuing a duplicate semantic marker.
- Both raw legacy distance names work: `endpoint marker distance` and
  `open arrow marker distance`. If both are non-default, the former takes
  precedence. Dedicated controls check baseline placement instead of contact.
- A continuous Proca edge has two inward, white-filled, line-colored triangles.
  A split crossed diagonal has markers only at the two real vertices.
- `proca start` / `proca end` select one loop endpoint. Curved triangles retain
  the seagull branch's requested equilateral side length, including its 3pt/10pt
  cases. The existing behavioral regression verifies those dimensions.
- Bubble-specific radius/distance controls continue to apply to managed bubbles.
  Generic raw open-arrow add-ons keep their separate open-arrow-distance key;
  managed add-ons retain vertex-aware semantics.
- Certification covers the listed uniform scales and circular vertex cases.
  Unknown custom shapes and arbitrary anisotropic/sheared transforms are not certified.

## Diagnostic matrix

`proca-endpoint-audit.tex` contains 156 diagrams on 26 pages:

| Pages | Cases |
| --- | --- |
| 1-3 | Raw straight/upper/lower curves: normal and short edges at three scales. |
| 4 | Diagonal paths with reversed endpoints at three scales. |
| 5 | Fixed 2cm path with 10pt and 12pt arrows at three scales. |
| 6 | Three-point external Proca, with dots at both ends. |
| 7-9 | s/t/u-tree exchanges, normal and short at three scales. |
| 10-12 | s/t/u four-legged bubbles, normal and short at three scales. |
| 13-15 | Box, crossed box, half-box bridge, normal and short at three scales. |
| 16-19 | Four triangle-contact orientations, normal and short at three scales. |
| 20-22 | Standalone bubble, sunset, inserted bubble plus exchange. |
| 23 | Raw custom-radius order; alias, color order, state reset. |
| 24 | Single-endpoint styles/circ; both legacy distance keys and generic add-on. |
| 25 | Managed custom-radius order, semantic controls/reset, both legacy keys. |
| 26 | Actual integrated seagull loop and exchange at three scales/lengths. |

The figures omit endcaps and independent crossing circles. Only the dedicated
circ compatibility control retains a circle. Short raw edges use 6pt markers;
larger-arrow controls use sufficient length for both triangles. Oversized
markers on an edge too short to contain them are not silently resized.

## Build and verify

From the repository root:

```sh
mkdir -p /tmp/proca-endpoint-audit
TEXINPUTS="$PWD//:" pdflatex -halt-on-error -output-directory=/tmp/proca-endpoint-audit regressions/propagators/proca-endpoints/proca-endpoint-audit.tex
python3 regressions/propagators/proca-endpoints/check-endpoint-contact.py /tmp/proca-endpoint-audit/proca-endpoint-audit.pdf --baseline regressions/propagators/proca-endpoints/proca-endpoint-audit-before.pdf
```

The numerical check requires `pypdf`. To include it in the full maintained run:

```sh
FEYNMANFUN_PDF_PYTHON=python3 scripts/check-regressions.sh
```

It reads actual PDF vector paths and stroke widths, checking expected triangle
and dot counts, white fill, color, visible contact, and baseline legacy controls.
This complements visual review. A deeply buried tip or visible ink gap fails.
The old pre-M01 raw paths still fail this visible-contact criterion; it has not
been relaxed by increasing a constant positional tolerance.

The archived 24-page before PDF uses the package at `0dbf733` and the source
recorded at `1b85ef8`. It is historical, not rebuilt from the current expanded
source. The current 26-page PDF uses the integrated checkout. Managed bubbles
intentionally retain the semantic clearance, so their coordinates are checked
for visible contact rather than equality to the older no-clearance fixture.
