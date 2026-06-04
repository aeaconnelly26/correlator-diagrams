# Box Loop Tomorrow Handoff

Branch: `codex/box-loop-topology`

## Current State

- The one-loop box topology exists as `\BoxLoopCorr[...]`.
- The same topology is available through `\FourPointCorr[topology=box,...]`.
- The topology structure is in place: four corner vertices, four internal edges, four diagonal external legs, edge momentum labels, and a central clockwise loop arrow.
- The examples now keep only one wavy/photon-style box specimen. The other box examples use plain lines so the topology can be inspected without the wavy-line issue getting in the way.

## Known Issue To Investigate

- Wavy/photon-style legs look suspicious. Do not merge yet.
- Tomorrow's first task should be to isolate whether the problem is:
  - the global photon override in `\corr@configurestyles`,
  - the interaction between TikZ-FeynHand photon decoration and short diagonal legs,
  - the box-specific defaults,
  - or a broader wavy-line style regression.

## Suggested Tomorrow Plan

1. Recompile `box-topology-regression.tex` and inspect the three boxes.
2. Compare the one wavy box against the two plain boxes.
3. If the plain boxes look structurally good, keep the topology implementation and focus only on photon/wavy style.
4. Try a small isolated TeX file with one diagonal photon leg, one horizontal photon edge, and one vertical photon edge.
5. Decide whether to tune global photon style, make a box-specific wavy style, or revert the global looseness and defer wavy polish.
6. After visual approval, rerun the full compile plan before opening/finishing the PR.

## Not Merge Ready Yet

The topology is in a good checkpoint state, but this branch should stay open until the wavy-line rendering is understood and cleaned up.
