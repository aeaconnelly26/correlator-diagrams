# M01 results - 2026-11-03

Completed locally on `codex/proca-endpoint-audit`, based on `0dbf733` plus the
uncommitted M00 inventory. No new topology, momentum controls, or index system
was implemented. M02 is next.

## Reproduced defect and the document/PDF discrepancy

The generic Proca decoration placed the **center** of a triangle a fixed 5.4pt
from the path endpoint. The actual tip position therefore depended on arrow
size, while the dot radius also changed with picture scale. The standalone
and inserted bubbles already use a separate managed endpoint helper and were
correct in the audited cases.

The user noted that many Proca examples in their LaTeX document looked
correct. This audit does not claim to have inspected that document or its
loaded package path. The controlled tests establish a plausible explanation:
size/scale choices and helper selection produce different endpoint results,
and a sufficiently small centerline gap can be hidden by the strokes.

For the baseline raw straight path with 6pt arrows, the measured distance
between the triangle tip and the dot's circle path was:

| Picture scale | Baseline gap, PDF points | After automatic tip anchoring |
| --- | --- | --- |
| 0.72 | 1.3271 | Less than 0.0001 |
| 1.0 | 0.7273 | Less than 0.0001 |
| 1.2 | 0.2989 | Less than 0.0001 |

These are circle-path distances, not perceived pixel gaps: the standard dot's
0.4pt outline and triangle outline extend beyond their paths. Increasing arrow
size under the old rule could also push the tip into the dot. The matrix varies
size and scale separately rather than treating all apparent discrepancies as
the same failure.

## Implemented change

Only the generic Proca marker family changed. A triangle's actual tip is now
anchored at the scaled 2.15pt dot boundary. The triangle retains its requested
size, white interior, and inherited outline color. The start/end-only styles
used by split crossed diagonals use the same logic, so the crossing gap does
not become an endpoint.

For custom circular vertices, the low-level per-line option
`proca vertex radius=...` sets the target radius in either style order. An
explicit non-default `endpoint marker distance` keeps the legacy placement.
Generic `openarrowin/out` and the managed bubble endpoint code are unchanged.

## Verification evidence

- [After PDF](proca-endpoint-audit.pdf) and [baseline PDF](proca-endpoint-audit-before.pdf)
  use the same 24-page source. The baseline loaded a separately extracted
  `feynman-fun.sty` from `git show 0dbf733:feynman-fun.sty` ahead of the checkout.
- All 144 diagrams compiled with no overfull/underfull box diagnostics. Each
  final page was rendered and inspected; loop-channel, split-crossing, custom
  radius, and legacy-control pages received larger-detail review.
- The independent [PDF-vector check](check-endpoint-contact.py) found exactly
  **573 triangles**, including **568 automatic contacts** and five deliberately
  unchanged legacy/generic controls. All automatic contacts pass. Maximum
  absolute distance to the dot circle path is **0.1890 PDF pt**, within the
  visible dot outline. Counts rule out extra crossing-gap markers.
- Every detected endpoint triangle retains white fill. Alias and blue/pink
  color-order controls pass; a subsequent default-radius diagram resets
  correctly after the custom-radius cases.
- Explicit legacy controls match baseline to 0.001 PDF pt. The standalone
  managed bubble's measured endpoint positions match baseline exactly.
- All **21 documents registered in `scripts/check-regressions.sh` pass**.
  The audit and previously unregistered relevant Proca, generic-marker,
  channel, crossed-box, and sunset regressions are now registered.
- The current-capability atlas was rebuilt; its 29 structural/layout and
  six styled IDs are unchanged. A later branch review adds a separately labeled
  eighth page with two unmerged seagull examples. See the branch-integration record.

The individual PDF-path measurements are saved in [contact-report.json](contact-report.json).

## Boundaries and remaining work

- This certifies the standard-dot/current-family matrix at uniform scales
  0.72, 1.0, and 1.2, plus the specified custom-radius and arrow-size controls.
  Arbitrary anisotropic/sheared transforms or unknown custom vertex shapes
  require their own geometry contract.
- Intentionally tuned non-default legacy distances retain their existing
  gaps/overlaps. They are tested for compatibility, not automatic contact.
- Oversized triangles on an edge too short to contain them are not silently
  resized. The revised diagnostic omits independent crossing circles and external caps;
  those defaults are separate from endpoint contact and were not changed in the package.
- Triangle-contact momentum labeling is still M02. New topology milestones
  must repeat the endpoint audit rather than extrapolate universal support.

## Branch-review correction

A subsequent branch audit found that `codex/seagull-insertion` already contains
older vertex-aware endpoint work alongside seagull, momentum, and index changes.
M01 was developed against the `main` checkout without that unmerged branch.
Its tests establish behavior in this checkout, not superiority over the other
implementation. Compare and reconcile the overlapping helpers before adopting
either fix as the integrated package. See
[branch integration](../../../docs/planning/branch-integration.md).
