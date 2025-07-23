'''
Variables in Python:-
    Variables is like a container which stores a value.
    a = 1, Store 1 in memory and give address to a

Data Types in Python:-
    - Integer
    - String
    - Bool
    - Float
    - None
    - Complex
    - List (Mutable)
    - Tupe (Immutable)
    - Dictonary

    -> Type of variables should be same for performing arithmetic operations in python

-> Everything in Python is an object (be it int, bool, string, etc.)
'''

a = 1
b = True
c = "Aman"
d = None
e = complex(1, 2)
f = 0.12345
g = 'A'

h = [1, 2, 3, [4, 5], ["apple", "mango"]]
i = (1, 2, 3, [4, 5], ("apple", "grapes"))
j = {"Name" : "Aman", "Branch" : "ECE", "Can Vote" : True}

print("Type of a : ", type(a))
print("Type of b : ", type(b))
print("Type of c : ", type(c))
print("Type of d : ", type(d))
print("Type of e : ", type(e))
print("Type of f : ", type(f))
print("Type of h : ", type(h))
print("Type of i : ", type(i))
print("Type of j : ", type(j))