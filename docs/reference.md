# Reference

Full package reference for `correlator-diagrams.sty`.

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
- [One-Loop `s/t/u` Channel Bubbles For `\phi^4`](#one-loop-stu-channel-bubbles-for-phi4)
- [Sunset Diagrams](#sunset-diagrams)
- [Explicit Tree-Level Channel Topologies](#explicit-tree-level-channel-topologies)
- [Which Example File To Open](#which-example-file-to-open)
- [Overleaf And Local Use](#overleaf-and-local-use)

## Quick Start

Main package:

- `correlator-diagrams.sty`

Main demos:

- `example.tex`
- `regressions/topologies/box/box-topology-regression.tex`
- `regressions/topologies/channel/channel-topology-regression.tex`
- `regressions/topologies/cross-box/cross-box-regression.tex`
- `regressions/topologies/triangle-contact/triangle-contact-regression.tex`
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
\usepackage{correlator-diagrams}
```

The main entry points are:

```tex
\TwoPointCorr[...]
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

### `\ThreePointCorr`

- slot 1 = upper-left leg
- slot 2 = right leg
- slot 3 = bottom leg

That slot order matters for:

- `leg-styles={...}`
- `momentum-labels={...}`
- `momentum-arrow-sizes={...}`
- `propagator-arrow-sizes={...}`
- `leg-labels={...}`

The default 3-point momentum convention is:

- upper-left leg incoming
- right leg outgoing
- bottom leg outgoing

Use `three-point-momentum-flow=all-in|all-out|default` to set all three arrows at once.

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

The two internal box-edge segments use:

- slot 5 = left edge
- slot 6 = right edge

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

If you need complete manual control, use:

- `leg-labels={...}`

`leg-labels` overrides `field` and `indices` for the legs you specify.

## Momentum Labels And Arrows

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

- `mode=q|k|p`
- `momentum-start=<integer>`
- `momentum-labels={...}`

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

- `channel-momentum-start=...`
- `channel-momentum-end=...`
- `channel-momentum-distance=...`
- `channel-momentum-angle=...`
- `channel-momentum-label-position=...`
- `channel-momentum-label-xshift=...`
- `channel-momentum-label-yshift=...`

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

The `proca` style is a massive-vector convenience style built on a straight
scalar-style dashed line with two white-filled open arrow markers just inside
the endpoints, with each arrow pointing toward the nearest vertex. The arrows
use the same size as the scalar-polarized arrow markers; their outlines follow
the propagator color while their interiors stay white. `Proca` is accepted as
an alias. Add `circ={}` explicitly when a blank midpoint circle is wanted.

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

In package-managed topologies, these add-ons are oriented relative to the
interaction vertex for each leg. In raw `\propag[...]` calls, they fall back to
path-end semantics: `...in` targets the path end and `...out` points away from
the path end. Endcaps are intended for external legs only; in topology helpers,
use `endcap` or `endcapout` on an external leg style to mark the outer cropped
endpoint. Endcaps inherit the resolved propagator color, including global
`color=...`, topology color keys, and common per-leg TikZ/xcolor styles such as
`{ewboson,fieldA,endcap}`, `{ewboson,blue!65!black,endcap}`, and
`{ewboson,color=orange!85!black,endcap}`.

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
- `circ fill=...`
- `circ draw=...`
- `circ label style={...}`

The circle keeps the configured `circ size`; labels are overlaid rather than
allowed to resize the marker. Increase `circ size` when a deliberately wide
custom label should fit fully inside the circle. By default, the circle outline
inherits the resolved propagator color, including Proca propagators; use
`circ draw=...` to override the outline color independently.

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

3-point geometry controls:

- `three-point-left-xspan=...`
- `three-point-upper-yspan=...`
- `three-point-right-xspan=...`
- `three-point-bottom-yspan=...`
- `three-point-central-label-yshift=...`

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

The default `scalarpolarized` style places an inward-pointing marker near the vertex.

`out` flips the marker so the triangle points outward while keeping it near the vertex end of the leg.

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

Box external momentum arrow placement:

- `box-external-momentum-start=...`
- `box-external-momentum-end=...`
- `box-external-momentum-label-fraction=...`
- `box-external-momentum-label-gap=...`
- `box-external-momentum-offset=...`

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
automatic blank marker.

Focused visual QA lives in
`regressions/topologies/cross-box/cross-box-regression.tex`.

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
- `triangle-contact-momentum-slots={1,2,3,4}`
- `triangle-contact-central-label-yshift=...`

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
- `half-box-momentum-start=...`
- `half-box-momentum-end=...`
- `half-box-momentum-offset=...`
- `half-box-momentum-label-fraction=...`
- `half-box-momentum-label-gap=...`
- `half-box-momentum-slots={1,2,3,4}`
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

The `halfbox-*` and `flatcontact-*` spellings are also accepted as aliases.
The momentum slot filters let a diagram show only selected external momentum
arrows, for example `half-box-momentum-slots={2,3}` for the two lower legs.

Inside package-managed topologies, `scalarpolarized`/`spol` external legs are
oriented toward the topology vertex. The endpoint arrow add-ons `arrowin`,
`arrowout`, `openarrowin`, and `openarrowout` follow the same topology-aware
orientation. For cropped external legs, use `endcapout` to put a terminal bar
exactly at the external endpoint of the leg. The explicit aliases such as
`spolin`/`spolout` remain available for manual control.

Focused visual QA lives in
`regressions/topologies/vertex-identity/vertex-identity-check.tex`.

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
2. Upload `correlator-diagrams.sty`.
3. Compile with `pdfLaTeX`.

For local use:

1. Keep your `.tex` file in the same folder as `correlator-diagrams.sty`.
2. Run:

```sh
pdflatex -interaction=nonstopmode -halt-on-error yourfile.tex
```

If you use `latexmk`:

```sh
latexmk -pdf yourfile.tex
```
