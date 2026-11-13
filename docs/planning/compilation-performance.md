# Intermediate session: compilation performance

Requested 2026-11-13, after publishing the crossed-vertex checkpoint and before
M09a. This session optimizes package structure to reduce document compilation
time. Complete locally on `codex/compilation-performance`; merge/push is pending.
Repeated diagram batches improve by about 4.5-5.3%, and the atlas median by 1.9%
in local paired measurements; loading is effectively unchanged. All 55 maintained
documents / 928 endpoint contacts and registered PDF checks pass, with 69
pixel-identical page comparisons. See [verification and reproduction commands](compilation-performance/verification.md).
M09a follows integration; no next feature implementation has started.

## Baseline and measurements

Started from published main `7069f39`, containing crossed-vertex feature
`8b41ca1`, on `codex/compilation-performance`. Preserve the existing public
macros, keys, aliases, default geometry, option precedence, and per-call reset.
Keep the single-package Overleaf installation workflow working.

Measure package loading separately from drawing. Use an empty document with
the package loaded, a simple diagram, repeated simple diagrams, and representative
decorated box/crossed-vertex and bubble/seagull/triangle insertions. Include the
atlas as an end-to-end workload. Record engine/version, source revision, commands,
diagram counts, repeated wall/user timings and their spread, with warm-up runs
identified. Run timings serially, with identical inputs and settings before and
after each change. Compare against a document without the package to estimate
fixed loading cost; do not mistake dependency loading for per-diagram work.

## Structural review

Use measurements to select small changes. Initial inspection identifies these
questions, not established bottlenecks:

- `FourPointCorr` currently invokes resets for numerous topology families on
  every call. Can unrelated work be avoided while preserving keys supplied
  before/after topology selection, wrapper defaults, and consecutive-call isolation?
- Which option parsing, list resolution, geometry calculations and decoration
  setup repeat within one diagram? Can resolved values be reused safely within
  its local scope?
- How much time is spent loading definitions versus expanding helpers and
  drawing TikZ paths? Splitting the source into files alone is not evidence
  of a compilation improvement.

## Acceptance and closeout

Retain only changes with repeatable measured benefit on the affected workloads,
and report any regressions elsewhere. Compare rendered output against the
published baseline; preserve graph connectivity, labels, markers, caps, indices,
scales, crossing gaps and intentional tuning. Exercise mixed consecutive calls,
global/local options, wrappers, and array/aligned compatibility when changing
initialization or dispatch. Run the maintained suite and its PDF checks before
closing the session. Save reproducible benchmarks and before/after results.

M09a and new diagram features follow this session. D01 index appearance, D03
crossing/circle spacing and D04 decoration cleanup remain separate unless a
measured performance change requires touching their internals while preserving
their visible behavior.
