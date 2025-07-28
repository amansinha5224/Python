'''
Lambda Functions in Python:-
    - 'lambda' keyword help us to define a function in form of an expression
    - Useful when need to write single line function logic
    - Structure:    
        lambda argument: expression
'''

# def square(x):
#     return x**2

# Pass function as an argument
def calculate(func, val):
    return 6 + func(val)


square = lambda x: x**2
cube = lambda x: x**3
avg = lambda x, y, z: (x+y+z) / 3

print(square(5))
print(cube(5))
print(avg(12, 14, 16))

print(calculate(square, 10))
print(calculate(cube, 10))
print(calculate(lambda x: x**4, 10))    # Can also help to pass anonymously