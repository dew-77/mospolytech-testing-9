import pytest

from calculator import Calculator


@pytest.fixture(scope="module")
def calc():
    return Calculator()


@pytest.mark.parametrize("a,b,res", [(1, 2, 3), (0, 0, 0), (-1, 5, 4)])
def test_add(calc, a, b, res):
    assert calc.add(a, b) == res


@pytest.mark.parametrize("n,expected", [(2, True), (3, True), (4, False), (17, True), (1, False), (0, False)])
def test_is_prime_number(calc, n, expected):
    assert calc.is_prime_number(n) == expected


def test_divide_ok(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(-9, 3) == -3


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)
