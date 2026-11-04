# Current diagram inventory

[Open the atlas](inventory.pdf) or [copy a recipe](recipes.md).

Built against `codex/m03a-t-tree-bubbles`, based on synchronized
`main` at `b917ed2`, on 2026-11-03. There are **54 current examples on eleven
pages**, including the structural/style gallery, five seagull examples, three
integrated annotation controls, and eight M02 annotation examples. These are not
54 distinct graph topologies: aliases, orientations, and style variants are
identified separately.

M03a adds lower-left, upper-right and lower-right t-tree bubble placements.
I29 retains slot 1; B02-B04 show the other legs. This branch is checkpointed
locally and has not yet been merged or pushed.

## How to read it

- Pages 1-6 show minimal structures with fields and momentum annotations hidden;
  page 6 now includes all four t-tree self-energy insertion placements.
- Page 7 demonstrates named style/annotation features, including the explicitly
  requested pink Proca t-bubble with four double-capped EW legs.
- Page 8 shows the supported seagull prototype and one-/two-sided Proca loop
  markers, without caps, circles, labels, or momenta. U01/U02 retain their stable
  identifiers from the former branch-only preview; they now work here.
- Page 9 demonstrates compact indices, logical-slot momentum hiding, unlabeled
  arrows, and the tree-channel side-label fix.
- Page 10 demonstrates independent triangle-contact momentum placement in all
  four orientations. T01-T04 have reproducible per-slot recipes.
- Page 11 shows continuous arrows with outward labels in all four orientations
  (T05-T08), selected globally or per annotation with `layout=side`.

Important limits:

- Bubble insertions support **t-tree external slots 1-4**, one at a time.
  Seagulls remain **t-tree external slot 1 only**. S/u hosts and internal
  bubble insertions are unsupported; accepted keys can still do nothing there.
- Horizontal/vertical contact pairings are disconnected pairs, not tree exchanges.
- The existing crossed box fixes its side edges and crosses its diagonals;
  internal momentum/index coverage remains incomplete.
- All four triangle-contact orientations have independent annotation controls
  for slots 1-7. A regular triangle attached to a tree is a different missing graph.
- `SunsetDiagram` is a two-loop graph.
- The integrated endpoint matrix certifies its documented circular vertices,
  scales, and settings, not every arbitrary custom transform or vertex shape.

The original unmerged seagull preview is preserved in
[history](../planning/history/seagull-branch-examples-5a657cd.pdf). It is not
embedded in the current atlas. The Compton example uses existing package tree
and contact primitives; see `compton-example/` for its reusable example macros.

## Rebuild

From the repository root:

```sh
python3 docs/diagram-inventory/build.py
```

Requires Python 3, `pdflatex`, the package's normal TeX dependencies, and
`adjustbox`. All examples are compiled against the current checkout in one
build; the builder no longer extracts a package from another Git revision or
embeds a branch-only PDF. Compiler products stay in a temporary directory.

`catalog.json` is the source for example metadata/options. Edit it and rebuild;
do not edit the generated TeX or recipe index independently.

To compile the checked-in TeX without regenerating the catalog outputs:

```sh
TEXINPUTS="$PWD//:" pdflatex -halt-on-error -output-directory=/tmp docs/diagram-inventory/inventory.tex
```

Generated PDF byte hashes can change between builds because TeX records build
metadata. Compare content and rendering, not byte identity.

See [verification](verification.md) for the audit boundary and
[the roadmap](../development-plan.md) for work that has not been implemented.

## Aliases and presets

These names do not add graph topologies:

| Alias / preset | Canonical construction |
| --- | --- |
| `TwoPtCorr`, `ThreePtCorr`, `FourPtCorr` | `TwoPointCorr`, `ThreePointCorr`, `FourPointCorr` |
| `SelfEnergyCorr`, `SelfEnergyBubbleCorr` | `BubbleCorr` |
| `SLoopChannelCorr`, `TLoopChannelCorr`, `ULoopChannelCorr` | `SChannelCorr`, `TChannelCorr`, `UChannelCorr` |
| `SunsetDiag` | `SunsetDiagram` |
| `ThreePointThesis`, `ThesisVertex` | Styled `ThreePointCorr` preset |
| `FourPointCorr[topology=...]` | Dispatch form of the named contact/channel/box/identity helpers |

The generic three-point corner orientation and legacy cardinal orientation
keys resolve to the same four layouts. The compatibility package
`correlator-diagrams.sty` loads `feynman-fun`; it is not a separate inventory.
