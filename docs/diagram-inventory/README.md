# Current diagram inventory

[Open the atlas](inventory.pdf) or [copy a recipe](recipes.md).

Inventoried from `main` at `0dbf733` on 2026-11-03 and refreshed with M01 on
`codex/proca-endpoint-audit`. The eight-page atlas contains **29
structural/layout examples and 6 styled examples** on seven current-capability pages, plus **two unmerged-branch seagull examples** on page eight. These are
not 35 distinct graph topologies: aliases, rotations, pairings, and marker
presets are identified as such. M01 corrects generic Proca endpoint placement;
it adds no topology. See the [endpoint audit](../../regressions/propagators/proca-endpoints/README.md).

## How to read it

The first six pages use plain lines with annotations hidden. Page seven shows
selected existing styles, including the requested t-channel bubble with pink
Proca internals and four double-capped EW external legs. Each example has a
stable ID and a complete recipe in the recipe index. The caption names any
important limitation. Page eight is explicitly branch-only: its seagull recipes require `codex/seagull-insertion` at the pinned revision; they do not work in the current checkout.

- Horizontal and vertical contact pairings are disconnected pairs, not tree
  exchanges with a hidden bridge.
- The existing crossed box fixes its side edges and crosses its diagonals.
  A crossing is not a vertex; internal momentum/index coverage is incomplete.
- The four triangle-contact orientations already exist. A regular triangle
  attached to a tree is a different graph and remains future work.
- `SunsetDiagram` is a two-loop graph.
- Bubble insertion currently works only on t-tree external slot 1.
  Accepted insertion keys for other combinations can be silently ignored.
- Plain-line coverage does not certify every decorated or densely labeled
  combination. M01 verifies standard-dot endpoint contact in its diagnostic
  matrix; triangle labels remain M02 work, and new families must repeat endpoint checks.

## Rebuild

From the repository root:

```sh
python3 docs/diagram-inventory/build.py
```

Requires Python 3, Git (to read the pinned branch package), `pdflatex`, `feynman-fun`'s normal TeX dependencies, `adjustbox`, and `pdfpages`. The builder uses a temporary directory for compiler output and
keeps only the PDF, generated TeX, and Markdown recipes here. `catalog.json`
is the single source for the example metadata and options, including the
branch-preview revision. The builder compiles the branch page in a temporary
directory with that revision's package, then embeds its PDF in the atlas; it
never switches or merges the working branch. Edit it, then
rebuild; do not edit the generated files independently.

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
