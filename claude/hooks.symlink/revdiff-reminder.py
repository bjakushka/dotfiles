#!/usr/bin/env python3
"""revdiff-reminder.py - PreToolUse hook for Claude Code.

Reminds Claude where diffs go: short ones in chat, the rest through revdiff.
"""

import json
import sys

REMINDER = (
    "Small edit (one file, ~15 lines): make it on a temp copy so the edit "
    "tool's diff is the preview, then ask to apply. Larger: revdiff. "
    "Multi-file: a temp git worktree. Never show a diff as plain chat text."
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
