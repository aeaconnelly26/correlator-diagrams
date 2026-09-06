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

- Confirm whether the previous git checkpoint was completed.
- If not completed, make the requested regression-check commit.
- Create this planning document so future work has a durable roadmap.
- Do not push.
- Do not rename the remote repository.
- Do not delete branches.

Stretch goal if there is enough time after the plan:

- Inspect the current topology and momentum helper structure in
  `feynman-fun.sty`.
- Identify the smallest next implementation slice for single propagator legs
  and half-box bridge momentum arrows.

## Next Session

Recommended first technical session:

- Focus area: helper design and inventory.
- Read the existing helper families for external legs, internal momentum slots,
  topology dispatch, and key handling in `feynman-fun.sty`.
- Document the slot conventions for the topologies that already work.
- Add a short internal note in this file describing which helpers should be
  reused for new loop topologies.
- Avoid adding new visual features until the helper plan is clear.

Likely deliverable:

- A small implementation memo in this file, or a new `docs/internal-design.md`
  if the notes become too large.

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

1. Single propagator legs implementation.
2. Momentum arrows for half-box bridges.
3. Triple vertex momentum implementation for the main orientations.
4. Option for an extended leg.

Why this order:

- Single propagator legs and half-box bridges are close to existing helper
  behavior and should improve confidence before larger topology work.
- Triple vertex momentum probably touches orientation conventions, so it should
  happen after the helper inventory.
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

## Last Session Update

2026-09-06:

- Verified branch: `codex/adopt-feynman-fun`.
- Verified baseline before the regression commit: `2253c64 Adopt feynman-fun
  package`.
- Ran `scripts/check-regressions.sh`; all listed checks passed.
- Committed the requested regression-check files as `057bfbd Add feynman-fun
  regression checks`.
- Created `docs/development-plan.md` as the planning and handoff document.
- Did not push.
- Did not rename the remote repository.
- Did not delete branches.

Next planned action:

- Start Phase 1 and Phase 2 together in a light way: inspect current topology,
  index, and momentum helpers, then write down the helper inventory before
  implementing new diagram features.
