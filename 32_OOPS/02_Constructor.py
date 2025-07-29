'''
Constructor:-
    - It is a method in class which invoked automatically whenever a new object is created
    - Generally use to initialize an object
    - It returns none
    - Python doesn't allow to create multiple constructor, if there are multiple constructor than the last constructor in the class will be called

Types of Constructor:-
    - Parameterized
    - Non-Parameterized
    - Default Constructor
'''

class Person:
    # Constructor
    def __init__(self, name, occupation):
        self.name = name
        self.occupation = occupation

    # Default Constructor
    # def __init__(self):
    #     print("This is a default constructor")

    # Class Methods
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = Person("Aman", "Developer")
b = Person("Pears", "HR")

a.info()
b.info()