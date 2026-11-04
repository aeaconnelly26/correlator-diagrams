# Feynman Fun Development Plan

Current roadmap and session handoff, refreshed 2026-11-03. The original plan
is preserved in [the history archive](planning/history/development-plan-before-2026-11-03.md).

## Current state

- Audited baseline: `main` at `0dbf733` (merge of PR #27, `codex/bubble-on-leg`).
- Current branch: `codex/m03b-s-tree-bubbles`, based on published main `6549efa`.
- M03b is complete locally: all four s-tree external bubble placements; see
  [M03b verification](planning/m03b-verification.md). It is not merged or pushed.
- M03a, including loop-arrow spacing/label-side fixes, is merged and published
  to GitHub. The implementation branch is retained.
- M03a is complete: bubble insertion on any one t-tree external leg.
  See [M03a verification](planning/m03a-verification.md).
- Index-label positions are a known deferred workflow item, D01. Do not retune
  their appearance during M03b or the current feature sessions; preserve their
  attachment and controls. See [deferred workflows](planning/deferred-workflows.md).
- M02 was fast-forwarded into main and published to GitHub on 2026-11-03;
  that published baseline is retained. The implementation branch is retained.
- M02 is complete: independent controls for all seven triangle-contact
  momentum annotations, with outside-facing defaults. See
  [M02 verification](planning/m02-verification.md).
- M00 produced the inventory and roadmap. M01 now corrects generic Proca tip
  contact; it adds a low-level custom-radius line option and no new topology.
- Existing square box defaults, four-legged s/t/u bubbles, and all four
  triangle-contact orientations are already implemented.
- Semantic bubbles support s/t-tree external slots 1-4. Seagulls remain t-tree
  slot 1 only. U-tree and internal bubble insertions are unsupported and can be no-ops.
- Preserve existing public APIs and intentional visual tuning. Do not rename
  the repository or delete branches.

## Start here

| Record | Purpose |
| --- | --- |
| [Current capability atlas](diagram-inventory/inventory.pdf) | Twelve pages: 58 current examples, including all eight s/t-tree bubble placements. |
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
| M01 | Audit and correct demonstrated Proca endpoint failures | Complete on published main; diagnostic and vector checks passed |
| Integration | Reconcile seagull/endpoint work with M01 | Complete; reconciled on local/GitHub `main`; combined tests pass |
| M02 | Independent triangle-contact annotations, four orientations | Complete on published main; 35 regression documents and 600 endpoint contacts pass |
| M03a / M03b | External self-energy bubbles on t-tree / s-tree slots 1-4 | M03a published; M03b complete locally, awaiting publication |
| M04 | External seagulls on s/t trees | Slot-1 prototype integrated; expand to other t/s legs |
| M05 | External swordfish on s/t trees | Planned |
| M06 | Regular tree-attached triangle corrections, four placements | Planned |
| M07 | Complementary crossed box, crossed external layouts, source routing questions | Planned; square defaults already verified |
| M08a / M08b | Contact external self-energy / seagull | Planned |
| M09a / M09b / M09c | Internal exchange self-energy / seagull / shared inner-vertex bubbles | Planned |
| M10 | Stemmed tadpoles; any separately established residual graph | Planned |
| M11 | Full API/example/reference and GitHub visual reconciliation | Planned; docs updated incrementally throughout |

## Next coding session

M04 is next: expand the existing t-tree slot-1 seagull to the remaining t-tree
legs, then the four s-tree legs, one insertion at a time. First integrate and
publish the verified M03b checkpoint from `codex/m03b-s-tree-bubbles` when
publication is authorized. The user needs no manual Git preparation.
Freeze the direct self-loop at one quartic host vertex; it is distinct from
the two-vertex self-energy bubbles. Read R11 and M04. Keep D01 deferred to a
separate later workflow; do not tidy index positions during the feature sessions.

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

## Historical session update - integration, 2026-11-03

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

## M02 implementation and review record - 2026-11-03

- Added `triangle-contact-momentum-1` through `-7` option blocks and aliases;
  grouped options remain fallbacks, independent of key order.
- Explicit grouped ranges/fractions now work on every slot. Tuned ranges
  use `auto`. Outside directions follow the triangle centroid. The subsequent
  review correction fits gaps to actual labels, shortens external arrows, and
  places quartic-side defaults nearer outer endpoints. Continuous side-label
  layout is now a separate global/per-slot choice.
- Label shifts/anchors move only the label; reversal keeps the same geometric
  side and fractions. Slot numbering, styles, indices, and visibility remain.
- All 35 maintained documents and 600 automatic endpoint contacts pass.
  Saved the five-page focused gallery; atlas updated to eleven pages/51 recipes.
- No new topology or insertion placement was added. M03a is next.
- Work is checkpointed on the M02 branch; no main merge or push for this slice.

### M02 screenshot review correction

The first checkpoint `b795f7f` left empty arrow gaps below displaced labels and
used unnecessarily long quartic-side arrows. The reviewed version replaces
those defaults with measured inline gaps, compact external arrows, orientation-
aware quartic placement, and explicit continuous-arrow/side-label mode. All 35
regression documents, 97 focused public-diagram checks and 600 endpoint contacts
pass. The gallery has five pages/20 examples; the atlas has eleven pages/51 recipes.

The subsequent direction-default request makes both quartic-to-trivalent middle
arrows point toward their trivalent endpoints in all four orientations, in gap
and side layouts. The third internal edge and all explicit direction controls
are preserved. No topology or slot layout changed.

## Historical closeout - M02 publication, 2026-11-03

- Fetched GitHub before merging; its main had no new commits beyond `6657735`.
- Fast-forwarded main to verified M02 checkpoint `8f95755`, preserving all
  implementation/review commits and the feature branch.
- Package code, regressions, and generated PDFs match the verified checkpoint;
  only handoff/publication records changed during closeout.
- Published through a normal push and verified local/remote main equality.
- Ready to switch tasks. M03a is the next roadmap item; it has not started.

## Historical session - M03a t-tree bubble expansion

- Preserved the slot-1 baseline, then verified slots 2, 3 and 4 in sequence.
- Shared selected-leg aliases route host geometry, style, momentum labels,
  visibility, direction, cap placement and indices without swapping a/b arcs.
- The graph has eight propagators, four interaction vertices and one loop;
  exactly one external leg is replaced. Lower-leg host momentum labels default
  below their legs; explicit positions still take precedence.
- All 36 maintained documents pass. The focused source checks 52 complete
  graphs; its isolated page verifies 16 Proca tips, alongside the existing
  600-contact audit. The four-page gallery has 16 examples; atlas has 54 recipes.
- Only M03a is complete. Seagulls remain t-tree slot 1; s-tree bubbles are M03b.
- Work is checkpointed locally on `codex/m03a-t-tree-bubbles`; no merge or push.

### M03a loop-spacing review

Reduced default bubble momentum offset from 12pt to 8pt, preserving the existing
style clearance and explicit overrides. Loop labels now sit outward from their
actual arcs, so the right-hand a/b swap cannot invert above/below placement.
The focused tests measure 34 rendered label sides/clearances across four slots
and reversed arrows. The gallery/inventory are regenerated; no topology changed.

## M03b implementation record - 2026-11-03

- Published M03a and its arrow-spacing/label-side fixes to main; `6549efa`
  records publication and the explicitly deferred D01 index workflow.
- Created `codex/m03b-s-tree-bubbles` from that synchronized baseline.
- Added external s-tree bubbles in slots 1-4 sequentially, reusing semantic
  host-relative geometry and the existing public insertion controls.
- Preserved index values/attachment/controls without changing index positions.
- Added the focused four-page gallery and atlas recipes C01-C04. Verification,
  measured contact results and reproduction commands are in M03b verification.
- M03b is checkpointed locally; main/GitHub still contain M03a, not M03b.
  M04 is the next feature milestone after M03b publication.
