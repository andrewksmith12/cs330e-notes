#!/usr/bin/env python3

#pylint: disable = too-few-public-methods

# -------------
# Decorators1.py
# -------------

import time
def my_timer(orig_func):
    def wrapper():
        t1 = time.time()
        result = orig_func()
        t2 = time.time() - t1
        return t2
    return wrapper

