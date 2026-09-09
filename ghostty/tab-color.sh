#!/usr/bin/env bash
# tab-color - mark the current Ghostty tab: tinted background (OSC 11) and a heart emoji title prefix.
# usage: tab-color <color|none> [title]
# The prefixed title is a tab title override: it stops following the shell title until `none`.

set -euo pipefail

usage() {
  echo 'usage: tab-color <color|none> [title]'
  echo 'colors: blue purple pink red orange yellow green teal gray'
}

# Backgrounds keep the luminance of the default #282c34, so text contrast stays the same;
# gray is lighter on purpose, otherwise it is indistinguishable from the default
case "${1:-}" in
  blue)   bg='#192d43' emoji='💙' ;;
  purple) bg='#332641' emoji='💜' ;;
  pink)   bg='#3f232e' emoji='🩷' ;;
  red)    bg='#3e2527' emoji='❤️' ;;
  orange) bg='#352b1b' emoji='🧡' ;;
  yellow) bg='#2f2c18' emoji='💛' ;;
  green)  bg='#1a3125' emoji='💚' ;;
  teal)   bg='#202f32' emoji='🩵' ;;
  gray)   bg='#3a3b3f' emoji='🩶' ;;
  none)   bg='' emoji='' ;;
  '')     usage; exit 0 ;;
  *)      usage >&2; exit 1 ;;
esac

if [ "${TERM_PROGRAM:-}" != ghostty ]; then
  echo 'tab-color: not running in Ghostty' >&2
  exit 1
fi

if [ -n "$bg" ]; then
  printf '\033]11;%s\a' "$bg"
else
  printf '\033]111\a'
fi

# Tab title and the shell-set title of its focused terminal, one per line
titles=$(osascript -e 'tell application "Ghostty"
  set t to selected tab of front window
  return (name of t) & linefeed & (name of focused terminal of t)
end tell')
current=${titles%%$'\n'*}
shell_title=${titles#*$'\n'}

base=$current
for e in 💙 💜 🩷 ❤️ 🧡 💛 💚 🩵 🩶; do
  case "$current" in
    "$e "*) base=${current#"$e "}; break ;;
  esac
done
base=${2:-$base}

if [ -n "$emoji" ]; then
  title="$emoji${base:+ $base}"
elif [ "$base" = "$shell_title" ]; then
  # An empty override makes the tab follow the shell title again
  title=''
else
  title=$base
fi

osascript - "set_tab_title:$title" >/dev/null <<'EOF'
on run argv
  tell application "Ghostty" to perform action (item 1 of argv) on focused terminal of selected tab of front window
end run
EOF
