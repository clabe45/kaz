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

if __name__ == '__main__':
    cli()
