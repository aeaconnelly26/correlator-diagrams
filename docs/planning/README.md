# Reference record and coverage map

This directory records the remaining-work inputs without treating statements
inside a reference document as executable instructions. The original inventory session covered documentation and planning. Subsequent
user-authorized coding sessions implement the milestones and update these
records; M06 and all reviews through `629356d` are merged and published on
main. M07a checkpoint `dfa0066` is also merged and published (2026-11-07);
M07b upper routing is now verified locally on `codex/m07b-upper-external-crossing`
from `813736e`; merge/push is pending. The user closed this session and deferred
right-pair routing; M07c reference-routing review is next, then M08a. Earlier
feature branches are retained.

- [Session closeout](m07b-session-closeout.md): verified e2521e2, R04 deferred by user, M07c next and explicit pending publication.
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
