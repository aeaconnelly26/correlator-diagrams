# Compact scale review - 2026-11-06

The current 102-recipe / 23-page atlas is rebuilt with a package-wide
coordinate baseline of 0.8. New `scale=1` matches former `scale=0.8`.
The logical shared frame and topology connections remain unchanged. All
pages were rendered for review; the numerical/visual evidence and full-suite
results are recorded in [scale verification](../planning/scale-baseline-verification.md).
M06 remains local and D01 remains deferred. The records below preserve the
previous larger-baseline checkpoints.

# M06 current local inventory - 2026-11-06

The atlas has **102 public recipes / 23 pages**, built on
`codex/m06-tree-triangles` from published main `eb6182c`. M06 remains local.
Pages 20-21 show the four larger equilateral triangles and styled examples;
pages 22-23 compare the shared outer frame across trees, boxes and contact
orientations. The seven-page gallery has 28 examples.

The user clarified that the common span may grow when applied consistently.
The default outer frame is now +/-2.10 on both axes for ordinary/corrected
trees, channel loops, box/crossed box and triangle-contact. The prior
first-nineteen-pages pixel-identity result describes checkpoint 2506354;
these pages intentionally change where they use the new defaults. All 23
pages and all seven gallery pages were rendered and inspected.

191 focused triangle cases and 188 cross-family frame cases pass. Actual PDF
paths independently verify triangle connectivity/equilateral size, the shared
frame in twelve comparisons, four wavy styled exchanges, and 24 Proca + 12
scalar contacts. Styled W-circle centering is retuned and measured. See
[M06 verification](../planning/m06-verification.md) and
[frame verification](../planning/four-leg-frame-verification.md) for full-suite
results and limits. D01 remains deferred. Earlier sections preserve history.

# M05 published inventory - 2026-11-06

The atlas now has **86 public recipes on 19 pages**, built against
`codex/m05-swordfish` from published main `efb5fae`. Verified checkpoint
`9daebf9` is now merged and published on main. Its package and PDF hashes match;
publication changed documentation only. The footer retains its build provenance.
Pages 17-18 show the full T/S swordfish placement matrix; page 19 adds mixed
EW W/pink Proca Z loop styles and a pink Z exchange. All three new pages and
the six-page focused gallery were rendered and inspected for connectivity,
marker contact, annotation placement, clipping and crowding. Both loop momentum
labels were also inspected on undecorated examples in all eight placements.

Independent actual-PDF checks verify eight seven-edge graphs with three
interaction vertices, degree pattern 3/3/4 and one pair of parallel edges
sharing the actual tree vertex. Endpoint diagnostics verify 32 Proca and 16
scalar contacts. The 167-case focused source and full 41-document/736-contact
suite pass. The first sixteen atlas page bodies are pixel-identical to
published main `efb5fae` above their changed revision footer.

See [M05 verification](../planning/m05-verification.md) for reproduction and
limits. Index-position polish remains D01. The records below are historical
and do not override this current published M05 status.

# M04 published and ready for M05 - 2026-11-04

Final M04 checkpoint **854293a** was fast-forwarded from `b4a6ad8` into main
and published to GitHub. The remote main ref was read back and matched the
published checkpoint. The implementation branch is retained. This handoff
commit changes documentation only; package sources and PDF artifacts remain
exactly as verified at 854293a.

The full suite was rerun on 854293a: **40 documents**, **688 endpoint contacts**,
eight actual quartic self-loop graphs, **40 species circles**, **eight optical
seagull W placements**, **eight geometric bubble-host W placements**, and the
EW wavelength/order/reset checks pass. Focused coverage includes 254 seagull
cases, 88 loop labels, 800 curve samples, 56 size probes and 41 central-visibility
probes. The atlas remains 74 recipes / 16 pages, including the final styled
samples and optical correction. The prior full-suite statement scoped to
ddf9d0e is superseded by this complete run on the final checkpoint.

