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

    /// Pay some money to someone
    #[pyfunction]
    fn pay(value: u32, person: String) -> PyResult<String> {
        Ok(format!(
            "You just paid ${} to {}!",
            value.to_string(),
            person
        ))
    }

    // Note that here I try to pass () as the result, trying to mimic an void return for the python
    // At the time I'm writing this comment, I don't know if it will work
    /// Deposit some money
    #[pyfunction]
    fn deposit(amount: u32) -> PyResult<()> {
        println!("You just deposited ${}!", amount);
        Ok(())
    }
}
