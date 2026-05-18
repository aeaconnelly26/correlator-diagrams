# Correlator Diagram Macros

![Correlator channel showcase](assets/readme-hero.png)

Reusable LaTeX macros for QFT correlators, contraction classes, amputated vertices, loop bubbles, exchange channels, and sunset diagrams.

This package is built for real notes and assignments where you want clean, repeatable Feynman-style figures without rewriting raw TikZ every time.

## Highlights

- `\TwoPointCorr`, `\FourPointCorr`, and `\SunsetDiagram` as the core entry points
- one-loop `s`, `t`, and `u` channel bubbles via `\SChannelCorr`, `\TChannelCorr`, and `\UChannelCorr`
- explicit tree-level exchange topologies and contact pairings
- amputated correlators with endpoint vertices via `external-legs=false` or `amputated`
- per-leg and per-internal-line styling, including global `color=...`
- built-in palette colors `fieldA` and `fieldB`
- external momentum flow presets such as `left-in-right-out`

![Contact pairing showcase](assets/readme-pairings.png)

## Quick Start

Place `correlator-diagrams.sty` next to your document or in your local `texmf` tree, then load:

```tex
\usepackage{amsmath}
\usepackage{correlator-diagrams}
```

The package depends on standard LaTeX tools plus `tikz-feynhand`, all of which are loaded internally.

Main demo files in this repository:

- [`example.tex`](example.tex)
- [`channel-topology-regression.tex`](channel-topology-regression.tex)
- [`sunset-example.tex`](sunset-example.tex)
- [`simple-sunset.tex`](simple-sunset.tex)

Compile with:

```sh
pdflatex -interaction=nonstopmode -halt-on-error example.tex
```

## Core Macros

```tex
\TwoPointCorr[...]
\FourPointCorr[...]
\SunsetDiagram[...]
```

Common wrappers and aliases:

```tex
\SChannelCorr[...]
\TChannelCorr[...]
\UChannelCorr[...]
\STreeChannelCorr[...]
\TTreeChannelCorr[...]
\UTreeChannelCorr[...]
\SunsetDiag[...]
```

## Examples

Minimal 4-point correlator:

```tex
\[
  \FourPointCorr[
    field=\phi,
    indices={a,b,c,d},
    central=\Gamma^{(4)}
  ]
\]
```

Amputated contact pairing with colored contractions:

```tex
\[
  \FourPointCorr[
    external-legs=false,
    center-vertex=false,
    show-momenta=false,
    contact-pairing=horizontal,
    leg-styles={{plain,fieldA},{plain,fieldB},{plain,fieldA},{plain,fieldB}},
    field=x,
    indices={1,2,3,4},
    central=\Gamma^{(4)}_{1212}
  ]
\]
```

One-loop `s` channel with left-in/right-out momentum flow:

```tex
\[
  \SChannelCorr[
    external-momentum-flow=left-in-right-out,
    field=\phi,
    indices={a,b,c,d},
    color=fieldA,
    loop-channel-top-line={plain,fieldB},
    loop-channel-bottom-line={plain,fieldB},
    central=\Gamma^{(1)}_{s}
  ]
\]
```

## Documentation

- Start with [`example.tex`](example.tex) if you want copy-paste examples.
- Use [`docs/reference.md`](docs/reference.md) for the full macro and tuning reference.
- Use [`channel-topology-regression.tex`](channel-topology-regression.tex) to inspect channel layouts in isolation.

The full reference covers:

- slot order and leg ordering
- momentum labels and arrow tuning
- loop-channel and sunset layout controls
- line styles, vertices, colors, and scalar-polarized legs
- one-loop `s/t/u` channels, tree channels, and sunset diagrams

## Repository Layout

- `correlator-diagrams.sty`: package source
- `example.tex`: broad feature gallery
- `channel-topology-regression.tex`: focused channel regression cases
- `sunset-example.tex`: sunset-specific examples
- `assets/`: README graphics

## License

[MIT](LICENSE)
