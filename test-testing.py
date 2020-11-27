from operator import sub
from reduceaks import my_reduce
def test_reduce () :
    try :
        my_reduce(sub, [])
        assert False
    except TypeError :
        pass
    assert my_reduce(None, [],        0) ==  0 # 0
    assert my_reduce(None, [2])          ==  2 # 2
    assert my_reduce(sub, [], 1) == 1 # 1
    assert my_reduce(sub,  [2],       0) == -2 # 0 - 2
    assert my_reduce(sub,  [2, 3, 4])    == -5 # 2 - 3 - 4
    assert my_reduce(sub,  [2, 3, 4], 0) == -9 # 0 - 2 - 3 - 4
    assert my_reduce(sub, [2,3,4],None) == -5
    print("done.")
test_reduce()