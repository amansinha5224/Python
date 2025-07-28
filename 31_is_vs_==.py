'''
'is' : It compares exact location of object in memory
'==' : It compares only value
'''

a = "Aman"
b = "Aman"

print(a is b)       # True
print(a == b)       # True
print(a is "Aman")  # True
print(a == "Aman")  # True

# Since all statements return True because in Python the constant value (which are immutable) is created only single time

l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4, 5]

print(l1 is l2)                 # False
print(l1 == l2)                 # True
print(l1 is [1, 2, 3, 4, 5])    # False
print(l1 == [1, 2, 3, 4, 5])    # True

# Since list are mutable hence every time Python creates a new list in different memory location