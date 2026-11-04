# Future coding milestones

Baseline: `0dbf733`, inventoried on 2026-11-03. These are future feature
sessions, not changes made by the inventory work. R IDs refer to
[requirements](requirements.md); S IDs refer to [reference panels](source-coverage.md).

## Integration correction - before the next coding milestone

The unmerged `codex/seagull-insertion` branch already contains the slot-1
seagull prototype and earlier endpoint/momentum/index work. See
[branch integration](branch-integration.md). Reconcile that branch with M01
before M02; then reassess this queue against the integrated package. M04 is
an expansion of an existing prototype, not a fresh implementation.

## Common session contract

Before coding, freeze a small contract: the reference panel(s), graph
vertices/edges, external slot order, supported host/placement combinations,
public options, preserved aliases, and a short plain/labeled acceptance gallery.
Store this contract beside that milestone's regression source. Trace crossings
explicitly; a visually similar but differently connected graph is a failure.

Use logical slot metadata and package-owned insertion geometry. Keep changes
local, reuse existing helpers where proven, and preserve public options and
intentional tuning. Do not begin with a broad index/momentum rewrite. New
controls must have documented precedence over existing grouped defaults and
must reset between diagram calls.

Diagnostic examples include only the feature being tested. Omit endcaps and
independent circles unless that particular example is a cap/circle test.

Each slice finishes with:

1. A focused TeX regression containing the plain graph and a labeled mixed-style case.
2. A PDF rendered and inspected at normal size and at endpoint/label detail.
3. Relevant checks for momentum on/off, reversed flow, indices, single/double
   outer caps, scale, and consecutive diagrams; use only meaningful variants.
4. The maintained regression suite passing, with the stable new regression registered.
5. Updated public reference, copy/paste recipe, requirement status, and atlas
   entry/PDF where a capability has actually become available.
6. A local checkpoint commit and session record naming the tested revision,
   outputs, known limits, next slice, and separate push/merge status.

Compilation is necessary but insufficient. An accepted option that does
nothing is a failing support claim. Record warnings or geometry defects
separately from compile failures. Review the changed and adjacent existing
families before advancing; a milestone's status stays partial until its
specified host/slot matrix is demonstrated.

## M00 - Inventory and durable roadmap (this session)

- Archive both originals byte-for-byte, preserve the previous development plan,
  and map every PDF item and all visible PowerPoint panels.
- Deliver the seven-page atlas, editable LaTeX, catalog, recipe index, and
  rebuild command without modifying package behavior.
- Gate: source checksums pass; every existing claim links to rendered evidence;
  all pages are visually inspected; package source is unchanged.

## M01 - Proca endpoint audit (completed for the documented current-family matrix)

**Requirements:** R15. **Dependency:** M00.

Completed on `codex/proca-endpoint-audit`; see [results](../../regressions/propagators/proca-endpoints/results.md). The requirements below remain the endpoint gate for future families.

- Start with a diagnostic sheet, not an assumed universal fix. Include the
  atlas families with internal propagators and representative external styles:
  ordinary/diagonal segments, bubble arcs, loop-channel arcs, box edges,
  crossed diagonals, half-box bridges, triangle edges, sunset, and insertion.
- Compare short and normal lengths at scales 0.72, 1.0, and 1.2. Include both
  path directions and the split crossed diagonal where applicable.
- Record each failing path/marker combination; make the smallest shared-helper
  fix justified by those failures. Add focused examples for the actual defects.
- Gate: tips meet the vertex boundary and point inward; white fill and line
  color survive; no extra tip appears at a crossing gap. Keep intentionally
  detached circ markers distinct from endpoint arrow placement.
- Follow-up sessions may fix separate affected helper families, one at a time.

## M02 - Independent triangle-contact annotations

**Requirements:** R06, preserving R07. **Dependency:** M01.

- Session A: external slots 1-4, independent arrow ranges and label positions.
  Remove hard-coded slot tuning that prevents an explicit setting taking effect.
- Session B: internal slots 5-7, independent ranges, fractions, clearances,
  and label offsets/anchors. Reuse existing grouped settings as fallbacks.
- Session C: verify top/bottom/left/right placement with unequal edge lengths
  and mixed EW/Proca styles; fix only demonstrated orientation/placement gaps.
- Gate: all default momentum labels lie outside the triangle; changing one
  slot does not shift or resize another; styles/indices retain logical identity;
  old recipes still compile. Do not add another triangle-contact topology.

## M03 - Generalize external self-energy bubbles

**Requirements:** R09, R10. **Dependencies:** M01, M02.

- M03a: preserve the t-tree slot-1 baseline and add slots 2-4 through a shared
  translated/reflected host-splitting model. Keep bubble a/b slot conventions.
- M03b: apply the proven model to s-tree slots 1-4.
- Host outer caps remain at outer endpoints. Keep pre/post segments and their
  momentum/index settings separate from the two internal bubble arcs.
- Gate: eight distinct host/slot recipes show a real inserted bubble, with
  exactly one selected leg changed and no inherited state from the prior call.
- Internal slot 5 remains outside this milestone; document its actual support
  rather than treating the accepted key value as working behavior.

## M04 - External seagulls

**Requirement:** R11. **Dependency:** M03.

- Specify the direct self-loop at a quartic point on a host propagator.
  This has one insertion vertex, unlike the two-vertex self-energy bubble.
- Integrate and verify the existing t-tree leg-1 prototype first; then expand
  the remaining t-tree legs and all s-tree legs. Keep one insertion per diagram.
