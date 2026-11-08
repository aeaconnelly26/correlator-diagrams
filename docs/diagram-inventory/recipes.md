# Current diagram recipes

Generated from `catalog.json`. These are existing capabilities, not proposed APIs.

Baseline: `M08a local; base main 096b2b3`, audited 2026-11-08. Atlas: [PDF](inventory.pdf).

Use `\usepackage{feynman-fun}`. Paste a recipe inside `\[ ... \]`.

The main atlas hides annotations. The appendix demonstrates selected annotation and style features.

`scale=1` uses the compact coordinate baseline: 0.8 times the former size. Use `scale=1.25` to recover the former `scale=1` size. Text and markers retain the existing TikZ scale behavior.

Ordinary S-tree exchanges and their external bubble/seagull/swordfish variants now use channel-vertex-xspan=1.05 by default. Regular triangle corrections retain 0.78; the shared outer frame is unchanged.

## Two- and three-point objects

### I01 - Two-point object

Two external segments meet at one marked point.

**Limit:** A central point or optional blob, not a loop correction.

```tex
\TwoPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0
]
```

### I02 - Three-point: upper left

One trivalent vertex; logical slot 1 points upper left.

**Limit:** Four orientations retain the same three logical slots.

```tex
\ThreePointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  orientation={top,left}
]
```

### I03 - Three-point: upper right

One trivalent vertex; logical slot 1 points upper right.

**Limit:** Four orientations retain the same three logical slots.

```tex
\ThreePointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  orientation={top,right}
]
```

### I04 - Three-point: lower left

One trivalent vertex; logical slot 1 points lower left.

**Limit:** Four orientations retain the same three logical slots.

```tex
\ThreePointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  orientation={bottom,left}
]
```

### I05 - Three-point: lower right

One trivalent vertex; logical slot 1 points lower right.

**Limit:** Four orientations retain the same three logical slots.

```tex
\ThreePointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  orientation={bottom,right}
]
```

## Contact and pairing layouts

### I06 - Central contact

Four external edges meet at one quartic vertex.

**Limit:** Connected four-point contact.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  contact-pairing=central
]
```

### I07 - Horizontal pairing

Top pair and bottom pair each meet separately.

**Limit:** Disconnected pairs; there is no vertical exchange edge.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  contact-pairing=horizontal
]
```

### I08 - Vertical pairing

Left pair and right pair each meet separately.

**Limit:** Disconnected pairs; there is no horizontal exchange edge.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  contact-pairing=vertical
]
```

### I09 - Crossed contact layout

Curved and straight external edges meet at a central point.

**Limit:** The central dot is an interaction, not an over/under crossing.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  contact-pairing=crossed
]
```

### I10 - Flat contact

One quartic vertex with a flat upper pair.

**Limit:** A contact layout, not an additional loop topology.

```tex
\FlatContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  flat-contact-line=plain
]
```

## Tree exchanges and four-legged bubbles

### I11 - s-channel tree

Two trivalent vertices joined by one exchange edge.

**Limit:** External insertions support S/T trees; U/internal hosts remain unsupported.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  channel-line=plain
]
```

### I12 - t-channel tree

Two trivalent vertices joined by one exchange edge.

**Limit:** External insertions support S/T trees; U/internal hosts remain unsupported.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  channel-line=plain
]
```

### I13 - u-channel tree

Two trivalent vertices joined by one exchange edge.

**Limit:** External insertions support S/T trees; U/internal hosts remain unsupported.

```tex
\UTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  channel-line=plain
]
```

### I14 - s-channel bubble

Two quartic vertices joined by two internal edges.

**Limit:** Four-legged bubble already exists; unlike a self-energy insertion.

```tex
\SChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  loop-channel-a-line=plain,
  loop-channel-b-line=plain
]
```

### I15 - t-channel bubble

Two quartic vertices joined by two internal edges.

**Limit:** Four-legged bubble already exists; unlike a self-energy insertion.

```tex
\TChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  loop-channel-a-line=plain,
  loop-channel-b-line=plain
]
```

### I16 - u-channel bubble

Two quartic vertices joined by two internal edges.

**Limit:** Four-legged bubble already exists; unlike a self-energy insertion.

```tex
\UChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  loop-channel-a-line=plain,
  loop-channel-b-line=plain
]
```

## Boxes and half-box layouts

### I17 - Square box

Four trivalent vertices around a single loop.

**Limit:** Default inner spans are both 1.34; explicit overrides remain possible.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain
]
```

### I18 - Existing crossed box

Fixed left/right edges plus two crossing diagonals.

**Limit:** Default left/right fixed; use P02 for top/bottom fixed.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain
]
```

### I19 - Straight half-box

Two trivalent vertices with a horizontal bridge.

**Limit:** An open tree helper, despite the half-box name.

```tex
\HalfBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  half-box-line=plain,
  half-box-bridge-line=plain,
  half-box-style=straight
]
```

### I20 - Angled half-propagator

Angled upper stubs on the same two-vertex graph.

**Limit:** A layout variant of the half-box, not a new loop.

```tex
\HalfBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  half-box-style=halfpropagator,
  half-box-line=plain,
  half-box-bridge-line=plain
]
```

### I21 - Left half-propagator marker

Angled half-box with the left lower-leg circle preset.

**Limit:** Blank circle retained to show the preset; same underlying graph.

