# Correlator Diagram Macros

This package provides small reusable LaTeX macros for drawing standard 2-point and 4-point correlator / Feynman-diagram skeletons with:

- automatic momentum labels such as `q_1,q_2,...`, `k_1,k_2,...`, or `p_1,p_2,...`
- visible center and external vertex controls
- external leg labels generated from a field symbol plus indices
- optional full manual override of leg labels and momentum labels
- global and per-leg arrow-size control
- per-leg propagator style overrides
- configurable `scalarpolarized` / `antiscalarpolarized` dashed leg styles with open arrowheads
- a central blob or vertex label for objects such as `G^{(2)}`, `G^{(4)}`, or `\Gamma^{(4)}`
- line styles from `tikz-feynhand`

The package is implemented in [correlator-diagrams.sty](/Users/aeaconnelly/Documents/LatexCode/correlator-diagrams.sty). A working demo is in [example.tex](/Users/aeaconnelly/Documents/LatexCode/example.tex).

## What You Get

Two macros are provided:

```tex
\TwoPointCorr[<options>]
\FourPointCorr[<options>]
\SunsetDiagram[<options>]
```

Short aliases are also available:

```tex
\TwoPtCorr[<options>]
\FourPtCorr[<options>]
\SunsetDiag[<options>]
```

These are meant for quick, consistent correlator diagrams rather than arbitrary hand-built topologies.

## Requirements

The package depends on:

- `tikz`
- `tikz-feynhand`
- `etoolbox`
- `listofitems`
- `xparse`

In this workspace, the example compiles with:

```sh
pdflatex -interaction=nonstopmode -halt-on-error example.tex
```

## Minimal Use

Load the package in your document:

```tex
\usepackage{correlator-diagrams}
```

Default 2-point diagram:

```tex
\[
  \TwoPointCorr
\]
```

Default 4-point diagram:

```tex
\[
  \FourPointCorr
\]
```

Default sunset diagram:

```tex
\[
  \SunsetDiagram
\]
```

This default is intentionally minimal: blank external field labels, scalar external legs, no visible central label, and the `balanced` sunset momentum-layout preset.

## Quick Examples

### 2-point function with Lorentz indices

```tex
\[
  \TwoPointCorr[
    mode=q,
    field=\phi,
    indices={\mu,\nu},
    central=G^{(2)}
  ]
\]
```

This gives leg labels `\phi_\mu` and `\phi_\nu`, with momentum labels `q_1` and `q_2`.

### 4-point function with `k_i` momenta

```tex
\[
  \FourPointCorr[
    mode=k,
    field=\phi,
    indices={a,b,c,d},
    central=G^{(4)}
  ]
\]
```

### 4-point function with fully custom external fields

```tex
\[
  \FourPointCorr[
    line=fer,
    momentum-labels={p_1,p_2,p_3,p_4},
    leg-labels={\psi_i,\bar\psi_j,\psi_k,\bar\psi_l},
    central=\Gamma^{(4)}
  ]
\]
```

### Visible center vertex and emphasized arrows on selected legs

```tex
\[
  \FourPointCorr[
    blob=false,
    center-vertex-style=ringdot,
    leg-styles={scalarpolarized,scalarpolarized,plain,plain},
    momentum-arrow-size=6pt,
    momentum-arrow-sizes={11pt,8pt,5pt,5pt},
    propagator-arrow-size=8pt,
    propagator-arrow-sizes={12pt,9pt,8pt,8pt},
    field=\varphi,
    indices={1,2,3,4},
    central=\Gamma_{\mathrm{mix}}^{(4)}
  ]
\]
```

### No blob, operator labels as superscripts

```tex
\[
  \FourPointCorr[
    mode=p,
    blob=false,
    field=\mathcal{O},
    indices={\alpha,\beta,\gamma,\delta},
    index-placement=sup,
    central=\mathcal{V}^{(4)}
  ]
\]
```

### Scalar-polarization direction and placement variants

```tex
\[
  \FourPointCorr[
    blob=false,
    leg-styles={scalarpolarizedin,scalarpolarizedout,antspolin,antspolout},
    scalar-arrow-position=0.12,
    anti-scalar-arrow-position=0.18
  ]
\]
```

### Sunset self-energy example

```tex
\[
  \SunsetDiagram[
    field=\phi,
    central=\Sigma(p)
  ]
\]
```

### Sunset momentum-layout presets

```tex
\[
  \SunsetDiagram[
    field=\phi,
    central=\Sigma(p),
    sunset-momentum-layout=wide
  ]
\]
```

## Labeling Rules

