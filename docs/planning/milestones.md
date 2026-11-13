# Future coding milestones

Baseline: `0dbf733`, inventoried on 2026-11-03. These are future feature
sessions, not changes made by the inventory work. R IDs refer to
[requirements](requirements.md); S IDs refer to [reference panels](source-coverage.md).

## Integration baseline - completed before M02

`codex/integrate-seagull-and-proca` now combines `1b85ef8` and `5a657cd`.
The seagull slot-1 prototype, prior marker/momentum/index work, and M01 raw
Proca fixes are reconciled. See [integration verification](integration-verification.md).
M04 expands the existing prototype. Integration commit `4584aff` is included
in published `main` at `6657735`. M02 checkpoint `8f95755` is now also merged
and published on main. M03a is published through `6549efa`; M03b checkpoint
`97495ba` is also merged and published on main. M04 checkpoint `854293a`,
implemented on `codex/m04-seagull-expansion` from `b4a6ad8`, is now merged and
published on main. The branch is retained. M05 checkpoint `9daebf9`, implemented
from `efb5fae`, is now also merged and published on main (2026-11-06).
The M05 branch is retained. M06 verified checkpoint `629356d`, implemented
on `codex/m06-tree-triangles` from `eb6182c`, is now merged and published on
main. Its feature branch is retained. M07a is now also published; M07b's upper slice is verified locally. See
[M05 verification](m05-verification.md) and [M06 verification](m06-verification.md).

## User-selected crossed-vertex follow-up (2026-11-08)

Exactly two half-moon layouts follow M07c: opposite cubic corners, collinear W
segments and a curved crossing without an extra interaction. Implemented on
`codex/crossed-vertex`; checkpoint `8b41ca1` is merged and published on main
(2026-11-13), with its source branch retained. The user-selected
[contract](crossed-vertex/contract.md) supersedes the proposed angular layout/API.
See [verification](crossed-vertex/verification.md) and [publication](crossed-vertex/publication.json).

## Intermediate compilation-performance session (2026-11-13)

The next user-selected session optimizes package structure to reduce compilation
time. Establish repeated loading/drawing benchmarks before selecting changes,
and preserve public behavior and rendered output. See the
[performance handoff](compilation-performance.md). M09a follows this session.

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

All public diagram scales are relative to the compact 0.8 coordinate baseline.
Do not compensate individual topology dimensions to undo the common reduction.
`scale=1.25` recovers the former unit-scale size when needed; preserve the
shared logical frame. See [verification](scale-baseline-verification.md).

Standard four-leg examples use p1/p2 incoming and p3/p4 outgoing, including
future milestones. Explicit reversed-flow demonstrations must be identified as
such; preserve their override coverage in tests.

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

Completed and reconciled on `codex/integrate-seagull-and-proca`; see [integration verification](integration-verification.md). The requirements below remain the endpoint gate for future families.

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

## M02 - Independent triangle-contact annotations (completed)

**Requirements:** R06, preserving R07. **Dependency:** M01.

Completed on `codex/m02-triangle-contact-annotations`, based on `6657735`.
Final checkpoint `8f95755` is merged into main and published to GitHub.
Sessions A-C are covered by the new slot option blocks and the focused
five-page gallery. All seven logical slots, four orientations, unequal spans,
grouped compatibility, scale, reversal, visibility and isolation are verified.
See [M02 verification](m02-verification.md). M03 has subsequently completed;
the acceptance contract below remains a regression gate.

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

M03a is complete on `codex/m03a-t-tree-bubbles`, based on `b917ed2`;
verified checkpoint `2c3b467` is merged and published on main.
All four t-tree external slots are checked, including actual graph/caps/momentum
and style/index coverage. See [M03a verification](m03a-verification.md).
M03b checkpoint `97495ba` is complete, merged and published on main: all four
s-tree placements, with existing t-tree output retained. Its implementation
branch `codex/m03b-s-tree-bubbles` is retained.
See [M03b verification](m03b-verification.md).
The following contract remains the regression gate for both families.
Index-placement appearance is expressly deferred to a later separate workflow,
[D01](deferred-workflows.md). Preserve attachment/controls during M03b; do not
retune positions or turn visual index polish into a current acceptance gate.

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

