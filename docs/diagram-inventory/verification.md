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
