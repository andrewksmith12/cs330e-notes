#!/usr/bin/env python3

# --------------
# DecoratorsT.py
# --------------

from unittest import main, TestCase
from Decorators1 import my_timer
import time

@my_timer
def func1():
    time.sleep(1) # delay of 1 second

@my_timer
def func2():
    time.sleep(2) # delay of 2 seconds
    
#Hint: you can get the current time in Python using the time() function provided by the time module.
class MyUnitTests (TestCase) :
    def test_1 (self) :
       self.assertTrue(1 <= func1() < 1.1)    
    def test_2 (self) :
       self.assertTrue(2 <= func2() <= 2.1)
               
if __name__ == "__main__" :
    main()