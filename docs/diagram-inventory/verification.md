# M03a inventory verification - 2026-11-03

Current atlas: **54 recipes on eleven pages**, built against
`codex/m03a-t-tree-bubbles` on baseline `b917ed2`. I29 retains slot 1;
B02-B04 add the lower-left, upper-right and lower-right external bubble placements.
The main topology pages remain plain and unlabeled. Seagulls remain t-tree slot 1.

The four-page focused gallery has 16 examples and 51 automatic public-diagram
checks: actual graph/vertex/selected-leg geometry, pre/post style inheritance,
logical momentum labels and visibility, blank/reversed momenta, independent
indices, outer-only caps, scale/position changes and state reset. Its isolated
Proca page has 16 vector-checked white-filled pink endpoint tips. All 36 maintained
documents and the existing 600-contact endpoint audit pass. Slot 1 was compared
with baseline: text is identical, with maximum PDF text displacement 0.014pt
from coordinate-copy/polar rounding; rendered connectivity and styling are retained.

All new gallery pages and changed atlas pages were rendered and reviewed.
See [M03a verification](../planning/m03a-verification.md) for scope, recipe and
reproduction commands. Records below preserve earlier milestone states/counts.

# Historical M02 inventory verification - 2026-11-03

Current atlas: **51 recipes on eleven pages**, compiled against M02 on baseline
`6657735`. Existing structural IDs and seagull examples remain intact. T01-T04
add one annotation example for each triangle-contact orientation; they are style
and annotation variants, not new topologies. T05-T08 add the continuous-arrow
alternative. All examples use current public APIs. The review corrections replace
the earlier displaced-label and fixed fractional-gap defaults.

The five-page M02 diagnostic includes 20 minimal rendered examples and automated
checks on complete public diagrams. These observe emitted coordinates, verify
all seven slots independently, preserve the other six, check outside half-planes,
label-only movement, grouped keys, aliases, reversed arrows, scales, visibility,
and consecutive diagrams. Further checks require actual label centers inside
default breaks, compact external arrows/gaps, the correct quartic-side slots,
and one continuous stroke per side-label annotation. No unnecessary endcaps
or circ decorations are used.
Both edges connecting the quartic vertex to a trivalent vertex now point toward
the trivalent vertex by default. Connectivity-based checks cover all four
orientations in both momentum layouts; explicit direction overrides remain.

All **35 maintained regression/example documents** pass; the independent Proca
PDF check still passes **600 automatic contacts**. The final atlas and M02 gallery
were rendered and inspected. See [M02 verification](../planning/m02-verification.md)
for the implementation boundary and reproducible commands. Older PDFs and audit
records below preserve the behavior of their stated revisions.

# Historical integrated inventory verification - 2026-11-03

Current atlas: nine pages and 43 recipes, all compiled against the combined
checkout from parents `1b85ef8` and `5a657cd`. There is no branch-only package
extraction or PDF inclusion. U01/U02 are now current-capability recipes;
S01-S03 demonstrate loop endpoint selection, and F01-F03 demonstrate the
integrated annotation controls. Earlier branch-only artifacts are archived.

The expanded endpoint audit has 26 pages and 600 automatic contacts; all
34 maintained regression/example documents pass. See
[integration verification](../planning/integration-verification.md) for the
marker reconciliation and geometry-check method.

The sections below are historical M00/M01 records, including their original
page counts and source-state statements. They do not override the current
integrated status above.

# Latest inventory branch review - 2026-11-03

The current atlas has eight pages: the original seven pages of current-checkout
capabilities (35 examples), plus two unmerged seagull examples on page eight.
The additional page is compiled in isolation with `codex/seagull-insertion`
at the full pinned revision in `catalog.json`, not with the current package.
Those recipes are explicitly branch-only. The earlier audit did not inspect
that branch; its no-seagull claim applied to the checked-out lineage only.

The remaining sections preserve the M00/M01 audit history. See
[branch integration](../planning/branch-integration.md) for the correction
and prerequisite work before M02.

# Inventory verification - 2026-11-03

## M01 refresh

