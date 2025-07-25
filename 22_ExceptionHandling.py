try:
    num = int(input("Enter a number : "))
    
    print(f"Multiplication Table of {num}")

    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

except Exception as e:
    print("Invalid Input")
    print(e)

except ValueError:
    print("Not an Integer")

except IndexError:
    print("Index Error")


# Finally keyword
def func1():
    try:
        l = [34, 54, 2, 43]
        
        i = int(input("Enter the index : "))

        print(l[i])

        return 1

    except:
        print("Some Error")

        return 0

    finally:
        print("Always Executed, even function is returned")

func1()

print("END of Program")