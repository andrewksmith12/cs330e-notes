def f(h) :
    w = 2
    def g(x):
        return h(x) * w
    return g

@f
def h(x) :
   return x ** 2

print(h(2))   