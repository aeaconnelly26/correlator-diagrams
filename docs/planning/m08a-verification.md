# M08a contact-leg self-energy bubbles - 2026-11-08

Implemented R13 on `codex/m08a-contact-bubbles`, based on published main
`096b2b3`. This is a local checkpoint; merge/push is pending. M08b contact-leg
seagulls is next after integration. The checklist's P4-01 and all four native
S10 panels are covered: TL -> slot 1, BL -> 2, TR -> 3, BR -> 4.

## Interface and graph

```tex
\FourPointCorr[
  field={},central={},leg-labels={,,,},blob=false,
  line=plain,show-momenta=false,
  insertion=bubble,insertion-slot=1
]
```

Change the selected slot to 2/3/4 for LL/UR/LR. `FourPtCorr` is an alias.
`contact-pairing=central` and `crossed` are equivalent quartic insertion hosts,
not different graph topologies. Disconnected horizontal/vertical pairings are
rejected. No seagull, swordfish, internal or simultaneous contact insertion is
claimed by this milestone.

The original contact C remains quartic. The selected outer--C propagator is
replaced by outer--A, two parallel A--B arcs, B--C. There are seven propagators,
three interaction vertices with valences 4/3/3, four degree-one external nodes
and one cycle. A and B are distinct, ordered and strictly inside the selected
leg. The common +/-2.10 outer frame and compact coordinate scale are unchanged.

Geometry is host-relative, reusing the tree bubble coordinate/arc helpers;
no slot-specific hand drawing or label positions. Defaults are position .50
and scale .50. Explicit position/scale, base bubble span and outer-frame
changes work if the bubble fits. Nonpositive scale/span and non-fitting
requests fail explicitly. Ordinary no-insertion diagrams use their previous
renderers. Hidden external legs suppress the insertion while preserving the
existing amputated endpoint placeholders. Hidden center vertices hide all
three interaction dots.

## Styles and metadata

Logical external styles, single/double caps and segment overrides use the
existing semantic helpers. Only the outer segment receives the logical outer
cap; post segments and loop arcs strip it. EW waves, Proca/spol endpoint
markers and independent bubble arc styles remain available. `circ` remains
explicit for pink Proca lines; its unset scale remains .8.

Both selected pre/post guides keep the selected logical external momentum.
Defaults are p1/p2 incoming, p3/p4 outgoing; global left/right reversal and
existing per-contact direction controls are honored. Visibility hides both
segments of the selected leg. Blank loop labels hide that arc's guide.
Pre/post momentum controls and each arc's controls remain independent. Loop
labels clear their guide along its actual outward normal. There is no exchange
edge or channel momentum on a contact host.

Bubble endpoint indices, external pre-segment indices and independent post
indices remain attached through the existing helpers. D01 appearance tuning
is explicitly deferred; attachment checks do not certify polished index layout.
R04 and R14/R22 routing work remain separate, unscheduled/deferred as recorded.

## Evidence and deliverables

- Slot 1 was compiled, inspected and passed the first focused slice before
  expanding the all-slot test matrix. The final maintained regression exercises
  **78 public diagram cases**, plus the amputated-host check. It checks selected
  host aliases, seven edges/three vertices, ordered collinear A/B, logical style
  inheritance and overrides, single/double outer caps, momenta/visibility/blanks,
  reversal/per-contact direction, endpoint/pre/post indices, scales .72/1/1.2,
  explicit frame/position/scale, hidden markers, aliases and consecutive resets.
- **38 rendered loop labels** have measured outward clearance, including
  explicit arrow-offset and label-distance overrides.
- **12 rejection cases** require the intended package error: slots 0/5/lists,
  disconnected pairings, endpoint positions, zero/negative scale/base span,
  and a non-fitting bubble. These are failures by design, not no-op compiles.
- Independent PDF stroke recovery verifies all four seven-edge graphs, valences,
  two parallel arcs, exact selected corner, one cycle and unchanged outer frame.
- Actual visible-ink checks verify **24 new white-filled pink endpoint contacts**:
  16 across the minimal four-scale Proca page, eight in the styled page. The
  latter also has eight black W circles at default .8 size and no pink circles.
- The maintained suite passes **51 documents / 874 automatic endpoint contacts**
  (the prior 850 plus 24 new); see [saved output](m08a-suite.txt).
- The five-page [focused gallery](../../regressions/topologies/insertion/contact-bubble-slots.pdf)
  separates plain connectivity, momenta, cap/index controls, minimal marker contact
  and named EW/Proca species samples. All pages were rendered and inspected.
- The [atlas](../diagram-inventory/inventory.pdf) now has **134 recipes / 31 pages**.
  CT01-CT04 are plain; CT11-CT14 are named species samples. All pages were
  rendered/reviewed and the new pages inspected at reading size. The previous
  **29 page bodies are pixel-identical at 90dpi**, excluding footer provenance.
  Original source archive checksums remain unchanged.

The [frozen contract](../../regressions/topologies/insertion/M08a-contract.md),
[checks and hashes](m08a-checks.json), [recipes](../diagram-inventory/recipes.md)
and [reference](../reference.md#semantic-insertions) are persistent handoff records.

## Reproduction

From the repository root:

```sh
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/private/tmp regressions/topologies/insertion/contact-bubble-slots.tex
python3 regressions/topologies/insertion/check-contact-bubble-errors.py
python3 docs/diagram-inventory/build.py
```

For PDF assertions, use a Python with `pypdf` (the bundled runtime was used):

```sh
python3 regressions/topologies/insertion/check-contact-bubbles.py \
  /private/tmp/contact-bubble-slots.pdf
FEYNMANFUN_PDF_PYTHON=/absolute/path/to/pypdf-python scripts/check-regressions.sh
```

Use `pdftoppm` to render both deliverables after changes; inspect connectivity,
marker contact, caps and labels before proceeding to M08b.
