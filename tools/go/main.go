package main

import (
	"context"
	"log"
	"os"

	"jgttech/dotfiles/cmds/install"
	"jgttech/dotfiles/cmds/purge"
	"jgttech/dotfiles/cmds/uninstall"
	"jgttech/dotfiles/cmds/version"
	"jgttech/dotfiles/src/cfg"

	"github.com/urfave/cli/v3"
)

func main() {
	build := cfg.Load()
	app := cli.Command{
		Commands: []*cli.Command{
			install.Command(build),
			uninstall.Command(build),
			purge.Command(build),
			version.Command(build),
		},
	}

	if err := app.Run(context.Background(), os.Args); err != nil {
		log.Fatal(err)
	}
}
