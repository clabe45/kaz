import click
from colorama import Fore, Style

def echo_error(msg):
    click.echo(Fore.RED + msg + Fore.RESET, err=True)

def format_value(value):
    if type(value) is str:
        if '\n' in value or '\r' in value:
            return Style.DIM + '(long text)' + Style.RESET_ALL
        else:
            return value
    else:
        return Style.DIM + "(binary)" + Style.RESET_ALL
