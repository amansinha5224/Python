'''
Types of Programming:-
    - Procedural Programming
    - Object Oriented Programming

OOPS in Python:-
    - OOPS stands for Object Oriented Programming
    - Use to map real world entities through programming
    - Class help us to create a template or blueprint for a object
    - Class contains attributes and methods
    - Object is an instance created using class

4 Pillars of OOPS:-
    - Encapsulation
    - Abstraction
    - Inheritance
    - Polymorphism

* 'self' keyword points to the object which calls the method
'''

class Person:
    # Class Attributes
    name = "Aman"
    occupation = "Software Developer"
    netWorth = 10

    # Class Methods
    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
a.name = "James"
a.occupation = "Chef"
a.netWorth = 100000

a.info()

b = Person()
b.name = "Katherine"
b.occupation = "Product Manager"
b.netWorth = 10000000

b.info()