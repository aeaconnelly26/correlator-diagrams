# Box Loop Visual QA Handoff

Branch: `codex/box-loop-topology`

## Current State

- The one-loop box topology exists as `\BoxLoopCorr[...]`.
- The same topology is available through `\FourPointCorr[topology=box,...]`.
- The topology structure is in place: four corner vertices, four internal edges, four diagonal external legs, edge momentum labels, and a central clockwise loop arrow.
- The photon style has been changed back to a single decorated wavy path instead of a charged-boson path plus a second wavy postaction.
- Box external momentum arrows now have box-specific placement controls, so their arrows can be longer without changing the external leg geometry.
- Three-point momentum arrows now share one default span and label fraction, so their label placement is consistent by default.
- The examples keep wavy and plain specimens so topology structure and photon rendering can be inspected separately.

## Visual Items To Reinspect

- Confirm the wavy/photon style now reads as a single clean wave in box, three-point, and channel diagrams.
- Confirm the thinner momentum arrows feel informative but not too faint.
- Confirm centered three-point momentum labels no longer create confusing collisions in examples.
- Confirm the W/Z label-only box still has no momentum arrows.

## Suggested QA Plan

1. Recompile `box-topology-regression.tex`, `three-point-check.tex`, and `example.tex`.
2. Inspect the rendered box and three-point pages as PNGs.
3. Inspect `channel-topology-regression.pdf`, since photon style is global.
4. If the visuals are accepted, run the full compile plan and prepare the branch for review.

## Not Merge Ready Yet

The topology is in a good checkpoint state, but this branch should stay open until the updated visuals have been inspected and accepted.
