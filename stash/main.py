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

if __name__ == '__main__':
    cli()
