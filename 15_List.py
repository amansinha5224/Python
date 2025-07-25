'''
List in Python:-
    - Store multiple values in single variable
    - Can store values of different data types
    - List are mutable in Python
    - Order of values are preserved
    - Zero-based indexing
    - Allow negative indexing

List Comprehension:-
    - Creating list on the go

List Methods:-
    - append    - sort
    - index     - reverse
    - count     - extend
    - copy      - concatination

    etc.
'''

marks = [89, 90, 93, 95, 92]
print(type(marks))
print(marks[2])

if(90 in marks): print("Yes")
else: print("No")

print(marks[:]) # Print whole list

# List comprehension

evenNum = list(num for num in range(10) if num % 2 == 0)
oddNum = [num for num in range(10) if num % 2 != 0]
sqNum = [num*num for num in range(5)]

print(evenNum)
print(oddNum)
print(sqNum)

# List Methods

l = [16, 12, 30, 4, 5]

l.append(9)
l.sort(reverse=True)
l.reverse()

print(l)

print(l.index(4))
print(l.count(5))

# m = l # Pass Refernce
m = l.copy() # Copy list
m[0] = 0

print(l)
print(m)