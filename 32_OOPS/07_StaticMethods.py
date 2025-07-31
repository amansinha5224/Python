'''
Static Methods:-
    - These are the methods in a class which doesn't belong (or associated) to any instance of the class
    - No need to pass self keyword as an argument in the function
    - Can be called using instance or class
'''

class Math:
    def __init__(self, num):
        self.num = num

    def addToNum(self, n):
        self.num += n
    
    @staticmethod
    def add(num1, num2):
        return num1 + num2
    
a = Math(5)
print(a.num)
a.addToNum(5)
print(a.num)

print(a.add(7, 8))       # Can be called using instance
print(Math.add(7, 8))    # Can be called using class