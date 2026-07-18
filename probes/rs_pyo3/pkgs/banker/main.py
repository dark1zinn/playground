import typer

app = typer.Typer()

@app.command()
def hello():
    print("Hello from banker!")
    exit(0)

@app.command()
def pay(person: str, amount: int):
    print("You just paid " + str(amount) + " to " + str(person) + "!")
    exit(0)

@app.command()
def deposit(amount: int):
    print("You just deposited $" + str(amount))
    exit(0)

if __name__ == "__main__":
    app()
