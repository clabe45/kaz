import click

from hold import item

@click.group()
def cli():
    """Simple local storage cli"""

    pass

@cli.command(name='list')
def ls():
    """Show all stashed items"""

    click.echo('\n'.join(item.load().keys()))

@cli.command()
@click.argument('name')
def get(name):
    """Print the value of an item"""

    items = item.load()
    if not name in items:
        click.echo('No such item: {}'.format(name))
        return

    click.echo(items[name])

@cli.command()
@click.argument('name')
@click.option('--edit/--no-edit', '-e/-E', default=False, help='Open the item in the default text editor')
@click.argument('value', required=False)
def set(name, edit, value):
    """Store a value in an item"""

    items = item.load()
    old = items[name] if name in items else None

    if edit:
        if value is not None:
            click.echo('Value cannot be present while --editor is set.')
            return
        edited = click.edit(text=old)
        # click.edit() returns None when no changes were made, so account for that
        value = edited.rstrip() if edited is not None else old
    else:
        if value is None:
            value = click.prompt('Value')

    items[name] = value
    item.save(items)
    print("{} '{}'".format('Added' if old is None else ('Updated' if value != old else 'No changes made to'), name))

@cli.command()
@click.argument('name')
def remove(name):
    """Remove an item"""

    items = item.load()
    if not name in items:
        click.echo('No such item: {}'.format(name))
        return

    del items[name]
    item.save(items)
    click.echo("Removed '{}'".format(name))

@cli.command()
def clear():
    """Remove all items"""

    count = len(item.load())
    item.save({})
    click.echo('Removed {} item{}'.format(count, '' if count == 1 else 's'))

if __name__ == '__main__':
    cli()
