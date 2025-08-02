'''
Dunder/Magic Method:-
    - Magic methods, also known as “dunders” from the double underscores surrounding their names, are powerful tools that allow you to customize the behaviour of your classes. They are used to implement special methods such as the addition, subtraction and comparison operators, as well as some more advanced techniques like descriptors and properties.

    - __init__: The init method is a special method that is automatically invoked when you create a new instance of a class. This method is responsible for setting up the object's initial state, and it is where you would typically define any instance variables that you need. Also called "constructor"

    - __str__ and __repr__: The str and repr methods are both used to convert an object to a string representation. The str method is used when you want to print out an object, while the repr method is used when you want to get a string representation of an object that can be used to recreate the object.

    - __len__: The len method is used to get the length of an object. This is useful when you want to be able to find the size of a data structure, such as a list or dictionary.
    
    - __call__: The call method is used to make an object callable, meaning that you can pass it as a parameter to a function and it will be executed when the function is called. This is an incredibly powerful tool that allows you to create objects that behave like functions.
'''

class Employee:
    def __init__(self, name):
        self.name = name
    
    def __len__(self):
        l = 0
        for c in self.name:
            l += 1
        
        return l
    
    def __str__(self):
        return f"The name of the employee is {self.name}"
    
    def __repr__(self):
        return f"Employee Name: {self.name}"
    
    def __call__(self):
        print("This is a callable magic method")

emp1 = Employee("Aman")

print(emp1.name)
print(len(emp1))
print(str(emp1))
print(repr(emp1))
print(callable(emp1))
emp1()