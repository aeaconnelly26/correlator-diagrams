# Feynman Fun Development Plan

Living plan for the next phase of `feynman-fun`. This document should be
updated at the start and end of each work session so a future session can pick
up quickly without spending credits reconstructing context.

## Current State

- Date created: 2026-09-06
- Last updated: 2026-10-26
- Active branch: `codex/seagull-insertion`
- Recovery baseline: `2253c64 Adopt feynman-fun package`
- Regression checkpoint: `057bfbd Add feynman-fun regression checks`
- Merge base: `0dbf733` (merged bubble-on-leg prototype)
- Delivery status: five focused closeout commits prepared for PR review;
  merging remains a user action
- Remote repository: do not rename
- Branch cleanup: do not delete branches
- Current priority: confidence and maintainability before new diagram features
- Visual tuning in `feynman-fun.sty`: assume intentional unless it is dead
  commented scratch text

## Session Protocol

At the start of each session:

1. Run `git status --short --branch`.
2. Confirm the active branch against `Current State` and the user's request.
3. Read this file, especially `Last Session Update`, `Today`, and
   `Open Questions`.
4. Run `scripts/check-regressions.sh` before risky edits when enough credits
   remain.
5. Pick one narrow implementation target and one narrow documentation or
   regression target.

Before ending each session:

1. Update `Last Session Update` with what was actually completed.
2. Update `Today` and `Next Session`.
3. Move finished items from `Planned Work` to `Completed`.
4. Add any uncertainty to `Open Questions`.
5. Run `scripts/check-regressions.sh` if code changed and credits/time allow.
6. Record whether tests passed, failed, or were skipped.

## Today

Goal for 2026-10-26:

- Finish and review the seagull insertion, endpoint marker, momentum, and index
  changes already implemented on this branch.
- Include the scalar-QED Compton example as a buildable, documented demo.
- Keep curated PDFs beside sources and exclude metadata-only PDF changes.
- Expand regression coverage to all 33 regression and example documents;
  build in temporary directories without deleting repository scratch files.
- Create focused buildable commits, push, and open a PR against `main`.
- Leave the actual merge to the user.
- Do not rename the remote repository.
- Do not delete branches.

Historical adoption-session usage checkpoints (2026-09-11):

- Start of adoption closeout: 5-hour window 6% used, weekly window 1% used.
- Start of translation-safe topology slice: 5-hour window 35% used, weekly
  window 5% used.
- End of translation-safe topology slice: 5-hour window 72% used, weekly
  window 11% used.
- Available reset credits: 3 full Codex resets.
- Maintained regression suite passed during adoption closeout.
- Maintained regression suite passed after the translation-safe topology slice.

## Next Session

After this branch is reviewed and merged:

- Generalize bubble insertions to other external host slots and orientations.
- Follow with swordfish insertions, then triangle-contact momentum routing
  with per-internal-edge controls.
- Keep the current bubble/seagull insertion contract limited to t-tree slot 1
  until those follow-up changes have their own focused regressions.

Likely deliverable:

- A separate branch with broader insertion host-slot support, documented slot
  semantics, and focused visual and behavioral checks.

## Implementation Inventory

Current helper map from the 2026-09-06 inspection:

- Public topology selection is handled by `/corrdiag/topology` keys in
  `feynman-fun.sty`, with `\FourPointCorr` dispatching to contact, loop
  channels, tree channels, box, cross-box, half-box, flat-contact, and
  triangle-contact draw macros.
- The newer topology framework starts near the internal comment "Internal
  topology framework." It includes reusable wrappers for drawing propagators,
  placing external labels/vertices, selecting momentum slots, and placing
  propagator endpoint indices.
- `\propag` from `tikz-feynhand` is already the primitive behind most line
  drawing. Higher-level helpers usually set `\corr@propoptions`, append
  arrow-size/color/endcap options, then call `\propag`.
- `\corr@drawprop` is the basic external-leg wrapper. `\corr@drawchannelprop`,
  `\corr@drawsunsetprop`, `\corr@drawboxinternalprop`,
  `\corr@drawhalfboxprop`, and triangle-contact draw helpers are specialized
  variants around the same primitive.
