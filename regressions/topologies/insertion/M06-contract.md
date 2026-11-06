# M06: regular tree-attached triangles

Baseline: published main eb6182c; branch codex/m06-tree-triangles.
Requirement R08: S05-L2 (T bottom), S08-L2 (T top), S06-L2 (S left),
S07-L2 (S right). The original reference images are unchanged.

Replace one tree interaction H by A/B/C. A and B each carry one of H's
external legs; C connects to opposite tree interaction O through the exchange.
Loop edges are A--B, B--C, C--A. O keeps its other two external legs.
There are eight propagators, four trivalent interaction vertices, four external
endpoints and one cycle. No quartic point, overlapping vertex, self-loop,
parallel pair or contracted bridge is permitted. Triangle-contact is a
different graph. Use the package's established line/marker/annotation helpers.

Public API: TTreeChannelCorr / STreeChannelCorr with insertion=triangle and
tree-triangle-side=bottom|top|left|right.
Auto defaults to bottom for T and left for S. Only T top/bottom and S left/right
are supported. Incompatible sides and U/contact hosts do not activate it.
This is a vertex correction, not an external insertion: insertion-slot,
insertion-pre/post controls, insertion-position/orientation/scale, and bubble
or seagull controls do not specify this graph. Simultaneous corrections are
outside scope. external-legs=false retains the internal triangle and exchange,
removing only external propagators, as for standalone loop topologies; the
legacy four outer placeholder dots remain.

Slots remain external 1=UL, 2=LL, 3=UR, 4=LR and exchange 5, directed top to
bottom (T) or left to right (S). Loop 6=A--B, 7=B--C, 8=C--A. A/B are left/right
(T) or top/bottom (S). Base A/B lie tree-triangle-outer-shift beyond the old H;
C lies tree-triangle-depth toward O; A/B lie +/-tree-triangle-half-width across
the channel axis. Defaults: depth .75 and outer-shift .60 in TikZ coordinate units.
Half-width defaults to auto: (depth+outer-shift)/sqrt(3), giving equal side
lengths. An explicit half-width permits other shapes. Choose geometry with separated vertices and positive bridge.

External styles/flow/caps and exchange style/channel indices retain their
logical ownership. tree-triangle-loop-line is a grouped fallback;
tree-triangle-line-6/-7/-8 override it independent of key order. Empty fallback
inherits the global/logical line. Existing semantic endpoint markers must touch
both true endpoints, and caps appear only on outer ends.

All eight momentum annotations use measured-gap/continuous-side rendering and
actual triangle-centroid outside normals. External labels/flow/hiding remain
standard (p1/p2 in, p3/p4 out); channel label/show-channel-momentum retain their
meaning. tree-triangle-momenta={k,ell,q} independently names loop 6/7/8; blank
loop entries hide their guides. tree-triangle-momentum-N={...}, N=1..8, supplies
independent layout, range, fraction, offset, side, label shifts/anchor and
forward/reverse/none direction. External blank labels retain unlabeled arrows.
Loop defaults follow A--B--C--A; reverse overrides must retain geometric side.

Two endpoint-index lists, tree-triangle-propagator-left-indices and
-right-indices, map 1..8 in the stated directions. Existing topology index
placement/style controls are mirrored with the tree-triangle prefix. Preserve
standard field indices and exchange channel-indices; D01 visual polish remains
deferred. Tests establish values/order/edge ownership, not satisfactory spacing.

Implement and gate T bottom, T top, S left, S right in sequence. Each gate
checks graph/slot mapping, geometry, style/flow/cap/index ownership, marker
contact and mixed styling, annotation visibility/direction and state reset.
Render four plain and four annotated acceptance examples, plus isolated
Proca/scalar contact tests. Inspect every delivered page. Run the maintained
suite, update inventory/reference/requirements/roadmap, checkpoint locally and
report merge/push state separately. Do not implement M07 or D01 in this session.

The user review requests equilateral default triangles. Auto half-width derives
from height in all four orientations, including custom depth/outer shift. Bare
spol/antspol and their long aliases on these new internal edges use the semantic
end marker so tips meet vertices; legacy topology rendering is untouched.

Final gate: 183 focused public cases, four independently reconstructed
equilateral PDF graphs, 24 Proca + 12 scalar contacts, and all 42 maintained
documents / 772 total endpoint contacts pass. Atlas: 94 recipes / 21 pages;
the prior nineteen page bodies retain the published rendering.

The subsequent review requests larger loops and wavy styled exchanges. Increase
default outer shift to .60: each equilateral side is 50% larger than the first
preview, with the bridge tip fixed. On corrected T sides, extend outer endpoints
when needed to leave .28 axial clearance beyond the base; fourpoint-yspan is
a minimum extent there. Styled gallery/atlas exchange lines use EW waves.