```tex
\HalfBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  half-box-style=halfpropleft,
  half-box-line=plain,
  half-box-bridge-line=plain,
  half-box-left-lower-circ={}
]
```

### I22 - Right half-propagator marker

Angled half-box with the right lower-leg circle preset.

**Limit:** Blank circle retained to show the preset; same underlying graph.

```tex
\HalfBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  half-box-style=halfpropright,
  half-box-line=plain,
  half-box-bridge-line=plain,
  half-box-right-lower-circ={}
]
```

## Four triangle-contact orientations

### I23 - Quartic contact: bottom

The quartic/contact vertex lies on the bottom side.

**Limit:** Not the regular three-trivalent-vertex triangle attached to a tree.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=bottom,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain
]
```

### I24 - Quartic contact: top

The quartic/contact vertex lies on the top side.

**Limit:** Not the regular three-trivalent-vertex triangle attached to a tree.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=top,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain
]
```

### I25 - Quartic contact: left

The quartic/contact vertex lies on the left side.

**Limit:** Not the regular three-trivalent-vertex triangle attached to a tree.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=left,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain
]
```

### I26 - Quartic contact: right

The quartic/contact vertex lies on the right side.

**Limit:** Not the regular three-trivalent-vertex triangle attached to a tree.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=right,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain
]
```

## Loops and external bubble insertions

### I27 - Self-energy bubble

Two trivalent vertices and two internal arcs; one loop.

**Limit:** Two external legs; distinct from a four-legged channel bubble.

```tex
\BubbleCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  bubble-external-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### I28 - Sunset

Two quartic vertices joined by three internal edges.

**Limit:** Two loops, not a one-loop self-energy bubble.

```tex
\SunsetDiagram[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  sunset-left-line=plain,
  sunset-right-line=plain,
  sunset-top-line=plain,
  sunset-middle-line=plain,
  sunset-bottom-line=plain,
  sunset-central-label={}
]
```

### I29 - Bubble on t-tree leg 1

A self-energy bubble splits the upper-left external leg.

**Limit:** T-tree external slots 1-4; one self-energy insertion at a time.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  scale=0.82,
  channel-line=plain,
  insertion=bubble,
  insertion-slot=1,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### B02 - Bubble on t-tree leg 2

Two trivalent vertices split the lower-left external leg.

**Limit:** The other three legs and the exchange edge keep their logical identities.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=2,
  channel-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### B03 - Bubble on t-tree leg 3

Two trivalent vertices split the upper-right external leg.

**Limit:** The other three legs and the exchange edge keep their logical identities.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=3,
  channel-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### B04 - Bubble on t-tree leg 4

Two trivalent vertices split the lower-right external leg.

**Limit:** The other three legs and the exchange edge keep their logical identities.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=4,
  channel-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

## Existing styles and annotations

### A01 - Your pink Proca t-bubble

Four double-capped EW legs and two pink Proca internals.

**Limit:** Integrated endpoint checks cover visible contact and legacy overrides.

```tex
\TChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  line={ewboson,endcapp},
  loop-channel-left-line={proca,magenta!85!red},
  loop-channel-right-line={proca,magenta!85!red}
]
```

### A02 - Polarization and mixed legs

Double cap, single cap, and a pink scalar-polarized leg.

**Limit:** Scalar polarization is a style, not another topology.

```tex
\ThreePointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  leg-styles={{ewboson,endcapp},{ewboson,endcap},{spol,magenta!85!red,endcap}}
]
```

### A03 - EW circles and single caps

Independent internal particle circles and external endcaps.

**Limit:** Species labels decorate the existing square loop.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-line={ewboson,endcap},
  box-left-line={ewboson,circ=Z},
  box-top-line={ewboson,circ=W},
  box-right-line={ewboson,circ=Z},
  box-bottom-line={ewboson,circ=W}
]
```

### A04 - Bridge momentum and indices

A pink bridge with one momentum and endpoint indices.

**Limit:** Omit global line=plain: it overrides the bridge-specific style.

```tex
\HalfBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=1.0,
  half-box-line=ewboson,
  half-box-bridge-line={proca,magenta!85!red},
  show-momenta=true,
  momentum-labels={,,,},
  half-box-momentum-slots={},
  half-box-bridge-momentum=p,
  half-box-propagator-left-indices={,,,,a},
  half-box-propagator-right-indices={,,,,b},
  half-box-xspan=1.0
]
```

### A05 - Curved momentum and indices

External flow, curved loop momenta, and four endpoint indices.

**Limit:** Representative annotation layout; crowded cases need dedicated checks.

```tex
\BubbleCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  bubble-external-line={ewboson,endcap},
  bubble-top-line={ewboson,circ=Z},
  bubble-bottom-line={proca,magenta!85!red},
  show-momenta=true,
  bubble-momenta={k,p-k},
  bubble-momentum-rotation=clockwise,
  bubble-endpoint-indices={a,b,c,d},
  bubble-momentum-label-distance=5pt,
  momentum-labels={p,p},
  bubble-external-length=1.35
]
```

### A06 - Crossing and Proca circles

A blank circle on one pink diagonal and a Z on the other.

