num = input("Enter positive number less than 100 : ")

if(num == 'quit'): print("EXIT")
else:
    try:
        num = int(num)
        
        if(num < 0 or num > 100):
            raise ValueError("Invaild Input")

    except ValueError as e:
        print(f"Error Occured: {e}")
    except:
        print("Value should be an integer")