- Shared momentum drawing exists in `\corr@drawmomentumrange`,
  `\corr@drawmomentumrangeoffset`, `\corr@drawmomentumrangeoffsetout`, and
  `\corr@drawcustommomentumrangeoffset`. These should be reused for bridge and
  triple-vertex arrows.
- External momentum direction is still mostly slot based: slots 1 and 2 inherit
  left direction, slots 3 and 4 inherit right direction. Contact, box, and
  half-box add per-slot overrides on top of that.
- General list helpers include `\corr@getlistitemorblank`,
  `\corr@selectmomentumslot`, and topology-specific list setters for box,
  cross-box, triangle-contact, loop-channel, and sunset structures.
- The most reusable index helper is `\corr@putpropagatorindiceslot`, which
  reads `<topology>propagatorleftindices` and
  `<topology>propagatorrightindices` lists and places endpoint labels at fixed
  0.18 and 0.82 fractions on a named line segment.
- `box`, `half-box`, `flat-contact`, and `triangle-contact` already use
  `\corr@putpropagatorindiceslot`; this is the best pattern for the next
  general internal index rework.
- `channel`, `loop-channel`, and `sunset` have older, more specialized index
  systems with start/prop/end triplets, auto placement, and curve-aware label
  placement. Do not rewrite these first; mine them for behavior after the newer
  slot-list pattern is made explicit.
- Three-point orientation is handled by coordinate setup helpers for right,
  left, up, and down orientations. Momentum angles and label offsets are
  orientation-specific, while momentum labels still use slots 1, 2, and 3.
- Half-box already has a bridge line and bridge label. It also already places
  propagator endpoint indices on slot 5 for the bridge, but it does not yet
  have bridge momentum arrows. This makes half-box bridge momentum the cleanest
  first feature slice.
- Single propagator macros should not be prioritized as a public feature now.
  If used, they should be a tiny infrastructure probe that exercises the same
  `\propag` plus slot/index/momentum helper path planned for larger topologies.

Design direction from this inventory:

- Standardize around "slot metadata plus drawing primitive": each topology
  should declare stable slot numbers and named endpoint coordinates, then call
  shared helpers for labels, indices, and momentum where possible.
- Keep geometry local to each topology. The helper layer should know about
  slot lists, labels, directions, and index placement, not the physics shape.
- Migrate incrementally. First extend half-box bridge momentum using existing
  slot 5, then use that as the model for triple-vertex and future loop topology
  metadata.

Translation model for the next topology family:

- Public keys should address logical slots. Orientation changes should
  translate coordinates, label offsets, momentum offsets, and index anchors
  without changing which label, style, momentum, or index belongs to a slot.
- `\ThreePointCorr` is the current proving ground for this rule. Its slot 1,
  slot 2, and slot 3 data should remain attached to the same logical legs in
  right, left, up, and down orientations.
- Sunset remains useful as a record of the hard cases for parallel curved and
  straight internal-line indices, especially clearance between labels and
  endpoint/index triplets. It should not be copied wholesale for the new
  two-line bubble structures.
- The one-loop `s/t/u` channel topology is archival for future public API work.
  Its slot 5/6 curved-line machinery can still inform private helpers, but new
  diagram families should prefer the newer slot-list pattern used by half-box,
  box, flat-contact, and triangle-contact.
- Tree-level `s/t/u` channels remain useful as the structural precedent for two
  vertices joined by one internal propagator. Future bubble-on-leg diagrams can
  be thought of as tree exchange structures with one logical leg replaced by a
  translated bubble subdiagram.

## Planned Work

### Phase 1: Stabilize The Base

Target window: first 1 to 2 sessions.

- Keep the regression script maintained and easy to run.
- Add any missing high-value regression files to `scripts/check-regressions.sh`.
- Make sure compatibility through `correlator-diagrams.sty` remains covered.
- Remove only genuinely dead commented scratch text, not intentional visual
  tuning.
- Document the current macro families and slot order well enough that future
  work does not require rediscovery.

