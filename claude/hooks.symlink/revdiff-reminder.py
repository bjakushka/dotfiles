#!/usr/bin/env python3
"""revdiff-reminder.py - PreToolUse hook for Claude Code.

Reminds Claude where diffs go: short ones in chat, the rest through revdiff.
"""

import json
import sys

REMINDER = (
    "One logical change at a time, made on a temp copy (several files: a temp "
    "worktree) and approved before it reaches real files. One contiguous change "
    "per file, up to ~30 lines in one or two files: the editing tool's diff in "
    "chat, one per file; several places in one file, larger, or 3+ files: "
    "revdiff. Describe the change after the diffs, before the question, not in "
    "it. Never retype a diff."
)


def main():
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": REMINDER,
            }
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