**Limit:** Circles shown deliberately; internal annotations are available separately.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=ewboson,
  box-external-line={ewboson,endcapp},
  cross-box-up-line={proca,magenta!85!red,circ={}},
  cross-box-down-line={ewboson,circ=Z}
]
```

## Seagull insertion examples

### U01 - Seagull: bare structure

One quartic point on an external leg carries a self-loop.

**Limit:** Original t-slot-1 example; all s/t external slots 1-4 now supported.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=1.0,
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=0.85,
  insertion=seagull,
  insertion-slot=1,
  line=plain,
  channel-line=plain,
  seagull-loop-line=plain,
  insertion-pre-line=plain,
  insertion-post-line=plain
]
```

### U02 - Seagull: EW line style

The same supported graph with wavy EW propagators.

**Limit:** Original t-slot-1 example; all s/t external slots 1-4 now supported.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=1.0,
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=0.85,
  insertion=seagull,
  insertion-slot=1,
  line=ewboson,
  channel-line=ewboson,
  seagull-loop-line=ewboson,
  insertion-pre-line=ewboson,
  insertion-post-line=ewboson
]
```

### S01 - One endpoint marker

Select proca start on the pink seagull loop.

**Limit:** Loop endpoint selection follows the directed loop path; no caps or circles.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=1.0,
  line=ewboson,
  insertion=seagull,
  insertion-slot=1,
  seagull-loop-line={proca start,magenta!85!red}
]
```

### S02 - Opposite endpoint marker

Select proca end on the pink seagull loop.

**Limit:** Loop endpoint selection follows the directed loop path; no caps or circles.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=1.0,
  line=ewboson,
  insertion=seagull,
  insertion-slot=1,
  seagull-loop-line={proca end,magenta!85!red}
]
```

### S03 - Both endpoint markers

Select proca on the pink seagull loop.

**Limit:** Loop endpoint selection follows the directed loop path; no caps or circles.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  scale=1.0,
  line=ewboson,
  insertion=seagull,
  insertion-slot=1,
  seagull-loop-line={proca,magenta!85!red}
]
```

## Integrated annotation controls

### F01 - Compact external indices

Compact indices on an empty field base.

**Limit:** Explicit leg labels take precedence over field/index formatting.

```tex
\FourPointCorr[
  field={},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  indices={\alpha,\beta,\gamma,\delta},
  index-placement=mini
]
```

### F02 - Hide external momenta

Only the exchange momentum remains; its side label leaves a continuous arrow.

**Limit:** Visibility acts on logical external slots and preserves internal flow.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  channel-line=plain,
  show-momenta=true,
  momentum-labels={q_1,q_2,q_3,q_4,p},
  external-momentum-hide={1,2,3,4},
  channel-momentum-label-position=right
]
```

### F03 - Blank label versus hidden arrow

Slot 1 has an unlabeled arrow, slot 2 has q, and slot 3 has no arrow.

**Limit:** An empty entry hides text; external-momentum-hide hides the whole arrow.

```tex
\ThreePointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={,q,r},
  external-momentum-hide={3}
]
```

## Independent momentum placement

### T01 - Annotations: contact bottom

Slot 2 arrow clearance and slot 6 side label are independent.

**Limit:** Compact quartic-side defaults sit nearer the outer endpoints.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=bottom,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-momentum-2={offset=16pt},
  triangle-contact-momentum-6={layout=side,label-offset=3pt}
]
```

### T02 - Annotations: contact top

Slot 5 has its own range; middle arrows face trivalent vertices.

**Limit:** Compact quartic-side defaults sit nearer the outer endpoints.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=top,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-momentum-5={start=0.28,end=0.72,label-fraction=0.50}
]
```

### T03 - Annotations: contact left

Slot 3 uses a continuous arrow with its own side label.

**Limit:** Compact quartic-side defaults sit nearer the outer endpoints.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=left,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-momentum-3={layout=side,label-xshift=2pt},
  triangle-contact-yspan=1.15
]
```

### T04 - Annotations: contact right

Unequal edges retain mixed styles and logical slots.

**Limit:** Compact quartic-side defaults sit nearer the outer endpoints.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=right,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-internal-lines={proca,ewboson,proca},
  triangle-contact-xspan=1.20,
  triangle-contact-yspan=0.80
]
```

## Continuous arrows with outside labels

### T05 - Side labels: contact bottom

Continuous arrows; labels sit outward from each edge.

**Limit:** Use layout=gap in an individual slot to mix both modes.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=bottom,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-momentum-layout=side
]
```

### T06 - Side labels: contact top

Continuous arrows; labels sit outward from each edge.

**Limit:** Use layout=gap in an individual slot to mix both modes.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=top,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-momentum-layout=side
]
```

### T07 - Side labels: contact left

Continuous arrows; labels sit outward from each edge.

**Limit:** Use layout=gap in an individual slot to mix both modes.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=left,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-momentum-layout=side
]
```

### T08 - Side labels: contact right

Continuous arrows; labels sit outward from each edge.

**Limit:** Use layout=gap in an individual slot to mix both modes.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-orientation=right,
  triangle-contact-external-line=plain,
  triangle-contact-internal-line=plain,
  triangle-contact-momentum-layout=side
]
```

## External s-tree self-energy bubbles

### C01 - Bubble on s-tree leg 1

Self-energy correction on the upper-left external leg.

**Limit:** One insertion; internal-slot and u-tree support remain missing.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=1,
  channel-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### C02 - Bubble on s-tree leg 2

Self-energy correction on the lower-left external leg.

**Limit:** One insertion; internal-slot and u-tree support remain missing.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=2,
  channel-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### C03 - Bubble on s-tree leg 3

Self-energy correction on the upper-right external leg.

**Limit:** One insertion; internal-slot and u-tree support remain missing.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=3,
  channel-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### C04 - Bubble on s-tree leg 4

Self-energy correction on the lower-right external leg.

**Limit:** One insertion; internal-slot and u-tree support remain missing.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=4,
  channel-line=plain,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

## External t-tree seagulls

### G01 - Seagull on t-tree leg 1

One quartic self-loop insertion on the upper-left leg.

**Limit:** Same graph as U01; repeated here to show the full four-leg matrix.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=1,
  channel-line=plain,
  seagull-loop-line=plain
]
```