Completion test:

- `scripts/check-regressions.sh` passes.
- Current behavior is documented before broad topology changes begin.

### Phase 2: Helper Rework For Index And Momentum Reuse

Target window: sessions 2 to 4.

Main goal:

- Create or clarify a helper layer that can remember the index and momentum
  structure of smaller subdiagrams, especially tree-level diagrams, and reuse
  that logic when loop diagrams create keys, slots, positions, and labels.

Likely tasks:

- Inventory current key families for `momentum-labels`, `momentum-directions`,
  `leg-styles`, `internal-indices`, and line styles.
- Separate topology geometry from slot metadata where practical.
- Define a reusable slot map for external legs and internal propagators.
- Decide how tree-level channel conventions feed loop channel conventions.
- Add regression examples that verify copied or inherited momentum/index
  behavior.

Risks:

- TeX macro state can become fragile if the helper tries to be too generic too
  early.
- A too-broad rework could break carefully tuned diagrams.

Preferred approach:

- Extract only the patterns that are already repeated.
- Keep topology-specific visual placement local when it is genuinely unique.
- Add one helper, migrate one existing topology to it, test, then continue.

### Phase 3: Near-Term Feature Slices

Target window: sessions 4 to 7.

Implement in this order unless new information changes the risk:

1. Momentum arrows for half-box bridges.
2. Triple vertex momentum implementation for the main orientations.
3. Single propagator macros only if useful as an infrastructure probe.
4. Option for an extended leg.

Why this order:

- Half-box bridge momentum is close to existing helper behavior and already has
  a natural slot 5 through the propagator-index path.
- Triple vertex momentum probably touches orientation conventions, so it should
  happen after the helper inventory.
- Single propagator macros can lean on `feynhand`'s existing `\propag`
  primitive, so they do not need to lead the feature queue unless they clarify
  the slot/index model.
- Extended legs may be simple visually, but the option shape should be decided
  after the propagator and vertex momentum conventions are clearer.

Expected regressions:

- A focused propagator-leg regression.
- A focused half-box bridge momentum regression.
- A triple-vertex orientation gallery.
- One README or reference example only after the API feels stable.

### Phase 4: New And Corrected Topologies

Target window: sessions 7 to 12.

Candidate order:

1. Bubble-on-leg prototype using two 3-point vertices, reusing the standalone
   bubble slot and momentum conventions.
2. Tadpole.
3. Seagull.
4. Extended triangle.
5. Corrected cross-box.

Notes:

- The bubble-on-leg topology is not the same as the sunset: it should use two
  3-point vertices to form the bubble on a leg, while sunset has two 4-point
  vertices.
- Future bubble-on-leg variants should include `s` and `t` versions, so the
  implementation should preserve logical bubble slots and translate geometry.
- Tadpole should benefit directly from the helper work.
- The standalone `\BubbleCorr` self-energy macro is now the first real package
  version of the bubble system; future bubble-on-leg work should reuse its
  `bubble-a` / `bubble-b` slot naming, endpoint-index convention, and curved
  momentum defaults.
- Seagull may be conceptually small but needs careful labeling conventions.
- Extended triangle should wait until triangle-contact and triple-vertex
  momentum are more robust.
- Corrected cross-box should happen after the desired correction is pinned down
  visually, because cross-box geometry is easy to misread from text alone.

Expected regressions:

- One `.tex` file per topology under `regressions/topologies/<name>/`.
- Include both default output and at least one momentum/index-labeled variant.
- Add each stable regression to `scripts/check-regressions.sh`.

### Phase 5: General Internal Index Rework

Target window: after the topology/helper pattern is proven.

Main goal:

- Make internal index placement and naming predictable across old and new
  topologies.

Likely tasks:

- Define canonical slot naming for internal lines.
- Preserve backwards-compatible keys where possible.
- Add explicit docs for how external and internal slots are counted.
- Add regression sheets that compare slot behavior across tree, loop, triangle,
  box, and self-energy families.

Risk:

- This is probably the highest-blast-radius item. It should happen only after
  regression coverage is broad enough to catch visual and compile regressions.

