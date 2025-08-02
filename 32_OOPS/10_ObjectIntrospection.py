'''
Object Introspection:-
    - There are three methods for object introspection in Python and they are as 'dir', '__dict' and 'help'
    - dir: The dir() function is a built-in Python function that returns a list of names in the current local scope or a list of attributes of an object.
    - __dict__: The __dict__ attribute returns a dictionary representation of an object's attributes. It is a useful tool for introspection.
    - help: The help() function is used to get help documentation for an object, including a description of its attributes and methods.
'''

# dir()
x = [1, 2, 3]
print(dir(x))
print(x.__add__)

# __dict__
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("John", "23")
print(p.__dict__)

# help()
print(help(Person))