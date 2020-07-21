import os.path
import sys

import click
from colorama import Fore, Style

from kaz import item
from kaz.constants import kaz_home, VERSION
from kaz.util import echo_error

@click.group(invoke_without_command=True)
@click.help_option('-h', '--help')
@click.version_option(VERSION, '-v', '--version', message='%(prog)s v%(version)s')
@click.pass_context
def cli(ctx):
    """Simple local storage cli"""

    if ctx.invoked_subcommand is None:
        ctx.invoke(ls)
    pass

@cli.command(name='list')
@click.help_option('-h', '--help')
def ls():
    """Show all held items."""

    items = item.load()
    if items:
        click.echo('\n'.join(['{}{}'.format(name, Style.DIM + ' (binary)' + Style.NORMAL if type(value) is bytes else '') for name, value in items.items()]))
    else:
        click.echo(Style.DIM + 'No items' + Style.NORMAL)

def autocomplete_name(ctx, args, incomplete):
    return [name for name in item.load().keys() if name.startswith(incomplete)]

@cli.command()
@click.help_option('-h', '--help')
@click.argument('name', autocompletion=autocomplete_name)
def get(name):
    """Print the value of an item."""

    items = item.load()
    if not name in items:
        echo_error('No such item: {}'.format(name))
        return

    click.echo(items[name])

@cli.command()
@click.help_option('-h', '--help')
@click.option('--edit/--no-edit', '-e/-E', default=False, help='Open the item in the default text editor')
@click.argument('name', autocompletion=autocomplete_name)
@click.argument('value', required=False)
def set(name, edit, value):
    """Store a value in an item."""

    items = item.load()
    original_items = dict(items)
    old = items[name] if name in items else None

    if edit:
        if value is not None:
            echo_error('Value cannot be present while --editor is set.')
            return
        edited = click.edit(text=old)
        # click.edit() returns None when no changes were made, so account for that
        value = edited.rstrip() if edited is not None else old
    else:
        if value is None:
            click.echo('Value: ', nl=False)
            value = sys.stdin.buffer.read()

    items[name] = value
    item.save(items, original_items)
    if old is None:
        click.echo(Fore.GREEN + "Added '{}'".format(name) + Fore.RESET)
    else:
        if value == old:
            click.echo(Style.DIM + 'Nothing changed' + Style.NORMAL)
        else:
            click.echo(Fore.YELLOW + "Updated '{}'".format(name) + Fore.RESET)

@cli.command()
@click.help_option('-h', '--help')
@click.argument('name', autocompletion=autocomplete_name)
def remove(name):
    """Remove an item."""

    items = item.load()
    original_items = dict(items)
    if not name in items:
        echo_error('No such item: {}'.format(name))
        return

    del items[name]
    item.save(items, original_items)
    click.echo(Fore.MAGENTA + "Removed '{}'".format(name) + Fore.RESET)

@cli.command()
@click.help_option('-h', '--help')
def clear():
    """Remove all items."""

    original_items = item.load()
    count = len(original_items)
    count = len(item.load())
    item.save({}, original_items)
    click.echo((Style.DIM if count == 0 else Fore.MAGENTA) + 'Removed {} item{}'.format(count, '' if count == 1 else 's') + Style.RESET_ALL)

if __name__ == '__main__':
    cli()