### G02 - Seagull on t-tree leg 2

One quartic self-loop insertion on the lower-left leg.

**Limit:** External slots 1-4 only; one insertion.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=2,
  channel-line=plain,
  seagull-loop-line=plain
]
```

### G03 - Seagull on t-tree leg 3

One quartic self-loop insertion on the upper-right leg.

**Limit:** External slots 1-4 only; one insertion.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=3,
  channel-line=plain,
  seagull-loop-line=plain
]
```

### G04 - Seagull on t-tree leg 4

One quartic self-loop insertion on the lower-right leg.

**Limit:** External slots 1-4 only; one insertion.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=4,
  channel-line=plain,
  seagull-loop-line=plain
]
```

## External s-tree seagulls

### G11 - Seagull on s-tree leg 1

One quartic self-loop insertion on the upper-left leg.

**Limit:** External slots 1-4 only; one insertion.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=1,
  channel-line=plain,
  seagull-loop-line=plain
]
```

### G12 - Seagull on s-tree leg 2

One quartic self-loop insertion on the lower-left leg.

**Limit:** External slots 1-4 only; one insertion.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=2,
  channel-line=plain,
  seagull-loop-line=plain
]
```

### G13 - Seagull on s-tree leg 3

One quartic self-loop insertion on the upper-right leg.

**Limit:** External slots 1-4 only; one insertion.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=3,
  channel-line=plain,
  seagull-loop-line=plain
]
```

### G14 - Seagull on s-tree leg 4

One quartic self-loop insertion on the lower-right leg.

**Limit:** External slots 1-4 only; one insertion.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=seagull,
  insertion-slot=4,
  channel-line=plain,
  seagull-loop-line=plain
]
```

## Compact arrows and clear external labels

### H01 - T-tree seagull on leg 1

Inward T loop; compact host arrows.

**Limit:** Default outside labels; explicit placement keys still override.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  insertion=seagull,
  insertion-slot=1,
  channel-line=plain,
  seagull-loop-line=plain,
  seagull-loop-momentum=k
]
```

### H02 - T-tree seagull on leg 4

Inward T loop; compact host arrows.

**Limit:** Default outside labels; explicit placement keys still override.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  insertion=seagull,
  insertion-slot=4,
  channel-line=plain,
  seagull-loop-line=plain,
  seagull-loop-momentum=k
]
```

### H03 - S-tree seagull on leg 2

Outward S loop; compact host arrows.

**Limit:** Default outside labels; explicit placement keys still override.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  insertion=seagull,
  insertion-slot=2,
  channel-line=plain,
  seagull-loop-line=plain,
  seagull-loop-momentum=k
]
```

### H04 - S-tree seagull on leg 3

Outward S loop; compact host arrows.

**Limit:** Default outside labels; explicit placement keys still override.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  insertion=seagull,
  insertion-slot=3,
  channel-line=plain,
  seagull-loop-line=plain,
  seagull-loop-momentum=k
]
```

## Pink Z stems, scalar-polarized loops and W host segments

### J01 - T-tree seagull: pink Z stem

Pink Z stem; inner W; two-ended pink loop with k.

**Limit:** W centered in the visible arrow-to-vertex gap; central momentum hidden.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=0.7},
  insertion=seagull,
  insertion-slot=1,
  insertion-pre-line=ewboson,
  insertion-post-line={ewboson,circ=W,circ position=0.57332,circ scale=0.65},
  seagull-loop-line={proca,magenta!85!red},
  seagull-loop-momentum=k,
  show-channel-momentum=false
]
```

### J02 - T-tree bubble: pink Z stem

Pink Z stem; inner W; EW W arc and two-ended pink arc (k).

**Limit:** Central/W-loop guides hidden; no loop circles. Shorter W-loop wavelength.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=0.7},
  insertion=bubble,
  insertion-slot=3,
  insertion-pre-line=ewboson,
  insertion-post-line={ewboson,circ=W,circ position=0.5,circ scale=0.65},
  bubble-top-line={ewboson,ewboson wavelength=10\feynhandlinesize,circ=W,circ scale=0.65},
  bubble-bottom-line={proca,magenta!85!red},
  bubble-momenta={,k},
  show-channel-momentum=false
]
```

### J03 - S-tree seagull: pink Z stem

Pink Z stem; inner W; two-ended pink loop with k.

**Limit:** W centered in the visible arrow-to-vertex gap; central momentum hidden.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=0.7},
  insertion=seagull,
  insertion-slot=2,
  insertion-pre-line=ewboson,
  insertion-post-line={ewboson,circ=W,circ position=0.57513,circ scale=0.65},
  seagull-loop-line={proca,magenta!85!red},
  seagull-loop-momentum=k,
  show-channel-momentum=false,
  insertion-post-momentum-label-distance=4pt
]
```

