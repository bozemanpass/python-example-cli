# Copyright © 2024 Bozeman Pass, Inc.

import click

from .subcommands import command_group


@click.command(cls=command_group)
def main():
    pass
