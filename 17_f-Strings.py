'''
f-Strings in Python:-
    - Feature added in Python 3.6
    - Newer way to format string
    - Use '{}' to define any opeartion or variable
'''

name = "Aman"
country = "India"

# Formatting a string
message = "Hey! My name is {1} and I'm from {0}"
print(message.format(country, name))

# Formatting a string using f-String
print(f"Hey! My name is {{name}} and I'm from {{country}}")
print(f"Hey! My name is {name} and I'm from {country}")

price = 23.4565
print(f"The price of this product is : {price:.2f}/-")

print(f"2 x 30 = {2*30}")