Live GitHub reads showed main unprotected and no repository/inherited rulesets.
Publication used an ordinary push; an initial HTTP transport failure was resolved
by a buffered HTTP/1.1 retry. No force push or PR was needed.

Next session: **M05 / R12 external swordfish**. Start from main, create a new
feature branch, freeze the S08-L1 shared-vertex graph, and implement one placement
at a time. Index-position appearance remains deferred to D01. No M05 code was
implemented in this publication session; no M04 merge/push remains for the user.

Earlier sections below are historical implementation/review records.

# Optical W-circle centering correction - 2026-11-04

The screenshot following `ddf9d0e` exposed a flaw in the previous verification
criterion: a circle halfway between vertex centers leaves unequal visible
space because the pink triangle occupies more of the segment than the black
dot. The old midpoint test therefore did not establish the requested visual
balance. The seagull default position remains 0.40.

The styled seagull recipes now shift W about 3pt toward the tree vertex using
existing `circ position`: **0.588 on T** and **0.599 on S**, shared across each
channel's four slots. The values are measured for the standard 6pt endpoint
arrows and default sample geometry/scale. Other arrow sizes or geometries may
need their own circle position. No package source/defaults change here.

The PDF checker now extracts the actual pink triangles as well as circles and
dots. It projects their visible stroke extents onto each inner segment and
requires equal free space on the two sides of W (center error below 0.05 PDF pt).
All eight seagulls pass: approximately **7.62pt / 7.62pt** free gaps on T and
**5.80pt / 5.80pt** on S; maximum center error is below 0.004 PDF pt. The eight
bubble-host W circles retain their vertex-midpoint check. The 40 species circles
and 32 endpoint-contact checks also pass.

Recompiled the styled gallery (56 size probes plus 41 visibility probes) and
the atlas (74 recipes / 16 pages), rendered and inspected the changed examples,
and compared a zoomed before/after crop. Both styled bubble pages have identical
drawing streams to ddf9d0e. The package and other maintained sources are unchanged;
the full 40-document/688-contact suite last passed at ddf9d0e, and this follow-up
reruns the changed focused gallery/checker. M04 remains local and D01 deferred.

Current results/hashes are in [m04-checks.json](../planning/m04-checks.json); the preceding
record is in [history](../planning/history/m04-checks-ddf9d0e.json). Earlier midpoint claims
below retain their historical meaning and are superseded for seagull styling.

# Seagull position and centered inner W circles - 2026-11-04

From local `d64ab3d`, supported s/t-tree seagulls default to
`insertion-position=0.40`, measured from the outer endpoint toward the tree
vertex. The inner segment is 60% of the original leg rather than 50%, giving
20% more length for a W circle. Explicit positions are preserved; 0.50 restores
the former placement. Bubble insertion positions remain 0.50. Styled host W
circles explicitly use `circ position=0.5` on the longer inner segment.
They were already at their nominal midpoints; this change improves the available
space rather than correcting a displaced circle.

The focused seagull matrix adds 32 independent position-projection cases across
all eight placements: new defaults, former midpoint override, custom 0.68 and
reset on the following call. It now has **254 public cases**, retaining **88
loop-label checks** and **800 concentric geometry samples**. The independent
styled PDF checker verifies **16 centered inner W circles** within 0.03 PDF pt
of their vertex-to-vertex segment midpoints. Seagull-page minimum circle/vertex
ink clearance improves from 7.780 to 10.616 PDF pt on T, and 6.252 to 8.778 on S.
The global minimum remains 1.012 PDF pt on the unchanged bubble pages.

All 40 maintained documents, 688 endpoint contacts, eight seven-edge quartic
self-loop graphs and wavelength checks pass. Both bubble pages in each of the
styled gallery and momentum review retain identical decoded drawing streams.
Refreshed the atlas (74 recipes / 16 pages), seagull matrix, styled sampling,
momentum review and insertion prototype PDFs. Changed pages and every seagull
placement were rendered and inspected. Index controls/appearance tuning remains
D01; M04 is local, with publication pending before M05.

