'''
Multiple Inheritance:-
    - In multiple inheritance, single child class inherit properties form multiple parent class
'''

class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self, dance):
        self.dance = dance

    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Dancer, Employee):
    def __init__(self, name, dance):
        self.name = name
        self.dance =dance

a = DancerEmployee("Oliver", "Salsa")

print(a.name)
print(a.dance)
a.show()

# mro(): Method Resolution Operator
# It gives details about the order in which a method will be searched in a class hierarchy
# It follows 'Bottom to Top' and 'Left to Right' Approach
print(DancerEmployee.mro())