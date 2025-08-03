'''
Function Caching:-
    - Function caching is a technique for improving the performance of a program by storing the results of a function call so that you can reuse the results instead of recomputing them every time the function is called. This can be particularly useful when a function is computationally expensive, or when the inputs to the function are unlikely to change frequently.

    - In Python, function caching can be achieved using the functools.lru_cache decorator. The functools.lru_cache decorator is used to cache the results of a function so that you can reuse the results instead of recomputing them every time the function is called.
'''

import functools
import time

@functools.lru_cache(maxsize=None)
def func(n):
    time.sleep(1)
    return n*5

# Executing for the 1st time
print(func(20))
print("Done for 20")
print(func(40))
print("Done for 40")
print(func(60))
print("Done for 60")
print(func(80))
print("Done for80")

# Executing for 2nd time
print(func(20))
print("Done for 20")
print(func(40))
print("Done for 40")
print(func(60))
print("Done for 60")
print(func(80))
print("Done for80")