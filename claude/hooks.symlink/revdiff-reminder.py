#!/usr/bin/env python3
"""revdiff-reminder.py - PreToolUse hook for Claude Code.

Reminds Claude where diffs go: short ones in chat, the rest through revdiff.
"""

import json
import sys

REMINDER = (
    "Show short diffs in chat and anything longer through the revdiff skill; "
    "when unsure which, ask the user. Preview unapplied multi-file edits from "
    "a temp git worktree."
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
