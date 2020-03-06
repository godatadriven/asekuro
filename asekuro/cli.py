import os

import click

import asekuro
from asekuro.common import test_notebook, clean_notebook, check_files


@click.group()
def main():
    """
    Asekuro - it means insurance in esperanto.

    This command line app allows you to check for errors in jupyter notebooks.
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
        click.echo(click.style(f'found file: {file}'))
        clean_notebook(file)
    click.echo(click.style('All notebooks clean.', fg='green'))


@click.command(help='Check notebook files independantly.')
@click.argument('files', nargs=-1, type=click.Path())
def test(files):
    home_path = os.getcwd()
    click.echo(click.style('Will check a sequence of independent notebooks. Has support for %load.', fg='green'))
    for file in files:
        click.echo(click.style(f'Found file: {file}', fg='blue'))
        test_notebook(file)
        # the paths matter because of the %load mechanic
        # the test_notebook will switch paths and we switch back here
        os.chdir(home_path)
    click.echo(click.style('All notebooks are green.', fg='green'))


@click.command()
@click.argument('ipynb_file', nargs=1, type=click.Path())
@click.argument('py_file', nargs=1, type=click.Path())
@click.argument('prefix', default="FAIL: ", nargs=1)
@click.option('--verbose', '-v', count=True, help='Show more verbose output.')
def check(ipynb_file, py_file, prefix, verbose):
    """Check notebook file by following it with a python file with assert statements."""
    click.echo(click.style('Will check a sequence of (juypter/py) files.', fg='green'))
    for file in [ipynb_file, py_file]:
        click.echo(click.style(f'Found file: {file}', fg='green'))
    check_files(ipynbfile=ipynb_file, pyfile=py_file, verbose=verbose, prefix=prefix)
    click.echo(click.style('Notebook is confirmed by python file.', fg='green'))


main.add_command(version)
main.add_command(clean)
main.add_command(test)
main.add_command(check)


if __name__ == "__main__":
    main()