### Momentum labels

By default, momenta are generated automatically from:

- `mode=q` gives `q_1,q_2,...`
- `mode=k` gives `k_1,k_2,...`
- `mode=p` gives `p_1,p_2,...`

Example:

```tex
\FourPointCorr[mode=k]
```

produces `k_1,k_2,k_3,k_4`.

You can shift the numbering:

```tex
\FourPointCorr[mode=q,momentum-start=3]
```

which gives `q_3,q_4,q_5,q_6`.

You can also override everything explicitly:

```tex
\FourPointCorr[
  momentum-labels={p,p+q,r,r+q}
]
```

### Sunset internal indices

Preferred interface:

- `sunset-internal-indices={...}` for one centered index on each internal line
- `sunset-left-vertex-indices={...}` and `sunset-right-vertex-indices={...}` when you want the uncontracted vertex-side labels too

These internal indices are intentionally treated differently from momentum labels:

- they are smaller by default
- the vertex-side slots are smaller by default than the centered propagator slots
- the top and bottom slots follow the actual loop propagators
- the vertex-side slots stay tied to the ends of each internal line
- the sunset momentum labels can automatically back away from them

One-index-per-internal-leg form:

```tex
\[
  \SunsetDiagram[
    field=\phi,
    central=\Sigma(p),
    sunset-internal-indices={a,b,c}
  ]
\]
```

Three-slot uncontracted form:

```tex
\[
  \SunsetDiagram[
    field=\phi,
    central=\Sigma_{ab}(p),
    sunset-left-vertex-indices={a,c,e},
    sunset-internal-indices={\alpha,\beta,\gamma},
    sunset-right-vertex-indices={b,d,f}
  ]
\]
```

### Momentum arrow sizes

Momentum arrows are drawn by the package itself, so you can control them globally:

```tex
\FourPointCorr[
  momentum-arrow-size=8pt
]
```

or per leg:

```tex
\FourPointCorr[
  momentum-arrow-sizes={12pt,8pt,5pt,5pt}
]
```

This is useful if you want to emphasize some external momenta more strongly than others.

### External leg labels

If you set `field` and `indices`, the package constructs the labels automatically:

```tex
\FourPointCorr[
  field=\phi,
  indices={a,b,c,d}
]
```

which gives:

```tex
\phi_a,\phi_b,\phi_c,\phi_d
```

You can change index placement:

- `index-placement=sub` gives `\phi_a`
- `index-placement=sup` gives `\phi^a`
- `index-placement=none` gives `\phi a`

If you want total control, use `leg-labels`:

```tex
\FourPointCorr[
  leg-labels={A_i,B_j,C_k,D_l}
]
```

When `leg-labels` is present, it overrides `field` and `indices` for the legs you specify.

### Vertex visibility

The package always defines the geometric vertices, and you can decide whether they are visibly marked.

- `blob=true` draws the central blob
- `blob=false` removes the blob
- `center-vertex=true` draws a visible central vertex mark
- `external-vertices=true` draws visible endpoint vertices

By default:

- the central blob is shown
- the center vertex is visibly marked
- the external attachment points are not visibly marked

If you want a pure blob with no visible center dot on top of it, set `center-vertex=false`.
If you want visible endpoint markers, set `external-vertices=true`.
If you switch `blob=false`, the visible center vertex remains available, so you do not lose the central attachment point completely.

## Diagram Conventions

### 2-point ordering

`\TwoPointCorr` uses:

- leg 1 = left
- leg 2 = right

### 4-point ordering

`\FourPointCorr` uses:

- leg 1 = upper left
- leg 2 = lower left
- leg 3 = upper right
- leg 4 = lower right

Keys such as `leg-labels`, `leg-styles`, `momentum-labels`, `momentum-arrow-sizes`, and `propagator-arrow-sizes` follow this same leg ordering.

The default momentum-arrow side placement matches the usual `mom` / `mom'` convention: the arrows stay on the outer side of each leg.

### Sunset ordering

`\SunsetDiagram` uses:

- external leg 1 = left
- external leg 2 = right
- momentum / propagator index 1 = left external segment
- momentum / propagator index 2 = middle bridge segment
- momentum / propagator index 3 = right external segment
- momentum / propagator index 4 = top arc
- momentum / propagator index 5 = bottom arc

This matters when you use `leg-labels`, `momentum-labels`, `momentum-arrow-sizes`, or `propagator-arrow-sizes` with the sunset macro.

## Option Reference

### Core keys

- `mode=q`
  selects the momentum letter used for automatic labels
