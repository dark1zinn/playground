import typer
import greet

app = typer.Typer()

@app.command()
def hello():
    print(greet.greet("Banker"))
    # Seems that to allow certain features some flags should be set
    # For the `exit()` function for example, seems to need `--no-deployment-flag=site-builtins`
    # exit(0)

@app.command()
def pay(person: str, amount: int):
    # The LSP may complain here since there are no signatures at all of this pay() function
    # So despite it is there and it works, the LSP doesn't know about it
    print(greet.pay(amount, person))
    # exit(0)

@app.command()
def deposit(amount: int):
    greet.deposit(amount)
    # exit(0)

if __name__ == "__main__":
    app()
