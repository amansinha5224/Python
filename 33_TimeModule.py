'''
Time Module in Python:-
    - This module provides various time-related functions. For related functionality
    - https://docs.python.org/3/library/time.html
'''
import time

def usingWhile():
    i = 0

    while(i < 5000):
        i += 1
        # print(i, end = " ")

def usingFor():
    for i in range(5000):
        i += 0

init = time.time()
usingFor()
print(f"Time Taken by For Loop : {time.time() - init}")

print("Please Wait...")
time.sleep(2)

init = time.time()
usingWhile()
print(f"Time Taken by While Loop : {time.time() - init}")

print()

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
print(f"Current Date-Time : {formatted_time}")