- `momentum-symbol={\ell}`
  same idea as `mode`, but with an arbitrary symbol
- `momentum-start=1`
  starting index for automatic momentum numbering
- `momentum-labels={...}`
  explicit momentum labels, one per leg
- `momentum-arrow-size=6pt`
  global size for the momentum arrowheads
- `momentum-arrow-sizes={...}`
  per-leg momentum arrowhead sizes
- `field=\phi`
  base field or operator symbol used for automatic leg labels
- `indices={...}`
  comma-separated index list
- `leg-labels={...}`
  explicit external leg labels
- `leg-styles={...}`
  per-leg propagator style overrides
- `central=...`
  central text such as `G^{(2)}`, `G^{(4)}`, `\Gamma^{(4)}`

### Appearance keys

- `line=plain`
  line style passed to `tikz-feynhand`
- `propagator-arrow-size=8pt`
  global size for propagator arrowheads on styles that carry arrows
- `propagator-arrow-sizes={...}`
  per-leg propagator arrowhead sizes
- `scalar-arrow-direction=in`
  default direction for `scalarpolarized` and `spol`
- `scalar-arrow-position=0.08`
  position of the open scalar arrowhead along the leg, measured from the external endpoint
- `anti-scalar-arrow-direction=out`
  default direction for `antiscalarpolarized` and `antspol`
- `anti-scalar-arrow-position=0.08`
  position of the anti-scalar open arrowhead along the leg
- `blob=true` or `blob=false`
  show or hide the central blob
- `blob-style=blob`
  blob style, such as `blob`, `blobring`, `blobgray`
- `center-vertex=true` or `center-vertex=false`
  show or hide a visible central vertex marker
- `center-vertex-style=dot`
  central vertex marker style
- `external-vertices=true` or `external-vertices=false`
  show or hide visible endpoint vertices
- `external-vertex-style=dot`
  external vertex marker style
- `vertices=true` or `vertices=false`
  convenience switch for both center and external visible vertices
- `vertex-style=dot`
  convenience style setter for both center and external visible vertices
- `show-momenta=true` or `show-momenta=false`
  show or hide momentum arrows and labels
- `scale=1`
  scale the whole diagram

### Sunset-specific keys

`SunsetDiagram` applies its own local defaults before reading your options. The main ones are:

- `scale=1.2`
- `field=`
- `sunset-left-line=sca`
- `sunset-right-line=sca`
- `sunset-inner-span=1`
- `sunset-outer-span=1.6`
- `sunset-central-label=\hspace{1mm}`
- `sunset-momentum-layout=balanced`
- `sunset-index-layout=balanced`

- `sunset-external-momentum=p`
  sets both external momentum labels at once
- `sunset-left-momentum=...`
  left external momentum label
- `sunset-right-momentum=...`
  right external momentum label
- `sunset-top-momentum=...`
  momentum label on the top arc
- `sunset-middle-momentum=...`
  momentum label on the middle bridge line
- `sunset-bottom-momentum=...`
  momentum label on the bottom arc
- `sunset-left-line=...`
  line style for the left external segment
- `sunset-middle-line=...`
  line style for the central bridge segment
- `sunset-right-line=...`
  line style for the right external segment
- `sunset-top-line=...`
  line style for the top arc
- `sunset-bottom-line=...`
  line style for the bottom arc
- `sunset-internal-vertices=true` or `sunset-internal-vertices=false`
  show or hide the two interaction vertices
- `sunset-internal-vertex-style=dot`
  style for the two internal sunset vertices
- `sunset-inner-span=1`
  half-distance between the two internal vertices
- `sunset-outer-span=1.6`
  distance from each internal vertex to its external endpoint
- `sunset-loop-looseness=1.35`
  controls how large the top and bottom arcs are
- `sunset-central-label=\hspace{1mm}`
  default central label when `central=...` is not set explicitly
- `sunset-central-label-yshift=-24pt`
  moves the central sunset label vertically
- `sunset-external-arrow-start=0.22`
- `sunset-external-arrow-end=0.78`
  choose how much of each external leg is covered by the momentum arrow
- `sunset-external-arrow-yshift=10pt`
  vertical offset for both external momentum arrows
- `sunset-loop-arrow-start=0.16`
- `sunset-loop-arrow-end=0.84`
  choose how much of each loop arc is covered by the top and bottom momentum arrows
- `sunset-top-arrow-yshift=22pt`
- `sunset-bottom-arrow-yshift=-15pt`
  vertical offsets for the loop momentum arrows
  these are literal signed TikZ-style offsets: positive is up, negative is down
