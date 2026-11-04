# Seagull / M01 integration verification

Local integration branch: `codex/integrate-seagull-and-proca`.
Merge parents: `1b85ef8` (M00/M01 checkpoint) and `5a657cd` (seagull branch).
`main` remains at `0dbf733`. The original branches are retained; no remote
push, pull request, or main-branch merge was performed.

## Conflict resolution

- **Package:** retained M01's raw Proca tip anchor and the seagull branch's
  queued semantic marker/curve helpers. One-sided loop selection and its
  equilateral-size repair remain intact.
- **Compatibility:** explicit per-line `proca vertex radius` works before or
  after `proca` on managed straight edges. Explicit legacy distances still
  select their requested raw placement. Both `endpoint marker distance` and
  `open arrow marker distance` are supported; the former takes precedence
  when both are non-default. Ordinary managed styles retain their semantic
  vertex radius and default 0.25pt clearance.
- **Runner:** kept the seagull branch's isolated temporary output, failure
  logs, counts, and expanded document list; added M01's audit and optional
  numerical PDF check. No duplicate run entries or repository-wide scratch deletion.
- **Plan:** kept the current requirement map/roadmap and archived the old
  seagull development plan byte-for-byte instead of replacing the current plan.
- **Other work:** retained momentum visibility, empty-label behavior, channel
  side-label fixes, mini indices, reusable Compton macros, and their tests.

## Verification performed

All **34 maintained regression and example documents pass**, including the
momentum-visibility assertions, mini-index examples, one-sided marker counts
and equilateral dimensions, seagull examples, compatibility wrapper, and Compton
example. The full run also executes the independent PDF-vector audit when
`FEYNMANFUN_PDF_PYTHON` names a Python interpreter with `pypdf` installed:

```sh
FEYNMANFUN_PDF_PYTHON=python3 scripts/check-regressions.sh
```

The current endpoint diagnostic contains **156 diagrams on 26 pages**:
**609 endpoint triangles**, of which **600** are automatic contacts and nine
are intentional legacy/generic controls. The two added pages exercise managed
per-line/semantic overrides and actual seagull loops with Proca exchange edges
at all three scales. No unnecessary caps or crossing circles are used.

The checker now reads both dot and triangle stroke widths from PDF vector
operators. This preserves the semantic helper's documented 0.25pt clearance
while checking the user's visible-contact requirement directly. A real visible
gap above 0.02 PDF pt fails; deeply buried tips, missing white fill, lost color,
or unexpected marker/dot counts also fail. The integrated result has a maximum
circle-path gap of 0.3072 PDF pt but a maximum **visible ink gap of -0.0664
PDF pt**: all automatic outlines overlap/touch. The pre-M01 fixture still
exhibits a positive visible gap and therefore fails the same contact criterion.
The checker has not simply increased a constant tolerance to accept old gaps.

Raw legacy controls match the archived pre-M01 fixture to 0.001 PDF pt.
Managed explicit overrides match the corresponding raw controls. Managed
bubble tips are no longer required to match the old no-clearance coordinates:
they intentionally retain the seagull branch's semantic clearance. Actual
visible contact and one-sided dimensions are independently checked instead.

## Inventory and rendered evidence

The nine-page atlas has **43 current recipes**. All examples use the integrated
package. Seagulls are promoted from the historical unmerged preview to the
current gallery, with plain/EW and one-/two-marker examples. Annotation controls
have a separate minimal page. The older branch preview is preserved in
`history/`; it is not embedded in the new PDF.

Current atlas and endpoint audit pages were rendered and inspected, including
the new override/seagull cases and the side-label/visibility examples. Source
manifest checksums, archived-plan integrity, recipe IDs, local links, and
conflict-marker checks are part of closeout verification.

## Limits carried forward

Bubble and seagull insertions still support only t-tree external slot 1.
No s-tree, other external-leg, or internal-edge insertion was added by merging.
Triangle-contact independent placement is still M02; this integration does
not claim to implement it. Arbitrary nonuniform transforms/custom non-circular
vertices remain outside the endpoint audit's certification.

M02 should start from this integration commit (or its descendant), not the
older `main` checkout. The user does not need to merge branches manually.
