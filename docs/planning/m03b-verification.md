# M03b verification - external s-tree bubbles

Date: 2026-11-03. Baseline: published main `6549efa`, including M03a's
`2c3b467` loop-arrow fixes. Branch: `codex/m03b-s-tree-bubbles`.
M03a was fast-forwarded and pushed before this branch started. M03b is a local
checkpoint; its merge/push is pending. No user-side manual preparation is needed.

## Scope and public recipe

```tex
\STreeChannelCorr[
  field={},central={},leg-labels={,,,},show-momenta=false,
  line=plain,channel-line=plain,
  insertion=bubble,insertion-slot=3,
  bubble-top-line=plain,bubble-bottom-line=plain
]
```

Slots 1/2/3/4 mean upper-left/lower-left/upper-right/lower-right. Slots 1/2
attach to the left tree vertex; 3/4 to the right. Exchange remains slot 5.
Only the chosen external E--H edge changes: E--A, two parallel A--B arcs,
B--H. Four interaction vertices, eight edges, one loop. This is a self-energy
bubble, not a direct self-loop seagull or a shared-tree-vertex swordfish.
See the frozen [contract](../../regressions/topologies/insertion/M03b-contract.md).

The renderer reuses the proven host-relative split, styles, pre/post annotations,
loop momentum and index helpers. Historical private helper names containing
`ttree` remain internal implementation details; no public keys were renamed.
T-specific geometry and exchange annotation defaults stay T-specific. For the
new S insertions, automatic exchange momentum is 10pt above the horizontal edge
(angle 90, label above); explicit channel controls win. Ordinary S trees retain
their previous output. The existing 8pt loop-arrow clearance and outward label
sides carry over, including style allowance and reversal.

## Verification evidence

- Enabled S slots incrementally: slot 1, then 1-2, 1-3, 1-4. Each stage compiled
  and passed its actual graph and control checks before enabling the next slot.
- Final focused regression: **63 complete public-diagram cases**, including
  the generic `FourPointCorr[topology=s-tree]` dispatcher. It observes actual
  edge endpoints, selected host aliases, insertion ordering and collinearity,
  unchanged unselected legs, interaction-vertex count, inherited and explicit
  pre/post styles, single/double outer-only caps, mixed EW/Proca lines,
  logical momentum values/visibility, blank and reversed momentum, index
  attachment/controls, scales 0.72/1/1.2, geometry overrides and state reset.
  Coordinate-copy/PGF rounding tolerance is 0.03 TeX pt.
- **36 emitted loop-label geometry checks** verify that labels face outward
  and arrow clearance is 8pt plus existing style allowance, or an explicit 12pt.
  Explicit exchange angle/distance/label-side controls are asserted separately.
- The isolated Proca page has **16 white-filled pink tips** contacting the
  visible vertex outlines across all four S placements. The vector checker
  rejects extra/missing tips, loss of pink color, buried tips and visible gaps.
- **37 maintained regression/example documents pass**, with the existing
  **600 endpoint contacts**, **16 T-bubble contacts**, and **16 S-bubble contacts**.
- Twelve ordinary s/t/u tree control pages, including momentum/reversal and mixed
  styles/caps/indices, have **identical decoded PDF drawing streams** to published
  main `6549efa`. The T-bubble regression remains registered; its unsupported-host
  control now uses U instead of newly supported S.
- Atlas: **58 reproducible recipes on 12 pages**. C01-C04 add all four plain S
  insertions. Existing IDs and seagull examples are retained. Pages 1-5 and 7-11
  are pixel-identical above the intentionally changed baseline footer to M03a.
  Page 6 only adds the S-page cross-reference. Page 12 is new.
- Rendered and inspected all four gallery pages and all atlas pages (overview,
  changed pages at readable size). No clipping/overflow in the new pages. The
  dedicated index panel intentionally records the known, deferred placement issue.

## Explicit limits and deferred work

[D01](deferred-workflows.md) remains a separate later workflow. Index values,
attachment and existing controls are preserved; their messy visual positions
are not fixed or certified by M03b. No index anchor/offset/default was retuned.

One insertion at a time. U-tree and internal slot-5 bubbles remain unsupported;
S seagulls are still unsupported, including slot 1. Seagulls remain T slot 1
until M04. Bubble-local arc arrow-size slots remain 3/4 and share the existing
size list with external slots 3/4. Page-axis offsets retain their interpretation.
Arbitrary custom dimensions can still crowd the short pre/post host segments.

## Reproduce

From the repository root (use the bundled Python path for the optional PDF
vector checks when system Python lacks pypdf):

```sh
mkdir -p /tmp/feynmanfun-m03b-check
TEXINPUTS="$PWD//:" pdflatex -interaction=batchmode -halt-on-error \
  -output-directory=/tmp/feynmanfun-m03b-check \
  regressions/topologies/insertion/s-tree-bubble-slots.tex
python3 regressions/topologies/insertion/check-s-tree-bubble-contact.py \
  /tmp/feynmanfun-m03b-check/s-tree-bubble-slots.pdf
FEYNMANFUN_PDF_PYTHON=python3 sh scripts/check-regressions.sh
python3 docs/diagram-inventory/build.py
```

Gallery: `regressions/topologies/insertion/s-tree-bubble-slots.pdf`.
Numerical contact report: `regressions/topologies/insertion/s-tree-bubble-contact.json`.
Machine-readable closeout: [m03b-checks.json](m03b-checks.json).

Next feature session: **M04**, expand direct seagull insertions on remaining
T external legs and then S external legs, one placement at a time. Publish M03b
first when authorized. Index-placement cleanup stays deferred beyond these
feature sessions.
