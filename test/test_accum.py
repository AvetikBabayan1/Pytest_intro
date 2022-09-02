import pytest
from stuff.accum import Accumulator

def test_Accumulator_initial():
    accum = Accumulator()
    assert accum.count == 0

def test_Accumulator_add_one():
    accum=Accumulator()
    accum.add()
    assert accum.count==1

def test_Accumulator_add_five():
    accum = Accumulator()
    accum.add(5)
    assert accum.count==5

def test_Accumulator_gets_doubled():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count==2

def test_cant_get_Count():
    accum= Accumulator()
    with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count=10