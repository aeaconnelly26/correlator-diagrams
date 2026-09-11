# Feynman Fun Development Plan

Living plan for the next phase of `feynman-fun`. This document should be
updated at the start and end of each work session so a future session can pick
up quickly without spending credits reconstructing context.

## Current State

- Date created: 2026-09-06
- Active branch: `codex/adopt-feynman-fun`
- Recovery baseline: `2253c64 Adopt feynman-fun package`
- Regression checkpoint: `057bfbd Add feynman-fun regression checks`
- Push status: pushed by Codex as review branch after 2026-09-11 adoption
  closeout
- Remote repository: do not rename
- Branch cleanup: do not delete branches
- Current priority: confidence and maintainability before new diagram features
- Visual tuning in `feynman-fun.sty`: assume intentional unless it is dead
  commented scratch text

## Session Protocol

At the start of each session:

1. Run `git status --short --branch`.
2. Confirm the branch is `codex/adopt-feynman-fun` unless the user says
   otherwise.
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

Goal for 2026-09-11:

- Finish the adoption branch, then start one focused topology-foundation slice.
- Use `\ThreePointCorr` to prove the logical-slot translation model before
  adding new bubble, seagull, or swordfish topologies.
- Add a focused regression for rotated labels, indices, styles, and momenta.
- Keep public APIs stable unless a narrow bug fix requires a change.
- Do not rename the remote repository.
- Do not delete branches.

Usage checkpoints:

- Start of adoption closeout: 5-hour window 6% used, weekly window 1% used.
- Start of translation-safe topology slice: 5-hour window 35% used, weekly
  window 5% used.
- End of translation-safe topology slice: 5-hour window 72% used, weekly
  window 11% used.
- Available reset credits: 3 full Codex resets.
- Maintained regression suite passed during adoption closeout.
- Maintained regression suite passed after the translation-safe topology slice.

## Next Session

Recommended first technical session:

- Focus area: use the three-point topology to prove translation-safe logical
  slots before adding new loop topologies.
- Start from the existing three-point orientation coordinate helpers, label
  offset metadata, and momentum angle helpers.
- Keep `\ThreePointCorr` public keys stable while making private helpers
  clearer about logical slot data versus translated geometry.
- Add a focused orientation regression before any broad topology migration.

Likely deliverable:

- A small design note, a private three-point helper cleanup, one focused
  translation regression `.tex`, and updates to reference docs only if the API
  changes.

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

1. Self-energy/bubble.
2. Tadpole.
3. Seagull.
4. Extended triangle.
5. Corrected cross-box.

Notes:

- Self-energy/bubble and tadpole should benefit directly from the helper work.
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
- For seagull, what is the preferred visual convention: two external legs plus a
  loop at one vertex, or a contact-like vertex with an attached loop?
- For corrected cross-box, what specifically is wrong in the current version:
  geometry, momentum direction, internal index order, crossing style, or API?
- Should future topology names follow physics names only, or include aliases
  like `self-energy`, `bubble`, and `two-point-loop`?

## Completed

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

Next planned action:

- Commit and push `codex/translation-safe-topology` as a reviewable foundation
  slice. After review, decide whether the next branch should deepen the
  reusable triple-vertex helper or begin the first two-line bubble topology
  prototype.
