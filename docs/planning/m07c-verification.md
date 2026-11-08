# M07c reference-routing audit - 2026-11-07

Completed as a source/specification audit on
`codex/m07c-reference-routing-review`, created from M07b closeout `843c2bf`.
The inherited package remains the tested `e2521e2` implementation. No package
feature, maintained test or capability-atlas recipe/PDF is changed.

[Illustrated three-page audit](m07c/routing-audit.pdf),
[numbered graph/slot data](m07c/routing-map.json),
[current public recipes](m07c/recipes.md),
[precise future slice](m07c/future-routing-plan.md) and
[independent PDF checks](m07c/pdf-checks.json).

## Source result

Both slide-13 native images were extracted unchanged from the archived PPTX.
Image49 is the left panel (slide x offset 643467 EMU); image50 is the right
panel (6253817 EMU). Each has three filled interaction dots: a quartic Q and
cubic A/B. The dense right-side crossing is formed by external paths and flow
arrowheads; it has no separate interaction dot. The loop is W/W/Z.

| Panel | External hosts 1/2/3/4 | Quartic pair | Internal Z joins |
| --- | --- | --- | --- |
| S13-left | Q / A / B / Q | 1/4 | A(q2) -- B(q3), internal slot 6 |
| S13-right | A / Q / Q / B | 2/3 | A(q1) -- B(q4), internal slot 5 |

Both maps have seven logical propagator edges, interaction valences 4/3/3
and one cycle. Q/A/B are source-trace names, not new public package identifiers.
External q numbering follows the established UL/LL/UR/LR convention; q numbers
are not printed in the original slide images. The correspondence between these
maps and the PDF's q1-q4/q3-q2 wording is an inference from the two references,
recorded explicitly in the map and illustrated report.

## Capability result

All four documented triangle-contact choices were compiled through public
`TriangleContactCorr` calls, with equal 1.1 internal half-spans:

- top: quartic pair 1/3;
- bottom: pair 2/4;
- left: pair 1/2;
- right: pair 3/4.

Two additional public recipes show existing EW/Z styling (Z on slot 6 for top,
slot 5 for bottom). They preserve the existing adjacent-pair routing and are
explicitly marked as loop/style examples, not reproductions of S13.

The shape family and square bounding-frame controls already exist. Fixed-slot
opposite quartic attachments do not: relabeling outer text, rotating a figure,
or changing spans is not a working recipe for the required attachment map.
R14/R22 are now **Missing**, with a resolved specification, rather than unclear
references. R22 preserves both source-panel records for the same R14 extension;
no additional loop family is added to M10 or counted in the current atlas.
The user-deferred ordinary-box right crossing R04 remains a separate item.

## Verification and boundaries

- Fresh compile: `routing-audit.tex`, three pages, no LaTeX errors/overfull boxes.
- All three pages rendered and visually inspected; traces use minimal plain
  lines with only endpoint/vertex labels and the highlighted Z edge.
- Actual PDF stroke reconstruction independently verifies the two source traces
  and six existing public outputs: seven edges, valences 4/3/3, one cycle,
  fixed shared outer frame, correct quartic external pairs and no gap vertex.
- The styled recipes each place one default-scale .8 Z circle on the edge
  joining the two cubic vertices. Square span overrides are measured from output.
- The existing package's documented orientation choices and hardcoded host
  assignments were inspected; no general external-host routing key exists.
- The archived original PDF/PPTX and native extracted panel checksums are verified.
- Package, maintained regression source/script and the current 126-recipe /
  29-page atlas artifacts match the existing checked hashes. Its prior full
  **50-document / 850-contact** result remains applicable; this audit does not
  claim a fresh full-suite run or new implemented target diagrams.

The targets on page 1 are labeled source-trace specifications, drawn for this
audit. Only pages 2/3 are public package outputs. The current-capability atlas
is linked to the audit without adding unsupported recipes or altering its PDF.
The PDF reconstruction checker is a checkpoint-specific audit tool, not a
maintained claim that future public routing choices are absent.

## Handoff

M07c's specification audit is complete. The proposed opposite-pair routing
extension remains **unscheduled and unimplemented**, with exact graph maps and
staged acceptance criteria saved for a later requested coding session.
Next scheduled work is **M08a contact-leg self-energy bubbles**, one leg first,
then all four; M08b contact seagulls follows. R04 remains user-deferred; D01
index appearance and D03 residual circle/crossing spacing remain separate.

This branch inherits all unmerged M07b work. No merge, push or PR was performed;
local main remains `813736e`. The assistant handles integration when authorized
and selects the correct prerequisite base for future sessions. Historical M07b
closeout/verification records retain their earlier scheduling; this audit and
the current development plan supersede those next-step notes.