### J04 - S-tree bubble: pink Z stem

Pink Z stem; inner W; EW W arc and two-ended pink arc (k).

**Limit:** Central/W-loop guides hidden; inner-label gap 4pt. Shorter W-loop wavelength.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  show-momenta=true,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=0.7},
  insertion=bubble,
  insertion-slot=4,
  insertion-pre-line=ewboson,
  insertion-post-line={ewboson,circ=W,circ position=0.5,circ scale=0.65},
  bubble-top-line={ewboson,ewboson wavelength=10\feynhandlinesize,circ=W,circ scale=0.65},
  bubble-bottom-line={proca,magenta!85!red},
  bubble-momenta={,k},
  show-channel-momentum=false,
  insertion-post-momentum-label-distance=4pt
]
```

## External t-tree swordfish diagrams

### K01 - Swordfish on t-tree leg 1

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=1,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### K02 - Swordfish on t-tree leg 2

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=2,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### K03 - Swordfish on t-tree leg 3

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=3,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### K04 - Swordfish on t-tree leg 4

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=4,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

## External s-tree swordfish diagrams

### K11 - Swordfish on s-tree leg 1

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=1,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### K12 - Swordfish on s-tree leg 2

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=2,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### K13 - Swordfish on s-tree leg 3

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=3,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

### K14 - Swordfish on s-tree leg 4

One trivalent loop vertex; two curves meet the actual quartic tree vertex.

**Limit:** One external insertion. No bridge or duplicate shared vertex.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=4,
  bubble-top-line=plain,
  bubble-bottom-line=plain
]
```

## Independent loop styles at a shared interaction

### K21 - T-tree slot 1: mixed loop

W loop, pink two-ended Z loop (k), pink Z exchange.

**Limit:** Species circles intentional; no central/W guide, caps or indices.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=1,
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=.7},
  bubble-top-line={ewboson,ewboson wavelength=14\feynhandlinesize,circ=W,circ scale=.65},
  bubble-bottom-line={proca,magenta!85!red},
  bubble-momenta={,k}
]
```

### K22 - T-tree slot 3: mixed loop

W loop, pink two-ended Z loop (k), pink Z exchange.

**Limit:** Species circles intentional; no central/W guide, caps or indices.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=3,
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=.7},
  bubble-top-line={ewboson,ewboson wavelength=14\feynhandlinesize,circ=W,circ scale=.65},
  bubble-bottom-line={proca,magenta!85!red},
  bubble-momenta={,k}
]
```

### K23 - S-tree slot 2: mixed loop

W loop, pink two-ended Z loop (k), pink Z exchange.

**Limit:** Species circles intentional; no central/W guide, caps or indices.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=2,
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=.7},
  bubble-top-line={ewboson,ewboson wavelength=14\feynhandlinesize,circ=W,circ scale=.65},
  bubble-bottom-line={proca,magenta!85!red},
  bubble-momenta={,k}
]
```

### K24 - S-tree slot 4: mixed loop

W loop, pink two-ended Z loop (k), pink Z exchange.

**Limit:** Species circles intentional; no central/W guide, caps or indices.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=swordfish,
  insertion-slot=4,
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  line=ewboson,
  channel-line={ewboson,magenta!85!red,circ=Z,circ scale=.7},
  bubble-top-line={ewboson,ewboson wavelength=14\feynhandlinesize,circ=W,circ scale=.65},
  bubble-bottom-line={proca,magenta!85!red},
  bubble-momenta={,k}
]
```

## Regular tree-attached triangle corrections

### L01 - T-tree triangle: bottom

Three trivalent loop vertices; bridge to the other tree vertex.

**Limit:** One vertex correction. Equilateral defaults; explicit width allows other shapes.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=bottom
]
```

### L02 - T-tree triangle: top

Three trivalent loop vertices; bridge to the other tree vertex.

**Limit:** One vertex correction. Equilateral defaults; explicit width allows other shapes.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=top
]
```

### L03 - S-tree triangle: left

Three trivalent loop vertices; bridge to the other tree vertex.

**Limit:** One vertex correction. Equilateral defaults; explicit width allows other shapes.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=left
]
```

### L04 - S-tree triangle: right

Three trivalent loop vertices; bridge to the other tree vertex.

**Limit:** One vertex correction. Equilateral defaults; explicit width allows other shapes.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=right
]
```

## Independent lines and continuous momentum arrows

### L11 - T bottom: momentum and mixed lines

EW base and wavy exchange; pink two-ended loop edges.

**Limit:** No caps, circles, central guide or indices. Index polish remains D01.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=bottom,
  line=ewboson,
  channel-line={ewboson,magenta!85!red},
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  tree-triangle-loop-line={proca,magenta!85!red},
  tree-triangle-line-6=ewboson,
  tree-triangle-momenta={k,\ell,q},
  tree-triangle-momentum-1={layout=side},
  tree-triangle-momentum-2={layout=side},
  tree-triangle-momentum-3={layout=side},
  tree-triangle-momentum-4={layout=side},
  tree-triangle-momentum-5={layout=side},
  tree-triangle-momentum-6={layout=side},
  tree-triangle-momentum-7={layout=side},
  tree-triangle-momentum-8={layout=side}
]
```

### L12 - T top: momentum and mixed lines

EW base and wavy exchange; pink two-ended loop edges.

**Limit:** No caps, circles, central guide or indices. Index polish remains D01.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=top,
  line=ewboson,
  channel-line={ewboson,magenta!85!red},
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  tree-triangle-loop-line={proca,magenta!85!red},
  tree-triangle-line-6=ewboson,
  tree-triangle-momenta={k,\ell,q},
  tree-triangle-momentum-1={layout=side},
  tree-triangle-momentum-2={layout=side},
  tree-triangle-momentum-3={layout=side},
  tree-triangle-momentum-4={layout=side},
  tree-triangle-momentum-5={layout=side},
  tree-triangle-momentum-6={layout=side},
  tree-triangle-momentum-7={layout=side},
  tree-triangle-momentum-8={layout=side}
]
```

