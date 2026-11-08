# Remaining requirements and existing capacity

Baseline: `main` / `0dbf733`, 2026-11-03. See [atlas recipes](../diagram-inventory/recipes.md), [source panels](source-coverage.md), and [milestone gates](milestones.md). This record distinguishes geometry from annotation/style completeness.

Machine-readable counterpart: `requirements.json`. Update both representations together. Existing-capability claims below refer to the specific inspected recipes, not arbitrary feature combinations.

## R01 - Square box defaults

- **Status:** Verified existing.
- **Existing construction / evidence:** I17; BoxLoopCorr resets box-xspan and box-yspan to 1.34. M07a checks the ordinary box and both crossed layouts; actual PDF paths verify matching square spans.
- **Remaining target / limitation:** Already implemented for defaults. Preserve explicit user dimension overrides. Do not add another square-box macro solely to satisfy this request.
- **Milestone:** M07a verification complete; preserve throughout M07. **Dependencies:** None.
- **Acceptance:** Default box and crossed-box vertex spans agree horizontally and vertically; no regression to rectangular defaults.
- **Sources:** P1-01; S02-right, S03-left.

## R02 - Complementary internal crossed box

- **Status:** Verified existing.
- **Existing construction / evidence:** M07a: `CrossBoxCorr[cross-box-layout=top-bottom]` complements the compatible `left-right` default. P01-P04/P11-P14 show square graphs, style variants and independent internal annotations; 104 focused cases and actual PDF reconstruction verify slots, four trivalent vertices and an unconnected crossing.
- **Remaining target / limitation:** Internal crossing only. External crossings remain R03/R04. One split descending diagonal; D01 index-position appearance is deferred. Explicit dimension overrides are preserved.
- **Milestone:** M07a complete on published main (`dfa0066`). **Dependencies:** M01; frozen M07a connectivity specification.
- **Acceptance:** Both internal-crossing layouts have matching slot maps, style controls, correct endpoint markers, and explicit crossing gaps.
- **Sources:** P1-02.

## R03 - Box with crossed upper external legs

- **Status:** Verified existing (M07b upper slice, local checkpoint).
- **Existing construction / evidence:** `BoxLoopCorr[box-external-crossing=top]`; P21-P24. 52 focused public cases plus actual PDF graph/marker/circle/cap checks verify UL-to-TR and UR-to-TL routing, four trivalent vertices and an unconnected upper crossing.
- **Remaining target / limitation:** Ordinary box only. Right-pair routing remains R04; D01 index appearance remains deferred; D02 circles are fixed in the later local follow-up. Internal loop slots 5-8 and the shared outer frame are unchanged.
- **Milestone:** M07b upper slice complete locally; right external pair next. **Dependencies:** M01; frozen M07b connectivity contract.
- **Acceptance:** S02-center reproduced with square loop geometry and unchanged external slot identities; see [verification](m07b-verification.md).
- **Sources:** P1-03; S02-center.

## R04 - Box with crossed right external legs

- **Status:** Missing.
- **Existing construction / evidence:** I17/I18 cannot independently cross the right external pair.
- **Remaining target / limitation:** Preserve the square loop and cross the right external pair.
- **Milestone:** M07. **Dependencies:** M01; source-panel routing specification.
- **Acceptance:** Reproduce S03-center; species, caps, labels, and slot identity follow the routed legs.
- **Sources:** P1-04; S03-center.

## R05 - Four-legged channel bubbles

- **Status:** Verified existing.
- **Existing construction / evidence:** I14-I16: SChannelCorr, TChannelCorr, UChannelCorr. A01 demonstrates two pink Proca internal lines and four double-capped EW external legs.
- **Remaining target / limitation:** Two quartic vertices joined by two internal lines, with four external legs. Existing topology; decorated endpoint and label quality are separate R15/R06 checks.
- **Milestone:** M00 complete; retain in M11. **Dependencies:** None.
- **Acceptance:** Keep three channel recipes and the exact requested styled t-channel example in the atlas; do not reimplement this family.
- **Sources:** P1-05; S04-TR, S04-BR, S12-left, S14-left, S14-right, S15-left.

## R06 - Independent triangle-contact labeling

- **Status:** Verified existing.
- **Existing construction / evidence:** M02: T01-T08 and `triangle-contact-annotations.tex/pdf` demonstrate independent controls for slots 1-7, outside-facing defaults in four orientations, unequal spans and mixed EW/Proca styles. Emitted-coordinate isolation, grouped fallbacks, reversal, label-only movement, scale, visibility and state-reset checks pass. Review checks cover actual gap centers, compact defaults, quartic-side placement, and continuous side-label layouts.
- **Remaining target / limitation:** Implemented. Long labels or unusually short legs can still require explicit per-slot tuning. No new topology was added.
- **Milestone:** M02 complete. **Dependencies:** M01 baseline endpoint audit.
- **Acceptance:** All four orientations pass a labeled mixed-Proca/EW example; changing one annotation does not move another; old public keys still work.
- **Sources:** P1-06, P1-07, P2-01, P4-02.