## Open Questions

- For "single propagator legs", should this mean standalone one-line diagrams,
  optional replacement of external legs with single propagator stubs, or both?
- For "extended leg", should the option be global, per-leg, or both?
- For half-box bridge momentum arrows, which bridge segments need arrows by
  default, and should their direction inherit from existing half-box momentum
  flow?
- For triple vertex momentum, which orientations matter first: all-in/all-out,
  rotated geometric variants, or the vertex-identity use cases?
- How should insertion orientation and momentum placement translate to the
  other external host slots after the t-tree slot-1 prototype?
- For corrected cross-box, what specifically is wrong in the current version:
  geometry, momentum direction, internal index order, crossing style, or API?
- Should future topology names follow physics names only, or include aliases
  like `self-energy`, `bubble`, and `two-point-loop`?

## Loop Momentum Audit Notes

2026-09-12 audit target:

- The old `loop-channel` and `sunset` systems should be treated as
  partially-finished visual systems, not as final defaults to inherit.
- `regressions/topologies/loop-audit/loop-momentum-audit.tex` compares current
  defaults, documented manual relief settings, reversed flow, mixed internal
  styles, crossed-channel crowding, and sunset momentum/index presets.

Initial findings from the rendered audit:

- Keep the logical idea of two internal loop slots (`a/b`, with visual
  top/bottom or left/right aliases) and per-line momentum text/direction.
- Keep per-line style overrides; they are useful for future bubble-on-leg
  diagrams where the two bubble propagators may differ.
- Revise loop-channel defaults before reusing them: the raw labels can ride too
  close to arrows/curves, while the documented relief settings sometimes feel
  too detached or large.
- Revise crossed-channel defaults separately; the `u` channel has different
  crowding because crossed external momenta compete with the right loop label.
- Avoid copying the sunset approach directly into bubble-on-leg work. Sunset is
  useful for multi-line momentum/index stress, but its two 4-point vertices and
  older y-shift-heavy controls are not the geometry model for a bubble made
  from two 3-point vertices.

Next implementation rule:

- Build a private modern curved-momentum helper for bubble-on-leg diagrams
  using the audited concepts, then backport improvements to `loop-channel` or
  `sunset` only after the new helper proves its defaults visually.

## Generic Insertion Architecture Notes

2026-09-12 planning target:

- Treat this branch as the standalone bubble and loop-audit groundwork branch;
  do not add public insertion keys here.
- Future bubble-on-leg, seagull, counterterm, and related diagrams should use a
  shared insertion model instead of one-off topology hacks.
- Research reference: TikZ-Feynman/FeynHand model `insertion` as an
  edge-attached object with position, size, and style. For this package, keep
  the same conceptual shape, but expose semantic keys and let each topology
  translate them into concrete geometry.

Planned first insertion API direction:

- Start with one insertion per diagram.
- Prefer semantic public keys such as `insertion=none|bubble|seagull|counterterm`,
  `insertion-slot=...`, `insertion-position=...`,
  `insertion-orientation=auto|top|bottom|left|right`, `insertion-style=...`,
  and `insertion-scale=...`.
- Do not make users pass arbitrary TikZ drawing code in the first public API.
  Advanced custom hooks can wait until semantic presets are stable.
- Topology macros should own the geometry: split the chosen host propagator,
  place the insertion object, preserve host momentum/label behavior, and route
  insertion-specific momenta/indices through the package's existing slot model.
- The first prototype should reuse `\BubbleCorr` conventions: `bubble-a` /
  `bubble-b` slots, two endpoint indices per internal propagator,
  vertex-side external indices, curved momentum defaults, and white-filled
  equilateral `spol`/Proca endpoint markers.

2026-09-12 implementation start:

- The first prototype branch is `codex/bubble-on-leg`.
- The first supported host is `TTreeChannelCorr` / `topology=t-tree`.
- The first supported insertion is `insertion=bubble` on external slot `1`.
- The prototype splits the slot-1 host leg into pre-insertion and
  post-insertion segments, places two insertion vertices on that leg, and draws
  the bubble internals with the standalone `\BubbleCorr` style conventions.
