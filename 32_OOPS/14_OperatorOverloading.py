'''
Opearator Overloading:-
    - Operator Overloading is a feature in Python that allows developers to redefine the behavior of mathematical and comparison operators for custom data types. This means that you can use the standard mathematical operators (+, -, *, /, etc.) and comparison operators (>, <, ==, etc.) in your own classes, just as you would for built-in data types like int, float, and str.
'''

class Vector:
    def __init__(self, i = None, j = None, k = None):
        if (i != None, j != None, k != None):
            self.i = i
            self.j = j
            self.k = k

    def __str__(self):
        return f"({self.i})i + ({self.j})j + ({self.k})k"
    
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

    def __sub__(self, x):
        return Vector(self.i - x.i, self.j - x.j, self.k - x.k)
    
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(str(v1))
print(str(v2))

# Add vectors
v3 = Vector()
v3 = v1 + v2
print(str(v3))

# Sub vectors
print(str(v1 - v2))