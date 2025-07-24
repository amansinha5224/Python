num = int(input("Enter a Number less than 100 : "))

# Incrementing while loop
while(num <= 100):
    print(num, end = " ")
    num += 2

print("\n")

# Decrementing while loop
while(num > 0):
    print(num, end=" ")
    num -= 2
else:
    print("\nNumber is negative")

# Emulating do while loop in python
i =  int(input("Enter a positive number : "))
print(i)

while(i > 0):
    print(i)
    i -= 1