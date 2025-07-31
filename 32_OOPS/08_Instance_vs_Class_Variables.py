'''
Class Variables:-
    - Class variables are defined at the class level and are shared among all instances of the class. They are defined outside of any method and are usually used to store information that is common to all instances of the class. For example, a class variable can be used to store the number of instances of a class that have been created.

Instance Variables:-
    - Instance variables are defined at the instance level and are unique to each instance of the class. They are defined inside the init method and are usually used to store information that is specific to each instance of the class. For example, an instance variable can be used to store the name of an employee in a class that represents an employee.
'''

class Employee:
    companyName = "Apple"
    totalEmployee = 0
    def __init__(self, name):
        self.name = name
        self.raiseAmount = 0.02
        Employee.totalEmployee += 1

    def showDetails(self):
        print(f"Name of Employee is {self.name} and the raise amount in {self.totalEmployee} sized {self.companyName} is {self.raiseAmount}")

emp1 = Employee("Aman")
emp1.raiseAmount = 0.3
emp1.companyName = "Apple India"
emp1.showDetails()

print(Employee.companyName)
Employee.companyName = "Google"
print(Employee.companyName)

emp2 = Employee("James")
emp2.showDetails()