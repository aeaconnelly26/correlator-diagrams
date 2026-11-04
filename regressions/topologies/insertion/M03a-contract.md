# M03a: external t-tree self-energy bubbles

Baseline: `b917ed2`; branch `codex/m03a-t-tree-bubbles`. Requirements R09/R10.
Implement slots 2, 3, 4 incrementally after preserving slot 1. One insertion.

Public recipe: `\TTreeChannelCorr[insertion=bubble,insertion-slot=N,...]`, N=1-4.
Slots stay upper-left, lower-left, upper-right, lower-right; exchange is slot 5.
Replace only the selected external edge E--H with E--A, two parallel curved
edges A--B, then B--H. A and B are distinct trivalent insertion vertices; H is
the original tree vertex. The graph has four external ends, four interaction
vertices and eight propagator edges. No extra edge crosses the bubble interior.

Use translated/rotated endpoint coordinates without reflecting text or swapping
logical a/b labels. Bubble a is the +90-degree arc of outer-to-host direction;
b is the -90-degree arc. Retain bubble-local slots 3/4 for arc arrow sizes and
all existing bubble-* style, momentum and endpoint-index controls. Host pre/post
segments inherit the selected logical leg's style and arrow size. Pre has the
outer caps; post has no external caps. Momentum labels/visibility/directions
use the selected leg's logical slot, not hard-coded slot 1. The channel remains
slot 5. Existing page-axis label/index shifts remain page-axis values.

No seagull expansion, s-tree insertion, internal-exchange insertion, swordfish,
simultaneous insertions, or public API rewrite. Unsupported host/slot combinations
retain their existing no-op behavior and are documented as unsupported.

Check one new placement before enabling the next. Acceptance: actual edges and
vertices, selected-leg geometry/order, unchanged unselected legs, inherited and
mixed styles, Proca contact, caps only on external ends, independent bubble/host
indices and momenta, reversed directions, hidden/blank momenta, scales, explicit
geometry/position settings, and fresh consecutive calls. Compare slot-1 output
with baseline, run the maintained suite and endpoint audit, inspect the focused
PDF, and update the public recipe inventory and requirement status.
