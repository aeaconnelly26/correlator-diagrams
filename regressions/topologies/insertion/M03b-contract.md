# M03b: external s-tree self-energy bubbles

Baseline: published main `6549efa`; branch `codex/m03b-s-tree-bubbles`.
Requirement R10; M03a remains a compatibility control.

Public recipe: `\STreeChannelCorr[insertion=bubble,insertion-slot=N,...]`.
Enable and verify slots 1, 2, 3, 4 in that order, one insertion at a time.
Slots remain upper-left, lower-left, upper-right, lower-right. Slots 1/2
attach to the left tree vertex; 3/4 attach to the right. Exchange is slot 5.
Replace only E--H with E--A, two parallel curved A--B edges, and B--H.
Four external ends, four interaction vertices, eight propagator edges; A/B
are distinct trivalent vertices, separate from the original tree vertices.

Reuse the semantic host-relative construction and controls without a public
API rewrite. Preserve selected logical host style/arrow size, pre/post overrides,
outer caps only, momentum values/visibility/directions, independent loop labels,
endpoint indices, and explicit geometry. Arc a is the +90-degree outer-to-host
arc, b is the -90-degree arc, retaining local arc arrow-size slots 3/4.
The s-tree exchange remains horizontal. Ordinary s/t/u trees and t insertions
must retain their output. Seagulls remain t-tree slot 1 only.

D01 is explicitly excluded: index positions are accepted temporarily and need
a separate later workflow. Verify values, attachment and control preservation;
do not retune index anchors, offsets, defaults, or appearance in this milestone.

Acceptance per slot: actual topology and geometric ordering, unselected legs,
styles and mixed propagators, Proca tip contact, outer caps, momentum labels,
hidden/blank and reversed momentum, index attachment, representative scales,
explicit insertion position/scale, and consecutive-call state reset. Loop arrows
retain 8pt base clearance plus style allowance; labels face outward with reversal
and explicit offsets preserved. Run focused checks before enabling the next slot.
Compile the maintained suite, inspect the gallery, and update the atlas and
requirements. Unsupported u-tree/internal insertions stay unsupported.
