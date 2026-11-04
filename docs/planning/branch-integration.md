# Branch state and coding-session closeout

Updated 2026-11-03. Branches are separate lines of development: a feature
existing on one branch does not put it in another branch or in `main`.

## Current integration state

| Line of work | Local state | Present in main? |
| --- | --- | --- |
| `main` | Last inspected at `0dbf733`, merge of bubble-on-leg PR #27 | Baseline |
| `codex/proca-endpoint-audit` | M00 inventory/roadmap, M01 audit/fix, and this documentation cleanup; checkpointed locally | No |
| `codex/seagull-insertion` | Five additional commits through `5a657cd`; local tracking ref points to the same commit | No |

The seagull branch contains more than seagulls: vertex-aware endpoint work,
external momentum visibility, channel label-gap changes, mini external indices,
a Compton example, and broader regression coverage. Its seagull prototype
supports **t-tree external slot 1 only**. It does not complete all four legs
or s-channel support. The inventory now includes two clearly marked examples
rendered against that branch's pinned revision, without merging its code.

The initial inventory audited the checked-out `main` lineage and did not inspect
the unmerged seagull branch. This omitted existing branch-only work and allowed
the M01 endpoint investigation to overlap older endpoint work. Before M02,
review the overlapping fixes and integrate deliberately. Do not treat either
branch's entire package file as the winner during conflict resolution.

Tracking-ref statements above are local observations; they are not a claim
that a fresh remote fetch has been performed.

## Next integration checkpoint

1. Start from a clean local checkpoint; inspect all relevant branch histories.
2. Compare the seagull branch's endpoint helpers with M01's tip-anchor change.
   Preserve its one-sided markers and existing APIs; resolve overlaps in the
   helper code rather than dropping a whole branch's implementation.
3. On an integration branch, reconcile code and documentation, retaining the
   archived source requirements and current branch provenance.
4. Run the combined regression set, endpoint vector checks, seagull-specific
   cases, and the existing momentum/index behavioral assertions. Visually
   inspect affected examples before declaring the integration complete.
5. Rebuild the inventory from the integrated package. Move seagulls from the
   unmerged appendix into the current-capability pages only after they actually
   work in that checkout. Reassess remaining milestones against the integrated
   source, especially M01 and M04, before starting M02.

This document records the integration work needed; this cleanup does **not**
perform the merge, push branches, or create/merge a pull request.

## Session workflow going forward

At session start, inspect the worktree, current branch, recent commits, and
relevant unmerged branches. Do not start a new feature from stale `main` when
its prerequisites are on another branch. The assistant handles the Git work
needed for an authorized task; the user does not need to perform manual merges
before continuing in this chat.

At session end:

1. Finish the focused code and applicable regression/visual checks.
2. Update recipes, reference, requirement status, inventory source and PDF,
   and the next-session handoff. Identify branch-only features explicitly.
3. Create a local checkpoint commit for the completed work. Preserve unrelated
   user edits and identify any intentional unfinished work separately.
4. Report the branch, commit, test results, working-tree state, inventory update,
   and exactly whether anything was pushed or merged.
5. Unless a push/PR/merge is requested or otherwise authorized, leave the
   checkpoint on its feature branch. Explain any pending integration instead
   of implying that a local branch was merged into `main`.

A local commit, a push, and a merge are three separate steps. Continuing on the
same feature branch uses its committed work immediately. Starting the next
branch requires the right prerequisite base; that is an assistant responsibility,
not a manual preparation task silently left for the user.

## Minimal diagnostic examples

Show only the features under test. Endpoint diagnostics use plain EW external
legs and Proca test paths, without endcaps or independent circ decorations.
The audit suppresses the crossed-box circle-placement pass locally in its test
harness; package defaults are unchanged. A dedicated circ compatibility control
can retain a circle because that particular example tests circ compatibility.

The inventory's main pages show minimal structure. Dedicated style examples
may demonstrate caps or circles when that is their stated purpose, including
the user's explicitly requested capped t-channel example. Seagull branch
examples have no caps, circs, labels, or momenta.
