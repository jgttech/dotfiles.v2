#!/usr/bin/env python
from core import Install

if __name__ == "__main__":
  install = Install()

  print(f"PLATFORM: {install.system}")

  # Does any backup work needed
  # prior to installing the dotfiles.
  install.backup()

  # Setup the terminal configurations.
  install.ghostty()
  install.alacritty()

  # Builds the dotfiles CLI.
  install.cli()

  # Generates the dotfiles JSON config.
  install.config()

  # Links all the dotfiles packages to
  # the system using GNU stow.
  install.stow()

  # Display an installation summary.
  install.summary()
