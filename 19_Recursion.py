'''
Recursion in Python:-
    - Function calling itself till base condition is achived.
'''

# Find factorial of a number
def fact(n):
    if(n < 2): return 1

    return n*fact(n-1)

print(fact(5))
print(fact(20))

# Display Fibonacci sequence
def fib(n):
    if(n < 2): return n
    return fib(n-1) + fib(n-2)

print(fib(10))