- Unsupported insertion slots and types remain no-ops for now.
- Next expansion target after visual approval: add an internal slot-5 insertion
  case or a second external slot, then decide whether seagull should share the
  same host-splitting helper.

2026-09-12 branch closeout:

- `codex/bubble-on-leg` now contains the first semantic insertion prototype:
  `insertion=bubble` on `TTreeChannelCorr` / `topology=t-tree` external slot
  `1`.
- The insertion implementation owns the host split into pre-insertion and
  post-insertion segments, reuses the standalone bubble visual conventions, and
  exposes tuning keys for bubble endpoint indices, pre/post slot-1 momentum,
  and the detached middle-channel momentum annotation.
- The branch intentionally stops at one insertion type on one host slot. This
  keeps the mergeable slice focused while proving the public semantic API
  shape.
- Follow-up order after merge:
  1. Quartic/seagull leg insertion using the same semantic insertion model.
  2. Swordfish-style insertion, reusing the host-split and momentum/index
     lessons from bubble and seagull.
  3. Triangle insertion/topology work after the lower-order insertion cases are
     visually stable.
- The next branch should avoid broadening arbitrary user draw hooks. Continue
  with package-owned insertion objects, semantic slot keys, and focused
  regressions for each new insertion family.

2026-09-12 seagull insertion start:

- Created `codex/seagull-insertion` from clean `main`.
- The branch adds `insertion=seagull` as the second semantic insertion object,
  still scoped to `TTreeChannelCorr` / `topology=t-tree` external slot `1`.
- V1 seagull means one quartic/contact insertion vertex on the host leg with a
  compact package-styled self-loop propagator that starts and ends at that
  vertex.
- This branch should not change triangle-contact momentum routing; that remains
  a later per-internal-edge cleanup.
- Revised follow-up order after seagull:
  1. Bubble insertion orientation and other host slots.
  2. Swordfish insertion.
  3. Triangle-contact momentum rework with per-edge internal controls.

## Completed

- 2026-10-26: Closed out seagull insertions, endpoint-marker repairs, external
  momentum controls, mini indices, and the scalar-QED Compton example. Removed
  superseded private helpers and repository metadata/scratch files, refreshed
  curated PDFs, and expanded the isolated regression runner to 33 documents.
- 2026-09-06: Confirmed the previous regression-check commit had not yet been
  made. Created commit `057bfbd Add feynman-fun regression checks` on
  `codex/adopt-feynman-fun` without pushing.
- 2026-09-06: Added this development plan.
- 2026-09-06: Committed the initial planning roadmap as
  `8ab5737 Add development planning roadmap`.
- 2026-09-06: Inspected the current helper structure and documented the
  implementation inventory in this file.
- 2026-09-06: Added opt-in half-box bridge momentum arrows, reference docs, and
  a focused regression.
- 2026-09-06: Made box and cross-box geometry square by default by matching
  `box-yspan` to `box-xspan` and `box-external-yspan` to
  `box-external-xspan`.
- 2026-09-11: Closed the adoption audit for branch review: restored the
  accidental `Icon\r` deletion, tracked the generated half-box bridge momentum
  regression PDF, confirmed maintained regressions pass, and pushed
  `codex/adopt-feynman-fun`.
- 2026-09-11: Started the translation-safe topology foundation on
  `codex/translation-safe-topology`, using `\ThreePointCorr` as the first
  controlled test for logical slots under rotated geometry.
- 2026-09-11: Added a three-point translation regression, simplified private
  three-point label/momentum helper calls, and confirmed focused plus full
  regressions pass.

## Last Session Update

2026-10-26 repository cleanup and merge preparation:

- Organized package work into separate seagull/endpoint-marker, momentum,
  mini-index, Compton-example, and repository-maintenance commits.
- Preserved intentional geometry and the t-tree external-slot-1 limitation
  for both insertion families. Broader host-slot support remains follow-up work.
- Removed unused marker experiments and an unused momentum helper; the active
  marker queue and curve-tangent path remain shared by bubbles and seagulls.
