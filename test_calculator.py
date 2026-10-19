import pytest
from calculator import add, subtract, multiply, divide

# HOW A TEST WORKS
#   1. The function name MUST start with `test_` so pytest finds it.
#   2. Call your code with some input.
#   3. `assert` what the answer should be. If the assert is False, the test fails.
#
# Run all tests:   pytest
# Run with detail: pytest -v


# SAMPLE TEST (done for you) 
def test_add():
    assert add(2, 3) == 5          # normal case
    assert add(-2, -3) == -5       # negative numbers
    assert add(-4, 10) == 6        # mixed signs
    assert add(0, 0) == 0          # zero
    assert add(2.5, 0.5) == 3.0    # decimals


# YOUR TURN
# Write the tests below. Follow the same pattern as test_add.


# TODO: write test_subtract()
def test_subtract():
    assert subtract(3, 2) == 1 # normal case
    assert subtract(-2, 3) == -5       # negative number first
    assert subtract(4, -10) == 14        # negative number second
    assert subtract(0, 0) == 0          # zero
    assert subtract(2.5, 0.5) == 2.0    # decimals

# TODO: write test_multiply()
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(1, 5) == 5
    assert multiply(0, 100) == 0
    assert multiply(-3, -4) == 12
    assert multiply(-4, 9) == -36
    assert multiply(-0.5, 0.5) == -0.25

# TODO: write test_divide()
def test_divide():
    assert divide(6, 2) == 3
    assert divide(-10, 5) == -2
    assert divide(0, 100) == 0
    assert divide(-100, -10) == 10
    assert divide(2, 3) == 0.6666666666666666
    assert divide(-0.5, -0.5) == 1

# TODO: write test_divide_by_zero()
#   divide() raises a ValueError when b is 0. Here's how to test for an error:
#       with pytest.raises(ValueError):
#           divide(1, 0)
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)

# BONUS: add any extra tests you want! 