### L13 - S left: momentum and mixed lines

EW base and wavy exchange; pink two-ended loop edges.

**Limit:** No caps, circles, central guide or indices. Index polish remains D01.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=left,
  line=ewboson,
  channel-line={ewboson,magenta!85!red},
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  tree-triangle-loop-line={proca,magenta!85!red},
  tree-triangle-line-6=ewboson,
  tree-triangle-momenta={k,\ell,q},
  tree-triangle-momentum-1={layout=side},
  tree-triangle-momentum-2={layout=side},
  tree-triangle-momentum-3={layout=side},
  tree-triangle-momentum-4={layout=side},
  tree-triangle-momentum-5={layout=side},
  tree-triangle-momentum-6={layout=side},
  tree-triangle-momentum-7={layout=side},
  tree-triangle-momentum-8={layout=side}
]
```

### L14 - S right: momentum and mixed lines

EW base and wavy exchange; pink two-ended loop edges.

**Limit:** No caps, circles, central guide or indices. Index polish remains D01.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=right,
  line=ewboson,
  channel-line={ewboson,magenta!85!red},
  show-momenta=true,
  show-channel-momentum=false,
  momentum-labels={p_1,p_2,p_3,p_4,P},
  tree-triangle-loop-line={proca,magenta!85!red},
  tree-triangle-line-6=ewboson,
  tree-triangle-momenta={k,\ell,q},
  tree-triangle-momentum-1={layout=side},
  tree-triangle-momentum-2={layout=side},
  tree-triangle-momentum-3={layout=side},
  tree-triangle-momentum-4={layout=side},
  tree-triangle-momentum-5={layout=side},
  tree-triangle-momentum-6={layout=side},
  tree-triangle-momentum-7={layout=side},
  tree-triangle-momentum-8={layout=side}
]
```

## Consistent endpoints across trees and boxes

### L21 - Ordinary T tree

Common outer corners: x and y are both +/-2.10.

**Limit:** Comparison repeat; connectivity and inner geometry remain topology-specific.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0
]
```

### L22 - T triangle, same endpoints

Common outer corners: x and y are both +/-2.10.

**Limit:** Comparison repeat; connectivity and inner geometry remain topology-specific.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=triangle,
  tree-triangle-side=top
]
```

### L23 - Box, same endpoints

Common outer corners: x and y are both +/-2.10.

**Limit:** Comparison repeat; connectivity and inner geometry remain topology-specific.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain
]
```

### L24 - Crossed box, same endpoints

Common outer corners: x and y are both +/-2.10.

**Limit:** Comparison repeat; connectivity and inner geometry remain topology-specific.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain
]
```

## The same endpoints in all triangle-contact orientations

### L31 - Triangle-contact: bottom

Same +/-2.10 outer corners as trees, box and crossed box.

**Limit:** Comparison repeat; the quartic vertex and internal spans are unchanged.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=bottom
]
```

### L32 - Triangle-contact: top

Same +/-2.10 outer corners as trees, box and crossed box.

**Limit:** Comparison repeat; the quartic vertex and internal spans are unchanged.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=top
]
```

### L33 - Triangle-contact: left

Same +/-2.10 outer corners as trees, box and crossed box.

**Limit:** Comparison repeat; the quartic vertex and internal spans are unchanged.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=left
]
```

### L34 - Triangle-contact: right

Same +/-2.10 outer corners as trees, box and crossed box.

**Limit:** Comparison repeat; the quartic vertex and internal spans are unchanged.

```tex
\TriangleContactCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  triangle-contact-orientation=right
]
```

## External caps survive segment styling

### N01 - T bubble: double caps

Four outer double caps retained.

**Limit:** Explicit segment caps override logical leg caps.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  line={ewboson,endcapp},
  channel-line=plain,
  insertion=bubble,
  insertion-slot=3,
  insertion-pre-line=ewboson,
  insertion-post-line=ewboson,
  bubble-top-line=plain,
  bubble-bottom-line=plain,
  seagull-loop-line=plain
]
```

### N02 - T seagull: double caps

Four outer double caps retained.

**Limit:** Explicit segment caps override logical leg caps.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  line={ewboson,endcapp},
  channel-line=plain,
  insertion=seagull,
  insertion-slot=3,
  insertion-pre-line=ewboson,
  insertion-post-line=ewboson,
  bubble-top-line=plain,
  bubble-bottom-line=plain,
  seagull-loop-line=plain
]
```

### N03 - T swordfish: double caps

Four outer double caps retained.

**Limit:** Explicit segment caps override logical leg caps.

```tex
\TTreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  line={ewboson,endcapp},
  channel-line=plain,
  insertion=swordfish,
  insertion-slot=2,
  insertion-pre-line=ewboson,
  insertion-post-line=ewboson,
  bubble-top-line=plain,
  bubble-bottom-line=plain,
  seagull-loop-line=plain
]
```

### N04 - S bubble: double caps

Four outer double caps retained.

**Limit:** Explicit segment caps override logical leg caps.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  line={ewboson,endcapp},
  channel-line=plain,
  insertion=bubble,
  insertion-slot=3,
  insertion-pre-line=ewboson,
  insertion-post-line=ewboson,
  bubble-top-line=plain,
  bubble-bottom-line=plain,
  seagull-loop-line=plain
]
```

