'''
Multi-threading in Python:-
    - Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process. In Python, we can use the threading module to implement multithreading. In this tutorial, we will take a closer look at the threading module and its various functions and how they can be used in Python.
'''

import threading
import time
from concurrent.futures import ThreadPoolExecutor

def function1(seconds):
    print(f"Sleeping for {seconds}sec.")
    time.sleep(seconds)

def main():
    # Without Threading
    time1 = time.perf_counter()
    function1(4)
    function1(2)
    function1(1)
    time2 = time.perf_counter()
    print(f"Time without threading: {time2 - time1}sec.")

    # With Treading
    time1 = time.perf_counter()
    t1 = threading.Thread(target=function1, args=[4])
    t2 = threading.Thread(target=function1, args=[2])
    t3 = threading.Thread(target=function1, args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(f"Time with threading: {time2 - time1}sec.")

def pollingDemo():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(function1, 3)
        future2 = executor.submit(function1, 2)
        future3 = executor.submit(function1, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())

        l = [3, 5, 4, 2, 1]

        results = executor.map(function1, l)
        for result in results:
            print(result)
    
pollingDemo()