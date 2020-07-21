import os.path

import click

from hold import item
from hold.constants import hold_home

@click.group(invoke_without_command=True)
@click.help_option('-h', '--help')
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

    click.echo('\n'.join(['{}{}'.format(name, ' (binary)' if type(value) is bytes else '') for name, value in item.load().items()]))

def autocomplete_name(ctx, args, incomplete):
    return [name for name in item.load().keys() if name.startswith(incomplete)]

@cli.command()
@click.help_option('-h', '--help')
@click.argument('name', autocompletion=autocomplete_name)
def get(name):
    """Print the value of an item."""

    items = item.load()
    if not name in items:
        click.echo('No such item: {}'.format(name), err=True)
        return

    click.echo(items[name])

@cli.command()
@click.help_option('-h', '--help')
@click.option('--binary/--no-binary', '-b/-B', default=False, help='Accept binary data from stdin')
@click.option('--edit/--no-edit', '-e/-E', default=False, help='Open the item in the default text editor')
@click.argument('name', autocompletion=autocomplete_name)
@click.argument('value', required=False)
def set(name, binary, edit, value):
    """Store a value in an item."""

    items = item.load()
    original_items = dict(items)
    old = items[name] if name in items else None

    if edit:
        if binary:
            click.echo('Cannot edit a binary file', err=True)
            return
        if value is not None:
            click.echo('Value cannot be present while --editor is set.', err=True)
            return
        edited = click.edit(text=old)
        # click.edit() returns None when no changes were made, so account for that
        value = edited.rstrip() if edited is not None else old
    else:
        if value is not None:
            if binary:
                click.echo('Value cannot be present while --binary is set.', err=True)
                return
        else:
            if binary:
                click.echo('Value: ', nl=False)
                stdin = click.get_binary_stream('stdin')
                value = stdin.read()
            else:
                value = click.prompt('Value')

    items[name] = value
    item.save(items, original_items)
    print("{} '{}'".format('Added' if old is None else ('Updated' if value != old else 'No changes made to'), name))

@cli.command()
@click.help_option('-h', '--help')
@click.argument('name', autocompletion=autocomplete_name)
def remove(name):
    """Remove an item."""

    items = item.load()
    original_items = dict(items)
    if not name in items:
        click.echo('No such item: {}'.format(name), err=True)
        return

    del items[name]
    item.save(items, original_items)
    click.echo("Removed '{}'".format(name))

@cli.command()
@click.help_option('-h', '--help')

def clear():
    """Remove all items."""

    original_items = item.load()
    count = len(original_items)
    count = len(item.load())
    item.save({}, original_items)
    click.echo('Removed {} item{}'.format(count, '' if count == 1 else 's'))

if __name__ == '__main__':
    cli()
