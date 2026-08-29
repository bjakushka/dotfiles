#!/usr/bin/env python3
"""approval-check.py - PreToolUse hook for Claude Code.

Asks Claude whether a write and every decision in it were approved. Fires for
Edit and Write, and for Bash only when the command looks like it writes files,
so reads and searches stay quiet. The Bash check is a heuristic, not a parser.
"""

import json
import re
import sys

REMINDER = (
    "Was this exact change explicitly approved, and was every decision in it "
    "discussed with the user first and approved?"
)

WRITING_COMMAND = re.compile(
    r"(^|[\s;&|(])(cp|mv|rm|ln|mkdir|touch|tee|install|patch|chmod)\s"
    r"|\bgit\s+(apply|checkout|restore|reset|mv|rm|stash)\b"
    r"|\bsed\s+-i"
    # A redirect into a file, but not 2>&1 or into /dev/null.
    r"|(?<![0-9&])>>?\s*(?!&|/dev/null)"
)


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    tool = event.get("tool_name")
    if tool == "Bash":
        command = event.get("tool_input", {}).get("command", "")
        if not WRITING_COMMAND.search(command):
            return 0
    elif tool not in ("Edit", "Write"):
        return 0
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
