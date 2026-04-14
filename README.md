# dotfiles

Personal configuration files for my machines.

## layout

Files are grouped by topic:

* `ghostty/`
* `git/`
* `ssh/`
* `zsh/`

Files ending with `.symlink` are intended to be symlinked manually to their target locations.

The `_local/` directory contains machine-specific overrides and is not committed to the repository.

## files

The following files are expected to be symlinked:

* `ghostty/config.symlink` → `~/.config/ghostty/config`
* `git/gitconfig.symlink` → `~/.gitconfig`
* `git/ignore.symlink` → `~/.config/git/ignore`
* `ssh/config.symlink` → `~/.ssh/config`
* `zsh/zshrc.symlink` → `~/.zshrc`

## installation

Clone the repository:

```sh
git clone https://github.com/bjakushka/dotfiles.git ~/.dotfiles
```

Create symlinks manually:

```sh
mkdir -p ~/.config/ghostty
ln -s ~/.dotfiles/ghostty/config.symlink ~/.config/ghostty/config

mkdir -p ~/.config/git
ln -s ~/.dotfiles/git/gitconfig.symlink ~/.gitconfig
ln -s ~/.dotfiles/git/ignore.symlink ~/.config/git/ignore

ln -s ~/.dotfiles/ssh/config.symlink ~/.ssh/config

ln -s ~/.dotfiles/zsh/zshrc.symlink ~/.zshrc
```

## overrides

Local machine-specific configuration lives in `_local/`.

These files are ignored by Git and should be created manually per machine.

To set up Git overrides:

```sh
cp ~/.dotfiles/_local/gitconfig.example ~/.dotfiles/_local/gitconfig
```

You can also create additional local overrides, for example:

* `_local/ghostty`
* `_local/gitconfig`
* `_local/ssh_config`
* `_local/zshrc`

These can be referenced from the main configs (e.g. sourced in `.zshrc` or included in `.gitconfig`).

## thanks

I used [Zach Holman](https://github.com/holman)'s excellent
[dotfiles](http://github.com/holman/dotfiles) as inspiration.