- `sunset-middle-arrow-start=0.24`
- `sunset-middle-arrow-end=0.76`
  choose how much of the bridge line is covered by the middle momentum arrow
- `sunset-middle-arrow-yshift=12pt`
  vertical offset for the bridge momentum arrow
- `sunset-top-arrow-bend=18`
- `sunset-bottom-arrow-bend=18`
  controls the curvature of the top and bottom momentum arrows
- `sunset-left-label-position=above`
- `sunset-right-label-position=above`
- `sunset-top-label-position=above`
- `sunset-middle-label-position=below`
- `sunset-bottom-label-position=below`
  standard TikZ node placement for each momentum label
- `sunset-left-label-xshift=0pt`
- `sunset-right-label-xshift=0pt`
- `sunset-top-label-xshift=0pt`
- `sunset-middle-label-xshift=0pt`
- `sunset-bottom-label-xshift=0pt`
  horizontal nudges for the five sunset momentum labels
- `sunset-left-label-yshift=0pt`
- `sunset-right-label-yshift=0pt`
- `sunset-top-label-yshift=27pt`
- `sunset-middle-label-yshift=-1pt`
- `sunset-bottom-label-yshift=-12pt`
  vertical nudges for the five sunset momentum labels
- `sunset-momentum-layout=legacy|compact|balanced|wide`
  applies a preset to the top, middle, and bottom sunset momentum arrow and label shifts
- `sunset-label-layout=...`
  alias for `sunset-momentum-layout`
- `sunset-index-aware-momenta=true` or `sunset-index-aware-momenta=false`
  automatically pushes the top, middle, and bottom momentum labels away from occupied internal-index regions
- `sunset-index-aware-momentum=...`
  alias for `sunset-index-aware-momenta`
- `sunset-top-label-index-clearance=7pt`
- `sunset-middle-label-index-clearance=6pt`
- `sunset-bottom-label-index-clearance=4pt`
  per-line extra label clearance used when index-aware momentum adjustment is active
- `sunset-label-index-clearance=...`
  sets all three momentum-label clearances at once
- `sunset-internal-indices={a,b,c}`
  one propagator / contracted index for the top, middle, and bottom internal lines
- `sunset-propagator-indices={a,b,c}`
  alias for `sunset-internal-indices`
- `sunset-left-vertex-indices={a,b,c}`
  left-end internal-line labels for the top, middle, and bottom lines
- `sunset-right-vertex-indices={a,b,c}`
  right-end internal-line labels for the top, middle, and bottom lines
- `sunset-contracted-indices={a,b,c}`
  fills all three slots on each internal line with the same symbol
- `sunset-top-indices={a,\alpha,b}`
- `sunset-middle-indices={c,\beta,d}`
- `sunset-bottom-indices={e,\gamma,f}`
  explicit three-slot labels for one internal line: left-end, propagator, right-end
- `sunset-top-left-index=...`
- `sunset-top-propagator-index=...`
- `sunset-top-right-index=...`
- `sunset-middle-left-index=...`
- `sunset-middle-propagator-index=...`
- `sunset-middle-right-index=...`
- `sunset-bottom-left-index=...`
- `sunset-bottom-propagator-index=...`
- `sunset-bottom-right-index=...`
  slot-by-slot control for individual internal-line labels
- `sunset-top-contracted-index=...`
- `sunset-middle-contracted-index=...`
- `sunset-bottom-contracted-index=...`
  fills all three slots for one internal line with the same symbol
- `sunset-index-layout=tight|balanced|wide`
  high-level preset for internal-index slot positions and default offsets
- `sunset-internal-index-layout=...`
  alias for `sunset-index-layout`
- `sunset-internal-left-slot-position=0.16`
- `sunset-internal-propagator-slot-position=0.50`
- `sunset-internal-right-slot-position=0.84`
  positions of the three internal-index slots along each internal line
- `sunset-top-end-index-position=below`
- `sunset-middle-end-index-position=below`
- `sunset-bottom-end-index-position=above`
  node placement for the vertex-side internal-index slots
- `sunset-top-internal-index-position=below`
- `sunset-middle-internal-index-position=below`
- `sunset-bottom-internal-index-position=above`
  node placement for the centered propagator-index slots
- `sunset-top-left-index-xshift=-2pt`
- `sunset-top-right-index-xshift=2pt`
- `sunset-middle-left-index-xshift=-2pt`
- `sunset-middle-right-index-xshift=2pt`
- `sunset-bottom-left-index-xshift=-2pt`
- `sunset-bottom-right-index-xshift=2pt`
  separate horizontal nudges for the vertex-side internal-index slots
