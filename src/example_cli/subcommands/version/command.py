
import click


@click.command()
@click.pass_context
def main(ctx):
    print("Hello version")
