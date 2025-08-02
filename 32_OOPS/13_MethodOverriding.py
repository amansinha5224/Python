'''
Method Overriding:-
    - Method overriding is a powerful feature in object-oriented programming that allows you to redefine a method in a derived class. The method in the derived class is said to override the method in the base class. When you create an instance of the derived class and call the overridden method, the version of the method in the derived class is executed, rather than the version in the base class.
'''

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        super().__init__(radius, radius)
    
    def area(self):
        return (22/7) * super().area()
    
square = Shape(4, 4)
print(square.area())

circle = Circle(2.2563)
print(circle.area())