The current atlas was rebuilt with the generic Proca endpoint correction on
`codex/proca-endpoint-audit` (base `0dbf733` plus working-tree changes).
Its page count and 35 example IDs are unchanged. See the
[M01 results](../../regressions/propagators/proca-endpoints/results.md) for
the 144-case/24-page diagnostic, 568 automatic contact checks, legacy controls,
and passing maintained regression suite. Triangle labeling remains M02 work.

The following sections preserve the **initial M00 audit record**; statements
about source being unchanged and endpoint work being pending describe that
earlier inventory baseline, not the current M01 working tree.

## Baseline and scope

- Repository baseline: `main` at `0dbf733`.
- `feynman-fun.sty` and `correlator-diagrams.sty` are byte-identical to HEAD.
- This work adds reference records, roadmap documentation, atlas source/data,
  recipes, and a documentation builder. It implements no package feature.
- Both supplied originals match their archived copies and manifest SHA-256
  checksums. The historical development plan matches the pre-refresh HEAD copy.

## Compilation

During baseline inspection, **all 27** pre-existing TeX documents in
`example.tex`, `vertex-example/vertex-example.tex`, and `regressions/**/*.tex`
compiled with `pdflatex -interaction=batchmode -halt-on-error`, repository
`TEXINPUTS`, and separate temporary output directories. This includes files
outside the current maintained smoke script. No tracked regression PDFs were
regenerated or replaced.

The final atlas compiled twice per build through `build.py`, with **35 unique
example IDs on seven PDF pages**. No overfull or underfull box diagnostics were
reported in the final build. All recipes use public package macros; there are
no hand-drawn substitute topologies. Temporary compiler products and page
renders remain outside the repository.

## Visual review

Every final page was rendered at 1450-pixel page height and inspected:

| Page | Inspection |
| --- | --- |
| 1 | Two-point node and all four three-point corner orientations. |
| 2 | Central/paired/crossed contact layouts; disconnected pairs are explicitly identified; flat contact. |
| 3 | Three tree exchanges and three four-legged bubbles; crossed tree has a gap and no crossing vertex. |
| 4 | Square box; existing internal crossing; straight/angled/left/right half-box presets and marker differences. |
| 5 | All four triangle-contact placements, with correct single quartic contact position. |
| 6 | One-loop bubble, two-loop sunset with its middle line, and an actual bubble on t-tree leg 1. |
| 7 | Pink Proca t-bubble with four double caps; polarization; circles/caps; pink bridge momentum/indices; curved bubble momenta/indices; crossed Proca circle. |

The final atlas has no clipped captions, overflowing cells, or missing examples.
Recipe-only corrections were made during review: omit the explicit global
`line=plain` in A04 so it does not override the pink bridge; label external
momentum arrows explicitly in A05; enlarge diagrams for readability.

## Coverage and integrity checks

- Exactly 29 main inventory IDs and six appendix IDs; each appears once in the PDF.
- All canonical public topology families are represented; wrappers/aliases are
  listed separately without adding to the topology count.
- Exactly 22 requirement IDs, 23 PDF source items, and 90 unique diagram-panel
  IDs; every panel maps to a known requirement.
- All 23 slides are accounted for. Cover/handwritten context and the embedded
  screenshot/tooltip are marked separately. Composite slide 11 is indexed as
  eight visible diagrams rather than its smaller image-object count.
- Duplicate structural examples and species/flow variants are identified.
  Slide 20 is an s-tree seagull sheet, not a contact-host sheet.
- Requirement-to-source references agree in the JSON records; Markdown
  records contain every requirement; local documentation links resolve.
- Source archive checksums pass; originals remain unchanged.

## What has not been certified

The atlas verifies the displayed structures and selected style recipes. It
does not certify every combination of labels/styles/indices, establish physics
equivalence, or replace the planned Proca and annotation audits. Known limits:

- Only t-tree external slot 1 supports semantic bubble insertion.
- The existing crossed-box draw path lacks the full internal momentum/index
  pass; a compiled unused option does not count as support.
- Triangle-contact annotation settings share controls and include hard-coded
  adjustments; independent placement remains M02 work.
- Existing Proca markers remain as rendered; full vertex-contact verification
  is M01, including short/curved/crossed paths.
- R14 and R22 require endpoint tracing at their future specification gates.

The source checklist's styling and naming requests are recorded as targets;
they were not treated as authorization to implement new package behavior in
this inventory session.
