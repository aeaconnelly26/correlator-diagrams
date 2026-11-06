# Current diagram inventory

[Open the atlas](inventory.pdf), [copy a recipe](recipes.md), or
[review all 16 insertion momentum examples](../../regressions/topologies/insertion/insertion-momentum-review.pdf).

Complete locally on `codex/m06-tree-triangles`, based on published main
`eb6182c` (2026-11-06). M06 has not been merged/pushed. There are **102 current
examples on twenty-three pages**. These are recipes and meaningful layouts/styles,
not 102 distinct graph topologies. M06 adds all four regular tree triangles
with equilateral defaults and four mixed-style/annotation samples; see
[verification](../planning/m06-verification.md). M05 remains published on main.

Every recipe now uses the compact coordinate baseline: `scale=1` matches the
former `scale=0.8`; use `scale=1.25` to recover the former unit-scale size.
The logical shared frame is still +/-2.10, rendered as a 3.36 cm square at
`scale=1`. Text and markers retain the existing TikZ sizing behavior. See
[scale verification](../planning/scale-baseline-verification.md).

Ordinary S exchanges and their external bubble/seagull/swordfish variants
now default to half-span 1.05 (about 35% longer exchange), with unchanged
outer endpoints. S triangle corrections retain 0.78. Explicit
`channel-vertex-xspan=0.78` recovers the former ordinary S geometry. See the
[plain comparison gallery](../../regressions/topologies/channel/s-tree-span-regression.pdf)
and [verification](../planning/s-tree-span-verification.md).

M03a adds the four t-tree bubble placements (I29, B02-B04) and is published
on main. M03b adds all four s-tree placements (C01-C04); verified checkpoint
`97495ba` is now also merged and published on main. Index positioning remains a later
[dedicated review](../planning/deferred-workflows.md); attachment checks do not
certify its visual placement. M04 adds all eight seagull placements (G01-G04,
G11-G14), included in published main. G01 repeats U01's structure
to present the complete t-tree placement matrix. T seagulls now default inward,
S seagulls outward. The shared insertion-arrow review shortens guides, clears
labels and uses 1/2 incoming, 3/4 outgoing throughout; H01-H04 demonstrate it.
Short bubble host arrows expand for readability; S bubble k/ell labels move
outward along the normal, with T bubble-loop annotation placement unchanged.
The subsequent seagull-k review uses concentric momentum curves and local-normal
labels at the arrow midpoint across all eight placements. The compact defaults
now use range 0.30-0.52, a 6pt radial offset and 2pt text clearance. Counts
were 74/16 after the M04 size/style sampling addition; M05 expands them to 86/19.
The loop-spacing review uses closer bubble momentum arrows and labels outward
from their actual arcs, consistently across left/right placements and reversal.

Seagulls now default to `insertion-position=0.40` (outer endpoint toward tree
vertex), giving the inner segment 20% more length. Styled seagull W circles
use `circ position=0.57332` (T) or `0.57513` (S) to balance the visible spaces
between the pink arrow and black dot in the shared 2.10/2.10 frame. This corrects the former geometric-0.5
criterion, which did not account for the arrow footprint. Set
`insertion-position=0.50` to recover the former seagull placement; bubble
positions remain 0.50.

Default bubble insertions now use scale 0.50 (about 24% smaller); seagulls
remain 0.66. Explicit `insertion-scale=0.66` restores the previous bubble size.
Page 16 samples pink EW Z stems (including the circle and Z text), bare
outer host segments, inner EW W circles, pink scalar-polarization loops
without circles, and mixed EW W / scalar-polarization Z bubbles. The pink loop
recipes use `proca` for two endpoint arrows; `circ` is a separate option. Only the pink
loop arc carries k; the W arc has no momentum guide or label. See the
[all-slot styled gallery](../../regressions/topologies/insertion/insertion-species-samples.pdf)
for all sixteen placements. The styled samples now hide central momentum
arrows and P labels with `show-channel-momentum=false`, while retaining Z
species circles. S samples use a 4pt inner-label gap; ordinary defaults remain
unchanged. The new visibility control is also available on plain s/t/u trees.
The W bubble arcs now use `ewboson wavelength=10\feynhandlinesize` for clearer
ripples around the W circle; the ordinary wavelength remains 22 line widths.

The shared default outer corners are now +/-2.10 on both axes, including the
ordinary/corrected trees, box/crossed box and triangle-contact. Explicit
`fourpoint-xspan/yspan` applies across these families; explicit family external
spans still override it. Inner box/triangle geometry and graph connectivity
are preserved. Historical PDFs/checkpoints retain their own default spans.

## How to read it

- Pages 22-23 compare the shared +/-2.10 outer frame across ordinary T trees,
  regular triangles, box/crossed box and all triangle-contact orientations
  (L21-L24/L31-L34). These repeat existing graphs to demonstrate alignment.
- Page 20 shows all four regular tree-attached triangles (L01-L04), using
  plain lines and no annotations. The triangle is equilateral by default,
  enlarged 50% from the first review preview, and
  has three trivalent loop vertices, joined to the fourth by an exchange bridge.
- Page 21 shows mixed EW/Proca triangle styles and continuous outside momentum
  labels and wavy EW exchanges (L11-L14), without caps, circles, central guides
  or indices.
- Pages 17-18 show all eight swordfish placements (K01-K04, K11-K14), with
  plain lines, visible vertices and no decorations. Each loop meets the actual
  quartic tree vertex; it has no inner host segment.
- Page 19 shows four swordfish style samples (K21-K24): EW W loop circle,
  pink two-ended Proca Z loop with k, and pink EW Z exchange/circle without
  a central momentum guide. No caps or indices are shown.
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
- Page 16 shows the species-styling sample (J01-J04), with intentional Z/W circles.
- Page 15 demonstrates the reviewed insertion momentum defaults, without
  caps, circles or index labels.
- Pages 13-14 show all eight s/t-tree seagull placements with plain lines and
  one marked quartic insertion vertex.
- Page 12 shows the four s-tree external bubble placements with plain lines,
  visible interaction vertices and no labels/caps/circles.
- Page 11 shows continuous arrows with outward labels in all four orientations
  (T05-T08), selected globally or per annotation with `layout=side`.

Important limits:

- Bubble insertions support **s/t-tree external slots 1-4**, one at a time.
  Seagulls and swordfish also support **s/t-tree external slots 1-4**, one at a time.
  Swordfish has no post segment; post style/momentum/index controls are inactive.
  U-tree/contact hosts and internal insertions remain unsupported; accepted
  keys can still do nothing there.
- Horizontal/vertical contact pairings are disconnected pairs, not tree exchanges.
- The existing crossed box fixes its side edges and crosses its diagonals;
  internal momentum/index coverage remains incomplete.
- All four triangle-contact orientations have independent annotation controls
  for slots 1-7. Regular tree-attached triangles are also supported, through
  `insertion=triangle`, with separate per-annotation controls for slots 1-8.
  Their side key selects a vertex correction; external insertion-slot/pre/post
  controls do not describe this graph.
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
