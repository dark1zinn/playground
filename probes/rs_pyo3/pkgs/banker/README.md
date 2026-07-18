# A very basic banking app

Used to be compiled by `nuitka` into an executable for testing purposes alongside `../greet` which is made with Rust

Follow these steps to test it:
- Make sure you've built the greet pkg already
- Run `uv run nuitka main.py`, it will compile the project
- Then run the generated executable with `./main.bin`

As of now you should see just a message like "Hello from Banker!"
