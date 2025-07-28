'''
Main Function in Python:-
    - Creating main function is not neccessary in Python, but it gives more structure to the code and makes code more understandable for a non Python programmer
    - Purpose of if __name__ == "__main__":
        - Prevents Unwanted Execution When Imported
        - When your Python script is imported as a module into another script, you don't want it to run automatically.
        - This conditional ensures that main() is only called when the script is run directly, not when it's imported.
'''

def rectArea(x, y):
    return x*y

def main():
    l = float(input("Enter Length : "))
    w = float(input("Enter Width : "))

    area = rectArea(l, w)

    print(f"Area : {area}")

if __name__ == "__main__":
    main()