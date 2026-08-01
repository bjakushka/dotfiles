---
name: bootstrap-project
description: Bootstrap a new project from an instructions template and tune its LLM instruction files (CLAUDE.md, PROJECT.md) iteratively, as reviewable diffs. Use only when the user explicitly invokes bootstrap-project to set up and shape a fresh project from a reference/template repo. Distinct from brainstorm (design dialogue, no template) and sync-llm-rules (aligns files in an existing project).
argument-hint: <path-to-template-repo>
disable-model-invocation: true
allowed-tools: Read Glob Grep Bash Edit Write Agent
---

# Bootstrap Project

Set up a new project from a reference template and shape its instructions through
dialogue, so every change lands as a diff the user can see and approve.

## Invocation
Explicit only (`bootstrap-project` / `$bootstrap-project`). Do not auto-fire.

## The keystone (do not skip or reorder)
Copy the template **verbatim** first → the user commits that clean base → **then**
iterate. Every later edit is a diff against the untouched template, so the
template→project transformation is visible and reviewable. This ordering is the
whole reason the process works. Do not "helpfully" fill placeholders during the
copy.

## Two disciplines — keep them separate
- **Editing files** → always show motivation + the exact diff, one file at a
  time, wait for explicit approval. Never relax this.
- **Asking the user choices** → calibrate. Ask when the fork is high-stakes or
  genuinely changes the work. For low-stakes gaps, pick the sensible default,
  apply it, and say which one you took. Do not turn every small choice into a
  question — over-asking is as much a failure as guessing.

## Inputs (Phase 0)
Gather, don't guess:
- **Template repo** — `$ARGUMENTS`, or ask for the path (e.g. an `_llm_rules`
  repo of instruction templates).
- **Template type** — if the template repo has type dirs (`non-coding-project/`,
  `coding-project/`, ...), list them and ask which to use.
- **Reference projects** — existing projects to mirror conventions from. When you
  need these and the user hasn't given paths, offer the choice: they hand you the
  paths, or you go look. Do not scan their whole tree on a guess.

## Phase 1: Clean base
1. Confirm the target is its own repo (or ask whether to init one) — the user's
   "I'll commit" presupposes a repo exists.
2. Copy the template files verbatim (placeholders and HOW-TO-USE blocks intact).
3. Verify the copies are byte-identical to the template.
4. Hand off: the user commits the clean base. Commits are the user's job
   throughout — never commit for them unless told to for a specific step.

## Phase 2: Understand the project
Learn what you're shaping before shaping it. Ask (calibrated, prefer multiple
choice, lead with a recommended option):
- what the project is and its goal
- domain, and whether it needs domain-specific rules
- how results/artifacts are produced and stored, if any
- language conventions (conversation vs files vs artifacts)

## Phase 3: Discuss structure before building
Interrogate structural decisions before committing to them. Push back on weak
ideas: give the strongest reason first, try a couple of distinct arguments, and
change your position when the user gives a strong counter. Apply YAGNI — a logical
boundary is cheap now; physical splits and automation wait for a real need.

Softly surface reusable structural options the user may want (see
"Options to raise"). Ask about them; never impose them.

## Phase 4: Tune instructions section by section
Turn the verbatim template into real instructions, one section (sometimes one
rule) at a time:
- for each: show motivation + exact diff → approval → apply
- keep the **portable / domain-specific** boundary clean — behavior rules live in
  CLAUDE.md, project facts in PROJECT.md; catch leaks in either direction
- strip every placeholder; delete sections that don't apply (ask separately for
  deletes)
- give each new markdown file a short hidden HTML maintenance comment at the top

See examples.md for concrete question and diff phrasings.

## Phase 5: Park deferred work
When something is worth doing but not now, write it to a notes inbox
(`_notes/inbox.md` or the project's equivalent) as a rough parked item — don't
drop it, don't build it. Close parked items out loud when a later phase resolves
them.

## Phase 6: Outside review
When the shape is done, get a fresh outside review (the `advisor` tool if
available, otherwise a clean subagent or a second model). Feed it the actual
diffs, not just a summary. Relay the feedback honestly, then close the findings
that need action with the user.

## Options to raise (know them, don't insist)
General, reusable structural choices to surface as gentle questions — the user may
simply have forgotten one. Only raise what applies to *this* project:
- repository topology — single repo vs a two-repo split (instructions/meta vs
  data/results), with a logical boundary as the lightweight middle ground
- whether to version-control at all, and git vs something else
- commit-message / pre-commit hooks (a reusable githooks template, if one exists)
- a notes/inbox location for parked ideas and backlog

Test before raising: would this apply to a random next project? If it's specific
to one project (a particular data schema, per-domain language rules, exact commit
rules), it is at most an illustration — never a default you push.

## Principles
- The keystone ordering is non-negotiable; everything else serves reviewability
- Understand the goal before proposing a solution
- One idea at a time in dialogue; prefer multiple choice; lead with a recommendation
- Explicit over implicit, in instructions and in files
- Don't over-build — structure grows only when the user decides it should
- Commits and other mutating git operations are the user's unless told otherwise

## Language
Keep artifacts (files, names, diagrams) in English.
