# Reference record and coverage map

This directory records the remaining-work inputs without treating statements
inside a reference document as executable instructions. The original inventory session covered documentation and planning. Subsequent
user-authorized coding sessions implement the milestones and update these
records; M06 and all reviews through `629356d` are merged and published on
main. M07a checkpoint `dfa0066` is also merged and published (2026-11-07);
M07b upper routing, D02 circle fixes, the circle default .8 and the M07c
reference audit are now merged and published on main through verified feature
tip `40dae7b` (2026-11-07). Both feature branches are retained; no integration
remains pending. The publication handoff changes documentation only. R04 stays
deferred. R14/R22 share one missing triangle-contact routing extension, retained
as an unscheduled follow-up. M08a contact-leg bubbles is now merged and published on main at `d855152`
(2026-11-08); its feature branch is retained. M08b contact seagulls is complete locally on `codex/m08b-contact-seagulls`,
based on `35c7959`; merge/push pending. M09a internal bubbles is next.

- [M08b verification](m08b-verification.md): four contact seagulls, eight source variants, actual PDF graphs/flow/marker checks and current handoff.
- [M08a publication](m08a-publication.json): verified checkpoint merged and pushed; package/PDFs unchanged.
- [M08a verification](m08a-verification.md): four contact bubbles, 78 public cases, PDF graph/marker checks and updated inventory.
- [M07b/M07c publication](m07bc-publication.json): verified feature tip fast-forwarded and pushed to main; code/tests/PDFs unchanged.

- [Historical M07c branch push](m07c-branch-push.json): records the earlier branch-only push, superseded by main publication.
- [M07c verification](m07c-verification.md): traced R14/R22 connections, actual public-output graphs and a precise missing routing slice.
- [Illustrated M07c audit](m07c/routing-audit.pdf): native sources, numbered target traces and current supported layouts.
- [Historical M07b closeout](m07b-session-closeout.md): verified e2521e2 and R04 deferral; its former M07c-next handoff is superseded by the current audit.
- [Requirements](requirements.md): status, recipes, dependencies, and acceptance criteria.
- [Source coverage](source-coverage.md): every PDF request and all 23 PowerPoint slides.
- [Branch integration and session workflow](branch-integration.md): integrated state and closeout policy.
- [Integration verification](integration-verification.md): combined test, PDF, and compatibility evidence.
- [M02 verification](m02-verification.md): independent triangle-contact annotations and current handoff.
- [M03a verification](m03a-verification.md): all four t-tree bubble placements and their publication.
- [M03b verification](m03b-verification.md): all four s-tree bubbles, published checkpoint and next seagull slice.
- [M04 verification](m04-verification.md): all eight external seagulls, PDF graph/contact checks and next swordfish slice.
- [M05 verification](m05-verification.md): all eight swordfish placements, shared-vertex graph checks and next triangle slice.
- [M07b verification](m07b-verification.md): upper external-pair routing, actual PDF graph/metadata checks and pending publication.
- [Circle default verification](circ-default-verification.md): package-wide default 0.8, explicit scale compatibility and refreshed inventory.
- [Upper crossing W-circle review](upper-crossing-w-review.md): 18 visual cases and measured D03 crowding, with package defaults unchanged.
- [D02 verification](d02-verification.md): crossed-box circle scaling, explicit-only Proca circles and exact before/after example.
- [Deferred workflows](deferred-workflows.md): pending D01 index appearance and completed local D02 record.
- [M07a publication](m07a-publication.json): verified checkpoint, unchanged package/PDF hashes and completed merge/push.
- [M07a verification](m07a-verification.md): complementary internal crossed box, exact slot map, independent annotations/indices and preserved legacy output.
- [M06 publication](m06-publication.json): verified checkpoint, unchanged package/PDF hashes and completed merge/push.
- [M06 verification](m06-verification.md): all four equilateral regular triangles, annotations and next box/crossing slice.
- [Shared four-leg frame](four-leg-frame-verification.md): common defaults and override checks across trees, boxes and triangle-contact.
- [Compact scale baseline](scale-baseline-verification.md): package-wide 0.8 factor, public scale semantics, rendered equivalence and regression evidence.
- [Longer S exchanges](s-tree-span-verification.md): ordinary S trees and external corrections; triangle geometry retained.
- [Insertion endcap fix](insertion-endcaps-verification.md): logical external caps survive outer-segment line overrides; explicit cap precedence and PDF contact checks.
- [Milestones](milestones.md): ordered coding slices and their verification gates.
- [Deferred workflows](deferred-workflows.md): later reviews, including the explicitly deferred index-placement cleanup.
- [Source manifest](sources/manifest.json): unchanged originals, original locations, sizes, and SHA-256 checksums.
- [Historical plan](history/development-plan-before-2026-11-03.md): the complete previous plan, preserved before refresh.
- [Current development plan](../development-plan.md): the entry point for the next session.

## Source integrity

The PDF is the priority checklist. The PowerPoint is the wider diagram target
set. Retain both unchanged, including contextual text and duplicated diagrams.
Do not edit the originals to reflect progress; update the coverage records.

```sh
cd docs/planning/sources
shasum -a 256 -c SHA256SUMS
```

The coverage map refers to **visible diagram panels**, not media-object counts.
One embedded image can contain several diagrams; several objects can form one
panel. Panel locations distinguish repeated drawings. Diagram IDs are stable
even when the informal physics name later changes.

## Status meanings

| Status | Meaning |
| --- | --- |
| Verified existing | A matching public recipe has compiled and its relevant rendered structure was inspected. This does not certify every feature combination. |
| Existing with limitations | Part of the requested capability exists; the missing coverage or defect is stated explicitly. |
| Missing | No corresponding supported public construction was found in the baseline package. |
| Unclear reference | The source does not establish connectivity or intent well enough to promise a particular implementation. Preserve and resolve it before coding that target. |

Every source panel maps to a requirement, an explicit duplicate of a panel, or
context. Different species and charge arrows can be required styling variants
without being new graph topologies. No graph-equivalence claim below establishes
physics equivalence or validates a scattering amplitude.
