---
name: plan-task
description: Analyze a new task, explore the codebase for context, and create structured task files before writing any code. Use when starting a fresh ticket that needs upfront analysis and a plan.
argument-hint: [TICKET-ID]
---

# Task Planning Workflow

Your job is to **analyze, not implement** — understand the task, explore the
codebase, and produce a plan. Do NOT write application code in this skill.

## Input
- Ticket ID (e.g. PRJ-1234) — passed as `$ARGUMENTS` or in the conversation
- Task description — inline, or ask the user to paste it before proceeding

If only the ticket ID is given without a description, ask for the description first.

## Step 1: Load context
Read the project instruction files (`CLAUDE.md`, and `.claude/CODEBASE.md` if present)
to understand structure, conventions, and the task-file layout this project uses.

## Step 2: Reformulate the task
Before exploring code, restate the task in your own words: what/why, likely-affected
area, patterns involved. Present to the user and confirm understanding before going deeper.

## Step 3: Explore the codebase
Use the Explore agent to investigate the relevant parts:
- Find existing analogues to follow (e.g. adding a V4 endpoint → read the full V3 one:
  controller, request, DTO, validators, mappers)
- Read interfaces, base classes, contracts, registration/config mechanisms
- Check how similar features are tested; read fixtures and test patterns
Read the key files yourself to verify and deepen understanding.

## Step 4: Identify scope and open questions
- Files to create / to modify / explicitly unchanged (auto-registration, existing enums)
- Open questions — ambiguities that can't be resolved without reading real code;
  for each, name the step that will resolve it
Present scope and open questions to the user for discussion.

## Step 5: Create the task files
After the user confirms the analysis, create the task directory `.claude/tasks/<ticket-id>/`
(lowercase; for inseparable multi-ticket work use a combined id like `prj-1234-5678` - see global
CLAUDE.md "Multi-ticket work") with three files:

- **`desc.md`** — the task description. Paste the original ticket text verbatim; strip only
  issue-tracker-specific markup (convert it to plain markdown). Add interpretation/design
  decisions in a separate `## Notes` section at the bottom, or link to `notes.md`.
- **`notes.md`** — design decisions and the "why": field mappings, chosen approaches and the
  reasoning, gotchas, open questions with lasting significance. This is the durable record a
  reviewer reads to understand why the code looks the way it does.
- **`plan.md`** — the execution plan:
  - Split steps into **blocks** by dependency order (e.g. DB/Entity → Presentation → Tests);
    state explicitly that later blocks depend on earlier ones.
  - Each step = one concrete artifact: the file path(s), a one-line why, any dependency.
  - Add **verification checkpoints after each block**, not only at the end (the exact checks
    are project-specific — take them from the project's CLAUDE.md).
  - A checklist with status per step so progress can be tracked across sessions.

Present the block structure and open questions to the user before starting implementation.

## Rules
- Write task files in the language the project mandates (see CLAUDE.md)
- Do NOT write application code — only analyze and plan
- Prefer bullet lists over tables
- Note explicitly when NO change is needed — it saves time during implementation
