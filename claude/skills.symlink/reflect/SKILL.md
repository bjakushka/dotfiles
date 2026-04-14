---
name: reflect
description: Session self-reflection. Use when the user asks to reflect on the session, review how things went, extract lessons, or improve project instruction files. Analyzes the assistant's own decisions, quality of explicit project instruction files (CLAUDE.md and similar), and interaction patterns. Proposes edits as diffs; never writes files automatically.
disable-model-invocation: true
---

Produce a self-reflection on the current session in four sections. If a section has nothing substantive, write "no significant observations" rather than padding. Every claim must cite a specific moment from the session. Propose changes, do not apply them.

## 1. Assistant's mistakes

Independent of instruction quality — what did I get wrong this session?

- Wrong assumptions about the task, codebase, or user intent
- Suboptimal approaches chosen (and what should have been chosen)
- Skipped checks or tool calls that would have prevented an error
- Answers from memory where verification was warranted

## 2. Project instruction files

Scope: CLAUDE.md and other checked-in instruction files for agents (`.cursorrules`, `AGENTS.md`, agent-facing sections of `docs/` or README). Not memory, not the system prompt, not user prompts in this session.

For each relevant file, identify:

- What guided correct behavior this session
- Gaps that would have prevented a mistake from §1
- Contradictions with the actual codebase or with other rules
- Ambiguities the user had to resolve manually

Output every proposed change as a diff. No prose-only suggestions — if it cannot be expressed as a diff, drop it.

```diff
# file: CLAUDE.md, section "Testing"
- Run tests before committing.
+ Run `pnpm test:unit` before committing. Integration tests (`pnpm test:e2e`)
+ require a running Postgres — skip locally unless explicitly asked.
```

New sections: show as pure `+` lines with target file and header.

## 3. Strategic project context

New knowledge about the project that emerged — strategy, not tactics. Goals, constraints, architectural directions, non-goals. Exclude specific bugs, file contents, one-off fixes.

For each item, propose a target location (file + section). If the target is a project instruction file, format as diff.

## 4. Interaction patterns

Report a pattern only with evidence from at least two concrete moments in this session. One-off events belong in §1 or §2.

- Outputs accepted without changes — what kind?
- Outputs reworked or rejected — what was the correction?
- Corrections avoidable with information available at the time

State patterns with evidence, not inferred preferences:

- Weak: "User prefers concise answers."
- Strong: "In 3 moments (migration plan review, API sketch, error message draft) the user cut output by 40–60%. For review/draft artifacts, start shorter than feels complete."

If a pattern points to a fix in a project file, put the diff in §2 and cross-reference here.

## Language

Respond in Russian. Keep artifacts (diffs, file names, code, config keys) in English.