## R07 - Four triangle-contact orientations

- **Status:** Verified existing.
- **Existing construction / evidence:** I23-I26: TriangleContactCorr with bottom/top/left/right orientation.
- **Remaining target / limitation:** Already implemented: two trivalent and one quartic vertex. Label quality remains R06.
- **Milestone:** M00 complete; retain in M02. **Dependencies:** None.
- **Acceptance:** Retain four plain recipes and extend their labeled coverage during M02.
- **Sources:** P2-02; S02-left, S03-right, S04-TL, S04-BL, S12-right, S15-right.

## R08 - Regular tree-attached triangle correction

- **Status:** Verified existing.
- **Existing construction / evidence:** M06: `insertion=triangle` with `tree-triangle-side` on T top/bottom and S left/right. Atlas L01-L04/L11-L14; 191 focused public cases and actual PDF paths verify four eight-edge graphs, four trivalent interactions, equilateral loop sides, and 36 white-filled pink endpoint contacts.
- **Remaining target / limitation:** One correction at a time. U/contact hosts, incompatible sides and simultaneous corrections are unsupported. Explicit half-width permits other shapes; extreme geometry is not clamped. Index-position appearance remains D01.
- **Milestone:** M06 complete on published main (`629356d`). **Dependencies:** M01, M02, insertion-slot conventions from M03.
- **Acceptance:** Four placements preserve the reference graph, styles, outer caps, independent momentum controls and endpoint values/ownership. No triangle-contact quartic point is substituted.
- **Sources:** P2-03; S05-L2, S06-L2, S07-L2, S08-L2. See [M06 verification](m06-verification.md).

## R09 - Bubble insertion on all t-tree external legs

- **Status:** Verified existing.
- **Existing construction / evidence:** M03a: I29 and B02-B04 render bubbles on t-tree external slots 1-4. Focused t-tree-bubble-slots.tex/pdf checks graph connectivity, selected-leg styles/momenta, outer caps, indices and state reset; 16 Proca tips are checked from rendered vectors.
- **Remaining target / limitation:** Implemented for one selected t-tree external leg at a time. S-tree external slots 1-4 are also implemented by M03b. U-tree hosts, internal slot 5 and simultaneous insertions remain unsupported.
- **Milestone:** M03a complete. **Dependencies:** M01, M02.
- **Acceptance:** Four t-tree external slots render the bubble; each retains host style, caps, pre/post momentum, and endpoint indices without state leakage.
- **Sources:** P2-04; S05-C2, S05-R2, S08-C2, S08-R2.

## R10 - Bubble insertion on all s-tree external legs

- **Status:** Verified existing.
- **Existing construction / evidence:** M03b: C01-C04 render s-tree external slots 1-4. s-tree-bubble-slots.tex/pdf verifies selected-edge connectivity, logical styles/momenta, outer caps, index attachment/controls and state reset; 16 pink Proca tips are checked from rendered vectors.
- **Remaining target / limitation:** Implemented for one selected external s-tree leg at a time. Index-placement polish is expressly deferred to D01; u-tree, internal slot 5 and simultaneous insertions remain unsupported.
- **Milestone:** M03b complete. **Dependencies:** M03a.
- **Acceptance:** Four s-tree recipes work with one selected leg at a time; logical data remain attached after translation/reflection.
- **Sources:** P3-02; S06-R1, S06-R2, S07-R1, S07-R2.

## R11 - Seagull on external tree legs

- **Status:** Verified existing.
- **Existing construction / evidence:** M04 implements all eight s/t-tree external placements. Atlas G01-G04/G11-G14 and the six-page seagull-slots gallery expose the single quartic self-loop; actual PDF graph extraction verifies seven edges and valences for all eight. Focused controls and 24 pink Proca/scalar marker contacts are checked independently. Nov 4 review verifies inward T/outward S defaults, scattering flow, compact guides and measured label clearance; explicit overrides remain supported.
- **Remaining target / limitation:** One selected s/t-tree external leg at a time. Internal slot 5, u-tree/contact hosts and simultaneous insertions remain unsupported. Index placement is deferred to D01; seagull vertex index values/order are preserved.
- **Milestone:** M04 complete. **Dependencies:** M03; prototype integration completed.
- **Acceptance:** Eight placements preserve one quartic insertion point, two host segments, and one self-loop; do not draw a two-vertex self-energy bubble instead.
- **Sources:** P2-05, P3-03, S05-C1, S05-R1, S06-C1, S06-C2, S07-C1, S07-C2, S08-C1, S08-R1, S20-TL, S20-TR, S20-BL, S20-BR, S21-TL, S21-TR, S21-BL, S21-BR. See [M04 verification](m04-verification.md).

