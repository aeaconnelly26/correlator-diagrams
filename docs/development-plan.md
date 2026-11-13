# Feynman Fun Development Plan

Current roadmap and session handoff, refreshed 2026-11-13. The original plan
is preserved in [the history archive](planning/history/development-plan-before-2026-11-03.md).

## Current state

- Audited baseline: `main` at `0dbf733` (merge of PR #27, `codex/bubble-on-leg`).
- Current branch: `codex/compilation-performance`, based on published main
  `7069f39`. The intermediate performance session is complete locally: repeated
  diagram batches improve by 4.5-5.3%, the atlas median by 1.9%, with no claimed
  loading-time gain. All 55 documents / 928 endpoint contacts and registered PDF
  checks pass; 69 rendered page comparisons are identical. Merge/push is pending.
  See [verification](planning/compilation-performance/verification.md).
- Published main: crossed-vertex checkpoint `8b41ca1` is merged and
  published on GitHub (2026-11-13); the feature branch is retained. Exactly two
  half-moon layouts preserve collinear W propagators on opposite diagonals.
  All 54 documents / 928 endpoint checks pass; the atlas has 150 recipes /
  36 pages. See [publication](planning/crossed-vertex/publication.json) and
  [verification](planning/crossed-vertex/verification.md). No merge/push remains.
- M08b checkpoint `e57499e`, including the Overleaf
  array compatibility fix, is merged and published to GitHub (2026-11-08).
  The feature branch is retained. All 53 documents / 894 contacts pass;
  the atlas remains 146 recipes / 34 pages. See
  [publication record](planning/m08b-publication.json). No M08b merge/push remains.
- After integrating the verified performance branch when requested, M09a is
  the next numbered diagram-roadmap milestone. See the
  [performance handoff](planning/compilation-performance.md). Thesis sources/PDFs under
  ignored `output/` are local artifacts and were not included in this publication.
- M08a checkpoint `d855152` is merged and published to GitHub; the publication
  handoff is `35c7959` (2026-11-08). The feature branch is retained. No M08a
  merge/push remains. See [publication record](planning/m08a-publication.json).
- M07b upper crossing, D02 circles, circle default .8
  and the M07c reference audit are merged and published to GitHub (2026-11-07),
  through verified feature tip `40dae7b`. Both feature branches are retained.
  This publication handoff changes documentation only; see
  [publication record](planning/m07bc-publication.json).
- At M07b/M07c publication, verified code `e2521e2` and audit `e99c4be`
  were included unchanged. That checkpoint passed 50 documents / 850 contacts
  and had a 126-recipe / 29-page atlas; M08a extends it as recorded above.
  No M07b/M07c merge/push remains. R04 ordinary-box right crossing stays deferred;
  R14/R22 opposite-pair routing is now published in the
  user-selected half-moon follow-up.
  See [M07c audit](planning/m07c/routing-audit.pdf) and
  [verification](planning/m07c-verification.md).
- The user-selected circle default is now equivalent to `circ scale=0.8`:
  9.6pt ring diameter and label scale 0.8; 50 documents / 850 endpoint checks
  pass. Explicit scale values retain their
  original meanings (`1` restores the former size). See
  [verification](planning/circ-default-verification.md). This is now published on main.
- D03 now records demonstrated overlap between wavy upper crossed external legs
  and a full-size W circle on the top internal edge. The 18-case
  [review](planning/upper-crossing-w-review.md) made no geometry/default change.
  The later circle-size choice is recorded above; D03 spacing remains separate
  from the completed D02 fix.
- Verified M07a checkpoint `dfa0066` is merged and
  published on GitHub (2026-11-07); its feature branch is retained.
  Both internal crossed-box layouts, independent annotations and endpoint
  indices are included. All 46 documents / 800 endpoint contacts passed at
  that unchanged checkpoint. See [verification](planning/m07a-verification.md)
  and [publication record](planning/m07a-publication.json). No M07a merge/push remains.
- Verified M06 checkpoint `629356d` is merged and published to GitHub; its
  feature branch `codex/m06-tree-triangles` is retained.
- M06 is complete on published main: regular triangle corrections on T top/bottom and S
  left/right, with equilateral defaults as requested. Each has four trivalent
  interactions and an exchange bridge. All 45 documents / 772 endpoint contacts
  pass. See [M06 verification](planning/m06-verification.md).
  No M06 merge/push remains. See [publication record](planning/m06-publication.json).
- The package-wide coordinate baseline is now 0.8 times the former size:
  `scale=1` matches former `scale=0.8`, while `scale=1.25` restores former
  `scale=1`. Shared geometry remains consistent. The atlas and focused PDFs
  are refreshed; see [scale verification](planning/scale-baseline-verification.md).
- Ordinary S-tree exchanges and external bubble/seagull/swordfish variants
  now default to half-span 1.05 (was 0.78), with unchanged outer endpoints.
  Triangle corrections retain 0.78. See [S-exchange review](planning/s-tree-span-verification.md).
- Explicit outer insertion segment styles now preserve the logical leg cap
  unless that segment supplies its own cap. All S/T bubble/seagull/swordfish
  slots are covered; see [endcap verification](planning/insertion-endcaps-verification.md).
- M05 checkpoint `9daebf9` is merged and published: swordfish insertions on all
  four external legs of both tree channels. The two loop edges meet the actual
  quartic tree vertex. All 41 maintained documents and 736 endpoint contacts
  passed at this unchanged checkpoint. See
  [M05 verification](planning/m05-verification.md). No M05 merge/push remains;
  the feature branch is retained.
- M04 checkpoint `854293a` is merged and published, including all Nov 4 reviews:
  all eight external s/t-tree seagulls, inward T/outward S defaults, 1/2-in and
  3/4-out flow, compact annotations, smaller bubbles, shorter W-loop waves and
  the final optical W-circle placement. Seagulls default to position 0.40;
  explicit positions remain effective. The feature branch is retained.
  See [M04 verification](planning/m04-verification.md). No M04 merge/push remains.
- M03b is complete, merged and published to GitHub: all four s-tree external
  bubble placements. See [M03b verification](planning/m03b-verification.md).
  The implementation branch is retained.
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
- Semantic bubbles, seagulls and swordfish support s/t-tree external slots 1-4, one at
  a time. Contact bubbles and seagulls support the same four physical slots on central/crossed
  quartic hosts (published M08b); U-tree/internal hosts remain unsupported.
  Seagulls have one quartic self-loop vertex, distinct from bubbles.
- Preserve existing public APIs and intentional visual tuning. Do not rename
  the repository or delete branches.

## Start here

| Record | Purpose |
| --- | --- |
| [Current capability atlas](diagram-inventory/inventory.pdf) | Thirty-six pages: 150 recipes, including both new plain/styled crossed-vertex views. All recipes, including the crossed-vertex additions, are published on main. |
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
| M03a / M03b | External self-energy bubbles on t-tree / s-tree slots 1-4 | M03a and M03b complete on published main |
| M04 | External seagulls on s/t trees | Complete on published main; verified checkpoint `854293a` |
| M05 | External swordfish on s/t trees | Complete on published main; verified checkpoint `9daebf9` |
| M06 | Regular tree-attached triangle corrections, four placements | Complete on published main at verified checkpoint `629356d`; feature branch retained |
| M07a | Complementary internal crossed box and annotations | Complete on published main at verified checkpoint `dfa0066`; feature branch retained |
| M07b | Crossed external layouts | Upper slice published on main; R04 right pair deferred by user |
| M07c | R14/R22 reference-routing audit | Audit and both user-selected half-moon routings published on main |
| M08a / M08b | Contact external self-energy / seagull | M08a and M08b published on main; M08b includes the array fix |
| Intermediate | Package structure and compilation performance | Complete locally; measured gains and compatibility verified; merge/push pending |
| M09a / M09b / M09c | Internal exchange self-energy / seagull / shared inner-vertex bubbles | Planned |
| M10 | Stemmed tadpoles; any separately established residual graph | Planned |
| M11 | Full API/example/reference and GitHub visual reconciliation | Planned; docs updated incrementally throughout |

## Next coding session

**First integrate the verified compilation-performance branch when requested.**
The intermediate session is complete locally; the package and public behavior
are verified against published main. See the
[results and reproduction commands](planning/compilation-performance/verification.md).

After publication, the next numbered diagram-roadmap milestone is
**M09a internal-exchange self-energy bubbles**. Begin with one tree channel's internal slot 5, verify its
two inserted cubic vertices and exchange segments, then expand to the other
channel. M09b internal seagulls and M09c shared inner-vertex bubbles are separate
later slices, with their own source graph maps.

M08b now covers all four direct contact-leg seagulls from S11: six edges,
one quartic contact plus one quartic self-loop insertion. Defaults put upper
loops up and lower loops down; styles, caps, momentum and index controls are
preserved. See [M08b verification](planning/m08b-verification.md).

M07c's audit established the two opposite-pair graphs. The user selected their
implementation on 2026-11-08 with a half-moon embedding and exactly two views.
`CrossedVertexCorr` now supplies both on published main; see [contract](planning/crossed-vertex/contract.md).
The former proposed top/bottom angular API was never implemented and is superseded.

M08a is published at verified feature checkpoint `d855152`, with the documentation
handoff at `35c7959`. M08b is now published at `e57499e`; its feature branch is retained. The maintained
suite now covers 53 documents / 894 automatic endpoint contacts; the atlas has
146 recipes / 34 pages. All five existing M08a gallery pages remain pixel-identical.
D01 index appearance, D03 crossing/circle spacing and the observed D04 coincident
raw-decoration overpaint remain separate later reviews. No manual Git preparation
is needed from the user.

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

## Historical M03b implementation record - 2026-11-03

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

## Historical M03b publication - 2026-11-03

- Fetched GitHub before merging; its main remained at `6549efa`.
- Fast-forwarded local main to verified M03b checkpoint `97495ba` and published
  it with this documentation handoff. The feature branch is retained.
- Package source, focused source, gallery, catalog and atlas match the verified
  SHA-256 records. The existing 37-document/632-contact verification applies;
  publication changed only handoff documentation.
- Current checkout is clean main, synchronized with GitHub. M04 is next.
  D01 remains deferred to a separate later workflow.

## M04 implementation record - 2026-11-03

- Started from synchronized main `b4a6ad8` on `codex/m04-seagull-expansion`.
- Preserved the t-tree slot-1 prototype and extended its host-relative mapping
  to T2/T3/T4, then S1/S2/S3/S4, verifying each step before enabling the next.
- Each selected leg gets one quartic insertion point, two host segments and
  one closed self-loop. Existing styles, caps, logical momentum and index
  values/order are preserved; loop labels follow the physical loop side.
- Added the six-page focused gallery, independent PDF graph/contact checker,
  and eight atlas recipes. Verification details and reproduction are in M04 verification.
- Index appearance is unchanged and remains D01. Unsupported hosts/slots are
  documented, including bubble-only post-index controls and the stored-only style key.
- M04 is checkpointed locally, not merged/pushed. Main/GitHub remain at
  `b4a6ad8`. M05 is next after M04 publication.

## M04 screenshot review - 2026-11-04

- Corrected auto seagull sides: all T loops inward, all S loops outward.
  Explicit orientation values retain their existing meanings.
- Default momentum symbol is p; external 1/2 enter and 3/4 leave. Preserve this
  convention in future coding-session examples. Explicit flow overrides remain
  supported and tested; reversal tests must be identified as such.
- Shared bubble/seagull host arrows are shorter and stay on their segments.
  Auto label placement measures the full text rectangle and puts it outside
  the guide, with 2pt clearance. Explicit tuning keys remain effective.
- Added a four-page, all-16-placement momentum review; refreshed insertion PDFs
  and the atlas (70 recipes / 15 pages). Current verification is in M04 verification.
- Index positions remain D01; no index anchors/offsets/defaults were retuned.
- Review checkpoint remains local on the M04 branch. Merge/push is still pending;
  main/GitHub remain at `b4a6ad8`. M05 is next after publication.

The subsequent Nov 4 review makes short bubble host arrows longer where space
allows (12pt target, capped within the segment), while keeping long seagull
guides compact. S-tree bubble k/ell labels use measured outward normal placement
with 4pt clearance; T-tree bubble loop annotations stay unchanged. Explicit
range and distance controls are preserved. These corrections are included in
the same local review checkpoint and updated PDFs.

## Seagull curve/label consistency follow-up - 2026-11-04

- Replaced translated momentum curves and four-way label anchors with shared,
  concentric loop geometry and labels on their actual local outward normals.
- Auto label fraction now selects the arrow-range midpoint. Explicit fraction,
  range, offset, looseness, distance and reversal remain supported.
- The seagull regression has 222 cases, 88 text-rectangle checks and 800 paired
  curve samples. Both bubble review pages retain identical PDF drawing output
  to the preceding checkpoint `9124a0b`.
- Refreshed seagull/review PDFs and atlas. No topology, propagator, vertex,
  marker or index-placement change. D01 remains deferred. Still local on M04;
  main/GitHub publication remains pending before M05.

## Compact seagull momentum refinement - 2026-11-04

The follow-up from `841b93e` reduces the default seagull momentum range to
0.30-0.52, radial offset to 6pt and k-to-arrow rectangle clearance to 2pt.
This keeps the same shared-center geometry and midpoint/local-normal placement
while making the annotation proportional to the small loop. Explicit overrides
remain supported; bubble annotations and D01 index placement are untouched.
The review/atlas PDFs are refreshed on the same local M04 branch.

## Smaller bubbles and species styling - 2026-11-04

Bubble insertions now default to scale 0.50, about 24% smaller than 0.66.
Explicit scales remain effective; seagulls retain 0.66. Atlas page 16 adds
J01-J04: pink EW Z stems with pink Z circles, bare outer host segments,
inner W circles, pink scalar-polarization loops without circles, and mixed
bubbles with an EW W arc and a pink Z arc. Only the pink
loop line has a k momentum guide/label; the W arc has neither. The all-slot
styled gallery has sixteen examples and 56 focused size/override/reset probes.
The maintained suite now has 40 documents; D01 remains deferred. This remains
local on the M04 branch, pending authorized publication before M05.

## Two-ended pink loop clarification - 2026-11-04

J01-J04 and the sixteen-example styled gallery now use `proca` for the pink
Z loop lines: two open endpoint arrows, no circle. `spol` normally has only
one arrow; neither style adds a circ automatically. The pink EW Z stems and
black W circles remain as requested. Only pink loop lines have k momentum.
This is an example/recipe change using existing APIs; package code is unchanged.
The focused gallery and PDF checks pass, including 32 actual endpoint contacts.
M04 remains local and D01 remains deferred.

## Quiet styled stems and S inner labels - 2026-11-04

The styled examples hide central momentum arrows/P labels using the additive
`show-channel-momentum=false` option, keeping their pink Z stems and circles.
The option defaults true per call and supports s/t/u tree exchanges plus s/t
insertions; external/loop momenta remain independent. S styled examples use
`insertion-post-momentum-label-distance=4pt`; global label-gap defaults are
unchanged. The focused gallery adds 41 public visibility/reset cases. Atlas
page 16 and the all-slot gallery are regenerated. M04 remains local; D01 is
still deferred, and M05 follows authorized publication.

## Short EW bubble waves - 2026-11-04

Added a per-line `ewboson wavelength` control, defaulting to the former
22 line widths. The styled W bubble arcs use 10 line widths, making them
visibly wavier around the W circle. External/central wave defaults are unchanged;
pink loop markers and momentum choices are retained. The EW frequency gallery
adds local-control, alias/order/reset and short-loop comparisons; its independent
PDF check measures 24/54/54/24 curve segments on four equal-length controls.
The original gallery page remains pixel-identical to the compiled baseline.
Updated atlas page 16 and all eight styled bubble placements. M04 remains local;
D01 is deferred and M05 follows authorized publication.

## Seagull position and centered W circles - 2026-11-04

Supported s/t-tree seagulls now default to position 0.40 from outer endpoint
toward the tree vertex, leaving 20% more inner-segment length for a W circle.
Explicit positions remain effective; 0.50 restores the former placement.
Bubbles retain position 0.50. Styled inner W circles explicitly stay at 0.5
along their own segments. All eight seagull placements are refreshed in the
atlas and focused PDFs. The focused matrix has 254 public cases; PDF checks
verify all 16 inner W centers, alongside the existing graph/marker checks.
M04 remains local, D01 remains deferred, and M05 follows authorized publication.

## Optical centering correction - 2026-11-04

The previous circle check measured vertex-to-vertex midpoints, which missed the
unequal visible space caused by the pink endpoint triangle. Styled seagull W
circles now move about 3pt toward the tree vertex: existing `circ position`
values 0.588 (T) and 0.599 (S), shared across each channel's four slots. The
independent PDF check now compares visible arrow/circle/dot ink gaps for all
eight seagulls; bubble-host circles keep their geometric midpoint checks.
These are tuned recipes for the standard marker size and geometry, using
existing public APIs. Package source/defaults are unchanged from ddf9d0e.

## M04 publication and M05 handoff - 2026-11-04

Fetched GitHub before merging; remote main remained at `b4a6ad8`. Re-ran the
complete maintained suite on final checkpoint `854293a`: all 40 documents,
688 endpoint contacts, eight independent seagull graphs, species-circle/optical
spacing checks and EW wavelength checks pass. Fast-forwarded main to that
checkpoint and published it through a normal push; the first HTTP transport
attempt failed, then a buffered HTTP/1.1 retry succeeded. GitHub's main ref
was read back and matched `854293a`. No force push or PR was needed; main is
unprotected and no repository/inherited rulesets were active at publication.
The M04 implementation branch is retained, and the 74-recipe/16-page inventory
and latest styled gallery are included in the published checkpoint.

This closeout updates documentation only. Next session: M05/R12 swordfish,
starting with the S08-L1 shared interaction vertex and one placement at a time.
Do not begin M05 during this publication session. D01 index positioning remains
reserved for its separate workflow.

## M05 implementation record - 2026-11-04

- Started from clean published main `efb5fae` on `codex/m05-swordfish`.
- Froze S08-L1's graph, then enabled T1/T2/T3/T4/S1/S2/S3/S4 in sequence.
  Each has seven propagators and three interaction vertices: two parallel
  A--H loop edges meet the actual tree vertex H, with no collapsed bridge.
- Preserved selected-leg style/caps, independent loop styles and momenta,
  endpoint-index values/ownership and per-diagram reset. Index polish remains D01.
- Passed 167 focused public cases, independent PDF checks of all eight graphs,
  48 new endpoint contacts, and the full 41-document/736-contact suite.
- Added the six-page focused gallery and atlas pages 17-19 (86 recipes total).
  The first sixteen atlas page bodies retain their published M04 rendering.
- Complete locally; main/GitHub remain `efb5fae`. Merge/push is a separate step.
  M06 follows publication. See [M05 verification](planning/m05-verification.md).

## M05 publication - 2026-11-06

- Fetched GitHub; main still matched prerequisite `efb5fae`.
- Verified all recorded M05 artifact hashes, then fast-forwarded main to
  `9daebf9`, retaining `codex/m05-swordfish`. Published with this handoff.
- Package source, regression sources and both PDFs are unchanged from the
  verified 41-document/736-contact checkpoint. Only publication records changed.
- Main is synchronized with GitHub; no M05 merge/push remains. M06 is ready
  for its next coding session. D01 index-position polish remains deferred.

## M06 implementation - 2026-11-06

- Started from clean published main `eb6182c` on `codex/m06-tree-triangles`.
- Froze R08's triangle-plus-bridge graph from S05/S06/S07/S08-L2. Enabled
  T bottom, T top, S left and S right sequentially.
- Added `insertion=triangle` with `tree-triangle-side`; slots 1-4 retain the
  outer legs, 5 is the bridge, 6-8 are A--B--C--A. No quartic point is used.
- User review changed the default to equilateral: automatic half-width derives
  from the chosen depth/outer shift. The follow-up enlarges sides by 50% and
  uses wavy styled exchange lines. Explicit width permits other shapes.
- Reused measured-gap/side-label annotation helpers with independent controls
  for all eight slots. Preserved external flow/styles/caps and endpoint values;
  D01 appearance remains deferred. New scalar loop markers use semantic tips.
- Added a five-page focused gallery and atlas pages 20-21 (94 recipes total).
  The first nineteen atlas page bodies retain the published M05 rendering.
- Complete locally; main/GitHub remain `eb6182c`. No M06 merge/push performed.
  M07 follows publication. See [M06 verification](planning/m06-verification.md).

### M06 endpoint-alignment review

The larger T triangles now fit inside the ordinary outer frame. All four
external endpoints keep their exact default/custom coordinates; the loop
translates inward while keeping its larger equilateral sides. The exchange
bridge shortens and styled lines remain wavy. The S layout is unchanged.
Focused coverage expands to 191 cases, with independent PDF frame checks;
the gallery/inventory and full-suite verification are refreshed. Still local
on `codex/m06-tree-triangles`; no M06 merge/push.

### Shared four-leg frame clarification

The user permits larger spans when applied consistently across families.
The common default is now +/-2.10 on both axes for contact/channel trees,
loops/insertions, box/crossed box and triangle-contact. Explicit shared spans
and family overrides remain effective. This fits the large T triangle with
its original stem; an inward fit is only a fallback for tight explicit frames.
Added 188 cross-family public cases and eight independent PDF comparisons.
Atlas: 102 recipes / 23 pages; gallery: seven pages. Earlier first-nineteen-page
pixel-identity statements describe the initial M06 checkpoint, before this
authorized default change. Still local; M07 remains next after publication.
See [shared-frame verification](planning/four-leg-frame-verification.md).

## M08a local closeout - 2026-11-08

Contact-host external self-energy bubbles now cover slots 1 UL, 2 LL, 3 UR,
4 LR. One insertion at a time; central/crossed are equivalent quartic views.
The first-leg slice was compiled and inspected before expanding the focused
checks. Invalid slots, disconnected pairings and non-fitting/nonpositive
geometry fail explicitly. Existing marker, style, cap, momentum and index
helpers are reused. No index appearance retuning or contact seagull work.
See [verification](planning/m08a-verification.md) and [contract](../regressions/topologies/insertion/M08a-contract.md).

## M08a publication - 2026-11-08

Verified checkpoint `d855152` was fast-forward merged from `096b2b3` into main
and pushed to GitHub. The feature branch is retained. This publication handoff
changes documentation only; the 51-document / 874-contact verification and
134-recipe / 31-page atlas remain unchanged. M08b follows from this baseline.

## M08b local closeout - 2026-11-08

All four external contact seagulls and all eight S11 Z/W variants are covered.
The original quartic contact survives; one new quartic vertex carries a direct
self-loop, without a stem or split bubble vertices. The first-leg slice passed
before the all-slot matrix. A seven-page gallery, independent PDF graph/contact/
charge-flow checks, and atlas CS01-CS04/CS11-CS14/CS21-CS24 are saved. M08b is
committed locally; merge/push is pending. M09a follows after integration.

## M08b array compatibility fix - 2026-11-08

Fixed the reported Overleaf slowdown: literal `&&` in the new geometry checks
broke contact seagulls inside a math array. Equivalent `min(...)>0` checks are
alignment-safe and retain the bounds. The actual nine-page project compiles
locally in about 8.5 seconds with only the package replaced; Overleaf source
was not edited. Twelve array/tabular/aligned cases and 32 negative cases now
pass, along with 53 maintained documents / 894 endpoint contacts. See
[fix record](planning/m08b-array-fix.md). The atlas PDFs and geometry are unchanged.

## M08b publication - 2026-11-08

Verified checkpoint `e57499e` (implementation `59c171f` plus array fix) was
fast-forward merged from `35c7959` and pushed to main. The source branch is
retained. This handoff changes publication/status documentation only; package,
regressions and PDFs retain the verified content. All 53 documents / 894
contacts pass; the atlas is 146 recipes / 34 pages. No manual merge/push remains
for the user. The local thesis artifacts in ignored `output/` were not published.
See [publication record](planning/m08b-publication.json).
## Crossed-vertex publication and performance handoff - 2026-11-13

Rechecked all recorded feature source/PDF hashes and reran the full maintained
suite: 54 documents, registered PDF checks and 928 endpoint contacts pass.
Fast-forwarded main from `bfb23ac` to `8b41ca1`, retaining the feature branch,
and published with this documentation handoff. Package, regressions, atlas and
gallery are unchanged from the verified checkpoint. The user selected an
intermediate compilation-performance session before M09a; its benchmark and
compatibility requirements are recorded in [the handoff](planning/compilation-performance.md).


## Compilation-performance closeout - 2026-11-13

Started from published main `7069f39` on `codex/compilation-performance`.
Measured loading separately from drawing, then replaced repeated style-table
parsing with direct PGF definitions, cached alternating topology/index lists,
and batched coordinate/guide paths without changing their geometry. Retained
all topology resets because their measured cost was small. Seven alternating
runs per workload show 4.5-5.3% gains on repeated diagram batches and 1.9% on the
150-recipe atlas; loading remains effectively unchanged. All 55 maintained
documents / 928 endpoint contacts and registered PDF checks pass; all 69 page
comparisons are pixel-identical. Existing atlas/recipes and D01 appearance are
unchanged. Local checkpoint only; no merge/push. M09a follows integration.
See [verification](planning/compilation-performance/verification.md).
