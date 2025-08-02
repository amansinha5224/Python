'''
Multilevel Inheritance:-
    - Multilevel inheritance in Python is a type of inheritance where a class inherits from a class that has already inherited from another class, forming a chain or hierarchy of inheritance
'''

class Animal:
    def __init__(self, name, breed, species):
        self.name = name
        self.breed = breed
        self.species = species
    
    def showAnimal(self):
        print(f"Species : {self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, breed, "Dog")
    
    def showDog(self):
        print(f"Breed : {self.breed}")
        Animal.showAnimal(self)

class GoldenRetriever(Dog):
    def __init__(self, name):
        super().__init__(name, "Golden Retriever")

    def showGoldenRetriever(self):
        print(f"Name : {self.name}")
        Dog.showDog(self)

petDog = GoldenRetriever("Tommy")
petDog.showGoldenRetriever()

print(GoldenRetriever.mro())