## R12 - Swordfish on external tree legs

- **Status:** Verified existing.
- **Existing construction / evidence:** M05 supports `insertion=swordfish` on all four external legs of both s/t trees. Atlas K01-K04/K11-K14 and styled K21-K24. The 167 public cases and independent PDF paths verify seven edges, one actual shared quartic tree vertex, no extra bridge/duplicate dot, and 48 white-filled pink endpoint contacts.
- **Remaining target / limitation:** One selected external insertion. U/contact/internal-slot-5 and simultaneous insertions remain unsupported. Post-segment controls do not apply; index appearance is D01.
- **Milestone:** M05 complete on published main (`9daebf9`). **Dependencies:** M03, M04 (published).
- **Acceptance:** Eight placements match the reference connections and vertex valences; no artificial bridge or overlapping pair of interaction vertices.
- **Sources:** P2-06, P3-01, P3-04; S05-L1, S05-L3, S08-L1, S08-L3. See [M05 verification](m05-verification.md).

## R13 - Self-energy bubble on contact external legs

- **Status:** Missing.
- **Existing construction / evidence:** I06 is a contact host; semantic bubble insertion dispatch covers s/t-tree external slots 1-4 but not contact hosts.
- **Remaining target / limitation:** A four-leg contact with a self-energy bubble splitting one external leg. Cover four choices shown on S10.
- **Milestone:** M08a. **Dependencies:** M03; M02 annotation conventions.
- **Acceptance:** Four contact-host recipes retain the quartic host vertex, two trivalent insertion vertices, caps, styles, momenta, and indices.
- **Sources:** P4-01; S10-TL, S10-TR, S10-BL, S10-BR.

## R14 - Crossed diagonal/vertex-correction routing

- **Status:** Unclear reference.
- **Existing construction / evidence:** The PDF asks for a Z edge connecting q1-q4 or q3-q2, but does not fix a complete endpoint/vertex map. Existing I23-I26 cover unpermuted triangle-contact placements.
- **Remaining target / limitation:** Record actual external slot permutation and internal endpoints before deciding whether existing triangle-contact geometry suffices or new routing is needed.
- **Milestone:** M07 specification gate. **Dependencies:** M02; resolve Q01 in milestones.md.
- **Acceptance:** Produce a labeled endpoint sketch and exact public recipe or a defined new layout; identify every crossing as connected or unconnected.
- **Sources:** P3-05, P3-06.

## R15 - Proca marker contact across topology families

- **Status:** Verified existing.
- **Existing construction / evidence:** Integrated 26-page audit: 156 diagrams, 609 triangles, and 600 automatic visible contacts; actual PDF-stroke measurements, visual review, and one-sided equilateral-size assertions pass.
- **Remaining target / limitation:** Current families include the seagull loop and managed override controls. Preserve raw and managed radius/distance APIs, repeat checks for new families, and retain the documented exclusions for arbitrary anisotropic transforms or unknown vertex shapes.
- **Milestone:** M01 and branch reconciliation complete for the audited current families; repeat endpoint checks later. **Dependencies:** None.
- **Acceptance:** Passed: visible dot/triangle outlines touch; tips are not buried; inward white-filled color and expected endpoint counts are preserved. Both legacy distance keys and managed overrides retain intended placement.
- **Sources:** P4-03. See [integration verification](integration-verification.md).

## R16 - Reference and GitHub documentation refresh

- **Status:** Existing with limitations.
- **Existing construction / evidence:** README.md and docs/reference.md exist; historical development plan predates merged bubble-on-leg work.
- **Remaining target / limitation:** Current roadmap/atlas now; full API examples and GitHub visuals updated as milestones land; final reconciliation at M11.
- **Milestone:** M00 now; M11 closeout. **Dependencies:** All accepted capability milestones.
- **Acceptance:** All public capabilities have current examples, limitations are stated, roadmap statuses match evidence, and README graphics use the current package.
- **Sources:** P4-04.

## R17 - Self-energy on internal exchange propagator

- **Status:** Missing.
- **Existing construction / evidence:** Existing tree exchange slot 5 is an edge, but bubble insertion slot 5 is not rendered.
- **Remaining target / limitation:** A bubble with two trivalent insertion vertices and two bridge segments on the s/t internal exchange edge.
- **Milestone:** M09a. **Dependencies:** M03, M04.
- **Acceptance:** Both channels reproduce S23 top panels with host slot 5 data intact; no external-slot relabeling workaround.
- **Sources:** S23-TL, S23-TR.

