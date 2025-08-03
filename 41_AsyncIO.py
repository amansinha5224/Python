'''
Async IO in Python:-
    - Asynchronous I/O, or async for short, is a programming pattern that allows for high-performance I/O operations in a concurrent and non-blocking manner. In Python, async programming is achieved through the use of the asyncio module and asynchronous functions.
'''

import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("Function 1 is executed")

async def function2():
    await asyncio.sleep(1)
    print("Function 2 is executed")

async def function3():
    await asyncio.sleep(4)
    print("Function 3 is executed")

async def main():
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()

    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)

asyncio.run(main())