def f (x, y, z) :
    return [x, y, z]

t = (3, 4)

assert f(z = 2, *t) == [3, 4, 2]
assert f(2, *t) == [2,3,4]
assert f(2,*t) == [2,3,4]   but    assert f(z = 2, *t) == [3, 4, 2]
print("done.")

# for tuple unpacking as arguments, it goes integers/unpacking then statements (x=2)