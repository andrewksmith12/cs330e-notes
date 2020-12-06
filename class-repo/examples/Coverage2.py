#!/usr/bin/env python3

# ------------
# Coverage2.py
# ------------

# https://coverage.readthedocs.org

from unittest import main, TestCase

def cycle_length (n) :
    assert n > 0
    c = 1
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class MyUnitTests (TestCase) :
    def test (self) :
        self.assertEqual(cycle_length(2), 2)
    def test2 (self):
        self.assertEqual(cycle_length(3),8)    #Add this test to cover 15->18. -m flag on coverage report gives us the line numbers. 

if __name__ == "__main__" : #pragma: no cover
    main()

""" #pragma: no cover
$ coverage run --branch Coverage2.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK



$ coverage report -m
Name           Stmts   Miss Branch BrPart  Cover   Missing
----------------------------------------------------------
Coverage2.py      16      1      4      1    90%   18, 15->18
"""