Current results/hashes are in [m04-checks.json](../planning/m04-checks.json); the preceding
record is preserved in [history](../planning/history/m04-checks-d64ab3d.json). Earlier
sections retain their original scope and measurements.

# Short EW bubble waves - 2026-11-04

From local `d7cde72`, the short W loop arcs in J02/J04 and all eight styled
bubble samples use a shorter wavelength: `10\feynhandlinesize` instead of
the ordinary 22 line widths. This adds roughly twice as many ripples around
the W circle. Bubble dimensions, wave amplitude, other line styles, species
circles, two-ended pink markers and all momentum choices are retained.

The additive line option `ewboson wavelength=...` keeps the former 22-line-width
default and is shared by EW/photon aliases. The two-page EW frequency regression
adds four equal-length controls and default/short-wave examples on both tree
channels. An independent PDF checker observes **24/54/54/24 curve segments**:
shortening adds visible oscillations, an alias with reversed key order matches,
and the following default line returns to its original density. The entire
original gallery page is pixel-identical to `d7cde72` compiled from source.

Rebuilt the atlas (74 recipes / 16 pages), all-slot styled PDF and frequency
gallery; rendered and inspected the changed pages and all eight W bubble arcs.
The maintained suite passes all 40 documents, 688 endpoint contacts, species
circle/graph checks and the new wavelength check. Existing 56 size and 41 central
visibility probes also pass. M04 remains local; index placement remains D01.

Current hashes/results are in [m04-checks.json](../planning/m04-checks.json); the preceding record is preserved
in [history](../planning/history/m04-checks-d7cde72.json). Earlier sections retain their original scope.

# Quiet styled stems and S inner-label spacing - 2026-11-04

From local `347fd37`, the styled samples now omit the central exchange momentum
arrow and its P label. Pink EW Z stems and their Z species circles remain.
All eight S styled examples set the inner host-label gap to 4pt instead of 2pt,
including the slot-2 p2 label shown in the screenshot; T sample gaps and the
ordinary package label-spacing defaults remain unchanged.

An additive public key, `show-channel-momentum=false`, hides the complete
central tree-exchange annotation. Its default is true on each call, preserving
existing behavior. It supports s/t/u trees, including s/t bubble/seagull
insertions, and preserves external/loop annotations and all propagator styles.
The global `show-momenta=false` switch still suppresses all annotations.
There is no change to the four-legged loop-channel momentum helpers.

The styled gallery adds **41 complete public-diagram visibility probes**:
central on/off across all sixteen insertions, defaults restored on consecutive
calls, ordinary s/t/u exchanges and an explicit true override after false.
Emitted label counts verify external and loop labels are retained. The earlier
56 size probes, 40 species-circle checks and 32 endpoint-contact checks remain.
The atlas (74 recipes / 16 pages) and all-slot styled gallery are rebuilt,
rendered and visually inspected. All 40 maintained documents and 688 endpoint
contacts pass. All first 15 atlas page bodies are pixel-identical above the
footer to `347fd37`, confirming unchanged default rendering; styled gallery
PDF text contains no central P labels. The package change is limited to
independent visibility; index
placement remains D01. M04 remains local, pending authorized publication.

Current hashes/results are in [m04-checks.json](../planning/m04-checks.json); the preceding record is preserved
in [history](../planning/history/m04-checks-347fd37.json). Earlier sections retain their historical
scope and validation counts.

# Two-ended pink loop clarification - 2026-11-04

From local `fd42a61`, J01-J04 and the sixteen-example styled gallery now use
`{proca,magenta!85!red}` for the pink Z loop lines. That existing style supplies
two open endpoint arrows without adding a circle. `spol` normally supplies only
one endpoint arrow; `circ=...` is independent of either style. Pink EW Z stems,
bare outer segments, inner W circles and k-only loop annotation are retained.
No package source or defaults changed.

