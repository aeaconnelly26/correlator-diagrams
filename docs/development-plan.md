# Feynman Fun Development Plan

Living plan for the next phase of `feynman-fun`. This document should be
updated at the start and end of each work session so a future session can pick
up quickly without spending credits reconstructing context.

## Current State

- Date created: 2026-09-06
- Active branch: `codex/adopt-feynman-fun`
- Recovery baseline: `2253c64 Adopt feynman-fun package`
- Regression checkpoint: `057bfbd Add feynman-fun regression checks`
- Push status: not pushed by Codex
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

Goal for 2026-09-06:

- Implement opt-in half-box bridge momentum arrows using existing bridge slot 5.
- Add a focused regression for bridge momentum behavior.
- Update the reference docs and this roadmap with the result.
- Do not push.
- Do not rename the remote repository.
- Do not delete branches.

Usage checkpoints:

- Start of implementation: 5-hour window 11% used, weekly window 19% used.
- After helper inspection: 5-hour window 24% used, weekly window 21% used.
- Before bridge-momentum implementation: 5-hour window 39% used, weekly window
  23% used.
- After bridge-momentum tests: 5-hour window 50% used, weekly window 25% used.

## Next Session

Recommended first technical session:

- Focus area: triple vertex momentum implementation for the main orientations.
- Start from the existing three-point orientation coordinate helpers and
  momentum angle helpers.
- Decide whether triple-vertex momentum means improving `\ThreePointCorr`
  itself, adding a reusable lower-level triple-vertex helper, or both.
- Add a focused orientation regression before any broad topology migration.

Likely deliverable:

- A small design note or code change for triple-vertex momentum orientation,
  one focused regression `.tex`, and updates to reference docs if the API
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

## Last Session Update

2026-09-06:

- Verified branch: `codex/adopt-feynman-fun`.
- Verified baseline before the regression commit: `2253c64 Adopt feynman-fun
  package`.
- Ran `scripts/check-regressions.sh`; all listed checks passed.
- Committed the requested regression-check files as `057bfbd Add feynman-fun
  regression checks`.
- Created `docs/development-plan.md` as the planning and handoff document, then
  committed the initial version as `8ab5737 Add development planning roadmap`.
- Inspected `feynman-fun.sty` for topology dispatch, `\propag` usage, momentum
  helpers, index helpers, half-box structure, and three-point orientation logic.
- Added the `Implementation Inventory` section above.
- Reframed single propagator macros as a possible infrastructure probe instead
  of a top user-facing priority.
- Implemented opt-in half-box bridge momentum arrows using existing bridge slot
  5.
- Added keys for bridge momentum label, direction, start/end, offset, label
  fraction, and label gap, plus `halfbox-*` aliases.
- Added `regressions/topologies/vertex-identity/half-box-bridge-momentum.tex`
  and included it in `scripts/check-regressions.sh`.
- Updated `docs/reference.md` with the new half-box bridge momentum keys and a
  compact example.
- Ran the focused bridge momentum regression; it passed.
- Ran `scripts/check-regressions.sh`; all maintained checks passed.
- Usage checkpoints: implementation started at 11% 5-hour / 19% weekly, and
  after helper inspection was 24% 5-hour / 21% weekly. Bridge-momentum work
  started at 39% 5-hour / 23% weekly; after tests it was 50% 5-hour / 25%
  weekly.
- Did not push.
- Did not rename the remote repository.
- Did not delete branches.

Next planned action:

- Plan or implement triple vertex momentum orientations. Start by clarifying
  whether the goal is only better `\ThreePointCorr` orientation behavior or a
  reusable lower-level triple-vertex helper that future loop topologies can
  call.
