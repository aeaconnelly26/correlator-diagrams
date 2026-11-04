# Integrated branch state and coding-session closeout

Updated 2026-11-03. The seagull and M01 lines are now combined on
`codex/integrate-seagull-and-proca`, with merge parents `1b85ef8` and `5a657cd`.
The original feature branches are retained. On 2026-11-03, local `main` was
fast-forwarded from `0dbf733` to verified integration commit `4584aff` at the
user's request. The current checkout is `main`. Nothing was pushed and no pull
request was created or merged. A documentation-only follow-up records this state.

## What is integrated

- Seagull insertion on **t-tree external slot 1**, including directed one-sided
  Proca loop markers and the branch's equilateral marker-size repair.
- External momentum visibility, continuous unlabeled arrows for empty entries,
  tree-channel side-label gap fixes, and compact external indices.
- The reusable scalar-QED Compton example and the broader regression runner.
- M01 raw Proca tip anchoring, custom per-line radius, and legacy overrides.
- The archived source record, requirements map, roadmap, minimal diagnostic
  preference, and inventory generation tooling.

Seagulls are rendered with the current integrated package, not an extracted
unmerged package. The atlas has nine pages and 43 current recipes. The earlier
branch-only page and seagull development plan are preserved in `history/`.

## Reconciliation decisions

The marker implementations address different paths. Keep M01 for raw Proca
paths and keep the seagull branch's managed straight/curved marker helpers,
including the configurable semantic radius and 0.25pt clearance. Explicit
per-line M01 radius or legacy-distance options still select the corresponding
raw geometry inside managed straight helpers, in either option order.
Both legacy distance key names are honored; the M01 endpoint-distance key takes
precedence when both are explicitly non-default. No duplicate markers are queued.

The combined audit measures actual visible stroke outlines: a 0.25pt semantic
clearance is not a visible gap when the dot and triangle outlines touch. It also
rejects buried tips, lost fill/color, and unexpected endpoint counts. This is
verified in addition to the original one-sided triangle-dimension assertions.
See [integration verification](integration-verification.md) for the evidence.

## Next coding session

M02 can now start on a new branch based on current local `main`, which includes
integration commit `4584aff`. No manual Git preparation is needed from the user. M04 remains
an expansion of the existing single-leg seagull prototype, not a new prototype.
The other t-tree legs, s-tree support, swordfish, and regular triangles remain
future requirements.

Local tracking refs were inspected without a fresh remote fetch; this record
does not claim to have checked for newer remote commits.

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
the user's explicitly requested capped t-channel example. Seagull
examples have no caps, circs, labels, or momenta.
