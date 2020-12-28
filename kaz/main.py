import os.path
import sys

import click
from colorama import Fore, Style

from kaz import item
from kaz.constants import kaz_home, KEY_VALUE_SPACING, VERSION
from kaz.search import search
from kaz.util import echo_error, format_value

def autocomplete_name(ctx, args, incomplete):
    return [name for name in item.load().keys() if name.startswith(incomplete)]

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
@click.argument('pattern', required=False, autocompletion=autocomplete_name)
def ls(pattern=None):
    """Show all items that match `pattern`."""

    items = item.load()
    if items:
        if pattern is not None:
            # Search for keys that match pattern
            items = search(items, pattern)
        if len(items) == 0:
            return
        max_len = max([len(key) for key in items])
        def format_name(name):
            return Fore.YELLOW + name + Fore.RESET
        def spacing(name):
            return (max_len - len(name)) + KEY_VALUE_SPACING

        lines = ['{}{}{}'.format(format_name(name), ' ' * spacing(name), format_value(value)) for name, value in items.items()]
        lines.sort()
        click.echo('\n'.join(lines))
    else:
        click.echo(Style.DIM + 'No items' + Style.NORMAL)

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
    """Bind a name to a value."""

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
            value = sys.stdin.buffer.read()

    # Modify items
    items[name] = value
    item.save(items, original_items)

    # Output result
    if old is None:
        click.echo("Added {} → {}".format(Fore.YELLOW + name + Fore.RESET, format_value(value)))
    else:
        if value == old:
            click.echo(Style.DIM + 'No changes made' + Style.NORMAL)
        else:
            click.echo("Updated {} → {}".format(Fore.YELLOW + name + Fore.RESET, format_value(value)))

@cli.command()
@click.help_option('-h', '--help')
@click.argument('pattern', autocompletion=autocomplete_name)
def remove(pattern):
    """Remove an item."""

    items = item.load()
    to_remove = search(item.load(), pattern)
    count = len(to_remove)
    if count == 0:
        echo_error('No items found')
        return

    new_items = { name: value for name, value in items.items() if not name in to_remove }
    item.save(new_items, items)
    click.echo('Removed {} item{}'.format(Fore.GREEN + str(count) + Fore.RESET, '' if count == 1 else 's') + Style.RESET_ALL)

if __name__ == '__main__':
    cli()
