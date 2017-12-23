import os
import subprocess

import click
import dotenv


@click.command(context_settings={
    'ignore_unknown_options': True,
    'allow_interspersed_args': False,
    'allow_extra_args': True,
})
@click.argument('command')
@click.argument('args', nargs=-1, type=click.UNPROCESSED)
@click.option(
    '--override/--no-override',
    default=False,
    help=("Whether contents in the .env file should override existing "
          "environment variables. Defaults behavior is to respect the "
          "existing environment."),
)
@click.option(
    '-f', '--file', 'filename',
    default=os.path.join(os.getcwd(), '.env'),
    type=click.Path(),
    help=("Location of the .env file, "
          "defaults to .env file in current working directory."),
)
@click.pass_context
def main(ctx, filename, override, command, args):
    """Run command with environment loaded with python-dotenv.
    """
    if os.path.isfile(filename):
        dotenv.load_dotenv(filename, override=override)
    if os.name == 'nt':
        # Windows has problems with `os.exec*`, according to Pipenv,
        # so let's launch a subshell instead.
        ctx.exit(subprocess.call([command] + list(args), shell=True))
    else:
        os.execlp(command, command, *args)


if __name__ == '__main__':
    main()
