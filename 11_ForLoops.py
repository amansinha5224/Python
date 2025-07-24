'''
Loops in Python:-
    - Repeating a task multiple times
'''

for odd in range(1, 10, 2):
    print(odd, end=" ")

print("\n")

name = "Aman Kumar Sinha"
for char in name:
    print(char, end=", ")

print("\n")

fruits = ["apple", "mango", "peach", "orange", "watermelon"]
for fruit in fruits:
    print(fruit.capitalize())