'''
Conditional in Python:-
    - if statement
    - if-else statement
    - if-elif statement is used
    - Nested if statement
    - Conditional Operators >, <, >=, <=, ==, !=
'''

# if-else statement
age = int(input("Enter Your Age : "))

if(age >= 18):
    print('Can Drive')
else:
    print('Cannot Drive')


# if-elif statement
num = float(input("Enter Number : "))

if(num < 0):
    print("Negative Number")
elif(num == 0):
    print("Zero")
else:
    print("Positive Number")
    if(num > 999):
        print("Number is greater than 999")
    elif(num == 999):
        print("Special Number")



# Short-Hand if-else

a = 330
b = 3303

print('A') if a > b else print("=") if (a == b) else print("B")

c = 9 if a > b else 0

print(c)