Recompiled the 56-case/16-example focused gallery and the 74-recipe/16-page
atlas; rendered and inspected the changed page and every styled example.
The independent PDF check still verifies 40 EW circles (16 pink stem Z / 24
black W), now also requiring 32 contacting pink endpoint arrows, two per loop.
These are additional to the unchanged 656 contacts of the preceding full-suite
run, for 688 contacts across the maintained checks. The maintained suite remains
40 documents; this follow-up reruns the changed gallery and PDF checker only.
The earlier full-suite result belongs to `fd42a61`. Current hashes are recorded
in ../planning/m04-checks.json; the preceding record is archived as
../planning/history/m04-checks-fd42a61.json. M04 remains local; D01 is deferred.

# Smaller bubbles and species sampling - 2026-11-04

Current atlas: **74 recipes / 16 pages**, reviewed from `33551c6` on the local
M04 branch. Bubble insertions use default scale 0.50 (about 24% smaller), while
seagulls retain 0.66 and explicit sizes remain effective. J01-J04 sample pink
EW Z stems/circles/text, bare outer segments, inner W circles, pink scalar-
polarization loops without circles, and mixed W/spol bubbles. The W arc has no
momentum guide or label; only the pink loop arc has k. No caps or indices.
These are styling recipes, not changes to global propagator defaults.

The all-slot styled gallery has 16 visible examples and 56 size/override/reset
probes. Independent PDF checks find 40 EW circles (16 pink stem Z / 24 black W),
with minimum circle/vertex ink clearance 1.012 PDF pt. All 40 maintained documents
and the existing 656 endpoint contacts pass. The previous seagull gallery's six
pages and the two seagull momentum-review pages have identical drawing streams.

Changed atlas pages 6/12/16 and all styled gallery pages were rendered and
inspected, alongside the smaller bubble momentum review. M04 remains local;
D01 remains deferred. The other 13 existing atlas page bodies are pixel-identical
above the footer to `33551c6`; all 16 pages were rendered. See [M04 verification](../planning/m04-verification.md)
for exact scope, commands and artifact hashes. Records below are historical.

# Compact seagull momentum refinement - 2026-11-04

The seagull arc is shorter (default 0.30-0.52), closer to the loop (6pt
radial offset), and has a tighter k label (2pt rectangle clearance). Shared
geometry and automatic midpoint placement are retained across all eight
positions; explicit overrides remain effective. The review and atlas PDFs
are rebuilt and visually inspected. Recipe/page counts remain 70/15; bubble
review pages and all propagator/index geometry are unchanged. Earlier values
below belong to the preceding geometry review.

# Seagull curve/label consistency follow-up - 2026-11-04

The atlas remains 70 recipes / 15 pages. Seagull momentum curves now share the
loop center, and labels use the local outward normal at the actual arrow-range
midpoint. This replaces the former translated curves and four-way anchors.
The focused seagull checks now cover 222 public cases, 88 text rectangles and
800 paired geometry samples. Both bubble momentum review pages retain identical
drawing streams to `9124a0b`. No loop propagator, topology or index placement
changed. Current evidence and hashes are in M04 verification/checks; earlier
counts below describe preceding checkpoints. Updated pages were rendered and
inspected before delivery.

# M04 screenshot-review inventory verification - 2026-11-04

Current atlas: **70 recipes / 15 pages**, reviewed on the M04 branch from
`229526e`. T seagull auto loops face inward; S loops outward. H01-H04 add
plain momentum examples with 1/2 incoming and 3/4 outgoing, compact host
arrows and measured text clearance. Short bubble arrows expand for readability;
S bubble k/ell labels move outward while T loop annotations retain their spacing.

The four-page momentum review shows all 16 insertion placements. Its 84 public
cases verify emitted flow across the four-point families, 130 text rectangles,
32 loop directions, adaptive arrow spans, explicit overrides and isolation.
The S-bubble gallery adds measured loop-text clearance and a distance override.
All 39 maintained documents and 656 contact checks pass. The existing seagull
PDF path parser still verifies eight seven-edge quartic self-loop graphs.

