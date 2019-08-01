import os

import click

import asekuro
from asekuro.common import test_notebook, clean_notebook, _cwd


@click.group()
def main():
    """
    Asekuro - it means insurance in esperanto.

    This command line app allows you to check for errors in jupyter notebooks
    and it also allows you to supply a python file with assert statements.
    """
    pass


@click.command(help='Echo the version of asekuro.')
def version():
    click.echo(asekuro.__version__)


@click.command(help='Clean notebook files.')
@click.argument('files', nargs=-1, type=click.Path())
def clean(files):
    click.echo(click.style('Will clean notebooks.', fg='green'))
    for file in files:
        click.echo(click.style(f'Found file: {file}'))
        clean_notebook(file)


@click.command(help='Check notebook files independantly.')
@click.argument('files', nargs=-1, type=click.Path())
def test(files):
    home_path = os.getcwd()
    print(f"i am currently in {home_path}")
    click.echo(click.style('Will check a sequence of files if they klopt.', fg='green'))
    for file in files:
        click.echo(click.style(f'Found file: {file}'))
        test_notebook(file)
        os.chdir(home_path)


@click.command()
@click.argument('files', nargs=-1, type=click.Path())
def check(files):
    """Check (notebook) files in sequention for errors."""
    click.echo(click.style('Will check a sequence of files if they klopt.', fg='green'))
    for file in files:
        click.echo(click.style(f'Found file: {file}'))


main.add_command(version)
main.add_command(clean)
main.add_command(test)
main.add_command(check)


if __name__ == "__main__":
    main()
