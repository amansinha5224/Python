print("Calculator App")

while(True):
    print("""
Select an Operation
          1. Addition
          2. Subtraction
          3. Multiplication
          4. Division
          5. Floor Division
          6. Remainder
          7. Exponent
          8. EXIT
""")
    
    operation = input("Enter Choice : ")

    if(operation == '8'): break

    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number : "))

    if (operation == '1'):
        print("RESULT: ",num1 + num2)
    elif (operation == '2'):
        print("RESULT: ",num1-num2)
    elif (operation == '3'):
        print("RESULT: ",num1*num2)
    elif (operation == '4'):
        if(num2 != 0):
            print("RESULT: ",num1/num2)
        else:
            print('Undefined')
    elif (operation == '5'):
        if(num2 != 0):
            print("RESULT: ",num1//num2)
        else:
            print('Undefined')
    elif (operation == '6'):
        if(num2 != 0):
            print("RESULT: ",num1%num2)
        else:
            print('Undefined')
    elif (operation == '7'):
        print("RESULT: ",num1**num2)
    else:
        break

print("Error! Program has been terminated")