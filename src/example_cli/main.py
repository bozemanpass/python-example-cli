# Copyright © 2024 Bozeman Pass, Inc.

import click


from .types.command_types import BaseOptions
from .subcommands.create.command import main as create_command
from .subcommands.version.command import main as version_command
from .util.di import d


@click.group(context_settings=dict(help_option_names=['-h', '--help']))
@click.option("--debug", is_flag=True, default=False, help="Enable debug output")
@click.option("--quiet", is_flag=True, default=False, help="Suppress all non-essential output")
@click.option("--verbose", is_flag=True, default=False, help="Enable verbose output")
@click.pass_context
def main(context, debug, quiet, verbose):
    options = BaseOptions(debug, quiet, verbose)
    d.o = options


main.add_command(create_command, "create")
main.add_command(version_command, "version")
