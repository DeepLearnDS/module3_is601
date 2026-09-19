## Module 3 Updates

This version of the calculator includes the following improvements and updates:

### Operations Class
The arithmetic operations were reorganized into an `Operations` class located in:
```text
app/operations/__init__.py
```
The `Operations` class uses static methods for:

* `addition()`
* `subtraction()`
* `multiplication()`
* `division()`

The division method also checks for division by zero and raises a `ValueError` when the second number is zero.

### Parameterized Unit Tests
The operations are tested using pytest parameterized tests in:
```text
tests/test_operations.py
```
Parameterized tests allow multiple input values and expected results to be tested using the same test logic. This reduces duplicate test code and provides broader test coverage for the calculator operations.
The tests cover:

* Addition with multiple input values
* Subtraction with multiple input values
* Multiplication with multiple input values
* Division with multiple input values
* Division-by-zero error handling

### Test Coverage

The project maintains **100% test coverage** for the application.
The test suite and coverage requirement are also automatically checked through GitHub Actions.
