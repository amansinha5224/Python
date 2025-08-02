'''
Single Inheritance:-
    - This is the most common type of inheritance
    - Child class inherit attributes and methods from single parent class
'''

class Animal:
    def __init__(self, name = None, species = None):
        if(name != None, species != None):
            self.name = name
            self.species = species
    
    def makeSound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def makeSound(self):
        print("Bark")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def makeSound(self):
        print("Meow")

a = Animal()
d = Dog("Tommy", "Golden Retriever")
c = Cat("Lucy", "British Shorthair")

a.makeSound()
d.makeSound()
c.makeSound()