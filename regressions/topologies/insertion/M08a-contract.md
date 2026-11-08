# M08a contact external self-energy bubbles

Frozen before implementation, 2026-11-07; base main 096b2b3.

Public interface: `FourPointCorr[insertion=bubble,insertion-slot=1]`; slots 1 UL, 2 LL, 3 UR, 4 LR. First verify slot 1, then expand the same host-relative renderer to all four. `contact-pairing=central` and `crossed` describe the same quartic host; disconnected horizontal/vertical pairings are invalid hosts.

Graph: C is quartic. Replace selected outer--C edge by outer--A, two parallel A--B arcs, B--C. Seven edges, four external degree-one nodes, interaction valences 4/3/3, cycle rank one. A/B must be distinct, ordered, collinear and strictly inside the selected leg. Outer frame stays +/-2.10; default insertion-position=.50, insertion-scale=.50. Invalid slots and non-fitting insertions must fail explicitly.

Reuse existing pre/post appearance, bubble arc styles, endpoint/external/post indices, caps, momentum ranges/visibility/directions, and per-contact momentum directions. Momentum defaults p1/p2 in, p3/p4 out. Curved labels face outward by geometry. Hide the insertion with external-legs=false; retain center-vertex/blob controls. Reset between consecutive diagrams. Test all slots, scales, reversed directions, mixed styles and explicit overrides.

References: checklist P4-01 and native deck S10-TL/TR/BL/BR (quartic host plus two trivalent insertions). No seagulls, simultaneous insertions, internal exchange corrections or index appearance redesign.
