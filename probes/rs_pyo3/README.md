# Python packages with Rust

This is fun

> [NOTE]
> Make sure you have all the deps rigth (eg `uv venv` + `uv sync`, `cargo`, `gcc`, etc)
> If you have direnv and nix, just run `direnv allow` at the `rs_pyo3` root and you're good to go.

Follow these steps to test this:

- Run `uv run maturin develop`
- Run `python`
- In the live python interpreter:
  - Paste `import greet` and press enter
  - Paste `greet.greet("World")` and press enter
  - Paste `exit` and hit enter to close the live interpreter

You should see `Hello World!` being displayed
The `greet.greet()` function acually calls Rust compiled code contained in `src/lib.rs`
