import click
import greet
import sys

from ui.tui import ClockApp

def cli():
    click.echo("this is MAIN:")
    click.echo(f"\n  argc: {len(sys.argv)}\n  argv: {sys.argv}")

    # Inside an click.group function this would be unreachable code
    # since if no args (argv<2) are passed click intercepts into a help output
    # this means that when the function is run there would ALWAYS be more than 1 arg (argv>1)
    if len(sys.argv)<2:
        ClockApp().run() # Run TUI when no args are passed
        sys.exit(0)
    else:
        main()
    sys.exit(1)

@click.group()
def main():
    pass

@main.command()
def hello():
    click.echo(greet.greet("Banker"))
    # Seems that to allow certain features some flags should be set
    # for the `exit()` function for example, seems to need `--no-deployment-flag=site-builtins`
    # ---
    # EDIT: So apparently the problem is that just using plain `exit()` without importing from `sys`
    # the GIL interpreter implictly knows about it, but for `nuitka` since there is no imports for it to follow
    # it becomes an orphan fucntion (eg undefined function that doesn't exist at runtime)
    sys.exit(0)

@main.command()
@click.argument('person')
@click.argument('amount')
def pay(person: str, amount: int):
    # The LSP may complain here since there are no signatures at all of this pay() function
    # So despite it is there and it works, the LSP doesn't know about it
    click.echo(greet.pay(int(amount), person))
    sys.exit(0)

@main.command()
@click.argument('amount')
def deposit(amount: int):
    greet.deposit(int(amount))
    sys.exit(0)

if __name__ == "__main__":
    cli()
