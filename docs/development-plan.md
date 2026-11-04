# Feynman Fun Development Plan

Current roadmap and session handoff, refreshed 2026-11-03. The original plan
is preserved in [the history archive](planning/history/development-plan-before-2026-11-03.md).

## Current state

- Audited baseline: `main` at `0dbf733` (merge of PR #27, `codex/bubble-on-leg`).
- Current branch: `main`, fast-forwarded to verified integration `4584aff`
  on 2026-11-03; combined parents `1b85ef8` and `5a657cd`. Not pushed.
- Integration is complete and verified. M02 independent triangle-contact
  annotations is the next coding milestone, based on this integrated branch.
- M00 produced the inventory and roadmap. M01 now corrects generic Proca tip
  contact; it adds a low-level custom-radius line option and no new topology.
- Existing square box defaults, four-legged s/t/u bubbles, and all four
  triangle-contact orientations are already implemented.
- Semantic bubble and seagull insertions are implemented only on external slot 1 of t trees.
  Accepted keys for other insertion combinations can silently do nothing.
- Preserve existing public APIs and intentional visual tuning. Do not rename
  the repository or delete branches.

## Start here

| Record | Purpose |
| --- | --- |
| [Current capability atlas](diagram-inventory/inventory.pdf) | Nine pages: 43 current examples, including seagulls and integrated annotation controls. |
| [Copy/paste recipes](diagram-inventory/recipes.md) | Stable IDs and full public-macro options for every atlas example. |
| [Remaining requirements](planning/requirements.md) | 22 requirements with current support, limits, dependencies, and acceptance gates. |
| [Source coverage](planning/source-coverage.md) | 23 PDF items and 90 diagram panels across all 23 PowerPoint slides, including duplicates/context. |
| [Coding milestones](planning/milestones.md) | Small implementation slices, completion checkpoints, and unresolved source questions. |
| [Source record](planning/README.md) | Unchanged originals, checksums, previews, and historical plan. |
| [Inventory verification](diagram-inventory/verification.md) | What was compiled, visually inspected, and left unaudited. |

## Milestone queue

| Milestone | Work | State |
| --- | --- | --- |
| M00 | Archive sources; audit capacity; publish repository atlas and roadmap | Complete; included in checkpoint `1b85ef8` |
| M01 | Audit and correct demonstrated Proca endpoint failures | Complete locally; diagnostic and vector checks passed |
| Integration | Reconcile seagull/endpoint work with M01 | Complete; merged into local `main` at `4584aff`; combined tests pass |
| M02 | Independent triangle-contact annotations, four orientations | Next coding target on the integrated baseline |
| M03a / M03b | External self-energy bubbles on t-tree / s-tree slots 1-4 | Slot-1 t prototype exists; expansion planned |
| M04 | External seagulls on s/t trees | Slot-1 prototype integrated; expand to other t/s legs |
| M05 | External swordfish on s/t trees | Planned |
| M06 | Regular tree-attached triangle corrections, four placements | Planned |
| M07 | Complementary crossed box, crossed external layouts, source routing questions | Planned; square defaults already verified |
| M08a / M08b | Contact external self-energy / seagull | Planned |
| M09a / M09b / M09c | Internal exchange self-energy / seagull / shared inner-vertex bubbles | Planned |
| M10 | Stemmed tadpoles; any separately established residual graph | Planned |
| M11 | Full API/example/reference and GitHub visual reconciliation | Planned; docs updated incrementally throughout |

## Next coding session

Read M02 in [milestones](planning/milestones.md) and R06 in
[requirements](planning/requirements.md). Create the M02 branch from current
local `main`, which now includes integration commit `4584aff`. Begin with
independent external-slot annotation controls, then internal-edge controls and
all four orientations. Preserve the integrated marker and momentum/index behavior.

See [integration verification](planning/integration-verification.md) and
[branch state](planning/branch-integration.md) for the completed reconciliation.

## Session protocol

At the start:

1. Inspect branch and working tree; confirm the actual baseline rather than
   assuming an old branch named in historical notes.
2. Read this handoff and inspect relevant unmerged branches before assuming a
   capability is missing. Read the selected milestone, requirement IDs, and source panels.
3. Preserve unrelated local work. Create a `codex/` branch when starting a
   feature slice; avoid destructive branch cleanup.
4. Freeze the target graph, slots, compatibility rules, and acceptance examples.
5. Run relevant baseline checks before risky package edits.

Before closing a feature slice:

1. Compile the focused regression and inspect its rendered PDF, including
   endpoint and annotation detail. Successful compilation alone is insufficient.
2. Run the maintained regression suite and register stable new coverage.
3. Update the reference, recipe, atlas/PDF, requirement status, and milestone handoff.
4. Record tested revision, passes/failures, remaining limits, and next slice.
5. Do not mark a host/slot family complete until its stated matrix is demonstrated.
6. Create a local checkpoint commit and report its branch/commit, inventory
   update, test state, and separate push/merge status.

## M00 session record - 2026-11-03

- Archived the two supplied originals unchanged with SHA-256 checksums.
- Preserved the previous development plan in full before refreshing this entry point.
- Mapped all 23 PowerPoint slides: 90 diagram panels, with repeats and contextual
  material distinguished; transcribed 23 PDF checklist/figure items into 22 requirements.
- Built a seven-page atlas using existing public macros; supplied the catalog,
  generated LaTeX, recipes, and a temporary-output rebuild command.
- Recorded already-supported capabilities, incomplete annotation/marker coverage,
  missing insertion families, and two references requiring future endpoint tracing.
- All 27 pre-existing example/regression documents passed compilation during
  baseline inspection. Atlas compilation and final visual/coverage checks are
  recorded in the inventory verification file.
- No package implementation changed. No commit, push, or merge was performed.

## Historical M01 session update - 2026-11-03

- Created `codex/proca-endpoint-audit`, retaining all local M00 files.
- Reproduced fixed-distance generic marker gaps while managed bubble tips
  already met their vertices; recorded the user's observation that many
  document examples looked correct.
- Corrected only the generic Proca marker family: triangle-tip anchoring with
  uniform scale and a default 2.15pt target radius. Preserved explicit legacy
  marker distances, generic open-arrow add-ons, and managed bubble placement.
- Saved before/after 24-page PDFs, the 144-case source, independent vector
  checker and results. 568 automatic contacts pass; no crossing-gap markers.
- All 21 registered regression documents pass; atlas updated, with no new
  topology added. M02 is next.
- Work remains local and uncommitted; no push or merge performed.

## Historical handoff - branch review and focused examples

- Identified the unmerged `codex/seagull-insertion` branch through `5a657cd`,
  including a t-tree external-slot-1 seagull and earlier endpoint fixes. The
  original inventory was checkout-scoped and missed that work.
- Added two branch-only seagull examples to atlas page eight, compiled against
  the pinned branch package without merging or copying its code into this checkout.
- Removed unnecessary caps and crossed-box circ decorations from the M01
  diagnostics; retained only the dedicated circ compatibility control.
- Saved the local M00/M01/cleanup checkpoint on `codex/proca-endpoint-audit`.
  No branch was pushed or merged. Reconcile branches before M02.
- Future closeouts include a local commit, inventory update, verification record,
  and explicit push/merge status. See the branch-integration workflow.

## Latest session update - integration, 2026-11-03

- Combined `1b85ef8` and `5a657cd` on `codex/integrate-seagull-and-proca`,
  preserving both parent branches. Resolved package, runner, and plan conflicts.
- Kept managed seagull/one-sided marker sizing and semantic controls, M01 raw
  tip anchoring, per-line radius overrides, and both legacy distance keys.
- All 34 regression/example documents and 600 automatic visible-contact checks
  pass. New managed override and actual seagull cases are in the 26-page audit.
- Inventory: nine pages, 43 current recipes. Seagulls now compile in this checkout;
  their historical branch-only page and old seagull plan are archived.
- Integrated external momentum hiding, continuous blank-label arrows, mini
  indices, channel side-label fixes, and the Compton example remain covered.
- M02 is next. Slot-1-only insertion limits remain; no additional topology was
  implemented as part of integration. `main` is unchanged; no push or PR.
