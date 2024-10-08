# Copyright © 2024 Bozeman Pass, Inc.

import click

from .subcommands.version import command

@click.group
def main():
    pass

main.add_command(command.main, "version")
