<!--
Concrete phrasings for bootstrap-project. Illustrations from a real run, not
rules. Adapt to the project at hand; never copy project-specific choices as
defaults.
-->

# Examples

Worked phrasings from a real bootstrap (a non-coding assistant project). Treat
them as illustrations of the *shape* of good questions and diffs, not as a script.

## Calibrating: ask vs default

**Ask (high-stakes, changes the work):**
- "Two separate repo with the external meta-layer and internal project, or single repo? This changes
  the file map and the commit workflow."
- "What format for the data-files — it drives whether we need a conversion
  step later."

**Default and mention (low-stakes):**
- Title `Personal Assistant` vs `Assistant` → pick one, say "I used
  `Personal Assistant`; say if you'd rather the shorter one."
- Whether to delete an empty template section → "Deleting the empty `Meta` section
  (placeholder only); it comes back when there's something to put there."

The failure mode in both directions: guessing on a high-stakes fork, or turning a
low-stakes gap into a question. Neither is acceptable.

## Question style (Phase 2–3)

Prefer multiple choice, lead with a recommended option, mark it "(recommended)":
- one question carries one decision; don't stack unrelated choices
- give each option a one-line consequence, not just a label
- when you recommend, say why in the option description

## Pushing back before building (Phase 3)

The user proposed two physical repos. Instead of complying or refusing, the
exchange interrogated it:
- named what was right (keeping human-readable source, out of the binary
  collection format)
- separated *logical boundary* (cheap, do now) from *physical two-repo split*
  (has sync cost, wait for a real reason)
- recommended the lighter option, then changed position when the user gave a
  strong reason (they edit results by hand, outside the assistant)

The lesson encoded: push back with the strongest reason first, but update on a
genuine counter — don't dig in, and don't fold silently.

## Verbatim copy, then diffs (Phase 1 → 4)

Phase 1 copies the template untouched. The *first* Phase 4 diff is the
template→project transformation, visible in full:

```diff
-# {{PROJECT_NAME}}
+# Personal Assistant

 ## What this is

-{{ONE_OR_TWO_SENTENCES: what this project holds and its goal}}. Not code. The
-value is the notes and the thinking, not tooling around them.
+An assistant for building and organizing personal something. Not code. The value
+is the data and the thinking about how to make them, not tooling around them.
```

Each edit shows motivation + this exact diff, waits for approval, then applies.

## Catching a portable / domain leak (Phase 4)

A scope-guard line ("Don't build import pipelines... until I ask") was first put
in PROJECT.md, then caught: it's a *behavior* rule, so it belongs in CLAUDE.md,
not in the project-facts file. The boundary check — "is this how the assistant
behaves, or a fact about the project?" — moved it to the right file.

## Parking deferred work (Phase 5)

Open questions went to `_notes/inbox.md` as rough items under `##` headings, so
they survived out of the conversation:

```markdown
## Data raw format and schema inheritance

Decide the storage format for data files. Approach: add some real
data-files, then design the schema from it — don't design it in a vacuum.
```

When a later phase resolved one, it was deleted from the inbox and called out.

## Project-specific choices — illustrations only

These came out of one project. They are **not** options the skill raises for the
next one; they show the *kind* of decision that stays project-local:
- a YAML-per-deck source format with a per-domain schema
- language chosen per data-files
- exact commit-message character rules

The reusable move is the *process* that produced them, not the choices themselves.
