import click
from colorama import Fore

def echo_error(msg):
    click.echo(Fore.RED + msg + Fore.RESET, err=True)
