# M05: external swordfish insertions

Baseline: published main efb5fae; branch codex/m05-swordfish. R12, S08-L1
(upper-left t-tree), S08-L3 and S05-L1/L3; slide 9 is annotation context.

For selected external endpoint E and tree vertex H, replace E--H by E--A
and two distinct parallel A--H curves. H is the actual existing tree vertex,
now quartic; A is new and trivalent. The other tree vertex is trivalent.
The graph has seven propagator edges, three interaction vertices, four external
endpoints and one independent cycle. No A--B--H bridge, duplicate H dot,
zero-length edge, self-loop or overlapping distinct vertices is permitted.

Public API: TTreeChannelCorr / STreeChannelCorr with insertion=swordfish and
insertion-slot=1..4, one insertion at a time. Logical slots stay UL/LL/UR/LR;
exchange stays 5. Reuse insertion-pre-line for E--A (inheriting selected logical
style and outer cap), bubble-top-line / bubble-bottom-line for A--H curves,
bubble-momenta and bubble-endpoint-indices for their two directed arc slots.
Only one selected external momentum guide is drawn, on E--A; p1/p2 enter,
p3/p4 leave. Both loop guides are independent. show-channel-momentum applies.

Default A is halfway along E--H. insertion-position selects this location at
standard insertion-scale=0.66. Scale multiplies the A--H chord about fixed H:
A fraction from E is 1-(1-position)*scale/0.66. Keep A strictly inside E--H in
acceptance examples. swordfish-opening-angle=60 gives distinct loop tangents
at the quartic point; bubble-loop-looseness remains available. Arc a leaves A
at host-angle+opening and enters H from host-angle+180-opening; b is mirrored.

bubble-external-indices supplies two annotations on the sole E--A segment
(fractions 0.18/0.82); four bubble-endpoint-indices retain A/H ownership for
both loop edges. Existing exchange and other external indices are preserved.
D01 appearance remains deferred. There is no post segment: insertion-post-line,
post momentum and post indices are inactive and are not claimed as supported.
Insertion orientation is a seagull control; swordfish arc sides follow the
host axis. U/contact/internal slot 5 and simultaneous insertions remain unsupported.

Implement/verify T1, then T2/T3/T4, then S1/S2/S3/S4. Per slice require actual
graph/valences/shared H, host/slot isolation, geometry/scale, mixed styles,
white-filled Proca/scalar endpoint contact, momentum visibility/reversal/blank
labels, outer-only caps, loop/external index values/ownership and state reset.
Render plain and labeled examples without unrelated decorations. Run the full
maintained suite, update atlas/reference/requirements/handoff and checkpoint
locally. Publication remains a separate user-authorized action.

The external-legs master switch suppresses the insertion with its selected
external leg. Legacy outer placeholder dots remain unchanged. Final acceptance:
167 focused public cases; eight independent PDF graphs; 32 Proca + 16 scalar
endpoint contacts; 41 maintained documents / 736 total endpoint contacts.
