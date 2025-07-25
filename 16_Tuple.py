'''
Tuples in Python:-
    - Store multiple values in one variable
    - Tuples are immutable
    - Can hold multiple data types
'''

tup1 = (1)      # int
tup2 = (1,)     # tuple

print(type(tup1))   
print(type(tup2))

tup1 = (45, 54, 24, 765, 5, 67)

print(45 in tup1)

for index in range(len(tup1)):
    print(tup1[index], end=", ")

# Methods in Tuple

tup = (5, 4, 44, 64, 78, (1, 45, 5))

print(tup.count(5))
print(tup.index(44))
print(tup.index(64, 1, 4))
print(tup.index((1, 45, 5)))

print(tup)

tup = list(tup)

print(tup)