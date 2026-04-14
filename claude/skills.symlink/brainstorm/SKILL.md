---
name: brainstorm
description: Collaborative design dialogue before implementation. Use on "brainstorm", "let's think through", "help me design", "explore options", or when asked for thorough analysis of changes, features, or architecture.
disable-model-invocation: true
allowed-tools: Read Glob Grep Bash Agent
---

# Brainstorm

Turn ideas into designs through dialogue before writing code.

## Phase 1: Understand

0. Before asking questions, inspect the relevant project context when available.
   Do not ask for information that can be inferred from the repository.
1. Check project context — files, docs, recent commits relevant to the idea.
   Check recent commits only when they are likely to clarify ongoing changes or intent.
2. Ask questions **one at a time**, prefer multiple choice
3. Focus on: purpose, constraints, success criteria, integration points

## Phase 2: Explore approaches

1. Propose 2-3 approaches with trade-offs
2. Lead with recommended option and explain why
3. Keep it conversational — not a formal document

## Phase 3: Validate design

1. Break design into sections of 200-300 words
2. Ask after each section whether it looks right
3. Cover: architecture, components, data flow, edge cases
4. Backtrack if something doesn't fit

## Phase 4: Next steps

Ask whether to:
1. implement now,
2. write a concrete plan,
3. revisit one of the alternatives.

## Principles

- One question at a time — never overwhelm
- Multiple choice when possible
- YAGNI — cut unnecessary scope ruthlessly
- Always explore alternatives before settling
- Lead with a recommendation, but let the user decide
- Prefer the simplest viable option that fits the current codebase and minimizes migration risk
- Incremental validation — catch misunderstandings early

## Language

Respond in Russian. Keep artifacts (code, file names, diagrams) in English.

