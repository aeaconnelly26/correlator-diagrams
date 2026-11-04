# M02 verification - independent triangle-contact annotations

Baseline: synchronized local/GitHub `main` at `6657735`.
Implementation branch: `codex/m02-triangle-contact-annotations`.
Requirement: R06; retain R07's four graph layouts. M02 sessions A-C are complete.
Verified code checkpoint: `8f95755`. This slice was fast-forwarded into main
and published to GitHub on 2026-11-03. Code, regression sources and PDFs are
identical to that checkpoint; closeout changes only publication/handoff records.

## What changed

`triangle-contact-momentum-1={...}` through `triangle-contact-momentum-7={...}`
provide independent ranges, perpendicular arrow clearance, label fraction,
arrow break, label-only offset/shifts/anchor, and side. The `trianglecontact-*`
aliases are retained and extended. Grouped settings supply unspecified fields;
slot fields win regardless of key order. Options reset for each diagram.

The former hard-coded assignments overwrote explicit grouped settings on
external slots 2/4 and internal slots 5-7. Explicit settings now really affect
all selected slots. Some earlier internal labels faced inside the triangle;
sides now use the actual centroid and directed edge. Reversing an arrow retains
its side and label coordinate frame.

The first M02 checkpoint `b795f7f` moved external labels off-axis while leaving
wide fractional breaks behind. The user's screenshot review demonstrated that
this was incorrect. Reviewed defaults now put labels in their gaps and measure
the actual rendered node to size each break, with 0.8pt padding per side. External
arrows are compact (up to 24pt in diagram units), with the two quartic-side centers
at 0.30 from their outer endpoints and other external centers at 0.50. This follows
orientation rather than hard-coding slots 2/4. Internal default ranges remain.

`triangle-contact-momentum-layout=side` draws continuous arrows with outward
labels, using automatic boundary anchors and 3pt clearance. Slots can override
the global layout independently. Gap mode centers its break on the actual node;
an intentionally shifted off-axis label no longer leaves an empty break. Very
wide labels/short legs can still need explicit ranges or side layout.

Other topology momentum renderers are unchanged. Triangle-contact uses the
existing momentum font/fill/style, arrow-size, direction, visibility, and label
interfaces. Propagator/style/index code and endpoint code were not modified.
No topology, insertion placement, or connectivity was added.

The exact slot endpoint map, public interface, and acceptance matrix are in
the [contract](../../regressions/topologies/triangle-contact/M02-contract.md)
and [reference](../reference.md#triangle-contact-topology).

## Automated evidence

- **35 maintained regression/example documents pass**, including old triangle
  recipes, momentum direction/visibility and blank-label assertions, indices,
  one-sided markers, insertions, and the new focused regression.
- **97 complete public diagrams** in the focused regression have automatic
  geometry/behavior checks. All seven slots are altered independently in all
  four orientations with unequal spans. Unselected annotations stay identical.
- Outside-side checks observe emitted arrow coordinates relative to edge and
  centroid half-planes. Additional calls cover scales 0.72/1.2, grouped settings,
  aliases/key order, label-only motion without arrow motion, reversal without
  side flips, selected/hidden annotations, momentum off, and state reset.
- The independent PDF-vector audit still passes **600 automatic Proca endpoint
  contacts**. M02 does not relax or modify its checker.
- Review checks compare actual node centers with default gap midpoints to
  0.01pt, bound default breaks for the standard p/k labels to 18pt and external
  arrows to 24.01pt, and verify quartic-side fractions by vertex endpoints.
  Stroke counts require two strokes for a gap and one continuous stroke for
  side labels/off-axis labels. Global/per-slot layout mixing and aliases pass.
- Default internal direction checks compare against actual vertex connectivity
  in all four orientations, in both layouts: both quartic-incident edges point
  toward their trivalent endpoints. The third internal direction is unchanged.
  Explicit direction overrides remain effective; `auto` selects the default.

Reproduce the maintained suite with a Python interpreter containing `pypdf`:

```sh
FEYNMANFUN_PDF_PYTHON=python3 scripts/check-regressions.sh
```

The final full suite passed after the final package change. The focused regression
was additionally recompiled with the final break-width guard and revised examples.
The package hash
and counts are in [the check record](m02-checks.json).

## Rendered evidence and inventory

- [Focused gallery](../../regressions/topologies/triangle-contact/triangle-contact-annotations.pdf):
  five pages, 20 minimal examples; all orientations, unequal geometry/mixed
  lines, individual external/internal controls, and hidden/blank entries.
- [Current atlas](../diagram-inventory/inventory.pdf): eleven pages, 51 recipes;
  T01-T04 demonstrate independent controls; T05-T08 demonstrate side layout.
- [Recipes](../diagram-inventory/recipes.md): generated copy/paste examples.

All pages were rendered and inspected for labels, arrow directions, vertex
connectivity, clipping and crowding. The diagnostic avoids unnecessary endcaps
and circles. The existing atlas style appendix retains its purpose-specific
cap/circle examples. Historical diagnostic PDFs retain their stated baselines;
the current new gallery and atlas demonstrate M02 behavior.

## Limits and next step

This is manual placement control, not automatic label collision avoidance for
arbitrary text or degenerate geometry. Long labels, very short arrows, and
labels manually shifted toward the graph can require tuning. Fractions remain
relative to each directed edge, so unequal lengths can be adjusted separately.
Per-slot blocks replace earlier blocks for the same slot; unspecified fields
inherit grouped settings. A negative offset or explicit side can intentionally
put annotations inside. No other topology receives these new slot keys.

M03a is next: external self-energy bubbles on the remaining t-tree legs, starting
with a narrowly defined slot-2 case. Create its feature branch from synchronized
main, which now includes M02 checkpoint `8f95755`. No manual merge is pending.
