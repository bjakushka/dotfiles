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

The `_local/` directory contains machine-specific overrides. Only its `*.example` templates
are committed — see [overrides](#overrides).

## files

The following files are expected to be symlinked:

* `claude/settings.json.symlink` → `~/.claude/settings.json`
* `codex/config.toml.symlink` → `~/.codex/config.toml`
* `codex/hooks.json.symlink` → `~/.codex/hooks.json`
* `claude/skills.symlink` → `~/.claude/skills`
* `claude/skills.symlink/<skill>` → `~/.codex/skills/<skill>` (optional, one link per skill)
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
mkdir -p ~/.claude
ln -s ~/.dotfiles/claude/settings.json.symlink ~/.claude/settings.json
ln -s ~/.dotfiles/claude/skills.symlink ~/.claude/skills
ln -s ~/.dotfiles/claude/statusline.sh.symlink ~/.claude/statusline.sh

mkdir -p ~/.codex/skills
ln -s ~/.dotfiles/codex/config.toml.symlink ~/.codex/config.toml
ln -s ~/.dotfiles/codex/hooks.json.symlink ~/.codex/hooks.json

# Link whichever skills you want available in Codex, one by one:
ln -s ~/.dotfiles/claude/skills.symlink/<skill> ~/.codex/skills/<skill>

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

mkdir -p -m 700 ~/.ssh
ln -s ~/.dotfiles/ssh/config.symlink ~/.ssh/config

mkdir -p ~/.config/zed
ln -s ~/.dotfiles/zed/settings.json.symlink ~/.config/zed/settings.json

ln -s ~/.dotfiles/zsh/zprofile.symlink ~/.zprofile
ln -s ~/.dotfiles/zsh/zshrc.symlink ~/.zshrc
```

## overrides

Each file is created manually per machine. Start from a template whenever one exists
(`gitconfig` as example):

```sh
cp ~/.dotfiles/_local/gitconfig.example ~/.dotfiles/_local/gitconfig
```

### Loaded automatically

The main configs already reference these paths, so creating the file is enough:

* `_local/AGENTS.local.md` — imported by `llms/AGENTS.md.symlink`; Codex reads it through the `SessionStart` hook
* `_local/gitconfig` — `[include]` in `git/gitconfig.symlink`, placed last so overrides win
* `_local/ssh_config` — `Include` in `ssh/config.symlink`
* `_local/zprofile` — sourced from `zsh/zprofile.symlink`
* `_local/zshrc` — sourced from `zsh/zshrc.symlink`

### Linked manually

`_local/local.config.toml` holds machine-local Codex state — project trust and hook trust
hashes — which must stay out of the repository. It needs its own symlink:

```sh
cp ~/.dotfiles/_local/local.config.toml.example ~/.dotfiles/_local/local.config.toml
ln -s ~/.dotfiles/_local/local.config.toml ~/.codex/local.config.toml
```

Shared Codex configuration stays in `codex/config.toml.symlink`. The shared shell config
aliases `codex` to `codex --profile local`, so Codex loads both `~/.codex/config.toml` and
`~/.codex/local.config.toml`.

## thanks

I used [Zach Holman](https://github.com/holman)'s excellent
[dotfiles](http://github.com/holman/dotfiles) as inspiration.
