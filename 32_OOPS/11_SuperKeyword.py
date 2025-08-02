'''
Super Keyword:-
    - super keyword is used by child class to use parent class methods
    - It helps to reduce repeatation of code
'''

class Parent:
    def parentMethod(self):
        print("This is a parent method")

class Child(Parent):
    def parentMethod(self):
        print("Aman")
        super().parentMethod()
    def childMethod(self):
        print("This is a child Method")
        super().parentMethod()
    

childObject = Child()
childObject.childMethod()
childObject.parentMethod()


# Constructor using Super Keyword

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def empInfo(self):
        print(f"Name: {self.name}\nID: {self.id}")

class Programmer(Employee):
    def __init__(self, name, id, lang):
        super().__init__(name, id)
        self.lang = lang
    
    def programmerInfo(self):
        super().empInfo()
        print(f"Programming Language: {self.lang}")

Jane = Employee("Jane", 434)
Aman = Programmer("Aman", 123, "Python")

Jane.empInfo()
Aman.programmerInfo()