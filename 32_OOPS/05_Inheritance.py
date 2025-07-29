'''
Inheritance:-
    - Inheritance means to inherit properties and methods from parent class by children class
    - It increases code reuseibility and avoid redundancy of code

Types:-
    - Single Inheritance
    - Multiple Inheritance
    - Multilevel Inheritance
    - Multipath Inheritance
    - Hierarchical Inheritance
    - Hybrid Inheritance
'''

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"EMP ID: {self.id}\nEMP NAME: {self.name}")

# Class Programmer Inherited Properties and Methods form class Employee 
class Programmer(Employee):
    def showLanguage(self):
        print("The Default language is Python")

e1 = Employee("Aman", 1)
e2 = Programmer("Sam", 2)
e3 = Employee("Rishi", 3)

e1.showDetails()
e2.showDetails()
e3.showDetails()