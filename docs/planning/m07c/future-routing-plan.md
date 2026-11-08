# R14/R22: historical future implementation slice

**Superseded 2026-11-08:** the user selected exactly two half-moon crossed-vertex
views. Their [implemented contract](../crossed-vertex/contract.md) preserves the
fixed-slot graphs with a different embedding/API. The proposed values below
were never implemented. This file preserves the original audit recommendation.

This plan records the gap established by M07c. **No package implementation is
included; the follow-up is unscheduled.** It is separate from the user-deferred
R04 right external crossing on the ordinary box. The next scheduled session is
M08a contact-leg bubbles unless the user chooses this follow-up instead.

## Reuse the existing triangle-contact family

Both reference panels have three interactions (one quartic and two cubic),
seven propagator edges and one cycle. Reuse `TriangleContactCorr` and its
logical slots 1-7. Do not add a fourth interaction to force a box or replace
this with a regular tree-attached triangle.

A proposed interface is to extend the existing orientation choice with
`top-crossed` and `bottom-crossed`. These are **proposed values, not currently
accepted API**. Freeze the exact names before implementation; retain the four
working orientation values, aliases and defaults.

1. **Top-crossed / S13-left:** Q is the top quartic vertex, A/B are bottom
   left/right. External hosts: 1->Q, 2->A, 3->B, 4->Q. Internal slots:
   5 Q->A (W), 6 A->B (Z), 7 B->Q (W). Break external slot 4 at its
   intersection with continuous slot 3; the crossing is not an interaction.
2. **Bottom-crossed / S13-right:** A/B are top left/right, Q is bottom quartic.
   Hosts: 1->A, 2->Q, 3->Q, 4->B. Slots: 5 A->B (Z), 6 A->Q (W),
   7 Q->B (W). Break external slot 3 at its intersection with continuous
   slot 4. Same vertex valences, edge count and one-cycle invariant.

Start with the first layout and verify it before adding the second. The slot
maps are also recorded in `routing-map.json`.

## Geometry and metadata contract

- Keep outer corners +/-2.10 and compact coordinate baseline .8. Existing
  `triangle-contact-xspan=1.1,triangle-contact-yspan=1.1` demonstrates the PDF's
  square bounding-frame preference. Exact visual tuning remains reviewable;
  preserve old geometry and independent explicit span overrides.
- Derive the external crossing/gap from actual endpoints; do not assume a .5
  intersection or allow a path to pass through another interaction dot.
- Reuse the full-leg external style/cap/semantic-marker pipeline and a narrow
  split-stroke callback, as already established for M07b. No caps, indices,
  circles or raw legacy Proca tips belong at artificial gap endpoints.
- Update external host aliases used by indices/labels as well as the strokes.
  Preserve logical field styles, marker sizes/colors, species-circle controls
  and all seven momentum slots. Default external momenta remain p1/p2 incoming,
  p3/p4 outgoing. Explicit reverse/hide controls remain authoritative.
- Resolve quartic-side annotation defaults from the actual quartic pair, not
  only the old orientation name; retain M02's per-slot positioning keys.
  Preserve D01 index attachment without expanding into its appearance review.

## Acceptance before completing the feature

Compile plain target graphs with numbered endpoints; independently recover
seven logical edges, valences 4/3/3, one cycle and quartic pairs 1/4 and 2/3
from actual PDF paths. Verify Z on slots 6 and 5 joins the complementary
q2/q3 and q1/q4 cubic vertices. An unlabeled graph isomorphism or changed
outer label text is not sufficient to claim fixed-slot support.

Exercise EW, pink Proca/scalar polarization, explicit circles, single/double
outer caps, momentum gap/side layouts, reversal/hiding, indices, representative
scales, explicit span overrides, and consecutive-call reset. Inspect crossing
clarity and marker contact without unnecessary decorations in topology cases.
Run the maintained suite, add focused coverage, then update atlas/recipes and
R14/R22 together. Count the two source panels as variants of one existing
family extension, not two new loop families.
