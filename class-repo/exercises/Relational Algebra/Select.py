#!/usr/bin/env python3


# ---------
# Select.py
# ---------

# http://en.wikipedia.org/wiki/Selection_(relational_algebra)

def select_yield (r, up) :
    for d in r :
        if up(d) :
            yield d

def select_generator (r, up) :
    return (d for d in r if up(d))

def select_filter (r, up) :
    return filter(up, r)


def my_select_negate(table, up):
    for row in table:
        if up(row) is False:
            yield row