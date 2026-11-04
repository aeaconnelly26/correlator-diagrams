# M04: external seagulls on s/t trees

Baseline: published main `b4a6ad8`; branch `codex/m04-seagull-expansion`.
Requirement R11: PDF P2-05/P3-03; deck S05/S08 t-tree and S06/S07 s-tree
seagulls, repeated species variants on slides 20/21 (see source-coverage.md).

Public interface: `\TTreeChannelCorr` or `\STreeChannelCorr` with
`insertion=seagull,insertion-slot=N`, N=1-4, one insertion at a time.
Slots remain upper-left/lower-left/upper-right/lower-right. T slots 1/3 join
the upper tree vertex; 2/4 the lower. S slots 1/2 join left, 3/4 right.
Exchange remains logical slot 5. Preserve the original t-slot-1 prototype.

Replace selected E--H by E--V and V--H plus ONE closed self-loop V--V.
V is one new quartic vertex (a self-loop contributes two incidences).
The complete graph has seven propagator edges, three interaction vertices,
four external endpoints and one loop. Do not create a stem or two separate
bubble vertices. Coordinate aliases A/B may coincide with V to reuse the
pre/post momentum controls, but draw V only once and draw no A--B bubble arc.

Extend host-relative helpers incrementally: verify T1, then T2, T3, T4,
then S1, S2, S3, S4. Keep host slot styles/arrow sizes, outer-only single/double
caps, pre/post overrides, logical momentum visibility/direction, independent
loop momentum, existing endpoint/index controls and consecutive-call isolation.
Loop marker sizing remains local slot 3. Keep the existing 9pt seagull momentum
offset; bubble offsets remain unchanged.

`auto` now faces all T loops inward and all S loops outward (user review,
2026-11-04): +90 for logical slots 2/3, -90 for 1/4.
`top` selects +90, `bottom` selects -90 relative to outer-to-host direction;
`left`/`right` select absolute page angles 180/0. Preserve those meanings.
Momentum-label side follows the physical loop normal, including reversal.
No reflection of text or swapping logical index values.

D01 is excluded: preserve index values/attachment/controls without retuning
positions, anchors, offsets or defaults. Index appearance remains unfinished.
Internal slot 5, u-tree/contact hosts, multiple simultaneous insertions,
swordfish and stemmed tadpoles are outside this milestone.

Acceptance per slice: seven-edge graph and valences; selected V lies on the
selected external edge; untouched other endpoints; self-loop closure; scales
and insertion geometry; explicit orientations; mixed EW/Proca/scalar styles;
marker counts/contact/white fill/color; independent host/loop momenta,
hide/blank/reversed flow; outer caps only; index attachment; fresh calls.
Compile focused public-interface checks before enabling the next slot. Inspect
the rendered gallery/atlas, run the maintained suite, update R11/reference/
recipes/handoff and save a local checkpoint. Publication is a separate step.

## User review acceptance - 2026-11-04

Default external flow is 1/2 in, 3/4 out, with default symbol p. Keep explicit
flow overrides and reversed-flow tests, but visible standard examples use the
requested flow. Shorten pre/post guides without extending past the outer end;
measure outside label clearance perpendicular to the edge, including the full
text rectangle. Apply this shared correction to bubble and seagull insertions.
Preserve the explicit range, extension, offsets, anchors and page-axis shifts.
D01 remains excluded. Refresh the atlas and focused insertion PDFs.

Second screenshot review: short bubble host pieces expand automatically toward
12pt arrows, capped at 90% of available segment length; long seagull guides
stay compact. Explicit ranges/extensions win. Only S-tree bubble loop labels
move to measured normal placement (4pt text-rectangle clearance); T bubble
loop placement and arrow offsets remain unchanged. Preserve explicit label
distance controls. Verify both the minimum readable span and compact maximum.

Seagull-k follow-up: use concentric momentum geometry around the actual loop
center. Default label fraction auto means the arrow-range midpoint; numeric
fractions remain explicit overrides. Labels clear the full text rectangle on
the local tangent normal, independently of rotation and reversal. Verify paired
loop/arrow samples as well as actual label rectangles. Bubble annotations and
all loop propagators remain unchanged in this correction.

Compact-annotation follow-up from 841b93e: seagull momentum defaults are
start 0.30, end 0.52, radial offset 6pt, text clearance 2pt. The shared
midpoint remains 0.41. Preserve concentricity/local normals and explicit
overrides; do not alter bubble annotations or index placement.