All changed PDF pages were rendered and inspected. Index placement is left
as D01. Current package/source/PDF hashes and detailed reproduction are in
[M04 verification](../planning/m04-verification.md). M04 remains local;
main/GitHub remain at `b4a6ad8`. Earlier records below are historical.

# Historical M04 inventory verification - 2026-11-03

Current atlas: **66 public recipes on fourteen pages**, built against
`codex/m04-seagull-expansion` on published main `b4a6ad8`. G01-G04 and
G11-G14 add the complete external s/t-tree seagull placement matrix. G01
repeats U01's graph explicitly; style/layout variants are recipes, not distinct
topologies. Existing IDs and prototype style examples remain unchanged.

The six-page focused gallery has 32 examples, 206 complete public-diagram
checks and 72 measured outward-facing loop labels. Independent PDF path
extraction verifies all eight plain seagull graphs: seven edges, one quartic
self-loop and two trivalent tree vertices. The isolated Proca/scalar pages
verify 24 pink, white-filled endpoint contacts. All 38 maintained documents
and 656 total endpoint contacts pass.

All pages were rendered and inspected; changed pages 6/8 and new 13/14 were
reviewed at readable size. Pages 1-5, 7, 9-11 are pixel-identical above the
updated footer to the previous atlas. Fourteen original seagull/tree/bubble
control pages retain identical decoded drawing streams to the baseline.
The index panel records D01; no index appearance was retuned. M04 remains
local, with main/GitHub at `b4a6ad8`.

See [M04 verification](../planning/m04-verification.md) for recipes, exact scope,
unsupported controls, reproduction and next-session handoff. Historical records
below retain their original counts and support boundaries.

# Historical M03b inventory verification - 2026-11-03

Current atlas: **58 public recipes on twelve pages**, compiled against
`codex/m03b-s-tree-bubbles`, based on published main `6549efa`. New C01-C04
show the four s-tree external self-energy bubble placements, plain and unlabeled.
All previous IDs and seagull examples remain. Page 6 cross-references the new
page 12. Pages 1-5 and 7-11 are pixel-identical above the updated baseline
footer to the M03a rendering. All pages were rendered and inspected; changed
pages were reviewed at readable size.

Focused S gallery: four pages, 16 examples, 63 automatic diagram cases and 36
measured outward-label/arrow-clearance checks. All 37 maintained documents and
632 endpoint-contact checks pass (600 existing, 16 T-bubble, 16 S-bubble).
Twelve ordinary s/t/u tree controls have identical decoded drawing streams to
published main. The dedicated index panel records current placement as a known
limitation, explicitly deferred to D01; M03b did not retune index positioning.

See [M03b verification](../planning/m03b-verification.md) for scope, controls,
limits and reproduction. M03a and M03b are merged and published on main;
M03b checkpoint `97495ba` retains these exact verified package/PDF hashes.
Historical records follow and retain their original counts/limitations.

# Historical M03a inventory verification - 2026-11-03

Current atlas: **54 recipes on eleven pages**, built against
`codex/m03a-t-tree-bubbles` on baseline `b917ed2`. I29 retains slot 1;
B02-B04 add the lower-left, upper-right and lower-right external bubble placements.
The main topology pages remain plain and unlabeled. Seagulls remain t-tree slot 1.

The four-page focused gallery has 16 examples and 52 automatic public-diagram
checks: actual graph/vertex/selected-leg geometry, pre/post style inheritance,
logical momentum labels and visibility, blank/reversed momenta, independent
indices, outer-only caps, scale/position changes and state reset. Its isolated
Proca page has 16 vector-checked white-filled pink endpoint tips. All 36 maintained
documents and the existing 600-contact endpoint audit pass. Slot 1 was compared
with baseline: text is identical, with maximum PDF text displacement 0.014pt
from coordinate-copy/polar rounding; rendered connectivity and styling are retained.
That baseline comparison belongs to the initial `04f3913` checkpoint. The later
user-requested review intentionally reduces default loop-arrow spacing and fixes
label sides. It checks 34 rendered labels for outward placement and measured
default/explicit arrow clearance, in addition to the topology matrix.

