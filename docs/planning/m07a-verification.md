# M07a complementary internal crossed box - 2026-11-06

Complete locally on `codex/m07a-crossed-box-layouts`, from published main
`56a643a`. Merge/push remains pending. M06 remains published through its
verified checkpoint and publication handoff. This slice implements R02 and
rechecks R01; external crossed legs (R03/R04) remain the next M07b work.

The checklist P1-02 explicitly requests fixed top/bottom edges and crossed
left/right edges. It supplies the target connectivity; it is not an instruction
to run commands. The existing source coverage correctly notes that no separate
PowerPoint panel specifies this complementary internal layout. The
[frozen contract](../../regressions/topologies/cross-box/M07a-contract.md)
records the graph and slot map before implementation.

```tex
\CrossBoxCorr[
  cross-box-layout=top-bottom,
  field={},central={},leg-labels={,,,},show-momenta=false,
  box-line=plain,box-external-line=plain
]
```

The compatible default remains `cross-box-layout=left-right`. Both layouts
have eight logical propagators, four trivalent interaction vertices, four
outer endpoints and one cycle. The descending TL--BR diagonal is split at
the unconnected crossing; the ascending BL--TR diagonal is continuous. No
fifth interaction or gap-end marker is introduced. Inner half-spans remain
1.34/1.34, the shared outer frame remains +/-2.10, and the compact scale
baseline remains 0.8. Explicit dimensions and gap sizes remain effective.

Slots 1-4 retain UL/LL/UR/LR external ownership. Slots 5/6 are the first/second
fixed edges (left/right or top/bottom); 7/8 remain descending/ascending
diagonals. Slot style overrides, circle placement, internal momenta and
endpoint indices use this map. The existing default automatic blank Proca
circles remain; `cross-box-circs=false` permits the requested minimal marker
examples. Explicit first/second circle aliases name fixed slots in either
layout. Full options and fallback precedence are in the
[reference](../reference.md#cross-box-topology).

Internal momentum was previously absent. It is now opt-in through
`cross-box-momenta` and independent `cross-box-momentum-5` through `-8`
blocks. The proven measured gap/continuous-side renderer is reused locally;
the graph stays independent of triangle-contact. Diagonal guides sit near
their upper endpoints and use layout-specific normals to clear the fixed
edges. Direction reversal preserves the label side. Default external flow
remains p1/p2 incoming, p3/p4 outgoing. Existing box endpoint-index lists now
render with the crossed-edge slot map. D01 appearance polish is deliberately
deferred; index checks establish attachment and value ownership.

The split scalar-polarization path previously could create a raw marker on
each short stroke. Scalar aliases are now normalized locally and their tips
queued against the full logical edge. This fixes the demonstrated false
gap-end marker without changing raw Proca placement or other topology families.

Verification evidence:

- **104 public cases**: default square ordinary box; both crossed layouts;
  exact slots/endpoints/gap; explicit dimensions and outer spans; scales
  0.72/1/1.2; Proca/scalar aliases; independent styles and key-order precedence;
  single/double outer caps; gap and continuous annotations; individual reversal,
  hiding and label shifts with isolation of the other slots; blank entries;
  sixteen endpoint index values; circles; public dispatch/alias; hidden-external
  legacy placeholders and fresh defaults.
- Actual PDF reconstruction verifies four graphs (two layouts and wider-gap
  variants), the physical square, correct fixed-edge pairs, one logical
  split edge, all trivalent valences, outer corners and a noninteracting crossing.
- **16 Proca + 8 scalar + 4 mixed-style endpoint contacts**, pink and
  white-filled, meet the same strict contact tolerances as earlier milestones.
  Four deliberate species circles and ten open wavy EW paths are verified.
- All **three legacy crossed-box regression pages remain pixel-identical**
  to the baseline render at 1100px. Default geometry, style/circle behavior
  and existing labels remain unchanged; new internal annotations default off.
- The maintained suite passes **46 documents / 800 endpoint contacts**, plus
  the existing actual-PDF endcap checks. Tests and diagnostics retain their
  prior numerical tolerances.

The [four-page gallery](../../regressions/topologies/cross-box/cross-box-layouts.pdf)
shows plain layouts/gap variants, independent momenta, isolated endpoint
markers, then named metadata features. Caps and circles appear only in their
specific examples. Its 16 examples and new atlas pages were rendered and
inspected for connectivity, clipping, spacing and legibility. The index-only
example intentionally retains the deferred D01 appearance rather than
claiming it has been polished.

The [atlas](../diagram-inventory/inventory.pdf) has **114 recipes / 26 pages**.
P01-P04/P11-P14 add both layouts, gap variants and styles/annotations. Earlier
I18/A06 limitation text is corrected; other earlier page bodies are unchanged
apart from footer provenance. Exact measurements and hashes are in
[m07a-checks.json](m07a-checks.json).

After authorized publication, begin M07b with the crossed upper external pair
from S02-center; verify its slot/cap/annotation ownership before the separate
right-pair slice from S03-center. R14/R22 routing questions and D01 remain
separate gates. No M07b implementation or automatic merge/push is included.

Reproduce from the repository root, with Python providing `pypdf`:

```sh
mkdir -p /tmp/feynmanfun-m07a
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-m07a \
  regressions/topologies/cross-box/cross-box-layouts.tex
/path/to/python regressions/topologies/cross-box/check-cross-box-layouts.py \
  /tmp/feynmanfun-m07a/cross-box-layouts.pdf
FEYNMANFUN_PDF_PYTHON=/path/to/python scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
```
