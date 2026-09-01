# AGENTS.md — Rules for Cursor (and any agent) in k-sebe-yoga

Internal development project. Static landing page for a yoga practice.

## 0. Language policy (MANDATORY)

All repository content is in English — README, specs, docs, commit messages, PRs.
The landing page itself is in Russian (the audience is Russian-speaking), stored
as a static asset, not as repo documentation.

## 1. What this project is

Static landing site for **k-sebe-yoga** — yoga classes in Berlin/Potsdam
for Russian-speaking women. Free outdoor practice, gentle tone, "returning to
yourself" framing (not fitness). No backend, no auth, no database. Pure static
HTML/CSS served via GitHub Pages.

## 2. Process

- **PR-only to main.** Never commit or push directly to `main`. Every change:
  branch -> PR -> review -> merge.
- **Lite cycle** (decided by Danil for non-GitHub static): brief + README +
  registry + team copy review + light build plan + quick QA + owner approval.
  No full OpenSpec/BDD/TDD pipeline — it is overkill here.
- **GitHub Issues cover every change.** If no Issue exists for the intended
  change, create one before starting. Non-code Issues (docs, copy) can be opened
  and closed without a PR. Code changes must reference `Closes #...`/`Refs #...`.

## 3. Copy rules

- The copy is the client's voice — do not paraphrase her text without asking.
  Reviewers propose edits, the final word belongs to the owner.
- Dates/times/prices in the copy must match the brief exactly — do not invent
  or "fix" them from memory.

## 4. PR Stack & Force-Push Rules — GitHub auto-close protection

**Critical rule: `git push --force` to a branch with open PRs auto-closes them on GitHub.**

When you force-push to a branch that has an open Pull Request, GitHub detects
the force-push and closes the PR. This is **by design**, not a bug.

### Rules

1. **Never `git push --force` to a branch that has an open PR.** If you need to
   rewrite history, first close all PRs on that branch with an explanatory comment,
   then force-push, then reopen or create fresh PRs.
2. **Never force-push to a branch that is the `base` of another open PR.**
   Even if the branch itself has no open PR, force-pushing it closes every child
   PR that depends on it.
3. **When restructuring a stack, create new branches.** Do not rewrite old ones.
   Pattern: close old PRs (with comment) -> delete old remote branches ->
   create new branches -> open new PRs. Deleting is safer than force-pushing.
4. **If auto-close happens accidentally, do NOT reopen the same PR.** Create a
   fresh PR from the new branch head instead.
5. **Cursor/Grok must not touch branches belonging to other tasks.** No
   force-push to branches of other open PRs, stacks, or tasks.
6. **`git push --force-with-lease` is restricted to YOUR OWN branch only.**
   Permitted only for rebasing your own feature branch after a parent was merged.

## 5. Roles

- **Owner — Danil (zedxter).** Approves copy, green-lights work.
- **Yennefer** — coordination/PM.
- **Geralt** — CI/CD, tech review.