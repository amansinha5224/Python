'''
Break Statement:- Terminate loop on specific condition
Continue Statement:- Skip particular condition in a loop
Pass Statement:- Placeholder for future code
'''

print("MULTIPICATION TABLE OF 5")

for i in range(15):
    if(i == 0): continue
    if(i == 2): pass

    print(5, "x", i, "=", 5*i)

    if(i == 10): break