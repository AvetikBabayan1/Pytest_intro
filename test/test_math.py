import pytest

def test_add():
    assert 1+1 == 2


def test_wrong_add():
    a = 1
    b = 2
    c = 4
    assert a+b == c


def test_division_zero():
    with pytest.raises(TypeError) as e:
        num = 1 / "value"
    assert 'unsupported operand type' in str(e.value)