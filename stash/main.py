import click

import item

@click.group()
def cli():
    """Simple store for text items"""

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
@click.argument('value')
def set(name, value):
    """Store a value in an item"""

    items = item.load()
    old = items[name] if name in items else None
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

if __name__ == '__main__':
    cli()