- Gate: eight placements with the correct valence and host continuity;
  independent loop/host styles, loop momentum, and endpoint indices where
  defined by the contract; no new caps on the internal split points.

## M05 - External swordfish

**Requirement:** R12. **Dependencies:** M03, M04.

- Begin from S08-L1 and freeze its shared-vertex graph. Reuse style and slot
  helpers, but model the host vertex directly: do not collapse a nonzero bridge
  until two distinct bubble vertices happen to overlap.
- Complete t-tree external choices, then the four s-tree choices.
- Gate: one quartic loop/host vertex, one trivalent loop vertex, and the
  opposite tree vertex; reference external attachments and all eight placements
  match. Preserve momentum and index ownership at the shared interaction.

## M06 - Regular tree-attached triangles

**Requirement:** R08. **Dependencies:** M01, M02, M03 slot conventions.

- Implement bottom/top on t trees, then left/right on s trees. The loop has
  three trivalent vertices and one bridge to the opposite tree vertex.
- Build on proven slot/index/momentum helpers without reusing the
  triangle-contact quartic-vertex graph as a substitute.
- Gate: four plain plus four annotated examples match the source placements;
  all internal/external styles, momentum directions, and endpoint labels remain
  attached to their documented logical edges.

## M07 - Boxes and crossed routing

**Requirements:** R01-R04, R14, R22. **Dependencies:** M01, M02.

- Session A: confirm default square geometry, then add the complementary
  internal crossing. Preserve the existing CrossBoxCorr behavior as a supported
  default/alias. Complete missing internal momentum/index treatment for the
  crossed layouts rather than assuming box annotations already render there.
- Session B: add the upper and right external crossing layouts from S02-center
  and S03-center while preserving external slot identities and outer cap positions.
- Session C: resolve Q01/Q02 below, then implement only any demonstrated
  additional routing gap. No new shape should be inferred from an informal name.
- Gate: square default vertex spans; explicit user geometry overrides retained;
  correct connected/unconnected crossing semantics; independently styled edges;
  labels/indices routed with the edges rather than reassigned by visual position.

## M08 - Contact-host external corrections

**Requirements:** R13, R21. **Dependencies:** M03, M04, M02 conventions.

- M08a: self-energy insertion on one contact leg, then all four (S10).
- M08b: direct seagull insertion on all four contact legs (S11).
- Gate: the original quartic contact survives; new vertices have the required
  valences; no additional contact is introduced at a geometric crossover.
  Species/flow variants need examples but are not counted as new topologies.

## M09 - Internal exchange and shared inner-vertex loops

**Requirements:** R17-R19. **Dependencies:** M03-M05.

- M09a: s/t-tree slot-5 self-energy, with two trivalent insertion vertices and
  an exchange segment on each side (S23 top panels).
- M09b: direct quartic seagull on slot 5 in each channel (S23 bottom panels).
- M09c: the four mixed-valence inner-vertex bubble placements (S22). The
  quartic loop vertex carries the pair of external legs; the other loop vertex
  connects by a bridge to the opposite tree vertex.
- Gate: each case has its own explicit reference/edge map. A shared inner-vertex
  bubble and an external swordfish have different external attachments even
  when their vertex counts and valence multisets coincide.

## M10 - Stemmed tadpoles and resolved remaining variants

**Requirement:** R20; any newly resolved R22 gap. **Dependencies:** M04, M08;
M09 where internal hosts are involved.

- Session A: tree-vertex stemmed loops from S16. The original trivalent host
  becomes quartic; a stem ends at a separate trivalent self-loop vertex.
- Session B: external-leg stemmed loops on contact/s/t hosts from S17-S19.
  On a propagator the attachment point is a separate trivalent vertex with
  two host segments plus the stem; retain the loop endpoint vertex too.
- Session C only if required: implement a distinct graph established by the
  resolved S13 references. Otherwise record the existing recipe and close R22.
- Gate: preserve stem length and both endpoints; do not replace the appendage
  with a direct quartic seagull. Verify all referenced placements and document
  attachment valences rather than silently permitting a fifth-order contact.

## M11 - Documentation and completeness closeout

**Requirement:** R16. **Dependency:** completed/resolved preceding requirements.

- Reconcile every requirement and every source panel with a working recipe or
  an explicitly agreed exclusion. Keep resolved duplicates linked to one family.
- Regenerate atlas/PDF, public API reference, copy/paste examples, README
  graphics, and landing-page descriptions from the implemented state.
- Gate: full registered regression suite passes; every atlas page is inspected;
  no unsupported combination is advertised; original source checksums still pass.

## Specification questions to resolve at their milestone

- **Q01 / R14:** For q1-q4 and q3-q2, which interaction vertices and internal
  edge carry the Z, and which external slots are permuted? Start with an
  explicitly numbered sketch. Existing orientation controls may be sufficient;
  do not assume either new code or no new code before tracing it.
- **Q02 / R22:** Trace both S13 images at their native resolution. Determine
  which lines cross without joining, where vertices actually lie, and whether
  these are embeddings of a supported graph. Save the traced endpoint list
  before declaring an implementation missing or completed. Ask the user only
  if the originals still do not resolve the connections.

## Scope carried across sessions

One insertion at a time. Existing APIs remain compatible. No repository rename
or branch deletion. Use `codex/` for new feature branches; no automatic merge or
publish is implied. Keep the user-visible PDFs current at capability checkpoints,
not merely at the final documentation milestone.
