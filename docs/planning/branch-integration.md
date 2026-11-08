# Integrated branch state and coding-session closeout

Current checkout at M08a publication: `main`. Verified checkpoint `d855152`
was fast-forward merged from `096b2b3` and pushed to GitHub (2026-11-08).
The feature branch is retained; package/tests/PDFs are unchanged. No M08a
merge/push remains; M08b contact seagulls is next. See
[publication](m08a-publication.json) and [verification](m08a-verification.md).
Earlier records retain their historical publication states.

M03a checkpoint `2c3b467` is now merged and published on main; see
[M03a verification](m03a-verification.md) and the current development plan.
Index placement is deferred to a separate later workflow, [D01](deferred-workflows.md).
M03b checkpoint `97495ba`, based on `6549efa`, is now also merged and published
on main. The branch `codex/m03b-s-tree-bubbles` is retained. It preserves index
behavior without polishing positions; see [M03b verification](m03b-verification.md).
M04 checkpoint `854293a` is now merged and published on main, including all
Nov 4 geometry/style reviews and the final optical W-circle correction. The
branch `codex/m04-seagull-expansion` is retained. The complete final suite passed
40 documents and 688 endpoint contacts; see [M04 verification](m04-verification.md).
No M04 merge or push remains pending. On 2026-11-06, M05 checkpoint `9daebf9`
was fast-forwarded from `efb5fae` into main and published with its documentation
handoff at `eb6182c`. M06 verified checkpoint `629356d`, including all reviewed
scale, shared-frame, S-exchange and endcap fixes, is now fast-forwarded into
main and published to GitHub (2026-11-06). At M06 publication the checkout was synchronized main;
the M06 feature branch is retained. M07a checkpoint `dfa0066`, implemented on
`codex/m07a-crossed-box-layouts` from `56a643a`, is now fast-forwarded into
main and published on GitHub (2026-11-07). At publication the checkout was synchronized main,
and the M07a feature branch is retained. No M07a merge/push remains. At that publication the
checkout was synchronized `main`. Verified M07c feature tip `40dae7b`, including
all M07b upper-routing work, D02 fixes and the circle default .8, was fast-forward
merged and pushed to GitHub on 2026-11-07. Both feature branches are retained;
no M07b/M07c merge/push remains. R04 remains deferred; M08a followed on its feature branch.
See [publication record](m07bc-publication.json).
No M06 merge/push remains. See
[M06 verification](m06-verification.md) and [publication record](m06-publication.json).
The branch `codex/m05-swordfish` is retained; no M05 merge/push remains.
Its [verification record](m05-verification.md) covers all eight placements,
41 maintained documents and 736 endpoint contacts. The main/M02 record below
preserves earlier history.

The published integration baseline was `6657735`. M02 checkpoint `8f95755`
is now merged into main and published to GitHub. The feature branch
`codex/m02-triangle-contact-annotations` is retained; see the
[current development plan](../development-plan.md) and [M02 verification](m02-verification.md).
At that closeout the checkout was main, synchronized with GitHub. No M02 merge
or push remains pending. M03a was subsequently implemented on its feature branch.

Updated 2026-11-03. The seagull and M01 lines are now combined on
`codex/integrate-seagull-and-proca`, with merge parents `1b85ef8` and `5a657cd`.
The original feature branches are retained. On 2026-11-03, local `main` was
fast-forwarded from `0dbf733` to verified integration commit `4584aff` at the
user's request, then reconciled with live GitHub `main` at `0717abb` and published
through a normal push. At that checkpoint the checkout was `main`; local and GitHub main
contain the combined work. No new pull request or force push was needed.

GitHub's `0717abb` records the already-merged PR #28. Its tree exactly matches
the seagull branch at `5a657cd`, so preserving that merge added no package or
inventory changes to our verified integration. GitHub reports main as unprotected,
no active rules, and this account as having push/admin permission. Those settings
were checked live; future sessions should fetch before reporting remote status.

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

M07c's R14/R22 audit is complete and published on main together with M07b
upper crossing, D02 circle fixes and the default circle scale .8. The source
branch `codex/m07c-reference-routing-review` and M07b branch are retained.
The package, maintained regressions and PDFs match the verified checkpoints:
50 documents / 850 contacts and a 126-recipe / 29-page atlas. The merge is a
fast-forward to verified feature tip `40dae7b`; this later publication handoff
changes documentation only. See [publication record](m07bc-publication.json).

That published checkpoint was the baseline for M08a contact-leg bubbles. R04 ordinary-box right
crossing remains user-deferred; R14/R22 share a missing opposite-pair
triangle-contact routing extension with an unscheduled implementation.
No manual Git preparation or M07b/M07c integration remains for the user.

Remote state was refreshed before the merge. Main was pushed successfully;
final `git ls-remote origin refs/heads/main` is checked against local HEAD after
the publication handoff. Start the next feature from refreshed main.

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
