'''
Typecasting in Python:-
    - Typecasting refers to the conversion in variable from one datatype to another data type.
    - It is also known as type conversion.
    - int(), str(), float(), list(), tuple(), dict(), set(), ord(), etc.

    Type of Typecasting:-
        1) Explicit Conversion: Manual Conversion
        2) Implicit Conversion: Automatic Conversion
'''

firstName = "Aman"
lastName = " Sinha"

print(firstName + lastName)

a = '1'
b = '2'

print(a + b) # 12

# Explicit Type Conversion

a = int(a)
b = int(b)

print(a + b) # 3

# Implicit Type Conversion

a = 9   # implicit conversion from int to float
b = 5.0

print(a + b) # 14.0