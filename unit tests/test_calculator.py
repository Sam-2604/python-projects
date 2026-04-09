from calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0
    
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    assert multiply(-2, 3) == -6
    
def test_multiply_failure():
    # intentionally wrong to test failure
    assert multiply(2, 2) == 5
    
def test_divide():
    assert divide(10, 2) == 5.0
    assert divide(0, 5) == 0.0
    with pytest.raises(ValueError):
        divide(-6, 0)