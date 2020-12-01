def outer(i):
    def inner(j):
        def doubleinner(k):
            return i+j+k
        return doubleinner
    return inner
x = outer(10)(5)(1)
print(x)