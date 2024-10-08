import click
from pathlib import Path

commands_folder = Path(__file__).parent.absolute()


# Voodoo from: https://click.palletsprojects.com/en/8.1.x/commands/#custom-multi-commands
class command_group(click.MultiCommand):

    def list_commands(self, ctx):
        ret = []
        for directory in commands_folder.iterdir():
            if directory.is_dir():
                command_source_file = directory.joinpath("command.py")
                if command_source_file.exists():
                    ret.append(directory.name)
        ret.sort()
        return ret

    def get_command(self, ctx, name):
        namespace = {}
        commmand_source_file = commands_folder.joinpath(name, "command.py")
        with open(commmand_source_file) as f:
            code = compile(f.read(), commmand_source_file, "exec")
            eval(code, namespace, namespace)
        return namespace['main']
