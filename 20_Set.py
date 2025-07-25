'''
Set in Python:-
    - Store only unique elements
    - Store elements in unoredered format
    - Set are immutable
    - Can store different data types
    - Element cannot be accessed using index

Set Methods:-
    - Visit: https://www.w3schools.com/python/python_ref_set.asp
'''

s = {2, 4, 6, 7, 7, 2, 1, 5, 6, 5, 5}
print(s)

temp = {}
print(type(temp))   # dict

temp = set()
print(type(temp))   # set

for val in s:
    print(val, end = " ")
print("\n")


# Set Methods

s1 = {1, 4, 3, 5, 2, 34, 4, 5}
s2 = {10, 41, 13, 25, 2, 34, 4, 34}

print(s1.union(s2))
print(s1.intersection(s2))

print(s1, s2)

s1.update(s2)
s2.intersection_update(s1)

print(s1)
print(s2)
