
import click

from ...util.di import d

@click.command()
@click.pass_context
def main(ctx):
    print(f"Hello create, debug is: {d.o.debug}")
