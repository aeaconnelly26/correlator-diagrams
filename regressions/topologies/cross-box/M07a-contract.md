# M07a: complementary internal crossing

Baseline: published `main` at `56a643a`. Requirement R02; preserve verified R01.
The checklist P1-02 requests fixed top/bottom internal edges and crossed
left/right edges, complementary to the existing fixed-left/right layout.
External crossings (R03/R04) and ambiguous routing (R14/R22) are later slices.

Public interface: `CrossBoxCorr[cross-box-layout=left-right|top-bottom,...]`
and the existing `FourPointCorr[topology=cross-box,...]` dispatch. Default
`left-right` preserves existing geometry, styles and automatic circ behavior.
Inner half-spans remain 1.34/1.34, outer frame +/-2.10, compact scale 0.8.
Explicit dimension overrides remain valid.

| Slot | left-right (existing) | top-bottom (new) |
| --- | --- | --- |
| 1-4 | external UL/LL/UR/LR to corresponding corner | same |
| 5 | BL -> TL, fixed left | TL -> TR, fixed top |
| 6 | TR -> BR, fixed right | BL -> BR, fixed bottom |
| 7 | TL -> BR, split descending diagonal | same |
| 8 | BL -> TR, continuous ascending diagonal | same |

Each graph is a four-edge cycle with four trivalent interaction vertices and
four external endpoints. The diagonal crossing is unconnected: no fifth
vertex, and the split halves belong to one edge. Endpoint markers and indices
refer to the full logical edge, never the artificial gap endpoints.

Existing fixed-edge style fallback is box-left/right-line in left-right mode,
box-top/bottom-line in top-bottom mode. Diagonal up/down overrides stay
available; their fallback is box-top/bottom-line (old) or box-left/right-line
(new), respectively. Explicit slot line overrides are independent of layout.
Existing circle keys remain; first/second fixed-edge aliases avoid physical
side names in the new layout. `cross-box-circs=false` permits minimal Proca
diagnostics without changing the compatible automatic-circle default.

Add opt-in internal `cross-box-momenta={k5,k6,k7,k8}` and independent
`cross-box-momentum-5` through `-8` controls using the proven measured
gap/continuous-side annotation renderer. Internal annotations remain hidden
by default, preserving old output. Reuse box endpoint-index list controls
with the above slot table; retain D01 appearance as a later workflow.

Acceptance: actual-PDF graph reconstruction for both layouts, physical square
and crossing-gap checks, independent styles and slot overrides, no markers
at gap endpoints, mixed EW/Proca/scalar, labels in gaps or outside continuous
arrows, reversed/hidden momenta, index ownership, caps, custom dimensions and
scales, public aliases/dispatch and fresh-diagram reset. Preserve the existing
cross-box regression rendering and maintained suite. Update the reference,
requirements, atlas/recipes and session handoff before local checkpointing.
