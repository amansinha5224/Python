'''
Match Case in Python:-
    - Feature add from Python 3.10 onwards
    - Similar to switch case in C++ or Javascript
    - Using 'break' is not necessary
    - 'case _' denotes the default value
    - 'case <exp1> | <exp2> | <exp3>' checks for multiple expression
'''

day = int(input("Enter Day (Between 1 to 7) : "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednusday")
    case 4:
        print("Thrusday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Not Vaild")
