# Crossed vertex: user-selected half-moon routing

Selected 2026-11-08 from IMG_0135 and IMG_0136. This follows the M07c graph
audit but replaces its proposed angular drawing/API with the user's half-moon
shape. The user explicitly requested **exactly two layouts**, with both W
propagators on the same diagonal as their opposite external corners. The
handwritten plus/minus-one annotations are reference material, not output.

## Graph and public interface

`CrossedVertexCorr` is a preset of `TriangleContactCorr`, not an extra loop
family. Default `crossed-vertex-orientation=right`; the other value is `left`.
The equivalent underlying orientation values are `crossed-right/crossed-left`.
No top/bottom variants are accepted.

Slots 1/2/3/4 retain physical UL/LL/UR/LR. Q is the central quartic vertex;
A and B are the two cubic vertices. In both views, internal slots are:

| Slot | Connection | Styled sample |
| --- | --- | --- |
| 5 | Q to A, straight | EW boson with W circle |
| 6 | A to B, clockwise semicircle | Pink Proca, no circle, k guide |
| 7 | B to Q, straight | EW boson with W circle |

| View | A / B outer slots | Q outer slots | Interrupted outer slot |
| --- | --- | --- | --- |
| right / IMG_0135 | 1 / 4 | 2 / 3 | 3 |
| left / IMG_0136 | 2 / 3 | 1 / 4 | 1 |

Each has seven logical edges, interaction valences 4/3/3, and one cycle. The
arc/external crossing has no vertex. S13-left maps to the left view, S13-right
to the right view by fixed-slot connectivity; their original angular drawing
is not the requested new embedding. Both styled views now use slot 6 for Z,
whereas the earlier unimplemented M07c proposal used slots 6 and 5.

## Geometry and metadata

- Preserve shared external corners +/-2.10 and compact coordinate factor .8.
- Semicircle radius is `sqrt(triangle-contact-xspan^2 + triangle-contact-yspan^2)`.
  Project its diameter onto the actual outer diagonal, preserving collinearity
  even for unequal outer spans. These two internal span keys set the radius,
  not independent ellipse axes, in the crossed views.
- `crossed-vertex-crossing-gap=.04` is a half-fraction of the full external
  leg. Derive its center from the actual circle/ray intersection. Reject an
  invalid gap or a frame that cannot contain the internal span settings.
- Reuse semantic styles, circle scaling, full-leg cap handling and the narrow
  split-stroke callback. Artificial gap ends have no tips, indices or caps.
- Reuse all seven triangle-contact momentum controls. Slot 6 samples the
  circle, including outside/inside, gap/side, shift/anchor, reversal and hiding.
  Its default label/arrow center is .75 on the right, .25 on the left, avoiding
  the external crossing. Straight-edge defaults remain outside the half-disc.
- Default external momenta stay p1/p2 in, p3/p4 out. Straight internal momenta
  point Q toward A/B. Slot 6 is clockwise unless explicitly reversed.
- Endpoint indices retain their keys; slot 6 follows the curve. Do not retune
  D01 appearance or the thesis artifacts under ignored output/.

## Acceptance evidence

See `checks.json`, `verification.md`, the maintained nine-page regression,
and inventory CV01/CV02/CV11/CV12. Plain topology tests omit momenta, circles
and caps. Dedicated decoration cases exercise each feature explicitly.