- Rendered and compared curated PDFs against the merge baseline. Updated
  visibly different previews, kept the pixel-identical Proca sheet unchanged,
  and corrected the circ-marker tuning row's wrapped captions.
- Preserved the existing policy that selected build-only PDFs stay ignored.
  Moved the Compton PDF beside its source and documented reuse/build commands.
- Replaced repository-wide scratch deletion with a unique temporary build
  directory. The suite now includes all 30 regression documents plus the three
  main examples, with the final LaTeX log excerpt printed on failure.
- All 33 documents passed from the repository root and from `/private/tmp`.
  Focused intermediate commit builds passed, including momentum visibility,
  curved marker-count/dimension assertions, mini indices, and compatibility.
  The runner's simulated failure diagnostics, temporary cleanup, and existing
  scratch-file preservation also passed; `git diff --check` passed.
- Legacy loop-channel/sunset momentum crowding remains recorded in the audit;
  this closeout preserves those established layouts.
- Next action: PR review and user-controlled merge, then broader bubble host
  slots on a separate branch, followed by swordfish and triangle momentum work.

## Earlier Session Updates

The dated entries below retain the status and plans recorded at each session;
their references to uncommitted work are superseded by the closeout above.

2026-09-11:

- Verified branch: `codex/adopt-feynman-fun`.
- Audited branch contents against `main`; local adoption commits are
  `2253c64`, `057bfbd`, `8ab5737`, `ae00ab2`, `dd56536`, and `d195189`.
- Confirmed current usage at start of closeout: 5-hour window 6% used, weekly
  window 1% used, with 3 full reset credits available.
- Ran `scripts/check-regressions.sh`; all maintained checks passed.
- Restored the accidental tracked `Icon\r` deletion.
- Added the generated
  `regressions/topologies/vertex-identity/half-box-bridge-momentum.pdf` so the
  new regression follows the existing source-plus-rendered-PDF pattern.
- Updated this roadmap so the branch no longer looks like an abandoned
  adoption session.
- Pushed `codex/adopt-feynman-fun` to `origin/codex/adopt-feynman-fun` as a
  reviewable checkpoint.
- Switched to `main` after the adoption branch was merged, then created
  `codex/translation-safe-topology` for the next focused slice.
- Recorded the translation model for future bubble, seagull, and swordfish
  work: public keys bind to logical slots while orientation translates
  geometry, anchors, offsets, and momentum/index placement.
- Added
  `regressions/topologies/three-point/three-point-translation-check.tex` to
  make logical slot translation visible across right, left, up, and down
  orientations.
- Simplified `\ThreePointCorr` label placement and momentum drawing through
  private helper calls that use the orientation-resolved slot metadata.
- Usage checkpoint: 5-hour window 35% used, weekly window 5% used, with 3 full
  reset credits available at the start of this slice.
- Focused compile passed for
  `regressions/topologies/three-point/three-point-translation-check.tex`.
- Visually inspected both rendered translation-check pages. Logical slot data
  remains attached under right, left, up, and down rotations; the dense
  horizontal momentum-label cases expose crowding to consider in the deeper
  helper design.
- Ran `scripts/check-regressions.sh`; all maintained checks passed, including
  the new translation regression.
- Usage checkpoint after implementation and checks: 5-hour window 72% used,
  weekly window 11% used, with 3 full reset credits still available.
- Did not rename the remote repository.
- Did not delete branches.
- 2026-09-11: Added the next orientation slice: a generic `orientation` key
  that resolves corner pairs such as `{top,left}` and `{bottom,right}` for
  diagram families that opt into it. `\ThreePointCorr` now uses this resolver,
  while legacy `three-point-orientation` values remain aliases.
- Tuned three-point default momentum label clearance and added the missing
  reset for `three-point-momentum-label-gap`, so rotated diagrams do not depend
  on stale or too-tight defaults.
- Corrected the up/down three-point momentum-angle metadata so rotated
  momentum labels offset perpendicular to their propagator lines instead of
  riding the wavy line.
