# Deferred workflow reviews

## D05 - Common annotation names across topologies

**Source:** user's request on 2026-11-13, following the three-point leg-label controls.
**State:** nested external-leg `label-style` implemented, verified and published on main;
broader naming/refactoring workflow remains deferred.

Use the same public name for the same concept across diagram families. Geometry
and placement defaults should be resolved from the topology, rather than exposed
through a separate family-prefixed name for every equivalent control. Review
leg labels first, then the equivalent momentum and index annotation concepts.
Keep label text, label placement, propagator appearance and geometry distinct.

The user specifically found `three-point-field-label-N-style` and the proposed
`three-point-leg-label-N-style` unnecessarily long. Prefer the established
`leg-labels` vocabulary and use the existing list's slot order instead of
repeating the topology and leg number in each key.

Implemented external-leg syntax:

```tex
leg-labels={Z_\alpha,W^+_\gamma,W^-_\beta},
leg-styles={
  {ewboson,endcapp,label-style={xshift=-2pt,yshift=3pt}},
  {ewboson,endcap,label-style={xshift=5pt,yshift=3pt}},
  {endcap,spol,label-style={yshift=-3pt}}
}
```

The nested options are extracted once per logical leg and routed to the displayed
leg label's separate TikZ node. They are removed from propagator styles. Bare
`xshift`/`yshift` on existing propagator styles retain their original meaning.
The common syntax covers the shared external-label renderers, with topology-specific
placement defaults. Earlier three-point keys remain compatible; an explicit nested
style replaces the whole legacy style for its slot. See
[implementation and verification](leg-label-styles.md).

For the remaining annotation API review, agree on canonical names and precedence, map the existing
logical slots, preserve old spellings as compatibility aliases, and verify
global/local settings, orientation changes, insertion/split-leg ownership and
cache invalidation. The same controls should work wherever the same annotation
concept exists, with topology-specific default placement. This naming workflow
does not itself authorize retuning the D01 index appearance or other diagram
geometry. No broad momentum/index API rewrite has been started.

## D01 - Systematic index-label placement review

**Source:** user's request after M03a, 2026-11-03.
**State:** acknowledged, deliberately deferred to a separate later workflow session.

Index labels currently have messy positions in the rendered diagrams. Preserving
the correct labels, logical slots, endpoints and existing controls does not imply
that their placement is visually finished. Audit and improve their positions
systematically across the package in a dedicated later session.

This is not part of M03b or the current feature-implementation sessions. Do not
retune index positions, anchors, offsets or defaults while implementing the
s-channel bubbles. Preserve working index attachment and public controls; record
placement problems without expanding the current slice to fix them.

When this later workflow is explicitly started, collect representative minimal
index examples across orientations/styles, define consistent placement rules,
inspect rendered output, and add focused regressions. Reconcile the atlas and
reference after the placement work is verified. No implementation is included
in this note.

## D02 - Crossed-box circles and per-line circle styling

**Source:** user's report during M07b, 2026-11-07.
**State:** fixed and published on main with M07b/M07c (2026-11-07). The original
D02 verification checkpoint, based on `e64cc2f`, is retained as historical evidence.

Bare Proca lines now add no circle. Explicit `circ=...`, `circ={}` and topology
circle labels still work. The manual placement pass reapplies each logical
line's resolved style in a scope, preserving scale/color/fill/label styling
without propagator endpoint decorations on the circle nodes. Explicit hiding
and fresh-call reset remain effective; topology circle-position keys are retained.

The user's exact [reproducer](reproductions/d02-cross-box-circles.tex) now
produces two W circles, each with radius 3.587 PDF pt and text scaled by .6.
The historical [observed geometry](reproductions/d02-cross-box-circles-observed.json)
records the original three circles, all radius 5.978 PDF pt. That historical
record is preserved rather than overwritten.

See [verification](d02-verification.md), the
[before/after comparison](../../regressions/topologies/cross-box/cross-box-circle-comparison.pdf)
and [three-page regression gallery](../../regressions/topologies/cross-box/cross-box-circles.pdf).
Both layouts, per-slot scales/colors, aliases, manual labels, explicit Proca
circles, hiding and consecutive-call reset are checked from actual PDF output.

## D03 - Upper external crossing versus top-edge W circle

**Source:** user's request to inspect EW upper external legs and an EW top
internal edge with `circ=W`, 2026-11-07.
**State:** demonstrated crowding; no geometry/default change made in this review.

At diagram scale 1, a default-size centered W circle overlaps the continuous
upper EW leg by about 0.47 PDF pt. Smaller centered circles help; widening the
split-leg gap alone does not clear the other leg. Off-center circles can make
the crowding worse. See the [18-case visual/geometry review](upper-crossing-w-review.md).
D03 is independent of the completed D02 scaling/unsolicited-circle fix.

The later user-selected circle default .8 improves the centered diagram-scale-1
case (about .73 pt clearance). The .8 diagram-scale case remains very tight;
D03 is still an open spacing review. See [circle-default verification](circ-default-verification.md).

## D04 - Coincident raw charge-arrow/circle decorations

**Source:** measured during M08b, 2026-11-08. **State:** recorded for a later
style/decorator cleanup; no geometry or public-interface change in this slice.

Combining raw `with arrow=.5` and `circ=W` on the same EW loop paints both
markings twice at identical coordinates. A probe against published baseline
`35c7959` reproduces the same two coincident W rings on an existing s-tree
seagull. This predates contact seagulls. The eight source-variant panels have
44 distinct charge arrows (48 paints) and eight distinct species circles
(12 paints). Visible positions, connectivity and species/flow are correct;
PDF text extraction also repeats W on the four charged loops. The focused
checker records both physical paints and distinct visible positions rather
than treating repeated paint as an extra graph feature.

If addressed later, isolate the marking postactions while preserving existing
EW paths, visible arrow/circle placement, label size/color and option-order
compatibility. Use a minimal raw/tree/contact comparison and then regenerate
the named source-variant examples. This is separate from D01 index appearance
and D03 crossed-leg/circle spacing; do not expand M09 into this cleanup.
