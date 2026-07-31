---
name: start-work
description: Read project instructions and task context, then prepare a short work-start status. Use only when the user explicitly invokes `start-work` or `$start-work` to begin or resume work on a specific ticket without making changes yet.
---

# Start Work

Collect project and task context before implementation.

## Invocation Rule

Use this skill only on explicit user invocation such as `start-work` or `$start-work`.

Do not auto-apply this skill from a general request that merely sounds similar.

## Input

Expect a ticket id such as `PRJ-1234`, or a combined multi-ticket id such as `prj-1234-5678`
(see global CLAUDE.md "Multi-ticket work").

If the user does not provide a ticket id explicitly:
- list available ticket directories from `.claude/tasks/` when that directory exists;
- show only ticket names, not full paths;
- if no task directories exist, state that none were found;
- ask for the ticket id after showing the list;
- do not infer it from the branch name;
- do not infer it from recent task files;
- do not continue until the ticket id is provided.

## Resolve the task directory

Do not construct `.claude/tasks/<ticket-id>/` literally — list `.claude/tasks/`
and match the directory:

- case-insensitively (dirs may be lowercase, e.g. `prj-1234`);
- allowing a combined multi-ticket directory (e.g. `prj-1234-5678-9012/` covers
  `PRJ-1234`).

Use the matched directory as `<task-dir>` below. If no directory matches, follow
"Missing Task Directory".

## Read Order

Read these files in order when they exist:

1. `AGENTS.md` or `CLAUDE.md` in the current project root
2. `.claude/CODEBASE.md`
3. `~/.claude/CLAUDE.md`
4. `<task-dir>/desc.md`
5. `<task-dir>/notes.md` — if present: design decisions, field mappings, open questions, patterns
6. `<task-dir>/plan.md`
7. `<task-dir>/code-review.md` — if present: reviewer comments and their resolutions
   (one entry per comment: comment → decision done/deferred/rejected → why).
   A resolution with lasting design significance graduates into `notes.md`.

If a file is missing, continue with the remaining files and note what was missing.

## desc.md content rules

`desc.md` must contain the original ticket text as-is — do not rephrase, reformat, or restructure it. Strip only tool-specific markup (e.g. Jira `{{{}...{}}}` → backtick code, `*bold*` → `**bold**`), but keep all wording intact.

If `desc.md` already exists and reads like a paraphrase or restructured summary rather than the raw ticket, flag it to the user — do not silently trust or rewrite it.

If interpretation or design decisions are needed, add them as a separate section at the bottom of `desc.md` under `## Notes`, or put them in `notes.md` with a link from `desc.md`.

## Missing Task Directory

If `.claude/tasks/<ticket-id>/` does not exist:
- state that the task directory does not exist yet;
- do not invent task state;
- offer to create the task directory and starter files after user approval;
- stop after reporting this unless the user asks to continue with partial context only.

## Missing Plan File

If `desc.md` exists but `plan.md` does not:
- state that the task description exists;
- state that the task plan does not exist yet;
- continue with the available context;
- offer to create `plan.md` after user approval if needed.

## Optional code-review file

`code-review.md` is optional — created when review comments arrive on a task, not before.
It tracks reviewer comments during the review cycle, as both a fix-checklist and a record
of why code changed. One entry per comment: the comment, its decision (done / deferred /
rejected), and the reasoning.

Boundary: `code-review.md` is the per-comment working record during review; when a
resolution has lasting design significance, fold it into `notes.md` (the durable design
record). Do not duplicate — graduate.

When the user brings review comments on a task (now or in a later session), record them
in `code-review.md` — create it if absent. Add one entry per comment as above, and update
each entry's decision as comments are resolved. This keeps both the fix-checklist and the
"why it changed" history in one place. Per Change Policy, propose creating/updating it and
wait for approval before writing.

## Output

After reading, provide a concise status report with:

- current task state;
- what is already done;
- what is already completed in the plan, if `plan.md` exists;
- next concrete step;
- open questions, blockers, or assumptions to clarify before continuing.

Keep the report short and operational.

## Change Policy

Do not modify any files without the user's explicit approval.

Until approval is given:
- stay in read-only mode;
- do not create task files;
- do not update task files;
- do not start implementation;
- do not change code, config, or documentation.