All new gallery pages and changed atlas pages were rendered and reviewed.
See [M03a verification](../planning/m03a-verification.md) for scope, recipe and
reproduction commands. Records below preserve earlier milestone states/counts.

# Historical M02 inventory verification - 2026-11-03

Current atlas: **51 recipes on eleven pages**, compiled against M02 on baseline
`6657735`. Existing structural IDs and seagull examples remain intact. T01-T04
add one annotation example for each triangle-contact orientation; they are style
and annotation variants, not new topologies. T05-T08 add the continuous-arrow
alternative. All examples use current public APIs. The review corrections replace
the earlier displaced-label and fixed fractional-gap defaults.

The five-page M02 diagnostic includes 20 minimal rendered examples and automated
checks on complete public diagrams. These observe emitted coordinates, verify
all seven slots independently, preserve the other six, check outside half-planes,
label-only movement, grouped keys, aliases, reversed arrows, scales, visibility,
and consecutive diagrams. Further checks require actual label centers inside
default breaks, compact external arrows/gaps, the correct quartic-side slots,
and one continuous stroke per side-label annotation. No unnecessary endcaps
or circ decorations are used.
Both edges connecting the quartic vertex to a trivalent vertex now point toward
the trivalent vertex by default. Connectivity-based checks cover all four
orientations in both momentum layouts; explicit direction overrides remain.

All **35 maintained regression/example documents** pass; the independent Proca
PDF check still passes **600 automatic contacts**. The final atlas and M02 gallery
were rendered and inspected. See [M02 verification](../planning/m02-verification.md)
for the implementation boundary and reproducible commands. Older PDFs and audit
records below preserve the behavior of their stated revisions.

# Historical integrated inventory verification - 2026-11-03

Current atlas: nine pages and 43 recipes, all compiled against the combined
checkout from parents `1b85ef8` and `5a657cd`. There is no branch-only package
extraction or PDF inclusion. U01/U02 are now current-capability recipes;
S01-S03 demonstrate loop endpoint selection, and F01-F03 demonstrate the
integrated annotation controls. Earlier branch-only artifacts are archived.

The expanded endpoint audit has 26 pages and 600 automatic contacts; all
34 maintained regression/example documents pass. See
[integration verification](../planning/integration-verification.md) for the
marker reconciliation and geometry-check method.

The sections below are historical M00/M01 records, including their original
page counts and source-state statements. They do not override the current
integrated status above.

# Latest inventory branch review - 2026-11-03

The current atlas has eight pages: the original seven pages of current-checkout
capabilities (35 examples), plus two unmerged seagull examples on page eight.
The additional page is compiled in isolation with `codex/seagull-insertion`
at the full pinned revision in `catalog.json`, not with the current package.
Those recipes are explicitly branch-only. The earlier audit did not inspect
that branch; its no-seagull claim applied to the checked-out lineage only.

The remaining sections preserve the M00/M01 audit history. See
[branch integration](../planning/branch-integration.md) for the correction
and prerequisite work before M02.

# Inventory verification - 2026-11-03

## M01 refresh

The current atlas was rebuilt with the generic Proca endpoint correction on
`codex/proca-endpoint-audit` (base `0dbf733` plus working-tree changes).
Its page count and 35 example IDs are unchanged. See the
[M01 results](../../regressions/propagators/proca-endpoints/results.md) for
the 144-case/24-page diagnostic, 568 automatic contact checks, legacy controls,
and passing maintained regression suite. Triangle labeling remains M02 work.

