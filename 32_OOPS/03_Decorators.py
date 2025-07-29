'''
Decorators in Python:-
    - Decorators are the functions that takes another function is an arguments and returns a new function that modifies the behaviour of original function, the new function is generally referred as decorated function
    - *args: Function takes arguments as a tuple
    - **kwargs: Function takes arguments as a dictionary
    - *args and **kwargs can take any number of inputs irrespective to their position

'''

def greet(func):
    def modified_func(*args, **kwargs):
        print("Goor Morning")
        func(*args, **kwargs)
        print("Thank You for using this function")
    
    return modified_func

@greet
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a + b)

# greet(hello)()
hello()

# greet(add)(4, 5)
add(4, 5)