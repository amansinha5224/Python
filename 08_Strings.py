'''
Strings in Python:-
    - Strings are immutable in Python
    - Any method performed on string does not change original string but creates a new copy of that string

'''

name = "Aman"
surname = "Sinha"

# String Concatination
print(name + " " + surname)

# Multi line string
apple = """I want to
eat an apple.
"""

print(apple)

# String Index
print(name[0])
print(name[1])
print(name[2])
print(name[3])

# For loop in strings
for i in apple:
    print(i, end = " ")



# String Slicing

fullName = "AmanKumarSinha"

print("Length of Full Name :",len(fullName))

print("First Name is :",fullName[:4])
print("Middle Name is :",fullName[4:9])
print("Last Name is :",fullName[9:])

print("Skipping One Charater :",fullName[::2])
print("Full Name (Through Negative Indexing) :",fullName[-len(fullName) : -1]) # Skips last Charater



# Strings Methods

a = "--- Apple !!!"

print(a)

print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.lstrip("-"))
print(a.replace("A", "M"))
print(a.split(" "))

heading = "the bLog"

print(heading.capitalize())
print(heading.center(50))
print(len(heading.center(50)))
print(heading.count('b'))
print(heading.endswith('g'))
print(heading.find('o'))
print(heading.index('b'))

print(heading.isalnum())
print(heading.isalpha())
print(heading.islower())
print(heading.isspace())
print(heading.istitle())

Greeting = "Hello welcome to my python code"

print(Greeting.title())