import pytest
from stuff.accum import Accumulator

#Here is the fixture, which uses a decorator. It should always return a value
@pytest.fixture
def accum():#in parenthesis we can write the usage of scope as session, if only one test case has to run it
    # Optional is the usage of yield function. It is finishing the initial setup. Everything after it will be executed after each test, even if it failed
    yield Accumulator()
    print ("\nGonzo")
    #return Accumulator()

#here are tests itself. We are adding an argument to a function for each of them
def test_Accumulator_initial(accum):
    assert accum.count == 0

def test_Accumulator_add_one(accum):
    accum.add()
    assert accum.count==1

def test_Accumulator_add_five(accum):
    accum.add(5)
    assert accum.count==5

def test_Accumulator_gets_doubled(accum):
    accum.add()
    accum.add()
    assert accum.count==2

def test_cant_get_Count():
   # with pytest.raises(AttributeError, match=r"can't set attribute") as e:
        accum.count=10