## R18 - Seagull on internal exchange propagator

- **Status:** Missing.
- **Existing construction / evidence:** No quartic self-loop insertion exists on tree slot 5.
- **Remaining target / limitation:** A quartic self-loop point splits the s/t exchange propagator; both adjacent exchange segments remain connected.
- **Milestone:** M09b. **Dependencies:** M04, M09a.
- **Acceptance:** Both S23 lower panels match the vertex/edge graph with independent loop and exchange styling.
- **Sources:** S23-BL, S23-BR.

## R19 - Bubble sharing a tree vertex on the internal side

- **Status:** Missing.
- **Existing construction / evidence:** Four-legged channel bubbles I14/I15 have two quartic ends; self-energy I27 has two trivalent ends. Neither is this mixed-valence attached graph.
- **Remaining target / limitation:** Two loop edges join one quartic vertex carrying two external legs to one trivalent vertex attached by a bridge to the opposite tree vertex. Four s/t placements.
- **Milestone:** M09c. **Dependencies:** M05 shared-vertex model; M09a.
- **Acceptance:** Match all four S22 panels and species variants from S06/S07; do not replace with an external-leg swordfish or a free internal bubble.
- **Sources:** S06-L1, S06-L3, S07-L1, S07-L3, S22-TL, S22-TR, S22-BL, S22-BR.

## R20 - Stem-attached tadpole structures

- **Status:** Missing.
- **Existing construction / evidence:** No supported standalone tadpole/stem insertion family found. A stemmed appendage is distinct from a direct seagull on the host edge.
- **Remaining target / limitation:** A loop returns to a vertex at the end of a separate stem. References attach the stem at tree vertices or external-leg points; retain these as separate subcases.
- **Milestone:** M10. **Dependencies:** M04; M08 for contact hosts; freeze vertex valence case by case.
- **Acceptance:** Cover S16 tree-vertex appendages and S17-S19 external-leg appendages; preserve both stem endpoint vertices and explicitly document the valence of contact-host attachment points.
- **Sources:** S16-TL, S16-TR, S16-BL, S16-BR, S17-TL, S17-TR, S17-BL, S17-BR, S18-TL, S18-TR, S18-BL, S18-BR, S19-TL, S19-TR, S19-BL, S19-BR.

## R21 - Seagull on contact external legs

- **Status:** Missing.
- **Existing construction / evidence:** Contact baseline I06 exists; there is no quartic self-loop insertion on its external legs.
- **Remaining target / limitation:** Four external-leg seagull placements; species/loop-arrow variants are examples, not extra graph topologies.
- **Milestone:** M08b. **Dependencies:** M04, M08a.
- **Acceptance:** Reproduce S11 four placements, retain one quartic host and one quartic insertion point, and verify the displayed species/flow variants.
- **Sources:** S11-T1, S11-T2, S11-T3, S11-T4, S11-B1, S11-B2, S11-B3, S11-B4.

## R22 - Triangle-shaped crossed drawings

- **Status:** Unclear reference.
- **Existing construction / evidence:** S13 contains two dense triangle-like drawings with crossings/overlapping paths. No unsupported topology is asserted to be reproduced by I18 or I23-I26.
- **Remaining target / limitation:** Trace every endpoint from the original images before classifying these as crossed boxes, triangle corrections, or another graph. Preserve both panel references.
- **Milestone:** M07 specification gate; M10 only if a distinct family is established. **Dependencies:** Resolve Q02 in milestones.md.
- **Acceptance:** Save an unambiguous vertex/edge sketch for each panel, map to a reproducible recipe or a precisely scoped missing requirement, and then implement only the demonstrated gap.
- **Sources:** S13-left, S13-right.

## Audit boundaries

R14 and R22 are intentionally unresolved references, not promises that existing macros reproduce those drawings. They have explicit specification gates. Stemmed contact-host attachments in R20 also need their attachment valences recorded before implementation. None of these uncertainties blocks the current inventory.

Feature gaps found while constructing recipes: a global explicit `line=...` overrides the half-box bridge-specific style, so A04 omits the global setting. Blank external bubble momentum text still leaves arrows when `show-momenta=true`; A05 uses explicit external momenta rather than implying that blanks suppress arrows. These are existing behaviors recorded for later review, not package changes.

## Additional integrated capabilities

External momentum hiding, continuous unlabeled arrows for empty entries,
compact external indices, and channel side-label gap fixes are already available
and illustrated by inventory F01-F03. The Compton example is preserved as a
reusable application of existing tree/contact primitives, not an extra topology.
