# Reference

Full package reference for `feynman-fun.sty`.

For the short overview, visuals, and starter examples, see [README](../README.md).

## Sections

- [Quick Start](#quick-start)
- [The Basic Workflow](#the-basic-workflow)
- [What Each Macro Draws](#what-each-macro-draws)
- [Leg Order And Slot Order](#leg-order-and-slot-order)
- [Quick Start Examples](#quick-start-examples)
- [External Field Labels](#external-field-labels)
- [Momentum Labels And Arrows](#momentum-labels-and-arrows)
- [Line Styles, Arrows, And Vertices](#line-styles-arrows-and-vertices)
- [Scalar-Polarized Legs](#scalar-polarized-legs)
- [One-Loop Box Topology](#one-loop-box-topology)
- [Cross-Box Topology](#cross-box-topology)
- [Triangle-Contact Topology](#triangle-contact-topology)
- [Self-Energy Bubble](#self-energy-bubble)
- [Semantic Insertions](#semantic-insertions)
- [One-Loop `s/t/u` Channel Bubbles For `\phi^4`](#one-loop-stu-channel-bubbles-for-phi4)
- [Sunset Diagrams](#sunset-diagrams)
- [Explicit Tree-Level Channel Topologies](#explicit-tree-level-channel-topologies)
- [Which Example File To Open](#which-example-file-to-open)
- [Overleaf And Local Use](#overleaf-and-local-use)

## Quick Start

Main package:

- `feynman-fun.sty`

Compatibility package:

- `correlator-diagrams.sty` loads `feynman-fun` for older documents.

New documents should use `feynman-fun`; keep `correlator-diagrams` only for older documents that have not been renamed yet.

Main demos:

- `example.tex`
- `regressions/topologies/box/box-topology-regression.tex`
- `regressions/topologies/channel/channel-topology-regression.tex`
- `regressions/topologies/cross-box/cross-box-regression.tex`
- `regressions/topologies/triangle-contact/triangle-contact-regression.tex`
- `regressions/topologies/bubble/bubble-regression.tex`
- `regressions/topologies/insertion/insertion-regression.tex`
- `regressions/topologies/vertex-identity/vertex-identity-check.tex`
- `regressions/topologies/three-point/three-point-check.tex`
- `regressions/topologies/sunset/sunset-example.tex`
- `regressions/topologies/sunset/sunset-index-regression.tex`
- `regressions/propagators/circ/propagator-circ-check.tex`
- `regressions/propagators/endpoint-markers/endpoint-marker-regression.tex`
- `regressions/propagators/proca/proca-regression.tex`
- `regressions/propagators/scalar-polarization/scalar-polarization-check.tex`

Add the package to your document:

```tex
\usepackage{amsmath}
\usepackage{feynman-fun}
```

The main entry points are:

```tex
\TwoPointCorr[...]
\BubbleCorr[...]
\ThreePointCorr[...]
\FourPointCorr[...]
\BoxLoopCorr[...]
\CrossBoxCorr[...]
\TriangleContactCorr[...]
\SunsetDiagram[...]
```

Common aliases:

```tex
\TwoPtCorr[...]
\SelfEnergyCorr[...]
\SelfEnergyBubbleCorr[...]
\ThreePtCorr[...]
\FourPtCorr[...]
\SChannelCorr[...]
\TChannelCorr[...]
\UChannelCorr[...]
\SLoopChannelCorr[...]
\TLoopChannelCorr[...]
\ULoopChannelCorr[...]
\BoxLoopCorr[...]
\CrossBoxCorr[...]
\TriangleContactCorr[...]
\STreeChannelCorr[...]
\TTreeChannelCorr[...]
\UTreeChannelCorr[...]
\SunsetDiag[...]
```

Compile locally with:

```sh
pdflatex -interaction=nonstopmode -halt-on-error example.tex
```

Run the maintained regression smoke checks with:

```sh
scripts/check-regressions.sh
```

If you want the fastest first pass, start with `example.tex`, then copy one of the channel or contact examples and adjust the topology, labels, and line styles.

## The Basic Workflow

Most diagrams are easiest if you think in this order:

1. Pick the topology.
2. Label the external fields.
3. Label the momenta.
4. Adjust line styles, arrows, and vertices.
5. Add internal indices if the topology has internal propagators.

That is the logic used by this package.

## What Each Macro Draws

| Macro | Purpose | Default shape |
| --- | --- | --- |
| `\TwoPointCorr` | 2-point function | left leg, right leg, central blob/vertex |
| `\BubbleCorr` | self-energy bubble | two horizontal vertices, two internal arcs, two amputated external legs |
| `\ThreePointCorr` | 3-point vertex | upper-left, right, and bottom legs meeting at one vertex |
| `\FourPointCorr` | 4-point object | contact topology by default |
| `\BoxLoopCorr` | one-loop box | four corner vertices, square internal loop, four diagonal external legs |
| `\CrossBoxCorr` | crossed box | four corner vertices with crossed internal diagonals |
| `\TriangleContactCorr` | triangle-contact helper | two trivalent vertices and one quartic/contact vertex |
| `\HalfBoxCorr` | vertex-identity half-box | continuous top line through two triple vertices, with two downward legs |
| `\FlatContactCorr` | flat-top quartic/contact piece | central contact vertex with a flattened top pair |
| `\SunsetDiagram` | self-energy sunset | two external legs plus top/middle/bottom internal lines |

The convenience channel wrappers are just `\FourPointCorr` with a fixed topology:

- `\SChannelCorr`, `\TChannelCorr`, `\UChannelCorr` for the one-loop `\phi^4` bubbles
- `\BoxLoopCorr` for the one-loop four-point box, equivalent to `\FourPointCorr[topology=box,...]`
- `\CrossBoxCorr` for the crossed-box helper, equivalent to `\FourPointCorr[topology=cross-box,...]`
- `\TriangleContactCorr` for the triangle-contact helper, equivalent to `\FourPointCorr[topology=triangle-contact,...]`
- `\HalfBoxCorr` for the vertex-identity half-box, equivalent to `\FourPointCorr[topology=half-box,...]`
- `\FlatContactCorr` for the flat-top contact piece, equivalent to `\FourPointCorr[topology=flat-contact,...]`
- `\STreeChannelCorr`, `\TTreeChannelCorr`, `\UTreeChannelCorr` for the explicit tree-level exchange graphs

## Leg Order And Slot Order

### `\TwoPointCorr`

- slot 1 = left leg
- slot 2 = right leg

### `\BubbleCorr`

- slot 1 = left external leg
- slot 2 = right external leg
- `bubble-a` / `bubble-top` = upper internal propagator
- `bubble-b` / `bubble-bottom` = lower internal propagator

Use `momentum-labels={...,...}` for the two external legs. Use
`bubble-momenta={...,...}` or `bubble-a-momentum=...` /
`bubble-b-momentum=...` for loop momenta. Internal loop momentum arrows are
drawn only when their bubble momentum text is provided.
Use `bubble-momentum-rotation=clockwise|counterclockwise` when the two loop
arrows should circulate in opposite directions around the bubble.
The default `bubble-momentum-layout=manual` uses the same
`bubble-momentum-start`, `bubble-momentum-end`, and
`bubble-momentum-label-fraction` on both internal arcs. Use
`bubble-momentum-layout=vertex-split` to put the upper and lower arrows on
opposite halves of the loop, mirrored automatically by
`bubble-momentum-rotation`.
Tune that mode with either grouped triples or individual side keys:

```tex
bubble-momentum-layout=vertex-split,
bubble-vertex-split-left={0.14,0.40,0.24},
bubble-vertex-split-right={0.60,0.86,0.76},
bubble-vertex-split-offset-scale=0.75,
```

Each grouped value is `{start,end,label-fraction}`. The same controls are also
available individually as `bubble-vertex-split-left-start=...`,
`bubble-vertex-split-left-end=...`,
`bubble-vertex-split-left-label-fraction=...`, and the matching
`bubble-vertex-split-right-*` keys. Aliases
`bubble-vertex-split-near-left-*` and `bubble-vertex-split-near-right-*` are
provided for the same values. In vertex-split mode, the package keeps these
values inside a shoulder band of the bubble curve so arrows do not plunge into
the steep vertex tangent. `bubble-vertex-split-offset-scale=...` multiplies
`bubble-momentum-offset` for the split arrows only, so near-vertex arrows can
stay closer to the propagator curvature without changing the broad/manual
momentum layout.

Use `bubble-external-indices={left,right}` for vertex-side external-leg
indices near the bubble vertices. The generic `indices={...}` key belongs to
outer field labels when those labels are explicitly enabled.

Endpoint indices use two entries per internal propagator:

- `bubble-a-indices={left,right}`
- `bubble-b-indices={left,right}`
- `bubble-endpoint-indices={aL,aR,bL,bR}`

### `\ThreePointCorr`

- slot 1 = upper-left leg
- slot 2 = right leg
- slot 3 = bottom leg

That slot order matters for:

- `leg-styles={...}`
- `momentum-labels={...}`
- `momentum-directions={...}`
- `momentum-arrow-sizes={...}`
- `propagator-arrow-sizes={...}`
- `leg-labels={...}`

The default 3-point momentum convention is:

- upper-left leg incoming
- right leg outgoing
- bottom leg outgoing

Use the generic corner orientation key to move the diagonal slot-1 leg while
keeping slot data attached:

- `orientation={top,left}` or `orientation={left,top}`: diagonal leg points to the upper left
- `orientation={top,right}` or `orientation={right,top}`: diagonal leg points to the upper right
- `orientation={bottom,left}` or `orientation={left,bottom}`: diagonal leg points to the lower left
- `orientation={bottom,right}` or `orientation={right,bottom}`: diagonal leg points to the lower right

One-entry shorthand accepts `orientation={left}` and `orientation={right}`;
both default to the top diagonal. The three-point aliases
`three-point-corner={...}` and `three-point-diagonal-corner={...}` feed the
same resolver.

Use `three-point-momentum-flow=all-in|all-out|default` to set all three arrows at once.
Use `momentum-directions={in,out,out}` for per-leg arrow directions in slot
order. The topology-specific spelling `three-point-momentum-directions={...}`
is also accepted.

For per-leg overrides use:

- `three-point-upper-left-momentum-direction=in|out`
- `three-point-right-momentum-direction=in|out`
- `three-point-bottom-momentum-direction=in|out`

Shorter aliases also work:

- `three-point-left-momentum-direction=...`
- `three-point-ul-momentum-direction=...`
- `three-point-lower-momentum-direction=...`

### `\FourPointCorr`

External leg order is always:

- slot 1 = upper left
- slot 2 = lower left
- slot 3 = upper right
- slot 4 = lower right

For one-loop channel bubbles there are two extra internal propagator slots:

- slot 5 = internal line A
- slot 6 = internal line B

Interpretation of A/B depends on the topology:

- `topology=s`: A = top arc, B = bottom arc
- `topology=t`: A = left arc, B = right arc
- `topology=u`: A = left arc, B = right arc

That slot order matters for:

- `leg-styles={...}`
- `momentum-labels={...}`
- `momentum-directions={...}`
- `momentum-arrow-sizes={...}`
- `propagator-arrow-sizes={...}`

For `topology=box` and `\BoxLoopCorr`, the external order follows the box
around the diagram:

- slot 1 = upper left
- slot 2 = lower left
- slot 3 = upper right
- slot 4 = lower right

The box has four internal propagator slots:

- slot 5 = left edge
- slot 6 = top edge
- slot 7 = right edge
- slot 8 = bottom edge

The central loop momentum arrow uses slot 9 for `momentum-arrow-sizes={...}`.

For `topology=cross-box` and `\CrossBoxCorr`, the external order is the same
as the box order:

- slot 1 = upper left
- slot 2 = lower left
- slot 3 = upper right
- slot 4 = lower right

The two fixed internal segments use (default `cross-box-layout=left-right`):

- slot 5 = left edge
- slot 6 = right edge

With `cross-box-layout=top-bottom`, slot 5 is TL to TR (fixed top) and slot 6
is BL to BR (fixed bottom). The external and diagonal slot definitions stay
the same.

The crossed internal diagonals use:

- slot 7 = upper-left to lower-right diagonal, drawn with a small gap at the crossing
- slot 8 = lower-left to upper-right diagonal, drawn continuously

For `topology=triangle-contact` and `\TriangleContactCorr`, the external slots
stay spatially fixed for every orientation:

- slot 1 = upper left
- slot 2 = lower left
- slot 3 = upper right
- slot 4 = lower right

The contact vertex carries adjacent external pairs:

- `triangle-contact-orientation=bottom`: slots 2 and 4
- `triangle-contact-orientation=top`: slots 1 and 3
- `triangle-contact-orientation=left`: slots 1 and 2
- `triangle-contact-orientation=right`: slots 3 and 4

### `\SunsetDiagram`

External legs:

- slot 1 = left external segment
- slot 2 = right external segment

Internal segments:

- slot 3 = top arc
- slot 4 = middle bridge
- slot 5 = bottom arc

## Quick Start Examples

### Automatic `q_i`, `k_i`, or `p_i` labels

The default is `mode=p`, starting at 1. Four-leg external momenta default to
`p_1,p_2` incoming and `p_3,p_4` outgoing. Use `mode=q` or `mode=k` to
change the symbol. Explicit labels and direction overrides remain available.

```tex
\[
  \FourPointCorr[
    mode=q
  ]
\]
```

Supported built-in momentum letters:

- `mode=q`
- `mode=k`
- `mode=p`

You can also shift the numbering:

```tex
\[
  \FourPointCorr[
    mode=q,
    momentum-start=3
  ]
\]
```

### External labels from `field` plus `indices`

```tex
\[
  \FourPointCorr[
    field=\phi,
    indices={a,b,c,d},
  ]
\]
```

This gives `\phi_a`, `\phi_b`, `\phi_c`, `\phi_d`.

### 3-point vertex

```tex
\[
  \ThreePointCorr[
    line=ewboson,
    field=A,
    indices={\mu,\nu,\rho},
    momentum-labels={q_1,q_2,q_3},
    three-point-momentum-flow=all-in
  ]
\]
```

The 3-point layout has one upper-left leg, one right leg, and one bottom leg.
Use `leg-styles={...}` for per-leg propagator styles in that order.

### Fully manual external labels

```tex
\[
  \FourPointCorr[
    leg-labels={\psi_i,\bar\psi_j,\psi_k,\bar\psi_l},
    momentum-labels={p_1,p_2,p_3,p_4},
    momentum-directions={out,in,in,out}
  ]
\]
```

### Visible vertex, no blob

```tex
\[
  \FourPointCorr[
    blob=false,
    center-vertex-style=ringdot
  ]
\]
```

## External Field Labels

The standard pattern is:

- `field=\phi`
- `indices={...}`

Index placement:

- `index-placement=sub`
- `index-placement=sup`
- `index-placement=none`
- `index-placement=mini`

With `field={}`, `index-placement=mini` typesets each entry of `indices` as
an index on an empty math base, for example `{}_{\alpha}`. This gives a small,
lowered index without adding `\hspace`. With a nonempty field, `mini` uses the
normal field subscript, such as `A_{\alpha}`. Explicit `leg-labels` still take
precedence and are not reformatted. Other index-placement modes keep their
existing behavior.

```tex
\FourPointCorr[
  field={},
  index-placement=mini,
  indices={\alpha,\nu,\tau,\sigma},
  show-momenta=false
]
```


If you need complete manual control, use:

- `leg-labels={...}`

`leg-labels` overrides `field` and `indices` for the legs you specify.

## Momentum Labels And Arrows

### Hide selected external momenta

Use `external-momentum-hide={2}` to remove both the momentum arrow and its
label from logical external slot 2. Multiple slots can be hidden with, for
example, `external-momentum-hide={1,4}`. The default `{}` hides nothing.

```tex
\FlatContactCorr[
  momentum-labels={q_1,,p,q_3},
  external-momentum-hide={2}
]
```

The slot-2 propagator, particle label, and propagator arrow/endcap styling
remain visible. This key overrides nonempty momentum text and topology-specific
selection keys such as `flat-contact-momentum-slots`, regardless of key order.
Repeated numbers are harmless; numbers outside the external slots are ignored.
`show-momenta=false` still disables all momentum annotations.

An explicitly empty momentum-label entry (including `{}` or whitespace) keeps
a continuous **unlabeled arrow**, with no label node or artificial gap. Empty
entries retain their list positions: `{q_1,,p,q_3}` assigns `p` to slot 3.
An omitted/empty whole `momentum-labels` list uses the normal defaults; entries
beyond a shorter list also retain their normal automatic labels. No strings
such as `na` or `none` have special meaning in label text.

The hide key applies to external slots across two-, three-, and four-point
families, including bubble and sunset. Slots follow the family's logical
external label order, so they stay attached when a three-point diagram rotates.
Bubble and sunset external momentum slots are 1 (left) and 2 (right).
For bubble/seagull insertions on s/t-tree external slots 1-4 and external contact insertions, hiding the
selected slot suppresses both pre- and post-insertion momentum annotations. Channel, bridge, box-edge,
and loop momenta retain their existing controls; this key does not hide them.
The setting is scoped to the current diagram.

Focused visual and behavioral checks:
`regressions/momenta/external-momentum-visibility.tex`.

### First: what kind of key moves what?

For momentum annotations, the naming pattern matters:

- `loop-channel-top-momentum=\ell` changes the text itself
- `loop-channel-top-arrow-yshift=14pt` changes the arrow only
- `loop-channel-top-label-yshift=14pt` changes the label only
- `loop-channel-top-label-distance=12pt` changes the separation between label and arrow
- `loop-channel-top-label-fraction=0.50` slides the label along the same line or curve
- `loop-channel-top-arrow-start=0.24` and `loop-channel-top-arrow-end=0.76` shorten or lengthen the arrow along its line or curve

That is the quickest way to read the API.

### Global momentum text style

For simple diagrams you can rely on:

- `mode=p|q|k` (default `p`)
- `momentum-start=<integer>`
- `momentum-labels={...}`

The default grouped external flow is `external-momentum-flow=left-in-right-out`,
also selected by `external-momentum-flow=default`. The explicit `all-in`,
`all-out`, and `left-out-right-in` presets remain available, as do per-leg keys.
Three-point vertices retain their separate one-in/two-out convention.

Momentum labels use a normal-sized math label by default so they remain
readable when figures are reproduced smaller. There is no white box behind
them unless you add one yourself with:

- `momentum-label-fill=...`
- `momentum-label-inner-sep=...`
- `momentum-label-style=...`
- `momentum-label-size=...`

Momentum arrows are intentionally lightweight by default: the package uses a
thin line and small arrowhead so momentum flow reads as an annotation rather
than as a propagator. The default label gap leaves a small break around each
momentum label so the arrow segments do not crowd the text.

- `momentum-line-width=...`
- `momentum-arrow-size=...`
- `momentum-arrow-sizes={...}`
- `momentum-label-gap=...`
- `external-momentum-start=...`
- `external-momentum-end=...`
- `external-momentum-label-fraction=...`

### 3-point momentum flow

For `\ThreePointCorr`, the default momentum flow is useful for a vertex with one incoming leg and two outgoing legs:

```tex
\[
  \ThreePointCorr[
    momentum-labels={q_1,q_2,q_3},
    three-point-momentum-flow=default
  ]
\]
```

The flow presets are:

- `three-point-momentum-flow=default`: upper-left in, right out, bottom out
- `three-point-momentum-flow=all-in`
- `three-point-momentum-flow=all-out`

Per-leg direction keys take `in` or `out`:

- `three-point-upper-left-momentum-direction=...`
- `three-point-right-momentum-direction=...`
- `three-point-bottom-momentum-direction=...`

The shared arrow and label controls still apply:

- `momentum-labels={...}`
- `momentum-arrow-size=...`
- `momentum-arrow-sizes={...}`
- `momentum-label-fill=...`
- `momentum-label-inner-sep=...`
- `momentum-label-style=...`

3-point momentum placement controls apply to all three legs:

- `three-point-momentum-layout=default|outward`
- `three-point-momentum-start=...`
- `three-point-momentum-end=...`
- `three-point-momentum-label-fraction=...`
- `three-point-momentum-label-gap=...`
- `three-point-momentum-offset=...`

Use `three-point-momentum-layout=outward` when the default arrows crowd a
triple vertex or scalar-polarized marker. It moves the arrows toward the
external ends, increases their distance from the propagator lines, and centers
each label in its arrow break.

### One-loop `s/t/u` bubbles: the internal loop momenta

This is the part of the package where the label and arrow are most clearly treated as one annotation attached to one loop line.

If you do not want to mentally decode key families, skip straight to the paste-ready blocks below and edit one number at a time.

Use these names for the momentum text:

- `loop-channel-top-momentum=...`
- `loop-channel-bottom-momentum=...`
- `loop-channel-left-momentum=...`
- `loop-channel-right-momentum=...`
- `loop-channel-momenta={..., ...}`

You can also use the equivalent `a/b` names:

- `loop-channel-a-momentum=...`
- `loop-channel-b-momentum=...`

Direction:

- `loop-channel-top-momentum-direction=forward|reverse|none`
- `loop-channel-bottom-momentum-direction=forward|reverse|none`
- `loop-channel-left-momentum-direction=forward|reverse|none`
- `loop-channel-right-momentum-direction=forward|reverse|none`

#### Loop-channel motion cheat sheet

If you want to do this | Use this key family | What it changes
--- | --- | ---
Change the label text | `loop-channel-top-momentum=...` | text only
Move the label farther from the arrow | `loop-channel-top-label-distance=...` | label-arrow separation only
Slide the label along the same curve | `loop-channel-top-label-fraction=...` | label position along the curve
Change the side the label sits on | `loop-channel-top-label-position=above|below|left|right` | anchor side for the label
Nudge only the label | `loop-channel-top-label-xshift=...`, `loop-channel-top-label-yshift=...` | label only
Shorten or lengthen the arrow | `loop-channel-top-arrow-start=...`, `loop-channel-top-arrow-end=...` | arrow span only
Move the arrow guide away from the loop | `loop-channel-top-arrow-yshift=...` or `loop-channel-left-arrow-xshift=...` | arrow only
Change how curved the arrow guide feels | `loop-channel-top-arrow-looseness=...` | arrow curvature only

Replace `top` with `bottom`, `left`, or `right` as needed.

#### The two-step tuning workflow for loop-channel momenta

If a label is overlapping its arrow:

1. Increase `loop-channel-top-label-distance` or `loop-channel-left-label-distance`.
2. If the label should also slide along the curve, change `loop-channel-top-label-fraction` or `loop-channel-left-label-fraction`.

If the label and arrow look fine relative to each other, but the whole thing is too close to the loop or to the page edge:

1. Keep your chosen `loop-channel-top-label-distance` or `loop-channel-left-label-distance`.
2. Move the arrow with `loop-channel-top-arrow-yshift` or `loop-channel-left-arrow-xshift`.
3. Move the label by the same amount with `loop-channel-top-label-yshift` or `loop-channel-left-label-xshift`.

Example: separate first, then move together:

```tex
\[
  \TChannelCorr[
    loop-channel-left-momentum=\ell,
    loop-channel-left-label-distance=10pt,
    loop-channel-left-arrow-xshift=-6pt,
    loop-channel-left-label-xshift=-6pt
  ]
\]
```

Here the logic is:

- `label-distance` opens space between text and arrow
- matching `arrow-xshift` and `label-xshift` move the whole annotation left together

Example: vertical version for the `s` channel:

```tex
\[
  \SChannelCorr[
    loop-channel-top-label-distance=12pt,
    loop-channel-top-arrow-yshift=14pt,
    loop-channel-top-label-yshift=14pt
  ]
\]
```

Here the top momentum label is first pushed away from the arrow, and then the arrow+label pair is lifted upward together.

#### Paste-ready default blocks

Use these as real starting points.

Default `s`-channel internal loop momenta:

```tex
\[
  \SChannelCorr[
    loop-channel-top-momentum=\ell,
    loop-channel-top-momentum-direction=forward,
    loop-channel-top-arrow-start=0.24,
    loop-channel-top-arrow-end=0.76,
    loop-channel-top-arrow-xshift=0pt,
    loop-channel-top-arrow-yshift=13pt,
    loop-channel-top-arrow-looseness=1.02,
    loop-channel-top-label-position=above,
    loop-channel-top-label-distance=10pt,
    loop-channel-top-label-fraction=0.50,
    loop-channel-top-label-xshift=0pt,
    loop-channel-top-label-yshift=0pt,
    loop-channel-bottom-momentum=p_1+p_2-\ell,
    loop-channel-bottom-momentum-direction=forward,
    loop-channel-bottom-arrow-start=0.24,
    loop-channel-bottom-arrow-end=0.76,
    loop-channel-bottom-arrow-xshift=0pt,
    loop-channel-bottom-arrow-yshift=-13pt,
    loop-channel-bottom-arrow-looseness=1.02,
    loop-channel-bottom-label-position=below,
    loop-channel-bottom-label-distance=10pt,
    loop-channel-bottom-label-fraction=0.50,
    loop-channel-bottom-label-xshift=0pt,
    loop-channel-bottom-label-yshift=0pt
  ]
\]
```

Default `t`-channel internal loop momenta:

```tex
\[
  \TChannelCorr[
    loop-channel-left-momentum=\ell,
    loop-channel-left-momentum-direction=forward,
    loop-channel-left-arrow-start=0.24,
    loop-channel-left-arrow-end=0.76,
    loop-channel-left-arrow-xshift=-18pt,
    loop-channel-left-arrow-yshift=0pt,
    loop-channel-left-arrow-looseness=1.02,
    loop-channel-left-label-position=left,
    loop-channel-left-label-distance=9pt,
    loop-channel-left-label-fraction=0.50,
    loop-channel-left-label-xshift=0pt,
    loop-channel-left-label-yshift=0pt,
    loop-channel-right-momentum=q-\ell,
    loop-channel-right-momentum-direction=forward,
    loop-channel-right-arrow-start=0.24,
    loop-channel-right-arrow-end=0.76,
    loop-channel-right-arrow-xshift=18pt,
    loop-channel-right-arrow-yshift=0pt,
    loop-channel-right-arrow-looseness=1.02,
    loop-channel-right-label-position=right,
    loop-channel-right-label-distance=9pt,
    loop-channel-right-label-fraction=0.50,
    loop-channel-right-label-xshift=0pt,
    loop-channel-right-label-yshift=0pt
  ]
\]
```

Default `u`-channel internal loop momenta and crossed right-side external momenta:

```tex
\[
  \UChannelCorr[
    loop-channel-left-momentum=r-\ell,
    loop-channel-left-momentum-direction=forward,
    loop-channel-left-arrow-start=0.24,
    loop-channel-left-arrow-end=0.76,
    loop-channel-left-arrow-xshift=-18pt,
    loop-channel-left-arrow-yshift=0pt,
    loop-channel-left-arrow-looseness=1.02,
    loop-channel-left-label-position=left,
    loop-channel-left-label-distance=9pt,
    loop-channel-left-label-fraction=0.50,
    loop-channel-left-label-xshift=0pt,
    loop-channel-left-label-yshift=0pt,
    loop-channel-right-momentum=\ell,
    loop-channel-right-momentum-direction=forward,
    loop-channel-right-arrow-start=0.24,
    loop-channel-right-arrow-end=0.76,
    loop-channel-right-arrow-xshift=18pt,
    loop-channel-right-arrow-yshift=0pt,
    loop-channel-right-arrow-looseness=1.02,
    loop-channel-right-label-position=right,
    loop-channel-right-label-distance=11pt,
    loop-channel-right-label-fraction=0.50,
    loop-channel-right-label-xshift=4pt,
    loop-channel-right-label-yshift=6pt,
    loop-channel-crossed-external-momentum-start=0.00,
    loop-channel-crossed-external-momentum-end=0.24,
    loop-channel-crossed-external-momentum-label-fraction=0.08
  ]
\]
```

#### How to start guessing adjustments

Use these as the first numbers to change:

- `loop-channel-top-label-distance`, `loop-channel-bottom-label-distance`, `loop-channel-left-label-distance`, `loop-channel-right-label-distance`
  Defaults: `10pt` for `s`, `9pt` for `t`, `11pt` for the crowded right side of `u`.
  Bigger means more space between label and arrow.
  Smaller means label sits closer to the arrow.

- `loop-channel-top-arrow-looseness`, `loop-channel-bottom-arrow-looseness`, `loop-channel-left-arrow-looseness`, `loop-channel-right-arrow-looseness`
  Default: `1.02`.
  Bigger means the guide arrow bows farther and looks rounder.
  Smaller means the guide arrow gets flatter and tighter.

- `loop-channel-top-label-fraction`, `loop-channel-bottom-label-fraction`, `loop-channel-left-label-fraction`, `loop-channel-right-label-fraction`
  Default: `0.50`.
  Smaller means the label moves toward the first end of the arrow.
  Bigger means the label moves toward the second end of the arrow.

- `loop-channel-top-arrow-start`, `loop-channel-bottom-arrow-start`, `loop-channel-left-arrow-start`, `loop-channel-right-arrow-start`
  Default: `0.24`.
  Bigger means the arrow starts later, so the arrow gets shorter near its first end.
  Smaller means the arrow reaches farther toward its first end.

- `loop-channel-top-arrow-end`, `loop-channel-bottom-arrow-end`, `loop-channel-left-arrow-end`, `loop-channel-right-arrow-end`
  Default: `0.76`.
  Bigger means the arrow reaches farther toward its second end.
  Smaller means the arrow stops earlier, so it gets shorter near its second end.

- `loop-channel-top-arrow-yshift`, `loop-channel-bottom-arrow-yshift`, `loop-channel-left-arrow-xshift`, and `loop-channel-right-arrow-xshift`
  Defaults: `0pt` / `13pt` / `-13pt` in `s`, `-18pt` and `18pt` in `t/u`.
  Bigger absolute value means you push the arrow farther away from the loop in that direction.

When something still looks bad, this is the recommended order:

1. Change `label-distance`.
2. Change `label-fraction`.
3. Change `arrow-start` / `arrow-end`.
4. Change `arrow-looseness`.
5. Only then start moving the pair around with matching arrow and label shifts.

#### Loop-channel fix-it recipes

If the top `s`-channel label is sitting on top of its arrow:

```tex
\[
  \SChannelCorr[
    loop-channel-top-label-distance=14pt
  ]
\]
```

If that same top `s`-channel label is fine relative to the arrow, but the whole top annotation is still too low:

```tex
\[
  \SChannelCorr[
    loop-channel-top-label-distance=14pt,
    loop-channel-top-arrow-yshift=18pt,
    loop-channel-top-label-yshift=5pt
  ]
\]
```

Why this works:

- `label-distance=14pt` opens the gap
- arrow `13pt -> 18pt` moves the arrow up
- label `0pt -> 5pt` moves the label up by the same extra `5pt`

If the left `t`-channel label is sitting on the arrow:

```tex
\[
  \TChannelCorr[
    loop-channel-left-label-distance=12pt
  ]
\]
```

If the left `t`-channel annotation is too close to the loop and needs to move farther left as one unit:

```tex
\[
  \TChannelCorr[
    loop-channel-left-label-distance=12pt,
    loop-channel-left-arrow-xshift=-24pt,
    loop-channel-left-label-xshift=-6pt
  ]
\]
```

Why this works:

- default left arrow shift is `-18pt`
- changing it to `-24pt` moves the arrow `6pt` farther left
- changing the label from `0pt` to `-6pt` moves the label left by the same extra amount

If the loop arrow looks too flat and not curved enough:

```tex
\[
  \TChannelCorr[
    loop-channel-left-arrow-looseness=1.20,
    loop-channel-right-arrow-looseness=1.20
  ]
\]
```

If the loop arrow looks too round and exaggerated:

```tex
\[
  \TChannelCorr[
    loop-channel-left-arrow-looseness=0.90,
    loop-channel-right-arrow-looseness=0.90
  ]
\]
```

If the right side of the `u` channel is crowded:

```tex
\[
  \UChannelCorr[
    loop-channel-right-label-distance=13pt,
    loop-channel-right-label-xshift=6pt,
    loop-channel-right-label-yshift=8pt,
    loop-channel-crossed-external-momentum-start=0.00,
    loop-channel-crossed-external-momentum-end=0.20,
    loop-channel-crossed-external-momentum-label-fraction=0.06
  ]
\]
```

Why this works:

- the right loop label gets farther from its arrow
- the right loop label is nudged farther out and slightly up
- the crossed external momentum marks move closer to the outer leg ends, away from the crossing

### One-loop `s/t/u` bubbles: external straight-leg momenta

The straight external momentum arrows use a simpler system:

- `loop-channel-external-momentum-start=...`
- `loop-channel-external-momentum-end=...`
- `loop-channel-external-momentum-label-fraction=...`

For the crossed right side of the one-loop `u` channel:

- `loop-channel-crossed-external-momentum-start=...`
- `loop-channel-crossed-external-momentum-end=...`
- `loop-channel-crossed-external-momentum-label-fraction=...`

These do:

- `start/end`: shorten or lengthen the arrow segment along the external leg
- `label-fraction`: slide the label along that same segment

They do not provide a separate `label-distance` control. Use them to keep the external momentum marking away from a crowded vertex or crossing.

Paste-ready external momentum defaults for `t`:

```tex
\[
  \TChannelCorr[
    loop-channel-external-momentum-start=0.08,
    loop-channel-external-momentum-end=0.52,
    loop-channel-external-momentum-label-fraction=0.26
  ]
\]
```

Paste-ready crossed external momentum defaults for `u`:

```tex
\[
  \UChannelCorr[
    loop-channel-crossed-external-momentum-start=0.00,
    loop-channel-crossed-external-momentum-end=0.24,
    loop-channel-crossed-external-momentum-label-fraction=0.08
  ]
\]
```

Quick intuition:

- smaller `...-start` moves the arrow closer to the outer end of the leg
- bigger `...-end` extends the arrow farther toward the vertex
- smaller `...-label-fraction` moves the label toward the outer end
- bigger `...-label-fraction` moves the label toward the vertex

Important:

- `loop-channel-*` keys are for the one-loop `s/t/u` bubbles.
- `channel-*` keys belong to the explicit tree-level exchange topologies.

### Sunset diagrams: momentum tuning

For sunsets, the momentum text keys are:

- `sunset-external-momentum=...`
- `sunset-top-momentum=...`
- `sunset-middle-momentum=...`
- `sunset-bottom-momentum=...`

Start with `sunset-momentum-layout=compact|balanced|wide`. If a label is too close to an index, increase the corresponding clearance key:

- `sunset-top-label-index-clearance=...`
- `sunset-middle-label-index-clearance=...`
- `sunset-bottom-label-index-clearance=...`

Lower-level controls still exist for arrow and label shifts, including `sunset-top-arrow-yshift`, `sunset-top-label-yshift`, `sunset-middle-arrow-start`, `sunset-middle-arrow-end`, and the matching bottom keys. The sunset momentum system is older than the box and 3-point systems, so the next planned sunset branch should start with a visual capacity sheet before changing defaults.

### Tree-level exchange channels

The tree-level exchange topologies use the older `channel-*` family instead of `loop-channel-*`.

The most important motion keys there are:

- `show-channel-momentum=true|false` (default `true` per diagram)
- `channel-momentum-start=...`
- `channel-momentum-end=...`
- `channel-momentum-distance=...`
- `channel-momentum-angle=...`
- `channel-momentum-label-position=...`
  Side placements draw a continuous momentum arrow. Use `center` to place the
  label in an intentional arrow gap controlled by `momentum-label-gap`.
- `channel-momentum-label-xshift=...`
- `channel-momentum-label-yshift=...`

Use `show-channel-momentum=false` to hide both the central tree-exchange
momentum arrow and its momentum label while retaining external and insertion-loop
momenta. It works on s/t/u trees, including the s/t bubble/seagull insertions;
it does not hide the central propagator, its species circle, or its indices.
`show-momenta=false` still disables all momenta. Four-legged loop channels keep
their separate `loop-channel-*` controls.

The logic is:

- `distance` and `angle` place the internal momentum arrow line relative to the propagator
- `label-xshift/yshift` then nudge the text

## Line Styles, Arrows, And Vertices

Global line style:

```tex
\[
  \FourPointCorr[
    line=fer
  ]
\]
```

Global line color:

```tex
\[
  \FourPointCorr[
    color=fieldA
  ]
\]
```

`line-color=...` is an alias for `color=...`. Global color is appended to
propagator styles across the package, including ordinary correlators,
3-point vertices, box diagrams, channel diagrams, and sunset diagrams.

The default EW-boson style used by `ewboson` and `EWboson` is a single clean wavy
line with fixed-frequency squiggles. The `photon` and legacy `pho` aliases route
through the same shared style, so changing a leg or internal line to any of
these styles uses the same visual language in every topology.

Use the per-propagator key `ewboson wavelength=...` to control wave spacing.
Its default is `22\feynhandlinesize`, preserving the existing EW appearance.
A shorter value adds more ripples along the same path; amplitude is unchanged.
For a short bubble arc interrupted by a W circle, the styled examples use:

```tex
bubble-top-line={ewboson,ewboson wavelength=10\feynhandlinesize,circ=W,circ scale=0.65}
```

This setting applies only to that line. Ordinary external legs and central stems
keep their original wave spacing. `EWboson`, `photon` and `pho` share the same
wavelength control; it can appear before or after the line-style token.
`regressions/propagators/ewboson-frequency/ewboson-frequency-check.tex/pdf`
compares the defaults and shorter waves on straight lines and short s/t loops.
Its PDF checker verifies increased rendered wave density, alias/key order,
and reset on the next line.

The `proca` style is a massive-vector convenience style built on a straight
scalar-style dashed line with two white-filled open arrow markers. In
package-managed topologies, the package strips those markers from the raw line
style and redraws them as endpoint-aware triangles whose tips kiss the semantic
vertex boundary. The arrows use the same size as scalar-polarized markers;
their outlines follow simple propagator color tokens while their interiors stay
white. `Proca` is accepted as an alias. Neither `proca` nor `spol` adds a
circle automatically: `proca` supplies both endpoint arrows, while `spol`
normally supplies one. Add `circ={}` explicitly when a blank
midpoint circle is wanted.
Use `proca start` or `proca end` instead of `proca` for a single triangle
at the drawn path's start or end. This also applies to bubble internal lines
and `seagull-loop-line`. With the default lower seagull loop, `proca start`
marks the right branch and `proca end` marks the left branch; reversing the
loop orientation swaps their visual sides. Curved endpoint triangles use the
configured propagator arrow size independently of loop radius or diagram
scale, with their tips at the semantic vertex boundary.


On raw/manual Proca paths, triangle tips track the standard 2.15pt dot
boundary under uniform picture scale independently of arrow size. The per-line
option `proca vertex radius=...` targets a different circular vertex; for
example, `channel-line={proca,proca vertex radius=2.5pt}` can accompany a
ring-dot vertex. This explicit per-line override works in either style order,
including inside managed straight-leg helpers.

Ordinary package-managed endpoints retain the semantic vertex-radius and
`0.25pt` tip-clearance controls from the seagull implementation. For these,
use `semantic-marker-vertex-radius` and `semantic-marker-tip-clearance`.
Standalone/inserted bubbles and seagull loops retain the shared curved marker
helper and its one-sided marker sizing; bubble-specific radius/distance
controls still apply there.

An explicit non-default raw `endpoint marker distance` or
`open arrow marker distance` selects legacy center-distance placement, including
when supplied per-line on a managed straight Proca edge. If both differ from
the default, `endpoint marker distance` takes precedence. Raw/manual
`openarrowin/out` retain the separate `open arrow marker distance` key;
managed add-ons retain their vertex-aware semantics.

The [M01 diagnostic and results](../regressions/propagators/proca-endpoints/README.md)
cover short/normal paths, three uniform scales, all current internal topology
families, custom radius, alias/color order, and split crossings. Arbitrary
anisotropic transforms and custom non-circular vertex shapes are not certified.

Endpoint marker add-ons can be combined with any propagator style:

- `arrowin` / `arrowout`: filled arrowhead pointing toward or away from the
  topology vertex
- `openarrowin` / `openarrowout`: white-filled open arrowhead pointing toward
  or away from the topology vertex
- `endcapout`: short perpendicular terminal bar exactly at the cropped external
  endpoint of an external leg
- `endcapin`: the corresponding path-end form for raw `\propag[...]` usage
- `endcap`: ergonomic external-end alias; in package-managed topologies it
  behaves like `endcapout`
- `endcappout`, `endcappin`, `endcapp`: staggered double-endcap variants. The
  inner bar is longer than the terminal bar; in package-managed topologies
  `endcapp` behaves like `endcappout`.

In package-managed topologies, these add-ons are oriented relative to the
interaction vertex for each leg and use the same endpoint-aware triangle
placement as `proca`/`spol`. In raw `\propag[...]` calls, they fall back to
path-end semantics: `...in` targets the path end and `...out` points away from
the path end. Endcaps are intended for external legs only; in topology helpers,
use `endcap` or `endcapout` on an external leg style to mark the outer cropped
endpoint. Endcaps inherit the resolved propagator color, including global
`color=...`, topology color keys, and common per-leg TikZ/xcolor styles such as
`{ewboson,fieldA,endcap}`, `{ewboson,blue!65!black,endcap}`, and
`{ewboson,color=orange!85!black,endcap}`. Color inheritance is order-stable for
the cap add-on, so `{ewboson,endcapp,fieldA}` and `{ewboson,fieldA,endcapp}`
produce matching cap colors.

Endpoint cap tuning keys:

- `endpoint-cap-length=...` / `endcap-length=...`
- `endpoint-double-cap-inner-length=...` / `endcapp-inner-length=...`
- `endpoint-double-cap-gap=...` / `endcapp-gap=...`

Circled propagator markers can be added to any propagator style with `circ=...`:

```tex
\[
  \ThreePointCorr[
    line={ewboson,circ=Z},
    field={},
    show-momenta=false
  ]
\]
```

Use `circ={}` for a blank circle. The aliases `with circle=...` and
`circled=...` are also accepted. Marker tuning keys are:

- `circ position=...`
- `circ size=...`
- `circ scale=...`
- `circ label scale=...`
- `circ fill=...`
- `circ draw=...`
- `circ label style={...}`

The package default is now equivalent to `circ scale=0.8`: a **9.6pt diameter**
with label scale **0.8**. `circ scale` retains its existing 12pt reference:
explicit `circ scale=1` restores the former full-size circle/text, while explicit
`.6` and `.8` retain their previous meanings. `circ size` and `circ label scale`
remain independently adjustable. See the
[default/override gallery](../regressions/propagators/circ/circ-default-scale.pdf).

The circle keeps the configured `circ size`; labels are overlaid rather than
allowed to resize the marker. Increase `circ size` when a deliberately wide
custom label should fit fully inside the circle. By default, the circle outline
inherits the resolved propagator color, including Proca propagators; use
`circ draw=...` to override the outline color independently. Use
`circ scale=...` for short segment markers; it scales the 12pt reference circle
and the overlaid label contents together while keeping labels upright on sloped
segments. Use `circ label scale=...` to tune only the label size.

W-family markers are hand-tuned to keep the default circle size readable:

- `circ=W` for a compact neutral W marker
- `circ=Wp` for \(W^+\)
- `circ=Wm` for \(W^-\)

Arbitrary labels such as `circ=Z`, `circ=Y`, or raw math like `circ=W^+` still
work, but prefer `Wp` and `Wm` when you want charged W markers to align with
the default `circ=W` circle.

When a style contains commas inside `leg-styles={...}`, wrap that slot in braces:
`leg-styles={{ewboson,circ=W},plain,{ewboson,circ=Z}}`.

Per-leg overrides:

```tex
\[
  \ThreePointCorr[
    line=ewboson,
    leg-styles={scalarpolarized,ewboson,ewboson},
    three-point-momentum-flow=all-in,
    three-point-momentum-layout=outward,
    momentum-labels={q_1,q_2,q_3},
    propagator-arrow-sizes={14pt,,}
  ]
\]
```

Use `epspol` for a short scalar-polarized external leg with a double endcap:

```tex
\[
  \ThreePointCorr[
    line=ewboson,
    leg-styles={epspol,ewboson,ewboson},
    three-point-external-length=1.05,
    three-point-momentum-flow=all-in,
    three-point-momentum-layout=outward
  ]
\]
```

For the compact thesis-rule style used in electroweak three-point identities,
use `\ThreePointThesis` or the alias `\ThesisVertex`. It expands to
`\ThreePointCorr` with the common thesis defaults for scale, endpoint caps,
external labels, momentum labels, momentum-arrow placement, and slot-3 arrow
size. Any normal three-point key can still be passed as an override:

```tex
\[
  \ThreePointThesis[orientation={bottom,right}]
\]
```

The wrapper defaults are ordinary keys, so a figure can move the scalar-polarized
leg and rename momenta without rewriting the full preset:

```tex
\[
  \ThreePointThesis[
    orientation={top,left},
    leg-styles={{spol,magenta!85!red,endcap},{ewboson,endcap},{ewboson,endcapp}},
    momentum-labels={r,s,t}
  ]
\]
```

3-point geometry controls:

- `three-point-left-xspan=...`
- `three-point-upper-yspan=...`
- `three-point-right-xspan=...`
- `three-point-bottom-yspan=...`
- `orientation={top,left|top,right|bottom,left|bottom,right}`
- `three-point-corner=...`
- `three-point-diagonal-corner=...`
- `three-point-orientation=right|left|up|down`
- `three-point-external-length=...`
- `three-point-central-label-yshift=...`

`orientation={top,left}` is the compatibility layout used by existing figures.
The generic `orientation` key is intended for any diagram family that needs a
corner placement convention. For `\ThreePointCorr`, it chooses where the
diagonal slot-1 leg points while keeping slot-based labels, indices, styles,
and momentum controls attached to slots 1, 2, and 3. The legacy
`three-point-orientation` values remain available as aliases:
`right={top,left}`, `down={top,right}`, `up={bottom,left}`, and
`left={bottom,right}`. `three-point-external-length` shortens or lengthens slot
1 while preserving its default angle before orientation is applied.

3-point momentum placement controls:

- `three-point-momentum-layout=default|outward`
- `three-point-momentum-start=...`
- `three-point-momentum-end=...`
- `three-point-momentum-label-fraction=...`
- `three-point-momentum-label-gap=...`
- `three-point-momentum-offset=...`

Use `three-point-momentum-layout=outward` for crowded triple-coupling sketches,
especially when one leg is scalar-polarized. It moves the momentum arrows
toward the external leg ends, increases their distance from the propagators,
and keeps each momentum label centered in its arrow break. The existing
momentum directions are preserved. The shared start/end/fraction/gap/offset
keys above remain available for manual tuning.

Aliases for the upper-left leg geometry:

- `three-point-upper-left-xspan=...`
- `three-point-upper-left-yspan=...`

```tex
\[
  \FourPointCorr[
    line=plain,
    leg-styles={scalarpolarized,scalarpolarized,plain,plain}
  ]
\]
```

Arrow sizing:

- `momentum-arrow-size=...`
- `momentum-arrow-sizes={...}`
- `propagator-arrow-size=...`
- `propagator-arrow-sizes={...}`

Visibility and vertex controls:

- `blob=true|false`
- `blob-style=...`
- `center-vertex=true|false`
- `center-vertex-style=dot|ringdot|...`
- `external-vertices=true|false`
- `external-vertex-style=dot|ringdot|...`
- `vertices=true|false`
- `vertex-style=...`
- `scale=...`

The package-wide coordinate baseline is **0.8 times the former size**:
`scale=1` now produces the former `scale=0.8` drawing, and `scale=1.25`
recovers the former `scale=1` size. Every public diagram family and alias uses
this factor exactly once. Explicit scales remain relative to this baseline;
for example, `scale=0.8` now has the former `scale=0.64` geometry.
Existing family presets remain relative too: sunset's default 1.2 and the
thesis vertex's 0.75 are each reduced by the same factor.

This uses the existing TikZ coordinate-scale behavior: fonts, circles, line
widths and arrowhead sizes retain their existing sizing rules. Logical span,
insertion and label options keep their values. Raw user-created TikZ pictures
and standalone `\propag` lines are unaffected. See
[scale verification](planning/scale-baseline-verification.md).

Default behavior:

- 2-point and 4-point diagrams show the central blob
- visible center vertices are on by default
- external endpoint vertices are off by default
- sunset diagrams show the two internal interaction vertices

## Scalar-Polarized Legs

Special dashed scalar styles with white-filled open arrowheads:

- `scalarpolarized`
- `spol`

Directional aliases:

- `scalarpolarizedin`
- `scalarpolarizedout`
- `spolin`
- `spolout`

Relevant controls:

- `scalar-arrow-direction=in|out|none`
- `scalar-arrow-position=<0..1>`
- `/tikzfeynhand/open arrow marker distance=...` for raw/manual open arrows
- `semantic-marker-tip-clearance=...` for package-managed topology endpoints
- `semantic-marker-vertex-radius=...` for custom package-managed vertex dots
- `semantic-open-arrow-tip-clearance=...` as a compatibility alias

The default `scalarpolarized` style places an inward-pointing marker near the
vertex. In package-managed topologies, external scalar-polarized legs are
drawn with package-owned endpoint-aware triangle markers. The triangle tip is
placed at the semantic topology vertex edge plus a small clearance, even when
the propagator arrow size changes. The default clearance is `0.25pt`; tune
`semantic-marker-tip-clearance=...` only if a custom vertex size or line
weight needs the tip slightly closer to or farther from the dot. If a custom
vertex style uses a nonstandard dot radius, set
`semantic-marker-vertex-radius=...`. Raw/manual open-arrow decorations keep the
older `/tikzfeynhand/open arrow marker distance=...` key and TikZ decoration
geometry.

On raw/manual paths, `out` keeps the older decoration-style outward marker
orientation. Inside package-managed topologies, the semantic endpoint marker is
kept tied to the vertex boundary so the tip placement remains stable.

Legacy `antiscalar...` and `antspol...` names still work as aliases of the same scalar-polarized style.

The white fill masks the dashed line under the arrowhead. The open arrowhead
size tracks the normal propagator arrow-size controls.

## One-Loop Box Topology

The public box entry points are:

```tex
\BoxLoopCorr[...]
\FourPointCorr[topology=box,...]
```

The default box is a wavy four-point loop with four corner vertices, four
diagonal external legs, edge momentum labels, and a central clockwise loop
arrow.

Default external momenta:

- slot 1, upper left = `q_1`
- slot 2, lower left = `q_2`
- slot 3, upper right = `q_3`
- slot 4, lower right = `q_4`

Default internal momenta:

- left edge = `k`, arrow upward
- top edge = `q_1+k`, arrow rightward
- right edge = `q_1+k-q_4`, arrow downward
- bottom edge = `q_2-k`, arrow rightward
- center loop arrow = `k`, clockwise

Minimal box:

```tex
\[
  \BoxLoopCorr[
    field=A,
    indices={\mu,\nu,\rho,\sigma},
  ]
\]
```

The wrapper and explicit topology form are equivalent:

```tex
\[
  \FourPointCorr[
    topology=box,
    field=A,
    indices={\mu,\nu,\rho,\sigma}
  ]
\]
```

Mixed exterior line styles use the existing `leg-styles` slot order:

```tex
\[
  \BoxLoopCorr[
    leg-styles={spol,ewboson,ewboson,ewboson},
    scalar-arrow-direction=out,
    leg-labels={W_\mu,A_\nu,A_\rho,A_\sigma}
  ]
\]
```

Physical-polarization external legs add EW-boson external lines with endcaps
without changing the internal box lines:

```tex
\[
  \BoxLoopCorr[
    box-external-style=physical-pol,
    box-line=plain,
    box-external-color=fieldA,
    field={},
    show-momenta=false
  ]
\]
```

For grouped visual structure, use `leg-styles` for the external legs and
the per-edge line keys for the four box edges. This example colors the two left
external legs and left edge one color, the top/bottom middle edges another
color, and the right edge plus right external legs a third color:

```tex
\[
  \BoxLoopCorr[
    box-line=plain,
    show-momenta=false,
    field={},
    leg-styles={{ewboson,blue!65!black,endcap},
      {ewboson,blue!65!black,endcap},
      {ewboson,green!45!black,endcap},
      {ewboson,green!45!black,endcap}},
    box-left-line={plain,blue!65!black},
    box-top-line={plain,orange!85!black},
    box-right-line={plain,green!45!black},
    box-bottom-line={plain,orange!85!black},
    leg-labels={A_1,A_2,A_3,A_4}
  ]
\]
```

Box line controls:

- `box-external-line=...`
- `box-external-style=physical-pol`
- `box-physical-pol`
- `box-line=...`
- `box-internal-line=...`
- `box-internal-lines={left-style,top-style,right-style,bottom-style}`
- `box-left-line=...`
- `box-top-line=...`
- `box-right-line=...`
- `box-bottom-line=...`

Box color controls:

- `box-color=...`
- `box-external-color=...`
- `box-internal-color=...`

`box-color=...` colors both external and internal box propagators.
`box-external-color=...` overrides that color for the four diagonal external
legs, and `box-internal-color=...` overrides it for the four internal box
edges. These controls compose with `box-line`, `box-external-line`,
`box-internal-lines={...}`, and `leg-styles={...}`.

Box momentum labels:

- `box-left-momentum=...`
- `box-top-momentum=...`
- `box-right-momentum=...`
- `box-bottom-momentum=...`
- `box-edge-momenta={left-label,top-label,right-label,bottom-label}`
- `box-loop-momentum=...`

Use `box-edge-momenta={...}` for internal edge momentum arrows plus labels.
Use `box-edge-labels={...}` for internal side labels only, with no arrows.

Box external momentum directions use the external slot order
upper-left, lower-left, upper-right, lower-right:

- `box-upper-left-momentum-direction=in|out`
- `box-lower-left-momentum-direction=in|out`
- `box-upper-right-momentum-direction=in|out`
- `box-lower-right-momentum-direction=in|out`
- `box-external-momentum-directions={ul,ll,ur,lr}`

If a box-specific external direction is omitted, the older
`external-left-momentum-direction` and `external-right-momentum-direction`
fallbacks still apply.

Box internal edge momentum directions use edge order left, top, right, bottom:

- `box-left-momentum-direction=forward|reverse|none`
- `box-top-momentum-direction=forward|reverse|none`
- `box-right-momentum-direction=forward|reverse|none`
- `box-bottom-momentum-direction=forward|reverse|none`
- `box-edge-momentum-directions={left,top,right,bottom}`

For example, this flips the lower-left and upper-right external arrows inward,
reverses the left and right internal edge arrows, and hides the bottom edge
arrow. Internal box arrows default to the shorter range `0.32` to `0.68` so
they do not dominate the loop:

```tex
\[
  \BoxLoopCorr[
    box-external-line=plain,
    box-line=plain,
    field=A,
    leg-labels={A_1,A_2,A_3,A_4},
    box-edge-momenta={\ell_1,\ell_2,\ell_3,\ell_4},
    box-external-momentum-directions={out,in,in,out},
    box-edge-momentum-directions={reverse,forward,reverse,none},
    box-loop-momentum={}
  ]
\]
```

Label-only sides and hand-tuned arrow spans can be mixed with the same box
controls:

```tex
\[
  \BoxLoopCorr[
    box-external-line=plain,
    box-line=plain,
    field={},
    leg-labels={A_1,A_2,A_3,A_4},
    box-edge-momenta={p_L,p_T,p_R,p_B},
    box-edge-momentum-directions={forward,reverse,forward,none},
    box-left-arrow-start=0.18,
    box-left-arrow-end=0.45,
    box-top-arrow-start=0.54,
    box-top-arrow-end=0.86,
    box-right-edge-label=Z,
    box-bottom-edge-label=W,
    box-loop-momentum={}
  ]
\]
```

- `box-left-edge-label=...`
- `box-top-edge-label=...`
- `box-right-edge-label=...`
- `box-bottom-edge-label=...`
- `box-edge-labels={left-label,top-label,right-label,bottom-label}`
- `box-internal-labels={left-label,top-label,right-label,bottom-label}`

Box geometry:

- `box-xspan=...`
- `box-yspan=...`
- `box-external-xspan=...`
- `box-external-yspan=...`
- `box-central-label-yshift=...`

By default, box and cross-box diagrams use matching x/y spans so the internal
box and external envelope are square. Use the geometry keys above when a
rectangular, wider, or tighter box is wanted for a specific figure.

Box external momentum arrow placement:

- `box-external-momentum-start=...`
- `box-external-momentum-end=...`
- `box-external-momentum-label-fraction=...`
- `box-external-momentum-label-gap=...`
- `box-external-momentum-offset=...`

### Crossed upper external pair (M07b)

`\BoxLoopCorr[box-external-crossing=top,...]` (or
`\FourPointCorr[topology=box,...]`) preserves the square loop and crosses its
upper external pair. Default `box-external-crossing=none` preserves existing
output. The current choices are `none` and `top`; right-pair routing is still
R04. Nonempty routing on a different host raises a package error.

| Logical slot | Outer endpoint | Normal host | Top-crossed host |
| --- | --- | --- | --- |
| 1 | upper left | TL | TR |
| 2 | lower left | BL | BL |
| 3 | upper right | TR | TL |
| 4 | lower right | BR | BR |

Internal slots 5-8 remain left/top/right/bottom. Slot 1 has a crossing gap;
slot 3 stays continuous. `box-external-crossing-gap=.04` is its default
half-width as a fraction of the full logical leg. The crossing fraction is
derived from actual spans, not assumed to be 0.5. Positive inner/outer x spans,
an outer top above the loop, and a positive gap wholly inside the leg are
required. A crossing is not an interaction. Caps, indices and markers attach
to full logical endpoints; a split leg has only one species circle and preserves
its line-local `circ scale`, color and position.

Upper momentum guides default near fraction .23 from the outer endpoint with
compact spans and measured label gaps; slots 1/2 enter and 3/4 leave. Lower
legacy guides retain their existing defaults. Optional
`box-external-momentum-1={...}` through `-4={...}` independently control
`layout=gap|side`, `start`, `end`, `offset`, `label-fraction`, `label-gap`,
`label-offset`, `label-anchor`, `label-xshift`, `label-yshift`, `label`,
`direction=forward|reverse|none` and `side=outside|inside|left|right`.
`forward` follows outer-to-loop orientation. These blocks override global
box placement/direction keys regardless of key order. Explicit old global
start/end/fraction/gap controls are respected; the visibility mask and
`show-momenta=false` remain authoritative. Blocks may also opt ordinary box
legs into the measured annotation renderer. Options reset per public call.

```tex
\BoxLoopCorr[
  field={},central={},leg-labels={,,,},show-momenta=false,
  box-line=plain,box-external-line=plain,
  box-external-crossing=top
]
```

See [the focused gallery](../regressions/topologies/box/box-external-crossing.pdf)
and atlas P21-P24. D01 index-position polish is deferred. D02 now fixes
**internal** crossed-box circles: bare Proca adds none, and explicit circles
retain line-local scaling/color/label style. See the
[before/after comparison](../regressions/topologies/cross-box/cross-box-circle-comparison.pdf).

Box propagator index slots use the same numbering as the propagators:
external slots 1--4, then internal left/top/right/bottom slots 5--8.

- `box-propagator-left-indices={...}`
- `box-propagator-right-indices={...}`
- `box-index-left-position=...`
- `box-index-right-position=...`
- `box-index-left-xshift=...`
- `box-index-left-yshift=...`
- `box-index-right-xshift=...`
- `box-index-right-yshift=...`
- `box-index-style=...`
- `box-index-fill=...`
- `box-index-inner-sep=...`
- `box-index-size=normal|script|scriptscript`

Box edge arrow placement follows the same predictable pattern for each edge:

- `box-left-arrow-start=...`
- `box-left-arrow-end=...`
- `box-left-arrow-xshift=...`
- `box-left-arrow-yshift=...`
- `box-left-label-position=...`
- `box-left-label-distance=...`
- `box-left-label-xshift=...`
- `box-left-label-yshift=...`
- `box-left-label-fraction=...`

Replace `left` with `top`, `right`, or `bottom` for the other edges.
The default internal edge arrow range is `start=0.32,end=0.68`.

Central loop arrow controls:

- `box-loop-arrow-radius=...`
- `box-loop-arrow-start-angle=...`
- `box-loop-arrow-end-angle=...`
- `box-loop-label-angle=...`
- `box-loop-label-distance=...`
- `box-loop-label-position=...`
- `box-loop-label-xshift=...`
- `box-loop-label-yshift=...`

## Cross-Box Topology

The public crossed-box entry points are:

```tex
\CrossBoxCorr[...]
\FourPointCorr[topology=cross-box,...]
```

The default crossed box uses the same external slot order and geometry controls
as `\BoxLoopCorr`, and draws the two side internal box-edge segments plus the
two crossed diagonals between the four corner vertices. The upper-left to
lower-right diagonal is broken slightly at the crossing so the crossing reads
as over/under routing, not as a central vertex.

Useful controls:

- `box-xspan=...`
- `box-yspan=...`
- `box-external-xspan=...`
- `box-external-yspan=...`
- `box-external-line=...`
- `box-line=...`
- `box-left-line=...`
- `box-top-line=...`
- `box-right-line=...`
- `box-bottom-line=...`
- `cross-box-down-line=...`
- `cross-box-up-line=...`
- `cross-box-diagonal-lines={down-style,up-style}`
- `cross-box-crossing-gap=...`
- `cross-box-left-circ=...`
- `cross-box-right-circ=...`
- `cross-box-up-circ=...`
- `cross-box-down-circ=...`
- `cross-box-left-circ-position=...`
- `cross-box-right-circ-position=...`
- `cross-box-up-circ-position=...`
- `cross-box-down-circ-position=...`

`box-color`, `box-external-color`, and `box-internal-color` work for the
crossed-box helper too. The default has no circ markers; add them explicitly
with the `cross-box-*-circ` keys when needed. These place topology-level circ
markers independently of the line drawing, so the split diagonal can keep its
over/under crossing gap while its marker sits safely away from the crossing.
By default, side markers sit halfway along their side edges, the lower-left to
upper-right diagonal marker sits before the crossing, and the upper-left to
lower-right diagonal marker sits after it.

The usual box edge line keys are also accepted for screenshot-style EW-boson
circ edge controls: `box-left-line` and `box-right-line` style the side edges,
while `box-top-line` falls back to the lower-left to upper-right diagonal and
`box-bottom-line` falls back to the split upper-left to lower-right diagonal
when the explicit `cross-box-up-line` or `cross-box-down-line` keys are not
set.

```tex
\[
  \CrossBoxCorr[
    field={},
    show-momenta=false,
    box-line=plain,
    box-left-line={ewboson,circ=Z},
    box-top-line={ewboson,circ=W},
    box-right-line={ewboson,circ=A},
    box-bottom-line={ewboson,circ=W},
    central={}
  ]
\]
```

When `cross-box-up-line={proca,circ={}}` or
`cross-box-down-line={proca,circ={}}` is used, the blank circ is promoted to
the same topology-level placement automatically. This also works inside
comma-composed styles such as `{proca,fieldA,circ={}}`. An explicit
`cross-box-up-circ=...` or `cross-box-down-circ=...` label overrides the
explicit line-circle label.

Focused visual QA lives in
`regressions/topologies/cross-box/cross-box-regression.tex`.

M07a adds `cross-box-layout=top-bottom`, retaining `left-right` as the default.
The square 1.34/1.34 inner half-spans, shared outer frame and external slots
are unchanged. Existing explicit dimension overrides remain available.

| Logical slot | `left-right` | `top-bottom` |
| --- | --- | --- |
| 1 / 2 / 3 / 4 | external UL / LL / UR / LR to the corresponding corner | same |
| 5 | BL to TL: fixed left | TL to TR: fixed top |
| 6 | TR to BR: fixed right | BL to BR: fixed bottom |
| 7 | TL to BR: split descending diagonal | same |
| 8 | BL to TR: continuous ascending diagonal | same |

The center crossing is unconnected. The two split strokes belong to slot 7;
its markers and endpoint indices attach to TL/BR, not to the gap endpoints.
Use `cross-box-crossing-gap` between 0 and 0.5 for a visible valid gap. Its
value is the half-width as a fraction of the full diagonal.

`cross-box-line-5` through `cross-box-line-8` override individual internal
slots, independently of key order. Without a slot override, the fixed edges
use `box-left-line` / `box-right-line` in the default layout, or
`box-top-line` / `box-bottom-line` in the complementary layout. Explicit
`cross-box-up-line` / `cross-box-down-line` still style the diagonals. Their
fallback keys are `box-top-line` / `box-bottom-line` in the default layout,
or `box-left-line` / `box-right-line` in the complementary layout. Empty
edge-specific styles fall back to `box-line`. Existing box color controls
retain their precedence.

`cross-box-first-circ` / `cross-box-second-circ` and their `-position` keys
name the fixed slots 5/6 in either layout. The legacy `cross-box-left-circ` /
`cross-box-right-circ` keys remain aliases for those fixed slots. Up/down
circle keys retain their diagonal meaning. `cross-box-circs=false` hides
all topology-level circles. Default `true` displays circles only when requested
with `circ=...` or a topology circle key. D02 removes the old unsolicited empty
Proca circles; use `circ={}` to request an empty ring explicitly. Per-line
`circ scale`, `circ size`, `circ fill`, `circ draw` and `circ label style` are
retained by the manual placement pass, including split diagonals and overrides
for slots 5-8. Existing topology `-circ-position` keys still control placement.
See the [circle gallery](../regressions/topologies/cross-box/cross-box-circles.pdf).
Bare scalar-polarization
aliases now use semantic tips on the full logical edge, so the split path
cannot create a false marker near its crossing gap.

Internal crossed-box momentum is opt-in:

```tex
\CrossBoxCorr[
  cross-box-layout=top-bottom,
  field={},central={},leg-labels={,,,},
  box-line=plain,box-external-line=plain,
  show-momenta=true,
  cross-box-momenta={k_5,k_6,k_7,k_8},
  cross-box-momentum-7={layout=side,direction=reverse}
]
```

`cross-box-momenta` follows slots 5/6/7/8; blank entries hide the corresponding
internal annotation. It defaults empty to preserve existing diagrams.
`cross-box-momentum-5` through `cross-box-momentum-8` accept independent
`layout=gap|side`, `label`, `direction=forward|reverse|none`, `start`, `end`,
`offset`, `label-fraction`, `label-gap`, `label-offset`, `label-xshift`,
`label-yshift`, `label-anchor`, and `side=outside|inside|left|right`. Gap mode
fits the break to the actual label; side mode leaves the arrow continuous.
An explicit block with `label={}` can draw an unlabeled arrow; `direction=none`
hides it. `show-momenta=false` hides all these guides. Existing external
momentum controls retain p1/p2 incoming and p3/p4 outgoing defaults.

Fixed-edge annotations default to the outside. Diagonal guides sit near their
upper endpoints to clear the crossing; their normals are selected separately
for each layout to avoid the fixed edges. Reversing a direction keeps its
label on the same side. Ordinary box-edge momentum keys and the ordinary
box loop arrow are separate controls; use the crossed-box slot keys here.

`box-propagator-left-indices` / `box-propagator-right-indices` now follow the
crossed-box slot table above, including all eight slots and both endpoints.
The existing `box-index-*` controls apply. This verifies ownership and values;
D01 index-position appearance remains a separate later review.

See [M07a verification](planning/m07a-verification.md) and the
[four-page gallery](../regressions/topologies/cross-box/cross-box-layouts.pdf).
External crossed-leg routing is the separate M07b slice.


## Triangle-Contact Topology

The public triangle-contact entry points are:

```tex
\TriangleContactCorr[...]
\FourPointCorr[topology=triangle-contact,...]
```

This helper draws a triangular loop with two trivalent vertices and one
quartic/contact vertex. The contact vertex orientation is controlled by:

- `triangle-contact-orientation=bottom`
- `triangle-contact-orientation=top`
- `triangle-contact-orientation=left`
- `triangle-contact-orientation=right`

The default is `bottom`. External slots remain fixed as upper left, lower left,
upper right, and lower right while the contact vertex moves.

M07c verifies that these four orientations attach adjacent external pairs at
the quartic vertex: bottom 2/4, top 1/3, left 1/2, right 3/4. Opposite pairs
1/4 and 2/3 in S13-left/right require a missing external-routing extension.
The loop family, Z-edge styles and square bounding spans already exist;
relabeling outer text does not implement the fixed-slot attachments. See the
[illustrated audit](planning/m07c/routing-audit.pdf) and
[current working recipes](planning/m07c/recipes.md). Proposed future orientation
names in the audit plan are not accepted API.


Useful controls:

- `triangle-contact-xspan=...`
- `triangle-contact-yspan=...`
- `triangle-contact-external-xspan=...`
- `triangle-contact-external-yspan=...`
- `triangle-contact-line=...`
- `triangle-contact-external-line=...`
- `triangle-contact-internal-line=...`
- `triangle-contact-internal-lines={edge5-style,edge6-style,edge7-style}`
- `triangle-contact-color=...`
- `triangle-contact-external-color=...`
- `triangle-contact-internal-color=...`
- `momentum-directions={ul,ll,ur,lr}`
- `triangle-contact-momentum-directions={ul,ll,ur,lr}`
- `triangle-contact-momentum-slots={1,2,3,4}`
- `triangle-contact-momentum-start=...`, `triangle-contact-momentum-end=...`
- `triangle-contact-momentum-offset=...`
- `triangle-contact-momentum-label-fraction=...`, `triangle-contact-momentum-label-gap=...`
- `triangle-contact-central-label-yshift=...`

Internal triangle momentum labels are opt-in. Slots 5--7 use the same edge
order as `triangle-contact-internal-lines={...}`:

- `triangle-contact-internal-momenta={edge5,edge6,edge7}`
- `triangle-contact-internal-momentum-directions={forward,reverse,none}`
- `triangle-contact-internal-momentum-slots={5,6,7}`
- `triangle-contact-internal-momentum-start=...`
- `triangle-contact-internal-momentum-end=...`
- `triangle-contact-internal-momentum-offset=...`
- `triangle-contact-internal-momentum-label-fraction=...`
- `triangle-contact-internal-momentum-label-gap=...`

Each of the seven momentum annotations can be positioned independently:

```tex
\TriangleContactCorr[
  field={},central={},leg-labels={,,,},line=plain,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-momentum-2={offset=16pt},
  triangle-contact-momentum-6={layout=side,label-fraction=0.43,label-offset=4pt,
    label-xshift=-2pt,label-anchor=south}
]
```

The keys `triangle-contact-momentum-1` through `triangle-contact-momentum-7`
accept the following fields. Their `trianglecontact-momentum-N` aliases work
the same way. These controls use the existing slots, not a new ordering.

| Field | Meaning |
| --- | --- |
| `layout` | `gap` (default): label inside a break; `side`: one continuous arrow with the label alongside. |
| `start`, `end` | Arrow endpoints as fractions of the directed propagator, normally `0 <= start < end <= 1`; `auto` selects defaults. |
| `offset` | Perpendicular distance from propagator to arrow, in TeX units. |
| `label-fraction` | Label location along the same directed propagator, independent of arrow range. |
| `label-gap` | `auto` (default) fits the rendered label plus small padding. A numeric value overrides the half-gap as an edge fraction. |
| `label-offset` | Extra perpendicular label distance; `auto` gives `0pt` in gap mode and `3pt` in side mode. |
| `label-xshift`, `label-yshift` | Move only the label in the diagram's x/y frame; default `0pt`. |
| `label-anchor` | TikZ anchor; `auto` centers gap labels and anchors side labels on the boundary nearest the arrow. |
| `side` | `outside` (default), `inside`, `left`, or `right`; left/right are relative to the directed edge. |

Choose the layout for all seven annotations with
`triangle-contact-momentum-layout=gap|side` (alias
`trianglecontact-momentum-layout`). An individual slot's `layout` overrides it:

```tex
\TriangleContactCorr[
  field={},central={},leg-labels={,,,},line=plain,
  momentum-labels={p_1,p_2,p_3,p_4},
  triangle-contact-internal-momenta={k_5,k_6,k_7},
  triangle-contact-momentum-layout=side,
  triangle-contact-momentum-5={layout=gap}
]
```

Outside-facing sides use the actual triangle centroid in all four orientations.
In side mode, labels sit above top edges, below bottom edges, and outward from
sloping/vertical edges. Arrow reversal keeps the same side and label placement.
In gap mode, labels default to the arrow line; automatic gaps measure the actual
rendered node, including font/style and scale, with 0.8pt padding per side.
Manual shifts/anchors move the label without moving the arrow endpoints. The
break follows its actual along-edge position; if the label moves completely
off the arrow line, the arrow is drawn continuously rather than leaving an
empty gap. Prefer explicit `layout=side` for labels placed beside arrows.

Unspecified per-slot fields inherit the external/internal grouped settings;
per-slot fields win regardless of key order. Repeated blocks replace earlier
blocks for the same slot. All overrides reset between diagrams. Existing numeric
ranges/fractions/gaps still work and apply to every selected slot.

The reviewed `auto` external ranges are compact: at most 24pt in diagram units,
shortened to stay on the leg. The default label/range center is fraction `0.30`
on the two legs meeting the quartic vertex, closer to their outer endpoints;
it is `0.50` on the other two. This follows the contact orientation rather than
hard-coding lower legs. Explicit label fractions do not move arrow endpoints.
Internal auto ranges remain `0.30..0.72`, `0.25..0.75`, `0.28..0.70` for slots
5/6/7. All default label gaps now use size-aware `auto`, rather than the old
fixed edge fractions. Use dimensions for offsets and unitless fractions for
explicit ranges/gaps. Very long labels or unusually short legs can still need
manual ranges, a smaller momentum font, or side mode.

External slots run from the outer endpoint to the interaction vertex. Internal
edge endpoint order is:

| Contact orientation | Slot 5 | Slot 6 | Slot 7 |
| --- | --- | --- | --- |
| bottom | A to B | A to contact | contact to B |
| top / left | contact to A | A to B | B to contact |
| right | A to B | B to contact | contact to A |

For bottom/top, A/B are the left/right trivalent vertices. For left/right,
A/B are the upper/lower trivalent vertices. The four external slots remain
upper-left, lower-left, upper-right, lower-right. Directions, momentum visibility,
styles, and indices keep their existing interfaces. Blank external labels
keep a continuous unlabeled arrow; blank internal labels omit the annotation.
Internal directions now default to `{auto,auto,auto}`: both edges touching
the quartic vertex point toward their trivalent endpoint in every orientation.
The edge between the two trivalent vertices keeps its forward direction.
In bottom/right layouts this resolves to `{forward,reverse,forward}`; in
top/left layouts it resolves to `{forward,forward,reverse}`. Explicit `forward`,
`reverse`, and `none` entries still override defaults; `auto` inherits the
orientation-aware default for that slot. Blank/missing list entries retain
the legacy `forward` fallback. Directions do not move labels or change gaps.
See `regressions/topologies/triangle-contact/triangle-contact-annotations.tex`
and its PDF for the five-page gallery and automated geometry/isolation checks.

Triangle-contact propagator index slots use external slots 1--4 and internal
triangle-edge slots 5--7:

- `triangle-contact-propagator-left-indices={...}`
- `triangle-contact-propagator-right-indices={...}`
- `triangle-contact-index-left-position=...`
- `triangle-contact-index-right-position=...`
- `triangle-contact-index-left-xshift=...`
- `triangle-contact-index-left-yshift=...`
- `triangle-contact-index-right-xshift=...`
- `triangle-contact-index-right-yshift=...`
- `triangle-contact-index-style=...`
- `triangle-contact-index-fill=...`
- `triangle-contact-index-inner-sep=...`
- `triangle-contact-index-size=normal|script|scriptscript`

`triangle-contact-color=...` colors all triangle-contact propagators.
`triangle-contact-external-color=...` overrides the color for the four external
legs, and `triangle-contact-internal-color=...` overrides the color for the
three internal triangle edges. The global `color=...` key still works, and the
more specific triangle-contact color keys take precedence when both are set.

The `trianglecontact-*` spellings are also accepted as aliases.

Use `triangle-contact-internal-lines={...}` when the three internal
triangle-contact edges need independent propagator styles. Each item accepts
the same composed style syntax as ordinary propagators:

```tex
\[
  \TriangleContactCorr[
    field={},
    show-momenta=false,
    triangle-contact-internal-lines={{ewboson,circ=Z},
      {ewboson,circ=W},{ewboson,circ=A}},
    central={}
  ]
\]
```

Focused visual QA lives in
`regressions/topologies/triangle-contact/triangle-contact-regression.tex`.

## Vertex Identity Prototype Topologies

The vertex-identity derivation helpers are:

```tex
\HalfBoxCorr[...]
\FourPointCorr[topology=half-box,...]
\FlatContactCorr[...]
\FourPointCorr[topology=flat-contact,...]
```

The shared slot order is:

- slot 1 = left top
- slot 2 = left down
- slot 3 = right down
- slot 4 = right top

`\HalfBoxCorr` draws a continuous top EW-boson line through two triple
vertices, with two downward legs. `\FlatContactCorr` draws a flat-top
quartic/contact piece with one central vertex. Both default to `ewboson` but
still accept `leg-styles={...}`, `leg-labels={...}`, `momentum-labels={...}`,
`show-momenta=false`, and the usual color and vertex controls.

Half-box geometry and style controls:

- `half-box-xspan=...`
- `half-box-top-stub=...`
- `half-box-top-yspan=...`
- `half-box-mode=straight|angled|halfpropleft|halfpropright`
- `half-box-style=straight|halfpropagator|halfpropleft|halfpropright`
- `half-box-down-span=...`
- `half-box-down-xoffset=...`
- `half-box-line=...`
- `half-box-colors={slot-1,slot-2,slot-3,slot-4}`
- `half-box-bridge-line=...`
- `half-box-bridge-color=...`
- `half-box-bridge-label=...`
- `half-box-bridge-label-position=above|below|<anchor>`
- `half-box-bridge-label-xshift=...`
- `half-box-bridge-label-yshift=...`
- `half-box-bridge-momentum=...`
- `half-box-bridge-momentum-direction=forward|reverse|none`
- `half-box-bridge-momentum-start=...`
- `half-box-bridge-momentum-end=...`
- `half-box-bridge-momentum-offset=...`
- `half-box-bridge-momentum-label-fraction=...`
- `half-box-bridge-momentum-label-gap=...`
- `half-box-momentum-start=...`
- `half-box-momentum-end=...`
- `half-box-momentum-offset=...`
- `half-box-momentum-label-fraction=...`
- `half-box-momentum-label-gap=...`
- `half-box-momentum-slots={1,2,3,4}`
- `half-box-propagator-left-indices={...}`
- `half-box-propagator-right-indices={...}`
- `half-box-left-lower-circ=...`
- `half-box-right-lower-circ=...`
- `half-box-lower-circ-position=...`

The default `straight` half-box geometry is unchanged. Use
`half-box-style=halfpropleft` for an angled top-stub half-box whose lower-left
leg is an EW-boson half-propagator with a circ marker and whose lower-right leg
defaults to `spol`. Use `half-box-style=halfpropright` for the mirrored case.
Both styles add endcaps to the top external stubs. The circ labels default to
`Z`; override them with `half-box-left-lower-circ=...` or
`half-box-right-lower-circ=...`. `half-box-style=halfpropagator` is the shared
angled/endcap geometry without choosing which lower leg becomes scalar
polarized.

`half-box-line=...` sets the default line style for the half-box external
segments and bridge. Use `half-box-bridge-line=...` when only the middle bridge
should change, for example `half-box-bridge-line={proca,circ={}}`.

Bridge momentum is opt-in and uses bridge slot 5 for arrow sizing:

```tex
\HalfBoxCorr[
  momentum-labels={,p_1,q_1,},
  half-box-momentum-slots={2,3},
  half-box-bridge-label=Z,
  half-box-bridge-momentum=\ell
]
```

Flat-contact geometry and style controls:

- `flat-contact-xspan=...`
- `flat-contact-yspan=...`
- `flat-contact-line=...`
- `flat-contact-colors={slot-1,slot-2,slot-3,slot-4}`
- `flat-contact-momentum-start=...`
- `flat-contact-momentum-end=...`
- `flat-contact-momentum-offset=...`
- `flat-contact-momentum-label-fraction=...`
- `flat-contact-momentum-label-gap=...`
- `flat-contact-momentum-slots={1,2,3,4}`
- `flat-contact-propagator-left-indices={...}`
- `flat-contact-propagator-right-indices={...}`

The `halfbox-*` and `flatcontact-*` spellings are also accepted as aliases.
The momentum slot filters let a diagram show only selected external momentum
arrows, for example `half-box-momentum-slots={2,3}` for the two lower legs.
Half-box index slot 5 is the bridge; flat-contact index slots are the four
external paths. Both topologies also accept `*-index-left-position`,
`*-index-right-position`, matching x/y shift keys, `*-index-style`,
`*-index-fill`, `*-index-inner-sep`, and `*-index-size`.

Inside package-managed topologies, `scalarpolarized`/`spol`, `proca`,
`arrowin`/`arrowout`, and `openarrowin`/`openarrowout` are endpoint-aware:
marker-bearing styles are stripped from the raw propagator body and redrawn
after the vertices so triangle tips kiss the vertex edge instead of being
covered by the dot. The clearance is controlled by
`semantic-marker-tip-clearance=...`; custom dot sizes can use
`semantic-marker-vertex-radius=...`. For cropped external legs, use
`endcapout` to put a terminal bar exactly at the external endpoint of the leg.
The explicit aliases such as `spolin`/`spolout` remain available for manual
control.

Focused visual QA lives in
`regressions/topologies/vertex-identity/vertex-identity-check.tex`.

## Self-Energy Bubble

The standalone two-point self-energy bubble entry points are:

```tex
\BubbleCorr[...]
\SelfEnergyCorr[...]
\SelfEnergyBubbleCorr[...]
```

Minimal scalar bubble:

```tex
\[
  \BubbleCorr[]
\]
```

With loop momenta, two endpoint indices per internal propagator, and
vertex-side external indices:

```tex
\[
  \BubbleCorr[
    show-momenta=true,
    momentum-labels={p,p},
    bubble-momenta={\ell,p-\ell},
    bubble-a-indices={a,b},
    bubble-b-indices={c,d},
    bubble-external-indices={i,j}
  ]
\]
```

Outer field labels are opt-in:

```tex
\[
  \BubbleCorr[
    field=\phi,
    indices={i,j}
  ]
\]
```

Useful controls:

- `bubble-vertex-span=...`
- `bubble-external-length=...`
- `bubble-loop-looseness=...`
- `bubble-external-line=...`
- `bubble-a-line=...` / `bubble-top-line=...`
- `bubble-b-line=...` / `bubble-bottom-line=...`
- `bubble-vertex-radius=...`
- `bubble-endpoint-marker-distance=...`
- `momentum-directions={left,right}`
- `bubble-momenta={top,bottom}`
- `bubble-a-momentum-direction=forward|reverse|none`
- `bubble-b-momentum-direction=forward|reverse|none`
- `bubble-momentum-rotation=clockwise|counterclockwise`
- `bubble-momentum-layout=manual|vertex-split`
- `bubble-vertex-split-left={start,end,label-fraction}`
- `bubble-vertex-split-right={start,end,label-fraction}`
- `bubble-vertex-split-left-start=...`
- `bubble-vertex-split-left-end=...`
- `bubble-vertex-split-left-label-fraction=...`
- matching `bubble-vertex-split-right-*` keys
- `bubble-vertex-split-offset-scale=...`
- `bubble-momentum-start=...`
- `bubble-momentum-end=...`
- `bubble-momentum-offset=...`
- `bubble-momentum-style-clearance=...`
- `bubble-momentum-label-distance=...`
- `bubble-momentum-label-fraction=...`
- `bubble-external-momentum-start=...`
- `bubble-external-momentum-end=...`
- `bubble-external-momentum-label-fraction=...`
- `bubble-external-momentum-label-gap=...`
- `bubble-endpoint-indices={aL,aR,bL,bR}`
- `bubble-a-index-fractions={left,right}`
- `bubble-b-index-fractions={left,right}`
- `bubble-a-left-index-fraction=...`
- `bubble-a-left-index-position=...`
- `bubble-a-left-index-xshift=...`
- `bubble-a-left-index-yshift=...`
- matching `bubble-a-right-index-*`, `bubble-b-left-index-*`, and
  `bubble-b-right-index-*` keys
- `bubble-a-index-yshift=...`
- `bubble-b-index-yshift=...`
- `bubble-endpoint-index-yshift=...`
- `bubble-external-indices={left,right}`
- `bubble-left-external-index=...`
- `bubble-right-external-index=...`
- `bubble-external-index-position=...`
- `bubble-external-index-yshift=...`
- `bubble-external-index-size=normal|script|scriptscript`

The default external legs are horizontal amputated scalar-style stubs with
endpoint caps. Set their style with `bubble-external-line=...`. The internal
propagators default to solid/plain lines; set the upper and lower slots with
`bubble-a-line` / `bubble-top-line` and `bubble-b-line` /
`bubble-bottom-line`. Bubble internal scalar-polarized and Proca endpoint
markers are drawn as white-filled equilateral triangles against explicit tip
coordinates on the vertex boundary.
With `bubble-endpoint-marker-distance=auto`, the target point is the
`bubble-vertex-radius` edge plus `semantic-marker-tip-clearance`; set an
explicit distance only when you want the tip target moved inward or outward.
Loop momentum arrows are opt-in through
`bubble-momenta` or the per-slot momentum keys. Internal momentum arrows use
`bubble-momentum-offset` (default `8pt`, reduced from `12pt`), and add
`bubble-momentum-style-clearance` automatically when the corresponding internal
line is structurally wider, such as `ewboson`, `photon`, `proca`, or `circ=...`.
The existing style clearance defaults to `2pt`, so standard wide-style arrows
sit at a total offset of `10pt`. Explicit offset/clearance values still win.
Loop labels sit outward from their actual arc: above upper arrows, below lower
arrows, or left/right for near-vertical placements. This is independent of local
a/b identity and arrow direction, including right-hand tree insertions where
a/b exchange their page-top/page-bottom roles. `bubble-momentum-label-distance`
still controls the gap from the arrow to its label (default `2pt`).
`momentum-labels={...,...}` labels the two external momentum arrows. The bare
bubble is quiet by default, while explicit `field=...`, `indices={...}`, or
`leg-labels={...}` restores ordinary outer field labels.

Focused visual QA lives in
`regressions/topologies/bubble/bubble-regression.tex`.

## Shared outer frame for four-leg diagrams

Ordinary contact pairings, s/t/u trees and channel bubbles, supported tree
insertions/corrections, box, crossed box and all triangle-contact orientations
use outer corners at **x,y = +/-2.10** by default. The square box loop remains
1.34 in each inner half-span; this change concerns outer endpoints.

`fourpoint-xspan` and `fourpoint-yspan` set the common frame for these families.
Box/crossed box inherit it through their external-span defaults; triangle-contact
inherits it in the same way. An explicit `box-external-xspan/yspan` or
`triangle-contact-external-xspan/yspan` overrides the corresponding shared axis
for that diagram, independent of option order. The next call restores defaults.
Previous endpoint frames can still be requested explicitly. Half-box and flat
contact identity stubs retain their specialized layouts.

The new defaults intentionally supersede older tree (1.95/1.35) and
triangle-contact (1.72/1.55) outer spans. Box/crossed-box defaults already used
2.10/2.10. Shared-frame recipes and plain comparison examples are on atlas pages
22-23. See [frame verification](planning/four-leg-frame-verification.md).

## Semantic Insertions

Semantic insertions attach a package-owned object to a logical propagator slot.
The user chooses what and where; the topology owns the geometry.

Current semantic insertion hosts:

```tex
\[
  \TTreeChannelCorr[
    insertion=bubble, % or seagull or swordfish
    insertion-slot=1
  ]
\]
```

Contact external self-energy bubbles also use the existing semantic interface:

```tex
\FourPointCorr[
  field={},central={},leg-labels={,,,},blob=false,
  line=plain,show-momenta=false,
  insertion=bubble,insertion-slot=1
]
```

Slots are physical corners: 1 upper left, 2 lower left, 3 upper right,
4 lower right. `FourPtCorr` is an alias. The central quartic vertex survives;
the selected leg becomes outer--A, two parallel A--B arcs, B--contact. This
has seven propagators, two cubic insertion vertices and one quartic host.
`contact-pairing=central` (default) and `crossed` use this same insertion graph.
Horizontal/vertical pairings have no quartic host and are rejected for contact
bubbles, as are slots outside 1-4 or lists of simultaneous slots. Their ordinary
no-insertion behavior is unchanged. Contact seagulls now use the same slots with `insertion=seagull` (M08b).

Contact bubbles default to `insertion-position=0.50`, `insertion-scale=0.50`.
Position is the outer-to-contact fraction. Both insertion vertices must fit
strictly inside the selected leg; nonpositive scale/base span or a bubble that
does not fit produces a package error. The shared +/-2.10 outer frame and
package coordinate scale are unchanged; explicit `fourpoint-xspan/yspan` work.
`external-legs=false` hides the insertion, retaining existing amputated endpoint
placeholders. `center-vertex=false` hides all three interaction dots.

Pre/post line overrides, logical external caps, both bubble arc styles and
bubble endpoint/external/post indices use the existing helpers below. No new
index appearance tuning is included. `show-momenta=false` suppresses all guides;
`external-momentum-hide={slot}` hides both selected pre/post guides. The default
p1/p2 flow is incoming and p3/p4 outgoing; global left/right directions and
`contact-momentum-directions={ul,ll,ur,lr}` apply, including both selected
segments. Loop labels face outward along the actual normal; blank loop labels
hide their guide. Existing `bubble-*-momentum-*` and pre/post momentum controls
remain independent. There is no exchange edge or channel momentum on this host.
See the [five-page gallery](../regressions/topologies/insertion/contact-bubble-slots.pdf),
[copyable atlas recipes](diagram-inventory/recipes.md#self-energy-bubble-on-a-quartic-contact-leg)
and [verification](planning/m08a-verification.md).

Contact-leg seagulls can be used inside `array`, `tabular` and `aligned` layouts.
The alignment validation repair is described in the [fix record](planning/m08b-array-fix.md).

Contact-leg seagulls retain the quartic contact and attach a direct self-loop
at one new quartic vertex V: outer--V, V--contact and V--V replace the selected
leg. There are **six edges and two quartic interactions**, with no stem and no
pair of split bubble vertices. Use the same minimal recipe above with
`insertion=seagull,seagull-loop-line=plain`.

Central/crossed quartic views support slots 1 UL, 2 LL, 3 UR, 4 LR. Default
position is .40 and scale .66; loop size/looseness remain 1.55/1.0. The contact
seagull's `auto` side matches slide 11: upper loops up, lower loops down
(+90 from outer-to-host on slots 1/4, -90 on 2/3). Explicit `top`/`bottom`
remain host-relative +90/-90; `left`/`right` remain page-relative. Tree seagull
and bubble defaults are unchanged. Position must lie strictly between 0 and 1;
scale, loop size and looseness must be positive and the host leg nonzero.
Invalid slots/pairings/geometry fail explicitly.

External logical styles/caps, contact direction controls, pre/post momentum
controls, loop orientation/direction/clearance and all four
`seagull-vertex-indices` work as below. `insertion-post-indices` also attaches
to the contact-seagull V--contact segment. Hidden external legs suppress the
insertion and preserve existing amputated placeholders; hidden center vertices
hide both interaction dots. Index appearance remains D01.

The [seven-page gallery](../regressions/topologies/insertion/contact-seagull-slots.pdf)
shows all eight S11 species variants and named pink scalar-polarization samples.
Neutral Z uses EW with an explicit Z circle; directed W uses raw
`with arrow=0.5` plus an explicit W circle at fraction .25 to separate it from
the arrow at .5. External charge arrows are independent of momentum flow;
the gallery hides momentum guides on those source variants. Raw arrow+circ
coincident overpaint predates M08b and is recorded as
[D04](planning/deferred-workflows.md#d04---coincident-raw-charge-arrowcircle-decorations).
The preferred pink samples use `proca` for two scalar-polarization endpoint
arrows, without a loop circle; the k guide follows the actual concentric loop.
See [M08b verification](planning/m08b-verification.md).

Supported insertion keys:

- `insertion=none|bubble|seagull|swordfish|triangle`
- `insertion-slot=1|2|3|4|5`
- `insertion-position=...`
- `insertion-orientation=auto|top|bottom|left|right`
- `insertion-scale=...`
- `swordfish-opening-angle=...` (swordfish only; default 60 degrees)
- `insertion-style=...`
- `insertion-pre-line=...` / `insertion-outer-line=...`
- `insertion-post-line=...` / `insertion-inner-line=...`
- `insertion-post-indices={bubble-side,vertex-side}`
- `insertion-pre-momentum-start=...`
- `insertion-pre-momentum-end=...`
- `insertion-pre-momentum-label-fraction=...`
- `insertion-pre-momentum-guide-extension=...` / `insertion-outer-momentum-guide-extension=...`
- `insertion-pre-momentum-offset=...`
- `insertion-pre-momentum-label-position=...`
- `insertion-pre-momentum-label-distance=...`
- `insertion-pre-momentum-label-xshift=...`
- `insertion-pre-momentum-label-yshift=...`
- `insertion-post-momentum-start=...`
- `insertion-post-momentum-end=...`
- `insertion-post-momentum-label-fraction=...`
- `insertion-post-momentum-offset=...`
- `insertion-post-momentum-label-position=...`
- `insertion-post-momentum-label-distance=...`
- `insertion-post-momentum-label-xshift=...`
- `insertion-post-momentum-label-yshift=...`
- `insertion-middle-momentum-xshift=...`
- `insertion-middle-momentum-start-yshift=...`
- `insertion-middle-momentum-end-yshift=...`
- `insertion-middle-momentum-label-position=...`
- `insertion-middle-momentum-label-distance=...`
- `insertion-middle-momentum-label-xshift=...`
- `insertion-middle-momentum-label-yshift=...`
- `seagull-loop-line=...`
- `seagull-loop-size=...`
- `seagull-loop-looseness=...`
- `seagull-loop-momentum=...`
- `seagull-loop-momentum-direction=clockwise|counterclockwise|none`
- `seagull-loop-momentum-start=...`
- `seagull-loop-momentum-end=...`
- `seagull-loop-momentum-offset=...`
- `seagull-loop-momentum-label-fraction=...`
- `seagull-loop-momentum-label-distance=...`
- `seagull-loop-momentum-looseness=...`
- `seagull-loop-marker-distance=auto|...`
- `seagull-vertex-indices={host-left,host-right,loop-left,loop-right}`

For external S/T bubble, seagull and swordfish insertions, and external contact insertions,
`insertion-pre-line=...` changes the outer segment's appearance while retaining
single/double caps from the logical external leg. For example,
`line={ewboson,endcapp},insertion-pre-line=ewboson` keeps all four outer double
caps. Only cap metadata is inherited; field circles and polarization styles
are not added to the override. If the segment explicitly supplies a cap,
that segment's cap settings take precedence. To remove a cap, omit it from
the logical leg style. Post segments and loop arcs stay independent of the
external cap. See [verification](planning/insertion-endcaps-verification.md).

Ordinary S-tree diagrams, including external bubble, seagull and swordfish
variants, default to `channel-vertex-xspan=1.05`, giving the central exchange
length 2.10 coordinate units. S regular-triangle corrections retain their
0.78 half-span and existing bridge geometry. The shared outer corners remain
+/-2.10, and the compact coordinate scale still applies. Explicit
`channel-vertex-xspan=...` overrides either default; `0.78` recovers the former
ordinary S exchange. T/U geometry and four-legged loop bubbles are unchanged.

Default `insertion-position` is **0.40 for supported s/t-tree and contact seagulls** and
**0.50 for bubble insertions**, measured from the external endpoint toward the
host vertex. The seagull default leaves 60% of the leg for the inner host
segment, 20% more length than the former midpoint placement. Explicit positions
remain effective; `insertion-position=0.50` restores the old seagull placement.
The styled seagull W circles use optical centering between the visible pink
endpoint arrow and the black tree vertex: `circ position=0.57332` on T trees and
`circ position=0.57513` on S trees. These values account for the arrow occupying
more of the segment than the dot, using the samples' standard 6pt arrows and
shared 2.10/2.10 outer frame and default scale. Retune `circ position` for other marker sizes or geometry.
Ordinary circles and the styled bubble-host circles retain the geometric 0.5.

Default `insertion-scale` is **0.50 for supported s/t-tree and contact bubble insertions**
(previously 0.66), so the bubble footprint is about 24% shorter and each host
piece has more room for a species circle. Seagulls retain **0.66**. An explicit
`insertion-scale=0.66` restores the former bubble size; other explicit values
are honored independently on each diagram. Standalone `\BubbleCorr` and the
four-legged channel bubbles keep their own existing dimensions.

`insertion=bubble` supports external slots `1,2,3,4` of both
`topology=t-tree` and `topology=s-tree`:
upper-left, lower-left, upper-right, lower-right. One selected leg is replaced
by outer--A, two distinct A--B arcs, then B--tree-vertex. The two new vertices
are trivalent. For s-tree, slots 1/2 attach to the left tree vertex, 3/4 to
the right, with the horizontal exchange unchanged. `insertion=seagull` also
supports all four external slots of both trees, with one quartic vertex and
a self-loop instead of the bubble's two new vertices. `insertion=swordfish`
supports the same external matrix with one new trivalent vertex and two loop
arcs meeting the actual tree vertex, now quartic. Its position/scale defaults
are 0.50/0.66; see the swordfish section for geometry and applicable controls.
Contact bubbles support the four external slots described above. Contact seagulls also support those four external slots. Other contact
insertions, U-tree insertions and internal slot `5` remain unsupported. Legacy
unsupported tree requests may be no-ops; invalid contact bubble slots/pairings
now fail explicitly. Simultaneous insertions are not supported.

```tex
\TTreeChannelCorr[
  field={},central={},leg-labels={,,,},show-momenta=false,
  line=plain,channel-line=plain,
  insertion=bubble,insertion-slot=2,
  bubble-top-line=plain,bubble-bottom-line=plain
]
```

Use the same options with `\STreeChannelCorr` for an s-tree insertion:

```tex
\STreeChannelCorr[
  field={},central={},leg-labels={,,,},show-momenta=false,
  line=plain,channel-line=plain,
  insertion=bubble,insertion-slot=3,
  bubble-top-line=plain,bubble-bottom-line=plain
]
```

A minimal seagull on the lower-right s-tree leg:

```tex
\STreeChannelCorr[
  field={},central={},leg-labels={,,,},show-momenta=false,
  line=plain,channel-line=plain,
  insertion=seagull,insertion-slot=4,seagull-loop-line=plain
]
```

Choose `insertion=seagull` with `\TTreeChannelCorr` for the same logical slot
on a t-tree. The graph has seven propagator edges, three interaction vertices
(two trivalent tree vertices and one quartic insertion vertex), and one loop.
Both loop ends meet that single insertion point; there is no stem and no
separate pair of bubble vertices. The other three external edges stay intact.

For s-tree insertions the exchange momentum uses the normal
`channel-momentum-*` controls. Its automatic distance/angle/label-position
are `10pt`, `90` and `above`; explicit values win. The
`insertion-middle-momentum-*` vertical-guide keys remain t-tree controls.
The s-tree geometry keeps its existing spans; it does not inherit the t-tree
insertion-specific span defaults.

Index positions are known to need a separate later workflow, D01. M03/M04
preserve their attachment, values and existing positioning controls without
retuning their appearance. See [deferred workflows](planning/deferred-workflows.md).
Focused evidence: `regressions/topologies/insertion/s-tree-bubble-slots.tex/pdf`;
plain inventory recipes C01-C04.

The inserted bubble reuses the `bubble-*` key family for internal styles,
loop momenta, endpoint indices, vertex-side external indices, and Proca /
scalar-polarized endpoint markers. The selected external momentum is drawn on the
outer pre-insertion host segment so it does not collide with the bubble.
By default, the pre-insertion arrow stays on its real host segment, spans
fractions 0.15 to 0.65, and places its label at fraction 0.40. It no longer
extends past the outer endpoint. The post arrow normally spans 0.25 to 0.75,
with its label at 0.50. Short bubble host pieces automatically expand the range
toward a readable 12pt arrow (before diagram scaling), capped at 90% of the
available segment. Long segments retain compact half-segment arrows. Explicit
start/end settings or an explicit pre-guide extension retain their selected
fraction ranges. Both guides default to an 8pt normal offset from the propagator.
Explicit range, guide extension, offset and label-fraction keys still win:

```tex
insertion-pre-momentum-guide-extension=0,
insertion-pre-momentum-start=0.15,
insertion-pre-momentum-end=0.65,
insertion-pre-momentum-label-fraction=0.40,
insertion-pre-momentum-offset=8pt,
insertion-post-momentum-start=0.25,
insertion-post-momentum-end=0.75,
insertion-post-momentum-label-fraction=0.50,
insertion-post-momentum-offset=8pt,
```

Use `insertion-pre-line=...` and `insertion-post-line=...` to style the two
host-leg pieces independently; empty values inherit the selected logical leg's style.
The pre segment is drawn as the external piece and can keep `endcap` /
`endcapp`, while the post segment is drawn without insertion-side external
endcaps.
The logical a/b arcs always run from A (outer side) to B (tree side): a is the
+90-degree curve, b the -90-degree curve relative to that direction. Existing
`bubble-top-line` / `bubble-bottom-line` aliases still mean a/b; they need not
be page-top/page-bottom on right-hand legs. Bubble-local arrow-size slots remain
3/4, as in the prototype; they share the existing size list with external slots
3/4. No size-list renumbering was introduced.

Host pre/post momentum labels, visibility, directions and marker sizes follow
the selected external slot. Hiding that slot hides both host momentum annotations
without hiding the loop momenta. Blank host labels keep their arrows. Pre/post
label-position defaults are `auto`: measured outside placement perpendicular
to each guide. The full text rectangle clears its arrow by 2pt, keeping the
label clear of the propagator as well. This is a continuous arrow with a side
label, without an empty gap. Explicit above/below/anchor settings still win.
The normal placement can also be selected explicitly as `outside`. Label/index x/y shifts remain
page-axis values. `insertion-orientation` continues to control seagulls; bubble
arcs follow the selected host direction rather than that option.
The seagull insertion draws one quartic/contact insertion vertex on the host
leg with a single package-styled self-loop propagator that starts and ends at
that insertion vertex. With `insertion-orientation=auto`, T-tree loops face
inward toward the exchange: upper-leg loops down, lower-leg loops up. S-tree
loops face outward: left-leg loops left, right-leg loops right. This selects
+90 degrees for logical slots 2/3 and -90 degrees for slots 1/4. Explicit
`bottom` still selects -90 degrees and `top` selects +90 degrees from the
outer-to-tree host direction. These are host-relative sides, so `top` need not be
page-up on a right-hand leg. `left` and `right` instead select absolute page
angles 180 and 0. The t-tree slot-1 default is preserved.
Loop momentum labels face the physical loop side regardless of arrow reversal.
S-tree bubble loop labels use measured normal placement with 4pt text-rectangle
clearance from their arrows. `bubble-momentum-label-distance` still overrides
that distance. T-tree bubble loop labels retain their prior placement and 2pt
label distance; their 8pt arrow offset (plus style allowance) is unchanged.
The seagull momentum arrow uses the same loop center and an outer radius equal
to loop radius plus `seagull-loop-momentum-offset` (default `6pt`). Its curve
comes from the same outer-half sampler as the loop geometry, scaled about that
center. The compact default range is `seagull-loop-momentum-start=0.30`
to `seagull-loop-momentum-end=0.52`, rather than most of the outer half-loop.
Default `seagull-loop-momentum-label-fraction=auto` places the label at
the midpoint of the selected arrow range. A numeric fraction still overrides it.
The label clears the actual local outward normal by its full text rectangle
plus `seagull-loop-momentum-label-distance` (default `2pt`), independent of
clockwise/counterclockwise reversal. Explicit momentum looseness remains a
separate curve-shape control. No diagram-specific label positions are used. The default
`seagull-loop-looseness=1.0` uses a true oval loop, and the seagull momentum
arc is sampled from the same loop geometry. Scalar-polarized and Proca-style
seagull loops use vertex-aware white-filled triangular markers; the default
`seagull-loop-marker-distance=auto` places marker tips on the insertion
vertex edge plus `semantic-marker-tip-clearance`, and slot `3` of
`propagator-arrow-sizes={...}` controls the marker size. When either
insertion is active, the t-tree host uses roomier
default geometry with steeper external
legs and a shorter middle channel leg; explicit
`fourpoint-xspan=...`, `fourpoint-yspan=...`, and `channel-vertex-yspan=...`
values still override those insertion-friendly defaults.

Seagull vertex indices use `seagull-vertex-indices={host-left,host-right,
loop-left,loop-right}` in the original logical order. Their placement defaults
are deliberately unchanged (D01). `insertion-post-indices` remains a bubble
control; it does not create additional seagull segment indices. Loop marker
sizes still use slot 3 of the existing size list, shared with external slot 3.
`insertion-style` is currently stored but is not consumed by these renderers;
use explicit pre/post/loop line keys. Short host segments and arbitrary custom
spans can require the existing momentum position/offset controls.

For the short host segment after the inserted bubble, use
`insertion-post-indices={j,m}` to place two labels on the segment from the
bubble-side insertion vertex to the selected main tree vertex. Tune those labels
with `insertion-post-index-fractions={...,...}`,
`insertion-post-index-position=...`, `insertion-post-index-yshift=...`, or the
per-side keys `insertion-post-bubble-index-*` and
`insertion-post-vertex-index-*`. This is separate from
`bubble-endpoint-indices`, which label the inserted bubble's internal
propagator endpoints; tune those `a,b,c,d` labels with the `bubble-*-index-*`
keys above.

The pre/post momentum keys tune the two split selected-leg momentum arrows around the
inserted bubble. The aliases `insertion-outer-momentum-*` and
`insertion-inner-momentum-*` map to the same pre/post controls, respectively:

```tex
\[
  \TTreeChannelCorr[
    field={},
    show-momenta=true,
    insertion=bubble,
    insertion-slot=1,
    momentum-labels={q_1,q_2,q_3,q_4,q_1-q_3},
    insertion-outer-momentum-end=0.7,
    insertion-outer-momentum-label-fraction=0.4,
    insertion-outer-momentum-offset=6pt,
    insertion-outer-momentum-label-distance=1pt,
    insertion-inner-momentum-start=0.2,
    insertion-inner-momentum-end=0.8,
    insertion-inner-momentum-label-fraction=0.54,
    insertion-inner-momentum-offset=5pt,
    insertion-inner-momentum-label-distance=1pt
  ]
\]
```

The detached middle-channel momentum arrow is separate from the external-leg
and split host arrows. Move it with the `insertion-middle-momentum-*` keys,
or the equivalent `insertion-channel-momentum-*` aliases:

```tex
insertion-middle-momentum-xshift=34pt,
insertion-middle-momentum-start-yshift=12pt,
insertion-middle-momentum-end-yshift=-12pt,
insertion-middle-momentum-label-xshift=36pt,
insertion-middle-momentum-label-position=right,
insertion-middle-momentum-label-distance=4pt,
```

Focused visual QA lives in
`regressions/topologies/insertion/insertion-regression.tex` and
`regressions/topologies/insertion/seagull-insertion-regression.tex`.
M04 adds `regressions/topologies/insertion/seagull-slots.tex/pdf`: all eight
placements and the independent `check-seagull-contact.py` PDF graph/marker
checker. Atlas recipes G01-G04 and G11-G14 show the plain seagull matrix.
`insertion-momentum-review.tex/pdf` checks external flow across four-point
families, all 16 insertion placements, shorter arrows, label-rectangle clearance,
and explicit overrides. H01-H04 show the new defaults in the atlas.
Atlas page 16 (J01-J04) samples species styling: the central EW Z stem,
its `circ=Z` and its Z text are all pink. The split external leg uses a bare
EW outer segment and an EW `circ=W` inner segment. Pink loop lines use
`{proca,magenta!85!red}` for two endpoint arrows and no circles.
Mixed bubbles use an EW `circ=W` arc and a pink scalar-polarization
Z arc; `bubble-momenta={,k}` leaves the W arc without a momentum guide or
label and draws k only on the pink arc. Seagulls use
`seagull-loop-momentum=k`. The full all-slot styled sampling is
`regressions/topologies/insertion/insertion-species-samples.tex/pdf`.
Its 56 public-diagram probes verify shorter bubbles, recovered host space,
explicit former/custom sizes, unchanged seagull defaults and size-state reset.
`check-species-circles.py` independently checks the 40 actual PDF circles:
16 pink circles on central Z stems, 24 black W circles, and vertex clearance.
It also verifies all 32 pink loop endpoint arrows contact their vertices.
The styled samples set `show-channel-momentum=false`, leaving the pink Z stem
and its species circle without a central momentum guide or P label. S samples
also set `insertion-post-momentum-label-distance=4pt` (instead of the ordinary
2pt) to separate the selected inner external-leg label from its arrow. These
are explicit sample choices; ordinary tree momentum visibility and label-gap
defaults are preserved. A further 41 public-diagram probes verify independent
central visibility, retained external/loop labels, explicit true and per-call reset.

The all-slot t-tree gallery and graph/style/cap/momentum checks are in
`regressions/topologies/insertion/t-tree-bubble-slots.tex` and its PDF. Its
isolated Proca page has an independent 16-tip vector check in
`check-t-tree-bubble-contact.py`, run by the maintained suite when
`FEYNMANFUN_PDF_PYTHON` is set to a Python interpreter with `pypdf`.

### Swordfish: a loop sharing the tree interaction

`\TTreeChannelCorr` and `\STreeChannelCorr` support
`insertion=swordfish,insertion-slot=1|2|3|4`, one external leg at a time.
Slots remain upper-left, lower-left, upper-right, lower-right. For selected
external endpoint E and tree vertex H, the graph is E--A plus two A--H curves.
A is new and trivalent; H is the existing tree vertex and becomes quartic.
There is no inner host segment, extra bridge, duplicated dot or collapsed edge.

```tex
\TTreeChannelCorr[
  field={},central={},leg-labels={,,,},show-momenta=false,
  line=plain,channel-line=plain,
  insertion=swordfish,insertion-slot=1,
  bubble-top-line=plain,bubble-bottom-line=plain
]
```

Replace the macro with `\STreeChannelCorr` for an S tree. Available controls:

- `insertion-pre-line` styles E--A; it inherits the selected logical leg style
  if empty. Logical caps remain at the external endpoint only.
- `bubble-top-line` / `bubble-bottom-line` independently style the two directed
  A--H curves, including EW waves/circles and one-/two-ended Proca/scalar markers.
  Arc a/b follow the outer-to-host axis; their page-top/page-bottom roles swap
  on right-hand legs, as for external bubble insertions.
- `bubble-momenta={k,\ell}`, per-arc momentum directions, rotation, fractions,
  offsets and label distance retain their existing meanings. A blank entry or
  direction `none` hides that loop guide. Selected external momentum appears
  once, on E--A, with the existing pre/outer guide controls and hide/blank rules.
- `show-channel-momentum=false` hides only the tree-exchange guide. Default
  external flow is p1/p2 incoming, p3/p4 outgoing; explicit reversals remain.
- `insertion-position=0.50` places A halfway from E to H at the standard
  `insertion-scale=0.66`. Scale changes the loop chord about fixed H: A's fraction
  from E is `1-(1-position)*scale/0.66`. Choose values keeping A inside E--H.
- `swordfish-opening-angle=60` controls the two loop tangents; the default keeps
  distinct incidences visible at the shared quartic point. Upper out/in angles
  are host-angle+opening / host-angle+180-opening; lower angles are mirrored.
  `bubble-loop-looseness` remains available.
- `bubble-endpoint-indices={a_A,a_H,b_A,b_H}` keeps four independent loop-end
  values attached to the appropriate A/H ends. `bubble-external-indices={i,j}`
  places two labels on the sole E--A segment at fractions 0.18/0.82. Exchange
  and other external index controls remain unchanged; visual index polish is D01.

There is no post segment, so `insertion-post-line`, post momentum and post index
options are inactive for swordfish and are not supported controls for this graph.
`insertion-orientation` remains a seagull control. U-tree/contact/internal-slot-5
and simultaneous insertions are unsupported. With `external-legs=false`, the
external insertion is hidden and the existing outer-placeholder behavior remains.

The frozen contract, six-page gallery and independent graph/endpoint checker are
in `regressions/topologies/insertion/M05-contract.md`, `swordfish-slots.tex/pdf`
and `check-swordfish.py`. The 167 public cases verify structure, logical slots,
geometry, mixed styles, momentum, indices, caps and state reset. Actual PDF paths
verify all eight shared-quartic graphs and 48 pink, white-filled endpoint contacts.
Atlas K01-K04/K11-K14 show plain placements; K21-K24 demonstrate mixed loop styles.

### Regular tree-attached triangles

`\TTreeChannelCorr[insertion=triangle,tree-triangle-side=top|bottom]` and
`\STreeChannelCorr[insertion=triangle,tree-triangle-side=left|right]` replace
one tree interaction with a three-edge loop. A and B each carry one external
leg, C connects by a bridge to the opposite tree interaction O. All four
interaction vertices are trivalent. This is distinct from triangle-contact's
quartic vertex and from the parallel-edge swordfish loop.

```tex
\TTreeChannelCorr[
  field={},central={},show-momenta=false,
  line=plain,channel-line=plain,
  insertion=triangle,tree-triangle-side=bottom
]
```

`tree-triangle-side=auto` selects bottom for T, left for S. Incompatible sides,
U trees and contact hosts do not activate a triangle. This is a vertex
correction: `insertion-slot`, the bubble/seagull keys and external insertion
position/scale/pre/post keys do not place or style it. One correction is
supported at a time. With `external-legs=false`, the triangle and exchange
remain; the four outer placeholder dots retain their existing behavior.

The logical slots and directions are:

| Slot | Directed edge |
| --- | --- |
| 1-4 | UL/LL/UR/LR outer endpoint to its interaction vertex |
| 5 | Exchange bridge, top to bottom (T) or left to right (S) |
| 6 | A to B; A/B are left/right for T, top/bottom for S |
| 7 | B to C |
| 8 | C to A |

External legs retain their logical styles, outer caps, field labels and momentum
flow; `channel-line` and `channel-indices` retain ownership of the exchange.
`tree-triangle-loop-line={...}` supplies a loop-wide style fallback;
`tree-triangle-line-6`, `-7`, `-8` override individual edges, independent of key
order. Empty styles inherit the corresponding global/logical line style.
Internal Proca markers contact both endpoints without circles. Bare `spol`,
`antspol` and their long aliases use the semantic end marker on this graph's
internal lines; `spolout` selects the start. Existing topologies are unchanged.

Defaults are equilateral in every orientation:

- `tree-triangle-depth=0.75` moves C toward the opposite tree vertex from the
  old corrected interaction point.
- `tree-triangle-outer-shift=0.60` moves the A/B base outward from that point.
- `tree-triangle-half-width=auto` derives `(depth+outer-shift)/sqrt(3)` so all
  three sides have equal length, including after depth/outer-shift edits.
  An explicit half-width permits other shapes.

The reviewed defaults retain the 50% larger equilateral sides and use the same
shared square outer frame as ordinary trees, box, crossed box and triangle-contact:
`fourpoint-xspan=2.10,fourpoint-yspan=2.10`. This gives the default T triangle
room without shortening its exchange bridge. All four external endpoints stay
at the requested coordinates. If an explicitly tighter frame needs more room,
the three T loop vertices translate inward together until the base is at least
0.28 coordinate units inside the outer edge, preserving side lengths. This
fallback can shorten the bridge. Styled examples retain wavy EW exchange lines.

Dimensions use TikZ coordinate units and follow the diagram scale. Keep
vertices separated and the bridge nonzero. Extreme, collapsed or crossing
custom geometry is not certified and is not automatically clamped.

The first five momentum labels use `momentum-labels={p_1,p_2,p_3,p_4,P}`;
`channel-momentum=...` overrides slot 5. `tree-triangle-momenta={k,\ell,q}`
names loop slots 6/7/8. Blank loop entries hide their guides. External blank
labels retain unlabeled arrows; `external-momentum-hide={...}` and
`show-channel-momentum=false` preserve their meanings. Default external flow
is 1/2 incoming and 3/4 outgoing. Loop arrows follow A--B--C--A.

Each slot has its own `tree-triangle-momentum-N={...}` block, N=1 through 8:

```tex
tree-triangle-momentum-7={
  layout=side,direction=reverse,start=.2,end=.8,
  offset=9pt,label-fraction=.5,label-offset=3pt
}
```

Options are `layout=gap|side`, `direction=forward|reverse|none`, `label=...`,
`start`, `end`, `offset`, `label-fraction`, `label-gap`, `label-offset`,
`label-xshift`, `label-yshift`, `label-anchor`, and
`side=outside|inside|left|right`. They affect only the selected annotation.
A nonempty per-slot loop label can activate its guide without a grouped label.
Default gaps are measured around the actual text; `layout=side` gives an
unbroken arrow and an outward label. Reversal retains the geometric side.
External arrows default to a compact 24pt target and internal ranges to
0.14-0.86, with 8pt normal offset. Labels face away from the actual centroid.
These defaults belong to M06; triangle-contact tuning remains independent.

`tree-triangle-propagator-left-indices={...}` and `-right-indices={...}`
provide eight endpoint values each in the directed slot order above (fractions
0.18/0.82). The `tree-triangle-index-left/right-position`, corresponding
`-xshift`/`-yshift`, `tree-triangle-index-style`, `-fill`, `-inner-sep` and
`-math-style` control their appearance. Existing field and channel indices
remain available. Index-position polish is still deferred to D01.

Atlas L01-L04 show plain equilateral placements; L11-L14 show mixed styles
and continuous momentum arrows. The focused gallery and independent PDF
graph/shape/contact checker are in `regressions/topologies/insertion/` under
`tree-triangle-slots.tex/pdf` and `check-tree-triangle.py`. See
[M06 verification](planning/m06-verification.md) for coverage and limits.

## One-Loop `s/t/u` Channel Bubbles For `\phi^4`

These are the primary channel macros:

```tex
\SChannelCorr[...]
\TChannelCorr[...]
\UChannelCorr[...]
```

Equivalent explicit forms:

```tex
\FourPointCorr[topology=s,...]
\FourPointCorr[topology=t,...]
\FourPointCorr[topology=u,...]
```

### Minimal `s`-channel bubble

```tex
\[
  \SChannelCorr[
    field=\phi,
    indices={a,b,c,d},
    momentum-labels={p_1,p_2,p_3,p_4},
    loop-channel-top-momentum=\ell,
    loop-channel-bottom-momentum=p_1+p_2-\ell
  ]
\]
```

### Contracted internal indices

Use one label per internal line:

```tex
\[
  \SChannelCorr[
    field=\phi,
    indices={a,b,c,d},
    loop-channel-contracted-indices={\alpha,\beta}
  ]
\]
```

This means:

- top/left internal line gets one repeated index
- bottom/right internal line gets one repeated index

You can also set them one at a time:

- `loop-channel-top-contracted-index=...`
- `loop-channel-bottom-contracted-index=...`
- `loop-channel-left-contracted-index=...`
- `loop-channel-right-contracted-index=...`

### Uncontracted internal indices

Each internal line has three index slots:

- start-vertex slot
- propagator slot
- end-vertex slot

Per-line triplet form:

```tex
\[
  \TChannelCorr[
    field=\phi,
    indices={a,b,c,d},
    loop-channel-left-indices={m,\mu,n},
    loop-channel-right-indices={r,\nu,s}
  ]
\]
```

Pairwise list form:

```tex
\[
  \UChannelCorr[
    field=\phi,
    indices={a,b,c,d},
    loop-channel-start-vertex-indices={i,m},
    loop-channel-internal-indices={\rho,\sigma},
    loop-channel-end-vertex-indices={j,n}
  ]
\]
```

Direct per-slot keys are also available:

- `loop-channel-a-start-index=...`
- `loop-channel-a-propagator-index=...`
- `loop-channel-a-end-index=...`
- `loop-channel-b-start-index=...`
- `loop-channel-b-propagator-index=...`
- `loop-channel-b-end-index=...`

Useful aliases:

- `loop-channel-top-*`
- `loop-channel-bottom-*`
- `loop-channel-left-*`
- `loop-channel-right-*`

### One-loop channel geometry and layout

Main geometry keys:

- `fourpoint-xspan=...`
- `fourpoint-yspan=...`
- `loop-channel-vertex-xspan=...`
- `loop-channel-vertex-yspan=...`
- `loop-channel-loop-looseness=...`
- `loop-channel-a-line=...`
- `loop-channel-b-line=...`

Channel propagators use the same shared line-style and color machinery as the
rest of the package. Use `line=...` and `color=...` for broad styling,
`leg-styles={...}` for external slot overrides, and
`loop-channel-a-line=...` / `loop-channel-b-line=...` for the two internal
loop propagators.

Loop-momentum arrow geometry keys:

- `loop-channel-a-arrow-start=...`
- `loop-channel-a-arrow-end=...`
- `loop-channel-a-arrow-xshift=...`
- `loop-channel-a-arrow-yshift=...`
- `loop-channel-a-arrow-looseness=...`
- `loop-channel-b-arrow-start=...`
- `loop-channel-b-arrow-end=...`
- `loop-channel-b-arrow-xshift=...`
- `loop-channel-b-arrow-yshift=...`
- `loop-channel-b-arrow-looseness=...`

Useful aliases:

- `loop-channel-top-arrow-*`
- `loop-channel-bottom-arrow-*`
- `loop-channel-left-arrow-*`
- `loop-channel-right-arrow-*`

High-level index layout:

- `loop-channel-index-layout=tight|balanced|wide`

Index styling:

- `loop-channel-vertex-index-size=normal|script|scriptscript`
- `loop-channel-propagator-index-size=normal|script|scriptscript`
- `loop-channel-internal-index-style=...`
- `loop-channel-internal-index-fill=...`
- `loop-channel-internal-index-inner-sep=...`

Low-level placement keys are available if you need them:

- `loop-channel-a-start-slot-position=...`
- `loop-channel-a-propagator-slot-position=...`
- `loop-channel-a-end-slot-position=...`
- `loop-channel-b-start-slot-position=...`
- `loop-channel-b-propagator-slot-position=...`
- `loop-channel-b-end-slot-position=...`
- `loop-channel-a-start-index-xshift=...`
- `loop-channel-a-end-index-xshift=...`
- `loop-channel-a-end-index-yshift=...`
- `loop-channel-a-propagator-index-position=...`
- `loop-channel-a-propagator-index-xshift=...`
- `loop-channel-a-propagator-index-yshift=...`
- and the corresponding `b`, `top`, `bottom`, `left`, and `right` aliases

#### Paste-ready loop-channel index defaults

Safe reset for one-loop channel indices:

```tex
\[
  \TChannelCorr[
    loop-channel-left-indices={m,\mu,n},
    loop-channel-right-indices={r,\nu,s},
    loop-channel-index-layout=balanced,
    loop-channel-vertex-index-size=script,
    loop-channel-propagator-index-size=script
  ]
\]
```

Current defaults behind that reset:

- `loop-channel-index-layout=balanced`
- `loop-channel-vertex-index-size=script`
- `loop-channel-propagator-index-size=script`

Use `loop-channel-vertex-index-size=scriptscript` only when a very compact
diagram needs extra room.

What the loop-channel index presets actually do:

- `tight`
  Start/propagator/end slots are `0.18`, `0.50`, `0.82`
  This pulls the endpoint indices inward toward the propagator index.

- `balanced`
  Start/propagator/end slots are `0.10`, `0.50`, `0.90`
  This is the default.

- `wide`
  Start/propagator/end slots are `0.06`, `0.50`, `0.94`
  This pushes the endpoint indices outward toward the vertices and opens the center.

#### Loop-channel index fix-it recipes

If the propagator index is colliding with the two vertex-side indices:

```tex
\[
  \TChannelCorr[
    loop-channel-left-indices={m,\mu,n},
    loop-channel-right-indices={r,\nu,s},
    loop-channel-index-layout=wide
  ]
\]
```

If the indices look too spread out and detached from the propagator:

```tex
\[
  \TChannelCorr[
    loop-channel-left-indices={m,\mu,n},
    loop-channel-right-indices={r,\nu,s},
    loop-channel-index-layout=tight
  ]
\]
```

If the propagator index is visually too large compared with the vertex indices:

```tex
\[
  \TChannelCorr[
    loop-channel-left-indices={m,\mu,n},
    loop-channel-right-indices={r,\nu,s},
    loop-channel-propagator-index-size=scriptscript
  ]
\]
```

If the vertex indices are too tiny and hard to read:

```tex
\[
  \TChannelCorr[
    loop-channel-left-indices={m,\mu,n},
    loop-channel-right-indices={r,\nu,s},
    loop-channel-vertex-index-size=script
  ]
\]
```

If the left vertex-side indices are colliding with the external legs or momentum arrows:

```tex
\[
  \TChannelCorr[
    loop-channel-left-indices={m,\mu,n},
    loop-channel-left-start-index-xshift=-8pt,
    loop-channel-left-end-index-xshift=-8pt
  ]
\]
```

Why this works:

- the start and end indices on the left loop line are both pushed farther left
- the propagator index stays where it is

If only the left propagator index needs a local nudge:

```tex
\[
  \TChannelCorr[
    loop-channel-left-indices={m,\mu,n},
    loop-channel-left-propagator-index-xshift=-2pt,
    loop-channel-left-propagator-index-yshift=2pt
  ]
\]
```

If the right side of the `u` channel is crowded by the crossed legs:

```tex
\[
  \UChannelCorr[
    loop-channel-right-indices={r,\nu,s},
    loop-channel-right-start-index-xshift=-1pt,
    loop-channel-right-end-index-xshift=-1pt,
    loop-channel-right-propagator-index-xshift=-2pt
  ]
\]
```

Why this works:

- it pulls the right-side indices back toward the loop
- that usually buys space from the crossed external legs

If you want the current `u`-channel right-side defaults as a reset:

```tex
\[
  \UChannelCorr[
    loop-channel-right-indices={r,\nu,s},
    loop-channel-right-start-index-xshift=1pt,
    loop-channel-right-end-index-xshift=1pt,
    loop-channel-right-propagator-index-xshift=0pt
  ]
\]
```

## Sunset Diagrams

Minimal default sunset:

```tex
\[
  \SunsetDiagram[
    field=\phi,
  ]
\]
```

The packaged default layout is tuned for a simple scalar sunset:

```tex
\[
  \SunsetDiagram[
    sunset-left-line=sca,
    sunset-right-line=sca,
    scale=1.2,
    field=,
    sunset-external-momentum=p,
    sunset-top-momentum=k,
    sunset-top-label-yshift=27pt,
    sunset-top-arrow-yshift=22pt,
    sunset-middle-momentum=p-k-q,
    sunset-middle-label-yshift=-1pt,
    sunset-middle-arrow-yshift=12pt,
    sunset-bottom-momentum=q,
    sunset-bottom-label-yshift=-12pt,
    sunset-bottom-arrow-yshift=-15pt,
    sunset-outer-span=1.6,
    sunset-inner-span=1
  ]
\]
```

Sunset propagators use the shared package color machinery. Use `color=...` for
a whole sunset, and combine it with `sunset-left-line=...`,
`sunset-middle-line=...`, `sunset-right-line=...`, `sunset-top-line=...`, and
`sunset-bottom-line=...` for segment-level line styles.

### Sunset index model

Each internal sunset line has three slots:

- left vertex index
- propagator index
- right vertex index

Contracted form:

```tex
\[
  \SunsetDiagram[
    sunset-internal-indices={\alpha,\beta,\gamma}
  ]
\]
```

Uncontracted form:

```tex
\[
  \SunsetDiagram[
    sunset-left-vertex-indices={a,c,e},
    sunset-internal-indices={\alpha,\beta,\gamma},
    sunset-right-vertex-indices={b,d,f}
  ]
\]
```

Per-line triplets:

```tex
\[
  \SunsetDiagram[
    sunset-top-indices={a,\alpha,b},
    sunset-middle-indices={c,\beta,d},
    sunset-bottom-indices={e,\gamma,f}
  ]
\]
```

Helpful sunset layout controls:

- `sunset-momentum-layout=legacy|compact|balanced|wide`
- `sunset-index-layout=tight|balanced|wide`
- `sunset-index-aware-momenta=true|false`
- `sunset-top-label-index-clearance=...`
- `sunset-middle-label-index-clearance=...`
- `sunset-bottom-label-index-clearance=...`

#### Paste-ready sunset index defaults

Safe reset for sunset indices:

```tex
\[
  \SunsetDiagram[
    sunset-top-indices={a,\alpha,b},
    sunset-middle-indices={c,\beta,d},
    sunset-bottom-indices={e,\gamma,f},
    sunset-index-layout=balanced,
    sunset-vertex-index-size=scriptscript,
    sunset-propagator-index-size=script
  ]
\]
```

Current defaults behind that reset:

- `sunset-index-layout=balanced`
- `sunset-vertex-index-size=scriptscript`
- `sunset-propagator-index-size=script`

What the sunset index presets actually do:

- `tight`
  Top and bottom slots are `0.18`, `0.50`, `0.82`
  Middle slots are `0.22`, `0.50`, `0.78`
  This pulls endpoint indices inward toward the propagator index.

- `balanced`
  Top and bottom slots are `0.10`, `0.50`, `0.90`
  Middle slots are `0.12`, `0.50`, `0.88`
  This is the default.

- `wide`
  Top and bottom slots are `0.06`, `0.50`, `0.94`
  Middle slots are `0.08`, `0.50`, `0.92`
  This spreads the endpoint indices outward and opens the middle.

#### Sunset modernization note

`regressions/topologies/sunset/sunset-index-regression.tex` is the current
focused stress test for sunset index placement. The next planned sunset branch
should add a broader sunset capacity sheet before changing defaults, so the
visual problems are diagnosed in one place instead of handled through scattered
fix-it recipes.

## Explicit Tree-Level Channel Topologies

The one-loop channel bubbles are the default `s/t/u` story.

If you specifically want the tree-level exchange diagrams, use:

```tex
\STreeChannelCorr[...]
\TTreeChannelCorr[...]
\UTreeChannelCorr[...]
```

or:

```tex
\FourPointCorr[topology=s-tree,...]
\FourPointCorr[topology=t-tree,...]
\FourPointCorr[topology=u-tree,...]
```

Those use the legacy `channel-*` key family, for example:

- `channel-momentum=...`
- `channel-indices={start,prop,end}`
- `channel-contracted-index=...`
- `channel-index-layout=tight|balanced|wide`

## Which Example File To Open

- `example.tex`: broad package tour
- `regressions/topologies/channel/channel-topology-regression.tex`: one-loop `s/t/u` channel checks
- `regressions/topologies/box/box-topology-regression.tex`: one-loop box checks
- `regressions/topologies/cross-box/cross-box-regression.tex`: crossed-box checks
- `regressions/topologies/triangle-contact/triangle-contact-regression.tex`: triangle-contact orientation checks
- `regressions/topologies/vertex-identity/vertex-identity-check.tex`: vertex-identity helper checks
- `regressions/topologies/three-point/three-point-check.tex`: focused 3-point topology checks
- `regressions/topologies/sunset/sunset-example.tex`: focused sunset examples
- `regressions/topologies/sunset/sunset-index-regression.tex`: sunset index stress cases
- `regressions/propagators/circ/propagator-circ-check.tex`: circled propagator marker capacity sheet
- `regressions/propagators/endpoint-markers/endpoint-marker-regression.tex`: endpoint arrow and endcap add-on visual sheet
- `regressions/propagators/proca/proca-regression.tex`: focused Proca propagator visual sheet
- `regressions/propagators/scalar-polarization/scalar-polarization-check.tex`: single-leg scalar-polarized placement and arrow-size checks

## Overleaf And Local Use

For Overleaf:

1. Upload your `.tex` file.
2. Upload `feynman-fun.sty`.
3. Compile with `pdfLaTeX`.

For local use:

1. Keep your `.tex` file in the same folder as `feynman-fun.sty`.
2. Run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error yourfile.tex
```

If you use `latexmk`:

```sh
latexmk -pdf yourfile.tex
```


The compilation-performance follow-up reduces repeated internal style/list setup
and path construction while retaining these APIs and the single-file installation.
See [measured results and compatibility checks](planning/compilation-performance/verification.md).

## Crossed vertex correction: two half-moon layouts

`\CrossedVertexCorr` reuses the triangle-contact graph and its style/label
controls. `crossed-vertex-orientation=right` is the default and connects the
UL/LR cubic vertices through a half-moon; `left` connects LL/UR. In both, the
two straight W propagators share that same diagonal and meet the central
quartic vertex. The arc crosses one external leg without an interaction dot.

```tex
\CrossedVertexCorr[
  field={}, leg-labels={,,,}, central={}, blob=false,
  center-vertex=true, external-vertices=false,
  crossed-vertex-orientation=right,
  line=plain, show-momenta=false
]
```

For the reference-style sample, replace `line=plain, show-momenta=false` with:

```tex
triangle-contact-external-line=ewboson,
triangle-contact-internal-lines={{ewboson,circ=W},
                                {proca,magenta},
                                {ewboson,circ=W}},
show-momenta=true,
external-momentum-hide={1,2,3,4},
triangle-contact-internal-momenta={,k,},
triangle-contact-momentum-6={layout=side,label-offset=3pt}
```

The underlying form is `\TriangleContactCorr[triangle-contact-orientation=crossed-right]`
or `crossed-left`. These are presets/layouts of one graph family, not extra
loop topologies. Exactly two crossed views are supported.

| Logical slot | Connection |
| --- | --- |
| 1,2,3,4 | Physical UL, LL, UR, LR external corners |
| 5 | Q to first cubic vertex A; straight W in the sample |
| 6 | A to opposite cubic vertex B; continuous semicircle |
| 7 | B to Q; second straight W in the sample |

Q hosts slots 2/3 in the right view and 1/4 in the left. Slot 3 is interrupted
in the right view; slot 1 in the left. The full logical external edge keeps its
styles, semantic tips and outer caps. No artificial cut-end tips/caps are added.
`crossed-vertex-crossing-gap=.04` sets the half-gap as a fraction of that full
edge. Invalid orientations, spans and gaps produce errors.

The outer frame inherits `fourpoint-xspan/yspan` (2.10 by default), with explicit
`triangle-contact-external-xspan/yspan` overrides. In crossed views, the internal
span settings determine a **circular radius** `sqrt(xspan^2+yspan^2)`; the diameter
is projected onto the actual outer diagonal. They do not set ellipse axes.
This keeps the W segments straight through their outer corners, including
unequal-frame examples. Both internal spans must be positive and individually
smaller than their external counterparts.

All seven `triangle-contact-momentum-N` keys retain their per-edge controls.
Slot 6 follows the circle, with compact clockwise default arrows centered at
fraction .75 in the right view and .25 in the left, away from the crossing.
Choose `layout=side` for an unbroken arrow or `layout=gap` for a label in its
break; `side=inside/outside/left/right`, range, offset, label shifts and anchor
remain available. The grouped internal label fraction defaults to `auto`:
existing straight triangle-contact views still resolve to .50, while crossed
views use the above shoulder defaults. Explicit fractions are authoritative.
Reverse or hide with `triangle-contact-internal-momentum-directions`; default
external momentum stays p1/p2 incoming and p3/p4 outgoing. Slot-6 endpoint indices
attach to its actual curve; D01 index appearance remains a later workflow.

See inventory CV01/CV02/CV11/CV12, [the frozen contract](planning/crossed-vertex/contract.md),
and the maintained `regressions/topologies/crossed-vertex/crossed-vertex-regression.tex`.
