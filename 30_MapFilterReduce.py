'''
Maps:-
    - It maps every items of iteratable (let's say list) into new iteratable after performing some operations
    - It returns map object
Filter:-
    - It filter out the values from the iteratable which statisfy the given condition
    - It returns filter object
Reduce:-
    - It reduces all items of iteratable into a single value
    - Reduce function needs to be import form 'functools'

* All these three functions are higher order functions as they take function as an argument
'''

# Map
l = [23, 34, 45, 56, 67, 12]

new_l = list(map(lambda x: x**3, l))

print(new_l)


# Filter
filtered_list = list(filter(lambda x: x > 50, l))

print(filtered_list)


# Reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y: x + y, numbers)

print(sum)