M04 checkpoint `854293a` is complete, merged and published on main.
The implementation branch `codex/m04-seagull-expansion` is retained.
All eight external s/t-tree placements preserve one quartic self-loop vertex.
The Nov 4 review makes T loops face inward and S loops outward; default external
flow is 1/2 in and 3/4 out. Compact guides and measured label clearance apply
to both bubble and seagull insertions; explicit overrides remain supported.
See [M04 verification](m04-verification.md) for the final 40-document /
688-contact validation and styled reviews. D01 index appearance remains
deferred. The following is the regression gate.

- Specify the direct self-loop at a quartic point on a host propagator.
  This has one insertion vertex, unlike the two-vertex self-energy bubble.
- The t-tree leg-1 prototype is preserved; the remaining t-tree legs and all
  s-tree legs are implemented. Keep one insertion per diagram.
- Gate: eight placements with the correct valence and host continuity;
  independent loop/host styles, loop momentum, and endpoint indices where
  defined by the contract; no new caps on the internal split points.

## M05 - External swordfish

**Requirement:** R12. **Dependencies:** M03, M04 (published).
**State:** Complete on published main at checkpoint `9daebf9`; feature branch retained.
All eight placements pass 167 focused cases and independent actual-PDF graph
checks. Full suite: 41 documents / 736 endpoint contacts.
[Contract](../../regressions/topologies/insertion/M05-contract.md),
[verification](m05-verification.md), [gallery](../../regressions/topologies/insertion/swordfish-slots.pdf).
The following specification is satisfied within the documented geometry limits.

- Begin from S08-L1 and freeze its shared-vertex graph. Reuse style and slot
  helpers, but model the host vertex directly: do not collapse a nonzero bridge
  until two distinct bubble vertices happen to overlap.
- Complete t-tree external choices, then the four s-tree choices.
- Gate: one quartic loop/host vertex, one trivalent loop vertex, and the
  opposite tree vertex; reference external attachments and all eight placements
  match. Preserve momentum and index ownership at the shared interaction.

## M06 - Regular tree-attached triangles

**Requirement:** R08. **Dependencies:** M01, M02, M03 slot conventions.
**State:** Complete on published main at `629356d`; all four placements have equilateral defaults.
191 triangle cases, 188 shared-frame cases and independent PDF graph/shape/contact checks pass.
[Contract](../../regressions/topologies/insertion/M06-contract.md),
[verification](m06-verification.md), [gallery](../../regressions/topologies/insertion/tree-triangle-slots.pdf).
Index-position polish remains D01. M06 and its reviewed scale/geometry/endcap
fixes are merged and published; no M06 merge/push remains.

- Implement bottom/top on t trees, then left/right on s trees. The loop has
  three trivalent vertices and one bridge to the opposite tree vertex.
- Build on proven slot/index/momentum helpers without reusing the
  triangle-contact quartic-vertex graph as a substitute.
- Gate: four plain plus four annotated examples match the source placements;
  all internal/external styles, momentum directions, and endpoint labels remain
  attached to their documented logical edges.

## M07 - Boxes and crossed routing

**Requirements:** R01-R04, R14, R22. **Dependencies:** M01, M02.
**State:** M07a verified checkpoint `dfa0066`, implemented on
`codex/m07a-crossed-box-layouts` from `56a643a`, is now merged and published
on main (2026-11-07). Its feature branch is retained. See [verification](m07a-verification.md) and
[frozen contract](../../regressions/topologies/cross-box/M07a-contract.md).
104 public cases and independent PDF graph/gap/contact checks pass. M07b's
upper external pair is now published on main with M07c through feature tip
`40dae7b`: 52 public cases and actual PDF connectivity, markers, caps and circle
scaling. D02 and circle default .8 are included; all 50 documents / 850 contacts
passed at the unchanged package checkpoint. See [publication](m07bc-publication.json). At session closeout on 2026-11-07 the
user deferred right external routing (R04). M07c is now complete as an audit:
R14/R22 identified the same opposite-pair routing gap. Its user-selected
half-moon follow-up is now published on main; M08a/M08b are published. See [M07b verification](m07b-verification.md). D01 remains deferred; D02 crossed-box circles are fixed and published in the follow-up. See [D02 verification](d02-verification.md).

