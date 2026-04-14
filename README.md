# dotfiles

Personal configuration files for my machines.

## layout

Files are grouped by topic:

* `zsh/`
* `git/`
* `ghostty/`

Files ending with `.symlink` are intended to be symlinked manually to their target locations.

The `_local/` directory contains machine-specific overrides and is not committed to the repository.

## files

The following files are expected to be symlinked:

* `zsh/zshrc.symlink` → `~/.zshrc`
* `git/gitconfig.symlink` → `~/.gitconfig`
* `ghostty/config.symlink` → `~/.config/ghostty/config`

## installation

Clone the repository:

```sh
git clone https://github.com/bjakushka/dotfiles.git ~/.dotfiles
```

Create symlinks manually:

```sh
ln -s ~/.dotfiles/zsh/zshrc.symlink ~/.zshrc
ln -s ~/.dotfiles/git/gitconfig.symlink ~/.gitconfig

mkdir -p ~/.config/ghostty
ln -s ~/.dotfiles/ghostty/config.symlink ~/.config/ghostty/config
```

## overrides

Local machine-specific configuration lives in `_local/`.

These files are ignored by Git and should be created manually per machine.

To set up Git overrides:

```sh
cp ~/.dotfiles/_local/gitconfig.example ~/.dotfiles/_local/gitconfig
```

You can also create additional local overrides, for example:

* `_local/zshrc`
* `_local/gitconfig`
* `_local/ghostty`

These can be referenced from the main configs (e.g. sourced in `.zshrc` or included in `.gitconfig`).

## notes

Inside `zshrc`, the `DOTFILES` variable points to the local checkout path and is used to reference files inside this repository.
