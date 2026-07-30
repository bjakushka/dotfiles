---
name: sync-llm-rules
description: Align a project's LLM instruction files (CLAUDE.md, PROJECT.md) against a reference/template repo, in both directions. Use only when the user explicitly invokes sync-llm-rules to review and sync instruction rules with a template repo.
argument-hint: <path-to-reference-repo>
disable-model-invocation: true
---

# Sync LLM Rules

Review this project's LLM instruction files against a reference repo of instruction
templates and sync portable rules **both ways**, with confirmation.

## Invocation
Explicit only (`sync-llm-rules` / `$sync-llm-rules`). Do not auto-fire.

## Input
- Reference repo path — `$ARGUMENTS`, or ask for it.
- Current project — the cwd project.

## Step 1: Pick the template type
Scan the reference repo for type directories (e.g. `non-coding-project/`,
`coding-project/`), ignoring `.git` and other non-template dirs. List them and ask
which one to sync against. Default: one type. Allow selecting several only if asked.

## Step 2: Pair files by basename
Pair reference `X.tmpl.md` with the project's `X.md` (e.g. `CLAUDE.tmpl.md` ↔
`CLAUDE.md`, `PROJECT.tmpl.md` ↔ `PROJECT.md`). A file present on only one side is
itself a sync candidate (a missing counterpart may need creating).

## Step 3: Classify every rule into three buckets
This split is the whole point — do it before proposing anything:
- **Portable** — behavior/process rules that apply to any project (tone, editing
  protocol, "ask don't guess", push-back). These are what gets synced.
- **Domain/project-specific** — facts tied to one project (repo layout, paths,
  stack, "what this is"). Never sync these.
- **Template scaffolding** — `{{PLACEHOLDER}}` blocks, HOW-TO-USE and file-purpose
  comments. Never a diff; ignore them.

The reference type may be a different project class than the current project (e.g.
a coding project against a non-coding template). Sync the portable layer regardless.

## Step 4: Review differences, both directions
Each portable difference is one of:
- present on one side only → propose adding it to the other side
- present on both, worded differently → propose adopting the fuller/clearer wording

Direction (pull into project / push into template) follows from that. Judge by
content quality — completeness, clarity — not recency; there is no version signal.
Present the full classified set once, grouped by bucket and direction; take the
user's verdict per item.

## Step 5: Apply
Apply each confirmed change one file at a time: motivation + exact diff, wait for
approval. The show-diff-then-approval discipline applies to edits in **both** repos
(the reference repo may have no CLAUDE.md of its own). Do not commit either repo —
leave that to the user. Summarize what synced each way at the end.
