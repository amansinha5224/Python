'''
Class Methods:-
    - Class methods are useful in several situations. For example, you might want to create a factory method that creates instances of your class in a specific way. You could define a class method that creates the instance and returns it to the caller. Another common use case is to provide alternative constructors for your class. This can be useful if you want to create instances of your class in multiple ways, but still have a consistent interface for doing so.

Class Methods as Alternative Constructors:-
    - A class method belongs to the class rather than to an instance of the class. One common use case for class methods as alternative constructors is when you want to create an object from data that is stored in a different format, such as a string or a dictionary. 

'''

class Employee:
    company = "Apple"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name is {self.name} and the company is {self.company} with salary {self.salary}")
    
    @classmethod
    def fromStr(cls, string):       # Class Methods are used as alternative constructor
        return cls(string.split("-")[0], int(string.split("-")[1]))

    @classmethod
    def changeCompany(cls, companyName):    # First Argument will be consider as class instead of instance
        cls.company = companyName
    
e1 = Employee("Aman", 120000)
e1.show()
e1.changeCompany("Tesla")
e1.show()

print(Employee.company)

info = "Jane-130000"
e2 = Employee(info.split("-")[0], int(info.split("-")[1]))
e2.show()

info = "John-10000"
e3 = Employee.fromStr(info)
e3.show()