## Complementary internal crossings

### P01 - Crossed box: left/right fixed

Four trivalent vertices; the diagonal crossing is unconnected.

**Limit:** One split diagonal; no interaction at the crossing.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain,
  cross-box-layout=left-right
]
```

### P02 - Crossed box: top/bottom fixed

Four trivalent vertices; the diagonal crossing is unconnected.

**Limit:** One split diagonal; no interaction at the crossing.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain,
  cross-box-layout=top-bottom
]
```

### P03 - Left/right: wider crossing gap

Four trivalent vertices; the diagonal crossing is unconnected.

**Limit:** Same outer frame; the wider gap is a layout variant.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain,
  cross-box-layout=left-right,
  cross-box-crossing-gap=.08
]
```

### P04 - Top/bottom: wider crossing gap

Four trivalent vertices; the diagonal crossing is unconnected.

**Limit:** Same outer frame; the wider gap is a layout variant.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain,
  cross-box-layout=top-bottom,
  cross-box-crossing-gap=.08
]
```

## Independent edges and annotations

### P11 - Left/right: mixed EW and Proca

Wavy EW fixed edges; pink Proca diagonals meet the real vertices.

**Limit:** No caps, circles, indices or momentum guides.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  cross-box-layout=left-right,
  box-external-line=ewboson,
  box-line=ewboson,
  cross-box-line-7={proca,magenta!85!red},
  cross-box-line-8={proca,magenta!85!red},
  cross-box-circs=false
]
```

### P12 - Top/bottom: mixed EW and Proca

Wavy EW fixed edges; pink Proca diagonals meet the real vertices.

**Limit:** No caps, circles, indices or momentum guides.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  cross-box-layout=top-bottom,
  box-external-line=ewboson,
  box-line=ewboson,
  cross-box-line-7={proca,magenta!85!red},
  cross-box-line-8={proca,magenta!85!red},
  cross-box-circs=false
]
```

### P13 - Left/right: internal momentum gaps

Independent internal annotations; labels sit in measured arrow gaps.

**Limit:** Indices remain a separate D01 appearance review.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain,
  cross-box-momenta={k_5,k_6,k_7,k_8},
  show-momenta=true
]
```

### P14 - Top/bottom: continuous momentum arrows

Continuous arrows with labels beside their logical edges.

**Limit:** Per-edge directions and positions remain independently adjustable.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line=plain,
  box-external-line=plain,
  cross-box-layout=top-bottom,
  cross-box-momenta={k_5,k_6,k_7,k_8},
  show-momenta=true,
  cross-box-momentum-5={layout=side},
  cross-box-momentum-6={layout=side},
  cross-box-momentum-7={layout=side},
  cross-box-momentum-8={layout=side}
]
```

## Square box with crossed upper legs

### P21 - Box: upper external crossing

UL connects to TR; UR connects to TL. The square loop stays intact.

**Limit:** One split external leg; no interaction at the upper crossing.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-crossing=top,
  box-line=plain,
  box-external-line=plain
]
```

### P22 - Upper crossing: EW external legs

Same routed graph, with wavy external lines.

**Limit:** No extra caps, circles or annotations.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-crossing=top,
  box-line=plain,
  box-external-line=plain,
  box-external-line=ewboson
]
```

### P23 - Upper crossing: pink Proca legs

Endpoint tips belong to full legs, never to the gap.

**Limit:** Two tips per Proca leg; external endpoints stay in the shared frame.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-crossing=top,
  box-line=plain,
  box-external-line=plain,
  box-external-line={proca,magenta!85!red}
]
```

### P24 - Upper crossing: external momenta

p1/p2 enter; p3/p4 leave. Measured upper gaps; lower continuous arrows.

**Limit:** Independent box-external-momentum-1..4 controls; right crossing is still missing.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-crossing=top,
  box-line=plain,
  box-external-line=plain,
  show-momenta=true,
  box-left-momentum={},
  box-top-momentum={},
  box-right-momentum={},
  box-bottom-momentum={},
  box-loop-momentum={},
  box-edge-momentum-directions={none,none,none,none},
  box-external-momentum-2={layout=side},
  box-external-momentum-4={layout=side}
]
```

## Circle scales and bare Proca lines

### P31 - User example: circle scale 0.6

Two W circles; both rings and their labels use scale 0.6.

**Limit:** Caps are retained here to reproduce the exact user example.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  scale=.8,
  box-line={ewboson,circ=W,circ scale=.6},
  box-external-line={ewboson,endcapp},
  cross-box-up-line={proca,magenta!85!red},
  cross-box-down-line={magenta!85!red,ewboson}
]
```

### P32 - Same diagram: circle scale 1.0

Only the requested circle scale changes; endpoints remain fixed.

**Limit:** No automatic empty circle on the pink Proca diagonal.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  scale=.8,
  box-line={ewboson,circ=W,circ scale=1},
  box-external-line={ewboson,endcapp},
  cross-box-up-line={proca,magenta!85!red},
  cross-box-down-line={magenta!85!red,ewboson}
]
```

