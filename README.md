# dotfiles

Personal configuration files for my machines.

## layout

Files are grouped by topic:

* `claude/`
* `codex/`
* `ghostty/`
* `git/`
* `gnupg/`
* `llms/`
* `ssh/`
* `zed/`
* `zsh/`

Files ending with `.symlink` are intended to be symlinked manually to their target locations.

The `_local/` directory contains machine-specific overrides and is not committed to the repository.

## files

The following files are expected to be symlinked:

* `claude/settings.json.symlink` → `~/.claude/settings.json`
* `codex/config.toml.symlink` → `~/.codex/config.toml`
* `codex/hooks.json.symlink` → `~/.codex/hooks.json`
* `claude/skills.symlink` → `~/.claude/skills`
* `claude/skills.symlink/start-work` → `~/.codex/skills/start-work`
* `claude/skills.symlink/plan-task` → `~/.codex/skills/plan-task`
* `claude/statusline.sh.symlink` → `~/.claude/statusline.sh`
* `llms/AGENTS.md.symlink` → `~/.claude/CLAUDE.md`
* `llms/AGENTS.md.symlink` → `~/.codex/AGENTS.md`
* `ghostty/config.symlink` → `~/.config/ghostty/config`
* `git/gitconfig.symlink` → `~/.gitconfig`
* `git/ignore.symlink` → `~/.config/git/ignore`
* `gnupg/gpg-agent.conf.symlink` → `~/.gnupg/gpg-agent.conf`
* `gnupg/gpg.conf.symlink` → `~/.gnupg/gpg.conf`
* `ssh/config.symlink` → `~/.ssh/config`
* `zed/settings.json.symlink` → `~/.config/zed/settings.json`
* `zsh/zprofile.symlink` → `~/.zprofile`
* `zsh/zshrc.symlink` → `~/.zshrc`

## installation

Clone the repository:

```sh
git clone https://github.com/bjakushka/dotfiles.git ~/.dotfiles
```

Create symlinks manually:

```sh
ln -s ~/.dotfiles/claude/settings.json.symlink ~/.claude/settings.json
ln -s ~/.dotfiles/claude/skills.symlink ~/.claude/skills
ln -s ~/.dotfiles/claude/statusline.sh.symlink ~/.claude/statusline.sh

ln -s ~/.dotfiles/codex/config.toml.symlink ~/.codex/config.toml
ln -s ~/.dotfiles/codex/hooks.json.symlink ~/.codex/hooks.json
ln -s ~/.dotfiles/claude/skills.symlink/plan-task ~/.codex/skills/plan-task
ln -s ~/.dotfiles/claude/skills.symlink/start-work ~/.codex/skills/start-work

ln -s ~/.dotfiles/llms/AGENTS.md.symlink ~/.claude/CLAUDE.md
ln -s ~/.dotfiles/llms/AGENTS.md.symlink ~/.codex/AGENTS.md

mkdir -p ~/.config/ghostty
ln -s ~/.dotfiles/ghostty/config.symlink ~/.config/ghostty/config

mkdir -p ~/.config/git
ln -s ~/.dotfiles/git/gitconfig.symlink ~/.gitconfig
ln -s ~/.dotfiles/git/ignore.symlink ~/.config/git/ignore

mkdir -p ~/.gnupg
ln -s ~/.dotfiles/gnupg/gpg-agent.conf.symlink ~/.gnupg/gpg-agent.conf
ln -s ~/.dotfiles/gnupg/gpg.conf.symlink ~/.gnupg/gpg.conf

ln -s ~/.dotfiles/ssh/config.symlink ~/.ssh/config

mkdir -p ~/.config/zed
ln -s ~/.dotfiles/zed/settings.json.symlink ~/.config/zed/settings.json

ln -s ~/.dotfiles/zsh/zprofile.symlink ~/.zprofile
ln -s ~/.dotfiles/zsh/zshrc.symlink ~/.zshrc
```

> **Note:** Codex uses `codex/config.toml.symlink` for shared configuration. Machine-local state such as project trust and hook trust hashes belongs in `_local/local.config.toml`, which is loaded by running `codex --profile local`.

## overrides

Local machine-specific configuration lives in `_local/`.

These files are ignored by Git and should be created manually per machine.

To set up Git overrides:

```sh
cp ~/.dotfiles/_local/gitconfig.example ~/.dotfiles/_local/gitconfig
```

You can also create additional local overrides, for example:

* `_local/AGENTS.local.md`
* `_local/ghostty`
* `_local/gitconfig`
* `_local/local.config.toml`
* `_local/ssh_config`
* `_local/zprofile`
* `_local/zshrc`

These can be referenced from the main configs (e.g. sourced in `.zshrc` or included in `.gitconfig`).

## codex local state

To set up Codex local state:

```sh
cp ~/.dotfiles/_local/local.config.toml.example ~/.dotfiles/_local/local.config.toml
ln -s ~/.dotfiles/_local/local.config.toml ~/.codex/local.config.toml
```

The shared shell config aliases `codex` to `codex --profile local`, so Codex loads both `~/.codex/config.toml` and `~/.codex/local.config.toml`.

## thanks

I used [Zach Holman](https://github.com/holman)'s excellent
[dotfiles](http://github.com/holman/dotfiles) as inspiration.
