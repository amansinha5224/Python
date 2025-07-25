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

# For-else Loop
# 'else' block will be executed once all the iterations in loop is executed, if break in between than code in 'else' will not be executed

l = [1, 2, 3, 4]
for i in range(len(l)):
    print(l[i], end = " ")
    if(i == 2): break
else:
    print("Reached Limit")