### P33 - Bare Proca: left/right layout

Both endpoint tips are present, without circles.

**Limit:** Explicit circ or cross-box circle keys still request circles.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-line=plain,
  box-line={proca,magenta!85!red}
]
```

### P34 - Bare Proca: top/bottom layout

The complementary layout follows the same circle rule.

**Limit:** Cross-box-circs=false remains an explicit hide-all option.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  cross-box-layout=top-bottom,
  box-external-line=plain,
  box-line={proca,magenta!85!red}
]
```

## Smaller circles and labels by default

### P41 - Upper crossing: new default circle

Default ring diameter 9.6pt; label scale 0.8.

**Limit:** Same shared frame; no caps or momenta. D03 geometry review remains open.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-crossing=top,
  box-line=plain,
  box-external-line=plain,
  leg-styles={ewboson,plain,ewboson,plain},
  box-top-line={ewboson,circ=W}
]
```

### P42 - Upper crossing: explicit former size

Explicit scale 1 retains the original 12pt diameter.

**Limit:** Larger ring still crowds the upper crossing in this geometry.

```tex
\BoxLoopCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-external-crossing=top,
  box-line=plain,
  box-external-line=plain,
  leg-styles={ewboson,plain,ewboson,plain},
  box-top-line={ewboson,circ=W,circ scale=1}
]
```

### P43 - S-tree: default Z stem circle

The same smaller default applies to exchange-line circles.

**Limit:** Explicit circ scales and circle sizes still override defaults.

```tex
\STreeChannelCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  line=plain,
  channel-line={ewboson,circ=Z,magenta!85!red}
]
```

### P44 - Crossed box: default W circles

Manual crossed-box circles share the new default.

**Limit:** Circles remain explicit; Proca alone never requests one.

```tex
\CrossBoxCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  box-line={plain,circ=W},
  box-external-line=plain
]
```

## Self-energy bubble on a quartic contact leg

### CT01 - Upper left: slot 1

Seven edges; interaction valences 4/3/3; one loop.

**Limit:** Central/crossed quartic host only. One insertion; no contact seagull yet.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=1
]
```

### CT02 - Lower left: slot 2

Seven edges; interaction valences 4/3/3; one loop.

**Limit:** Central/crossed quartic host only. One insertion; no contact seagull yet.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=2
]
```

### CT03 - Upper right: slot 3

Seven edges; interaction valences 4/3/3; one loop.

**Limit:** Central/crossed quartic host only. One insertion; no contact seagull yet.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=3
]
```

### CT04 - Lower right: slot 4

Seven edges; interaction valences 4/3/3; one loop.

**Limit:** Central/crossed quartic host only. One insertion; no contact seagull yet.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=4
]
```

## Contact bubbles: EW W and pink scalar polarization

### CT11 - Upper left: mixed bubble

Inner W; two-ended pink arc without a circle; k only on pink arc.

**Limit:** No momentum guide on the W arc; no circle on the pink arc.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=1,
  line=ewboson,
  insertion-post-line={ewboson,circ=W},
  bubble-top-line={proca,magenta},
  bubble-bottom-line={ewboson,ewboson wavelength=10\feynhandlinesize,circ=W},
  show-momenta=true,
  external-momentum-hide={1,2,3,4},
  bubble-momenta={k,}
]
```

### CT12 - Lower left: mixed bubble

Inner W; two-ended pink arc without a circle; k only on pink arc.

**Limit:** No momentum guide on the W arc; no circle on the pink arc.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=2,
  line=ewboson,
  insertion-post-line={ewboson,circ=W},
  bubble-top-line={proca,magenta},
  bubble-bottom-line={ewboson,ewboson wavelength=10\feynhandlinesize,circ=W},
  show-momenta=true,
  external-momentum-hide={1,2,3,4},
  bubble-momenta={k,}
]
```

### CT13 - Upper right: mixed bubble

Inner W; two-ended pink arc without a circle; k only on pink arc.

**Limit:** No momentum guide on the W arc; no circle on the pink arc.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=3,
  line=ewboson,
  insertion-post-line={ewboson,circ=W},
  bubble-top-line={proca,magenta},
  bubble-bottom-line={ewboson,ewboson wavelength=10\feynhandlinesize,circ=W},
  show-momenta=true,
  external-momentum-hide={1,2,3,4},
  bubble-momenta={k,}
]
```

### CT14 - Lower right: mixed bubble

Inner W; two-ended pink arc without a circle; k only on pink arc.

**Limit:** Circle default .8. Slot 4 uses the equivalent crossed contact view.

```tex
\FourPointCorr[
  field={},
  leg-labels={,,,},
  central={},
  show-momenta=false,
  blob=false,
  center-vertex=true,
  external-vertices=false,
  line=plain,
  scale=1.0,
  insertion=bubble,
  insertion-slot=4,
  line=ewboson,
  insertion-post-line={ewboson,circ=W},
  bubble-top-line={proca,magenta},
  bubble-bottom-line={ewboson,ewboson wavelength=10\feynhandlinesize,circ=W},
  show-momenta=true,
  external-momentum-hide={1,2,3,4},
  bubble-momenta={k,},
  contact-pairing=crossed
]
```
