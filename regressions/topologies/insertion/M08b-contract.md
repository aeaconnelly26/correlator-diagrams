# M08b contact-leg seagulls

Frozen before implementation, 2026-11-08. Published M08a feature d855152; publication handoff/base main 35c7959.

Interface: `FourPointCorr[insertion=seagull,insertion-slot=1]`, then slots 2 LL, 3 UR, 4 LR. Verify slot 1 first, then all four. Central/crossed quartic views share one graph; reject disconnected horizontal/vertical pairings and invalid/multiple slots.

Graph: retain quartic C. Replace selected outer--C edge with outer--V, V--C and one V--V self-loop. Six edges, two quartic interactions, four degree-one external nodes, one cycle. No bridge/stem or second loop vertex. Preserve +/-2.10 frame and compact scale .8. V must lie strictly inside the leg; positive insertion scale, loop size and looseness.

Defaults: insertion-position .40, insertion-scale .66, seagull-loop-size 1.55; source-facing upper loops up and lower loops down. This is +90 from outer-to-host on slots 1/4, -90 on 2/3. Explicit legacy top/bottom are host-relative, left/right are page-relative. Do not retune tree or bubble defaults.

Sources: S11-T1/T2 -> LR4, T3/T4 -> UR3, B1/B2 -> LL2, B3/B4 -> UL1. Each pair has neutral Z / directed W species variants; editing tooltip is context only. Test native EW variants and separate preferred pink scalar-polarization examples using existing public line options.

Reuse cap/style/marker/loop-momentum helpers, geometric concentric arrows and outward labels. Default external momentum p1/p2 in, p3/p4 out; preserve contact per-slot directions, hide masks, independent pre/post controls, four seagull endpoint indices and post-segment indices. Respect hidden external legs/interaction dots and consecutive reset. D01 index appearance stays deferred. No simultaneous/internal/stemmed insertions.

Acceptance: minimal plain PDF independently recovers four six-edge graphs with two degree-four vertices and one self-loop. All slots pass mixed styles, scale/position/orientation controls, momentum reversal/on/off/blank/visibility, outer caps, indices, actual white-filled pink marker contact and species/flow checks. Update gallery/atlas/roadmap and run maintained regressions before local closeout.
