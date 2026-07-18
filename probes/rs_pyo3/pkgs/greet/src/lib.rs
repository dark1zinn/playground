use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
mod greet {
    use pyo3::prelude::*;

    /// Formats the sum of two numbers as string.
    #[pyfunction]
    fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
        Ok((a + b).to_string())
    }

    /// Greets someone
    #[pyfunction]
    fn greet(name: String) -> PyResult<String> {
        Ok(format!("Hello {}!", name))
    }
}
