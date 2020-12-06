#!/usr/bin/env python3

#pylint: disable = consider-using-enumerate

# ---------
# Reduce.py
# ---------

def reduce_for (action, iterable, v) :
    for w in iterable :
        v = action(v, w)
    return v
def reduce_while (action, iterable, v) :
    p = iter(iterable)
    try :
        while True :
            w = next(p)
            v = action(v, w)
    except StopIteration :
        pass
    return v
def reduce_for_range (action, iterable, v) :
    for i in range(len(a)) :
        v = action(v, a[i])
    return v