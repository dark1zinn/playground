import typer
import greet
import sys

from ui import ClockApp

app = typer.Typer(invoke_without_command=True)

@app.callback()
def main():
    ClockApp().run()

@app.command()
def hello():
    print(greet.greet("Banker"))
    # Seems that to allow certain features some flags should be set
    # for the `exit()` function for example, seems to need `--no-deployment-flag=site-builtins`
    # ---
    # EDIT: So apparently the problem is that just using plain `exit()` without importing from `sys`
    # the GIL interpreter implictly knows about it, but for `nuitka` since there is no imports for it to follow
    # it becomes an orphan fucntion (eg undefined function that doesn't exist at runtime)
    sys.exit(0)

@app.command()
def pay(person: str, amount: int):
    # The LSP may complain here since there are no signatures at all of this pay() function
    # So despite it is there and it works, the LSP doesn't know about it
    print(greet.pay(amount, person))
    sys.exit(0)

@app.command()
def deposit(amount: int):
    greet.deposit(amount)
    sys.exit(0)

if __name__ == "__main__":
    app()
