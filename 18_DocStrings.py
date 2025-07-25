'''
Docstrings in Python:-
    - It is used to explain a function, class or module
    - Placed just above the function defination
    - Uses triple (')

PEP 8:-
    - PEP stands for Python Enhancement Proposal
    - This provides set of comvention and recommendation for code layout, formatting, naming, and structure, aiming to improve the readability and consistency of Python code.

The Zen of Python:-
    - Can be access using 'import this'
'''

def squareNum(n):
    '''This function display square of a number.'''
    print(n*n)

squareNum(5)
print(squareNum.__doc__)

import this     # The Zen of Python