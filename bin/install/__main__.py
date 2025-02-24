#!/usr/bin/env python
from core import Install

if __name__ == "__main__":
  install = Install()

  # Generates the dotfiles JSON config.
  install.config()

  # Does any backup work needed
  # prior to installing the dotfiles.
  install.backup()

  # Builds the dotfiles CLI.
  install.cli()

  # Links all the dotfiles packages to
  # the system using GNU stow.
  install.stow()
