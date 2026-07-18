import typer
import greet

app = typer.Typer()

@app.command()
def hello():
    print(greet.greet("Banker"))
    exit(0)

@app.command()
def pay(person: str, amount: int):
    print(greet.pay(amount, person))
    exit(0)

@app.command()
def deposit(amount: int):
    greet.deposit(amount)
    exit(0)

if __name__ == "__main__":
    app()
