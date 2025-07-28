'''
Scope of a Variable:-
    - Local
    - Global
'''

x = 4   # Global variable, It can be accessed anywhere in the program

def function():
    global x    # 'global' keyword helps to change variable value even from inside of a function
    x = 5   # Local Variable, It can't be accessed outside the function scope
    print("Value of x inside function :",x)

function()
print("Value of x outside function :",x)