- `sunset-top-end-index-yshift=-1pt`
- `sunset-middle-end-index-yshift=-4pt`
- `sunset-bottom-end-index-yshift=1pt`
  shared vertical nudges for the vertex-side internal-index slots
- `sunset-top-internal-index-xshift=0pt`
- `sunset-middle-internal-index-xshift=0pt`
- `sunset-bottom-internal-index-xshift=0pt`
- `sunset-top-internal-index-yshift=-2pt`
- `sunset-middle-internal-index-yshift=-6pt`
- `sunset-bottom-internal-index-yshift=2pt`
  x/y nudges for the centered propagator-index slots
- `sunset-internal-index-style=...`
  extra TikZ node styling for all internal indices, for example `scale=0.9`
- `sunset-internal-index-size=normal|script|scriptscript`
  high-level size selector for all internal indices at once
- `sunset-vertex-index-size=normal|script|scriptscript`
  high-level size selector for the vertex-side index slots; the default is `scriptscript`
- `sunset-propagator-index-size=normal|script|scriptscript`
  high-level size selector for the centered propagator-index slots; the default is `script`
- `sunset-internal-index-math-style=\scriptstyle`
  prepends the same math style to all internal-index labels
- `sunset-vertex-index-math-style=\scriptscriptstyle`
  prepends a math style only to the vertex-side index slots
- `sunset-propagator-index-math-style=\scriptstyle`
  prepends a math style only to the centered propagator-index slots
- `sunset-internal-index-fill=white`
- `sunset-internal-index-inner-sep=0.6pt`
  background and padding controls for the internal-index nodes

### Index formatting

- `index-placement=sub`
- `index-placement=sup`
- `index-placement=none`

## Using TikZ-FeynHand Styles

The `line` key is passed directly to `tikz-feynhand`, so you can use its propagator styles, for example:

- `plain`
- `fer`
- `antfer`
- `sca`
- `pho`
- `glu`
- `bos`
- `scalarpolarized`
- `antiscalarpolarized`
- `scalarpolarizedin`
- `scalarpolarizedout`
- `antiscalarpolarizedin`
- `antiscalarpolarizedout`

Example:

```tex
\TwoPointCorr[
  line=fer,
  mode=p,
  leg-labels={\psi_i,\bar\psi_j}
]
```

`scalarpolarized` is defined in this package as:

- dashed scalar line
- transparent / open arrowhead
- arrowhead placed at the outer end of the leg rather than at mid-leg
- arrow tip points toward the central vertex
- compatible with `propagator-arrow-size` and `propagator-arrow-sizes`

The defaults are:

- `scalarpolarized` / `spol`: tip points inward
- `antiscalarpolarized` / `antspol`: tip points outward

Additional fixed-direction aliases are available:

- `spolin`, `spolout`
- `antspolin`, `antspolout`
- `scalarpolarizedin`, `scalarpolarizedout`
- `antiscalarpolarizedin`, `antiscalarpolarizedout`

You can also change the default behavior globally or per diagram:

```tex
\FourPointCorr[
  scalar-arrow-direction=out,
  scalar-arrow-position=0.15,
  anti-scalar-arrow-direction=in,
  anti-scalar-arrow-position=0.12
]
```

Allowed values for the direction keys are:

- `in`
- `out`
- `none`

## Global Defaults

If you want to set a default style once and reuse it, use:

```tex
\corrset{
  mode=q,
  field=\phi,
  line=sca
}
```

Then later:

```tex
\[
  \TwoPointCorr[indices={\mu,\nu},central=G^{(2)}]
\]
```

The local options passed to `\TwoPointCorr[...]` or `\FourPointCorr[...]` override the defaults from `\corrset`.

## Limitations

This package currently draws one fixed 2-point layout and one fixed 4-point layout:

- the 2-point diagram is a left-right correlator through a central point
- the 4-point diagram is a symmetric 4-leg object centered on one blob / vertex

It does not yet provide:

- distinct `s`, `t`, `u` channel templates
- loop topologies
- arbitrary manual graph construction
- arbitrary per-leg momentum placement geometry beyond the built-in layouts

For those cases, it is better to drop down to raw `tikz-feynhand` or define additional macros on top of this package.

## Files

- [correlator-diagrams.sty](/Users/aeaconnelly/Documents/LatexCode/correlator-diagrams.sty): the package
- [example.tex](/Users/aeaconnelly/Documents/LatexCode/example.tex): demo source
- [example.pdf](/Users/aeaconnelly/Documents/LatexCode/example.pdf): compiled demo
