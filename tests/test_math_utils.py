
import pytest

from lab.math_utils import add, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(10, 4) == 6


def test_multiply() -> None:
    assert multiply(3, 7) == 21


def test_divide() -> None:
    assert divide(8, 2) == 4


def test_divide_by_zero() -> None:
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_intentional_fail() -> None:
    assert 1 == 0
