# Reference record and coverage map

This directory records the remaining-work inputs without treating statements
inside a reference document as executable instructions. The original inventory session covered documentation and planning. Subsequent
user-authorized coding sessions implement the milestones and update these
records; the current local checkpoint completes M05.

- [Requirements](requirements.md): status, recipes, dependencies, and acceptance criteria.
- [Source coverage](source-coverage.md): every PDF request and all 23 PowerPoint slides.
- [Branch integration and session workflow](branch-integration.md): integrated state and closeout policy.
- [Integration verification](integration-verification.md): combined test, PDF, and compatibility evidence.
- [M02 verification](m02-verification.md): independent triangle-contact annotations and current handoff.
- [M03a verification](m03a-verification.md): all four t-tree bubble placements and their publication.
- [M03b verification](m03b-verification.md): all four s-tree bubbles, published checkpoint and next seagull slice.
- [M04 verification](m04-verification.md): all eight external seagulls, PDF graph/contact checks and next swordfish slice.
- [M05 verification](m05-verification.md): all eight swordfish placements, shared-vertex graph checks and next triangle slice.
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
