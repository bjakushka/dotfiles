---
name: onboard
description: Read a project's instructions, structure, and workflow at the start of a session so everything needed is loaded into context before work begins. Use only when the user explicitly invokes onboard to get oriented on a project without making changes.
disable-model-invocation: true
---

# Onboard

Get oriented on this project at the start of a session: load its instructions and
context, understand its structure and how work is organized. Make no changes.

## Invocation
Explicit only (`onboard` / `$onboard`). Do not auto-fire.

## Ground rule (state it back)
Do not change project files or instructions without approval. To propose a change:
show motivation + the exact diff, one file at a time; discuss if needed; apply only
after explicit approval. Delete/move asked separately.

## Steps
1. Read `CLAUDE.md` and follow every `@`-import in it (those pull in the project
   facts, e.g. PROJECT.md).
2. Read stable project context under `.claude/` (if absent, skip it silently):
   instruction and workflow markdown such as project, behaviour,
   troubleshooting, and active-task pointer files. Skip `settings*.json`,
   `skills/`, `agents/`, and `tasks/`.
3. Do not read task files during onboarding. Read `.claude/tasks/**` only when
   the user explicitly names a task, ticket, or task file.
4. Look over the project structure (top-level layout, entry points) to see how it
   is organized and how work with it flows.
5. Note any obvious inconsistency (a referenced file that is missing, stale
   pointers), but do not fix it — just surface it.

## Finish
Give a short summary: what the project is, how it is organized, the workflow, and
anything that needs clarifying. End with a brief "ready — what do we do?".
