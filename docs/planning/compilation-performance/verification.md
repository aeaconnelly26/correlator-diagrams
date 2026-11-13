# Compilation-performance session

Baseline: published main `7069f39`, including crossed-vertex feature `8b41ca1`.
Implementation branch: `codex/compilation-performance`.

## Changes and preserved behavior

- Define the existing propagator styles through `pgfkeysdef`, the same public
  PGF API used by its `.style` handler. This removes repeated parsing of the
  declaration table. The styles still reset on each diagram and `corrset` call;
  argument-taking styles and local scalar-arrow overrides retain their behavior.
- Cache two parsed topology lists by expanded contents within each diagram.
  Left/right index lookups reuse their parses. Input changes, alternating lists,
  eviction, empty entries, grouped commas and nested scopes are covered. Every
  diagram starts with an empty cache; the original parser and trimming remain.
- Batch adjacent coordinate definitions into single TikZ paths. Coordinates
  retain their names, expressions and order, including references to preceding
  coordinates. No geometry formulas or marker dimensions change.
- Draw the two disconnected parts of the generic gapped momentum guides as
  one path. The arrowhead remains on the final subpath; gap positions, labels,
  line width and reversal remain unchanged.

All topology resets remain in place: profiling found their combined cost too
small to justify changing initialization and option precedence. The package
remains a single `.sty` file with the existing Overleaf installation workflow.
No public keys, diagrams, defaults, dependencies or index-placement rules change.

## Reproduce

Use Python 3 for timing; use a Python with Pillow for image comparisons and
`pypdf` for the maintained PDF checks. `pdflatex` and `pdftoppm` must be on PATH.
Save the published package in an isolated baseline directory:

```sh
mkdir -p /tmp/feynmanfun-baseline
git show 7069f39:feynman-fun.sty > /tmp/feynmanfun-baseline/feynman-fun.sty
python3 scripts/benchmark-compilation.py \
  --baseline-dir /tmp/feynmanfun-baseline \
  --output-dir /tmp/feynmanfun-benchmark --warmups 1 --repeats 7
python3 scripts/profile-compilation.py \
  --package-dir /tmp/feynmanfun-baseline --output-dir /tmp/feynmanfun-profile-before
python3 scripts/profile-compilation.py --output-dir /tmp/feynmanfun-profile-after
python3 scripts/check-compilation-output.py /tmp/feynmanfun-benchmark \
  --report /tmp/feynmanfun-visual-checks.json
FEYNMANFUN_PDF_PYTHON=/path/to/python-with-pypdf scripts/check-regressions.sh
```

The benchmark copies both package variants into matching flat directories,
alternates their order on successive repetitions, runs serially, and records
wall/user/system times, source/package hashes and engine details. Warm-ups are
excluded. Each run is one fresh-directory pdfLaTeX pass. The atlas workload uses
the existing 150-recipe source, including its original provenance footer.

To reproduce the additional compatibility comparison, compile
`regressions/performance/compilation-compatibility.tex` once against each package
with separate output directories and `TEXINPUTS=/path/to/package:`. Put the PDFs
in `compatibility/baseline/` and `compatibility/candidate/`, then supply
`--compatibility-dir compatibility` to the image checker. These probes cover
19 list assertions, argument-taking styles, wrappers, global/local options,
topology/key ordering, consecutive-call isolation and math array/aligned use.

## Measurement limits

Timings describe this local pdfTeX installation and these workloads. They do
not establish an Overleaf speedup or a gain for every possible document. Helper
profiles use inclusive instrumented times, which must not be summed or treated
as end-to-end benchmarks. Loading TikZ and drawing its paths remain substantial
costs; the session targets repeated package work without changing the output.


## Measured results

Seven measured runs per variant after one warm-up; times below include loading
and PDF output. Ranges and every raw sample are in [benchmarks.json](benchmarks.json).

| Workload | Baseline median | Optimized median | Change |
| --- | ---: | ---: | ---: |
| Empty document control | 0.234 s | 0.235 s | +0.3% |
| Package loaded, no diagrams | 0.490 s | 0.495 s | +1.0% |
| One plain contact | 0.511 s | 0.505 s | -1.2% |
| 40 plain contacts | 1.220 s | 1.164 s | -4.6% |
| 20 three-point diagrams | 1.108 s | 1.056 s | -4.6% |
| 20 decorated diagrams | 3.290 s | 3.143 s | -4.5% |
| 20 indexed boxes | 2.312 s | 2.189 s | -5.3% |
| 150-recipe atlas | 9.933 s | 9.741 s | -1.9% |

Negative changes mean faster compilation. The empty/load controls show noise
at this scale; no loading-time improvement is claimed. The atlas median improves
by about 1.9%, with overlapping ranges and some slower individual trials. The
repeated-diagram workloads improve by about 4.5-5.3% in these local measurements.

The [before](profile-before.json) and [after](profile-after.json) profiles isolate
repeated setup work: style configuration across 20 indexed diagrams falls from
31.1 ms to 4.2 ms; list access across that workload falls from 96.2 ms to 20.2 ms.
All topology resets together are only a few milliseconds in the mixed workload,
so lazy topology initialization was not implemented.

## Output preservation

[Pixel comparisons](visual-checks.json) pass on all 64 benchmark pages at 90 dpi,
including all 36 atlas pages. Both compatibility pages and the three
momentum-visibility pages match at 144 dpi. Both new compatibility pages were
also inspected visually. The existing atlas PDF and
recipes remain unchanged; no inventory rebuild is needed for identical output.
The [focused PDF](../../../regressions/performance/compilation-compatibility.pdf)
retains the existing D01 index crowding rather than retuning its appearance.

The existing visibility regression now counts disconnected draw subpaths rather
than `draw` macro invocations. Its original continuity, hidden-slot and label
assertions pass against both baseline and optimized packages; their three-page
output is pixel-identical at 144 dpi. This preserves the behavioral checks while
allowing two disconnected segments to share one TikZ draw command.

## Final verification and handoff

The full maintained suite passes: **55 documents**, all registered PDF checks,
and the unchanged **928 automatic endpoint contacts**. The new focused regression
is registered in the suite. Full stdout is saved in [regressions.txt](regressions.txt).
The compatibility assertions and visibility regression also pass against the
published baseline. Sources and evidence hashes are in [run.json](run.json).

Complete locally on `codex/compilation-performance`; no merge/push has been
performed. Published main remains `7069f39`. Integrate this checkpoint when
requested, then proceed to M09a. D01/D03/D04 remain separate; no new diagram
feature was started during this session.
