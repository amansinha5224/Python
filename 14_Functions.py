'''
Functions in Python:-
    - Block of code that perform certain operation
    - Makes code more readable
    - Avoid repeation of code in a program

Types of Functions:-
    - Built-In Functions 
        - e.g. are max(), min(), etc.
    - User-Defined Functions
        - e.g. def findSum(a, b) etc.

Function Arguments:-
    - These are the values that are passed to the function

Types of Arguments in Function:-
    - Default Argument
    - Keyword Argument
    - Positional Argument
    - Variable-length Argument
'''

def geometricMean(a, b):
    # This function calculate geometric mean of two numbers
    return (a*b)/(a+b)

def findGreater(a, b):
    if(a > b):
        print("First Number is Greater")
    elif(a < b):
        print("second Number is Greater")
    else:
        print("Both Numbers a equal")

def undefinedFunction():
    pass    # A placeholder

print(geometricMean(10, 20))
print(geometricMean(13, 14))
print(geometricMean(19, 40))

findGreater(23, 45)




# Default Argument

def printNum(a = 1, b = 5):
    print(a, b)

printNum()

# Keyword Argument

def printName(first, middle, last):
    fullName = first + " " + middle + " " + last
    print(fullName)

printName(last = "Sinha", first = "Aman", middle = "Kumar")

# Positional Argument

def calDiff(a, b):
    return a - b

print(calDiff(5, 6))
print(calDiff(6, 5))

# Variable-length Argument

def average(*numbers):

    print(type(numbers))    # Tuple

    sum = 0
    
    for num in numbers:
        sum += num
    
    return sum / len(numbers)

def printWord(**words):

    print(type(words))      # Dict

    for alpha in words:
        print(alpha, ":", words[alpha])

print(average(1, 2, 3, 8, 9))

printWord(A = "Apple", B = "Ball", C = "Cat")