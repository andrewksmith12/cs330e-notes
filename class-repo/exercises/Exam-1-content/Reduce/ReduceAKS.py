def reduce_for(action, iterable, seed):
    for i in iterable:
        seed = action(seed,i)
    return seed
def reduce_while(action, iterable, seed):
    iterable = iter(iterable)
    try:
        while True:
            val = next(iterable)
            seed = action(seed,val)
    except StopIteration:
        pass
    return seed

def reduce_for_range(action, iterable, seed):
    for i in range(len(iterable)):
        seed = action(seed, iterable[i])
    return seed