- Session A: confirm default square geometry, then add the complementary
  internal crossing. Preserve the existing CrossBoxCorr behavior as a supported
  default/alias. Complete missing internal momentum/index treatment for the
  crossed layouts rather than assuming box annotations already render there.
- Session B: upper external crossing from S02-center is complete on published main.
  The right external pair from S03-center is deferred by the user (2026-11-07),
  retaining its requirement/acceptance record for a later requested session.
- Session C (audit complete): Q01/Q02 are resolved by [native source traces](m07c/routing-map.json) and [current public recipes](m07c/recipes.md). The missing opposite-pair attachment extension is specified in a [future plan](m07c/future-routing-plan.md), with no implementation in this audit.
- Gate: square default vertex spans; explicit user geometry overrides retained;
  correct connected/unconnected crossing semantics; independently styled edges;
  labels/indices routed with the edges rather than reassigned by visual position.

## M08 - Contact-host external corrections

**Requirements:** R13, R21. **Dependencies:** M03, M04, M02 conventions.
**M08a complete on published main** at `d855152`; feature branch retained. [Verification](m08a-verification.md). **M08b complete on published main** at `e57499e`, including the array fix; source branch retained. [Verification](m08b-verification.md). **Next session:** compilation performance; M09a internal-exchange self-energy bubbles follows.

- M08a: complete on published main; all four S10 external contact bubbles, 78 public cases and actual PDF graph/marker checks. Central/crossed quartic views only; invalid hosts/slots fail explicitly.
- M08b: complete on published main; all four direct contact seagulls and all eight S11 species/flow variants. Six edges, two quartic interactions, one self-loop; no stem.
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

**Requirement:** R20. R22 was resolved by M07c as an existing-family routing gap,
not another M10 loop family. **Dependencies:** M04, M08;
M09 where internal hosts are involved.

- Session A: tree-vertex stemmed loops from S16. The original trivalent host
  becomes quartic; a stem ends at a separate trivalent self-loop vertex.
- Session B: external-leg stemmed loops on contact/s/t hosts from S17-S19.
  On a propagator the attachment point is a separate trivalent vertex with
  two host segments plus the stem; retain the loop endpoint vertex too.
- The S13 references are now R14/R22 triangle-contact external-routing variants
  and do not add a stemmed-loop or other new family here.
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

- **Q01 / R14 (resolved by audit):** Under fixed spatial numbering, the Z joins
  cubic vertices carrying q2/q3 in S13-left and q1/q4 in S13-right. The PDF-to-slide
  correspondence is recorded as an inference; q labels are absent from the slides.
  Internal Z styling and square bounding spans already work; opposite-pair
  quartic attachments are now supplied by the published crossed-vertex follow-up.
- **Q02 / R22 (resolved by audit):** Both native images have seven logical edges,
  three interactions with valences 4/3/3 and one W/W/Z cycle. The external crossover
  has no interaction. They share the R14 extension of TriangleContactCorr;
  [maps](m07c/routing-map.json), [illustrated comparison](m07c/routing-audit.pdf)
  and [historical proposed slice](m07c/future-routing-plan.md) are saved. The user-selected
  half-moon contract now supplies CV01/CV02; no new loop family is counted.

## Scope carried across sessions

One insertion at a time. Existing APIs remain compatible. No repository rename
or branch deletion. Use `codex/` for new feature branches; no automatic merge or
publish is implied. Keep the user-visible PDFs current at capability checkpoints,
not merely at the final documentation milestone.
