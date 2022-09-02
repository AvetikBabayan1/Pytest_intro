# two positive int
# two float
# identify - *1
# zero - *0
# positive by negative
# negative by negative

import pytest

values = [
    (3,4,12), #two positive
    (1.1, 2, 2.20), # two float
    (5,1,5), #identify
    (6,0,0), #zero
    (50, -2, -100), # neg vs pos
    (-10, -20, 200) # 2neg
]

@pytest.mark.parametrize('a,b,c', values)
def test_parametrize(a,b,c):
        assert a*b == c