- 2026-09-12: Added the first package-level self-energy bubble,
  `\BubbleCorr`, with `\SelfEnergyCorr` and `\SelfEnergyBubbleCorr` aliases,
  standalone bubble keys, opt-in curved loop momenta, two-endpoint internal
  indices, managed amputated external endcaps, reference docs, and a focused
  bubble regression.

Next planned action:

- Finish and review `codex/seagull-insertion`, then use a separate branch to
  generalize bubble insertions across the other external leg slots before
  swordfish and the triangle-contact momentum rework.

## 2026-10-16 Tree-channel label-gap fix

- On `codex/seagull-insertion`, fixed the tree-channel momentum helper so
  side-positioned labels no longer leave an empty interruption in the arrow.
  Explicit `channel-momentum-label-position=center` retains the intentional gap.
- Added `regressions/topologies/channel/channel-momentum-label-gap.tex` and its
  rendered PDF, covering the supplied charged-scalar t-tree example, side
  labels on horizontal/vertical guides, and a centered label.
- Visually checked the focused PDF; all 18 maintained regression checks pass.
- Existing seagull/endpoint-marker work remains uncommitted. Next: finish its
  visual review and branch closeout before expanding insertion host slots.

## 2026-10-16 External momentum visibility

- Added `external-momentum-hide={...}` for logical external slots across
  two-/three-/four-point families, bubble, and sunset. It overrides supplied
  labels and existing topology slot selectors without changing propagators,
  particle labels, endpoint markers, or internal momenta.
- Hiding insertion slot 1 removes both pre/post momentum annotations. Rotated
  three-point geometry retains logical slot numbering.
- Explicitly empty label entries now emit a continuous unlabeled external
  arrow and no label node; empty list positions remain intact. Missing list
  entries retain their existing automatic labels. No sentinel label strings.
- Added a three-page visual regression and behavioral assertions in
  `regressions/momenta/external-momentum-visibility.tex`, registered in the
  maintained suite. Checks cover precedence, empty/braced/whitespace entries,
  ordinary labels, both flow directions, no state leakage, each diagram family,
  internal momentum preservation, and split insertion legs.
- All 19 maintained checks passed; the focused sheet passed again after visual
  layout tuning. Visually inspected all three pages, and documented the key in
  `docs/reference.md`. Changes remain uncommitted on `codex/seagull-insertion`.

## 2026-10-17 Mini external index formatting

- Added `index-placement=mini` using the existing external field/index helper.
  Empty fields now support compact indices on an empty math base (`{}_{...}`)
  without a horizontal spacer. Nonempty fields retain normal subscripts;
  explicit leg labels retain precedence. Other placement modes are unchanged.
- Added and visually inspected `regressions/labels/mini-index.tex` and its PDF,
  covering the square double-endcap example, field subscripts, explicit label
  overrides, rotated logical slots, and normal formatting in the next diagram.
- Documented the mode in `docs/reference.md` and added the focused regression
  to the maintained suite.
- All 20 maintained regression checks passed. Changes remain uncommitted on
  `codex/seagull-insertion`.

## 2026-10-17 One-sided curved Proca marker repair

- Reproduced the reported seagull example: start/end selections queued the
  correct markers, but the curve helper sized triangles from the tiny distance
  between the endpoint tip and a 16-percent curve sample. On the default
  seagull, that reduced marker sides to roughly 0.4pt and hid the feature.
- Fixed the shared curved endpoint helper to use the configured propagator
  arrow size for equilateral triangles, using the sampled outward curve tangent
  for orientation. Vertex-boundary tip placement remains intact.
- Added `regressions/propagators/proca/one-sided-loop-markers.tex` and its
  two-page PDF. The exact user macro is included with start-only, end-only,
  and both-end variants. Assertions check actual emitted marker counts and
  triangle dimensions across standalone bubbles, inserted bubbles, seagulls,
  and 3pt/10pt sizes on different loop radii. The old geometry fails this check.
- Visually inspected both pages and documented start/end semantics in the
  reference. Changes remain uncommitted on `codex/seagull-insertion`.
- All 21 maintained regression checks passed after the repair.
