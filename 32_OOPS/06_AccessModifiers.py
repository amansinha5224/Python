'''
Access Specifiers/Modifiers:-
    - It helps to limit class variables and class methods outside of a class while implementing the concepts of inheritance
    - There is as such no concept of public, private or protected in Python, but Python have naming convention to implement the concept of access specifers
    - Although we can still access private member of class using Name mangling
    - In name mangling process any identifier with two leading underscore and one trailing underscore is textually replaced with _classname__identifier where classname is the name of the current class

Types:-
    - Public
    - Private
    - Protected
'''

class Employee:
    def __init__(self):
        self.name = "Aman"                      # Public
        self._empId = 5                         # Protected
        self.__email = "aman.sinha@email.com"   # Private

a = Employee()

print(a.name)
print(a._empId)     # This can still be accessed outside of class becase it is just a naming convention not a strict enforcement

# Name Mangling
print(a._Employee__email)
print(a.__dir__())