The following sections preserve the **initial M00 audit record**; statements
about source being unchanged and endpoint work being pending describe that
earlier inventory baseline, not the current M01 working tree.

## Baseline and scope

- Repository baseline: `main` at `0dbf733`.
- `feynman-fun.sty` and `correlator-diagrams.sty` are byte-identical to HEAD.
- This work adds reference records, roadmap documentation, atlas source/data,
  recipes, and a documentation builder. It implements no package feature.
- Both supplied originals match their archived copies and manifest SHA-256
  checksums. The historical development plan matches the pre-refresh HEAD copy.

## Compilation

During baseline inspection, **all 27** pre-existing TeX documents in
`example.tex`, `vertex-example/vertex-example.tex`, and `regressions/**/*.tex`
compiled with `pdflatex -interaction=batchmode -halt-on-error`, repository
`TEXINPUTS`, and separate temporary output directories. This includes files
outside the current maintained smoke script. No tracked regression PDFs were
regenerated or replaced.

The final atlas compiled twice per build through `build.py`, with **35 unique
example IDs on seven PDF pages**. No overfull or underfull box diagnostics were
reported in the final build. All recipes use public package macros; there are
no hand-drawn substitute topologies. Temporary compiler products and page
renders remain outside the repository.

## Visual review

Every final page was rendered at 1450-pixel page height and inspected:

| Page | Inspection |
| --- | --- |
| 1 | Two-point node and all four three-point corner orientations. |
| 2 | Central/paired/crossed contact layouts; disconnected pairs are explicitly identified; flat contact. |
| 3 | Three tree exchanges and three four-legged bubbles; crossed tree has a gap and no crossing vertex. |
| 4 | Square box; existing internal crossing; straight/angled/left/right half-box presets and marker differences. |
| 5 | All four triangle-contact placements, with correct single quartic contact position. |
| 6 | One-loop bubble, two-loop sunset with its middle line, and an actual bubble on t-tree leg 1. |
| 7 | Pink Proca t-bubble with four double caps; polarization; circles/caps; pink bridge momentum/indices; curved bubble momenta/indices; crossed Proca circle. |

The final atlas has no clipped captions, overflowing cells, or missing examples.
Recipe-only corrections were made during review: omit the explicit global
`line=plain` in A04 so it does not override the pink bridge; label external
momentum arrows explicitly in A05; enlarge diagrams for readability.

## Coverage and integrity checks

- Exactly 29 main inventory IDs and six appendix IDs; each appears once in the PDF.
- All canonical public topology families are represented; wrappers/aliases are
  listed separately without adding to the topology count.
- Exactly 22 requirement IDs, 23 PDF source items, and 90 unique diagram-panel
  IDs; every panel maps to a known requirement.
- All 23 slides are accounted for. Cover/handwritten context and the embedded
  screenshot/tooltip are marked separately. Composite slide 11 is indexed as
  eight visible diagrams rather than its smaller image-object count.
- Duplicate structural examples and species/flow variants are identified.
  Slide 20 is an s-tree seagull sheet, not a contact-host sheet.
- Requirement-to-source references agree in the JSON records; Markdown
  records contain every requirement; local documentation links resolve.
- Source archive checksums pass; originals remain unchanged.

## What has not been certified

The atlas verifies the displayed structures and selected style recipes. It
does not certify every combination of labels/styles/indices, establish physics
equivalence, or replace the planned Proca and annotation audits. Known limits:

- Only t-tree external slot 1 supports semantic bubble insertion.
- The existing crossed-box draw path lacks the full internal momentum/index
  pass; a compiled unused option does not count as support.
- Triangle-contact annotation settings share controls and include hard-coded
  adjustments; independent placement remains M02 work.
- Existing Proca markers remain as rendered; full vertex-contact verification
  is M01, including short/curved/crossed paths.
- R14 and R22 require endpoint tracing at their future specification gates.

The source checklist's styling and naming requests are recorded as targets;
they were not treated as authorization to implement new package behavior in
this inventory session.
