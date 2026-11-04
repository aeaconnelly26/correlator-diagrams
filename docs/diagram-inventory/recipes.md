# Current diagram recipes

Generated from `catalog.json`. These are existing capabilities, not proposed APIs.

Baseline: `M04 on published main b4a6ad8`, audited 2026-11-03. Atlas: [PDF](inventory.pdf).

Use `\usepackage{feynman-fun}`. Paste a recipe inside `\[ ... \]`.

The main atlas hides annotations. The appendix demonstrates selected annotation and style features.

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

**Limit:** External insertions are implemented on t trees; s/u hosts are unsupported.

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

**Limit:** Bubbles: any one external leg. Seagull: external leg 1 only.

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

**Limit:** External insertions are implemented on t trees; s/u hosts are unsupported.

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

**Limit:** No interaction at crossing; internal momentum/index pass is incomplete.

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

**Limit:** Crossing stays unconnected; no internal momenta or indices claimed.

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
