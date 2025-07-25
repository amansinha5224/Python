'''
Dictionary in Python:-
    - Store items in key-value pair
    - Elements stored in ordered format
'''

stud1 = {"name": "John", "university" : "Stanford", "degree" : "MBA"}
stud2 = {"name": "Katherine", "university" : "Penn", "degree" : "MS in Cmoputer Science"}
stud3 = {"name": "Larry", "university" : "Stanford", "degree" : "MS in Compter Science"}

stud = {1: stud1, 2 : stud2, 3 : stud3}    # Nested Dictonary

print(stud1.keys())
print(stud1.values())
print(stud1.items())

for keys in stud1:
    print(keys, " => ", stud1[keys])


# Dictionary Methods

# Update
stud2["degree"] = "MS in Electrical Engineering"
print(stud2)

# Add
for student in stud:
    stud[student]["eligible to vote"] = True

print(stud1)
print(stud2)
print(stud3)

# Remove
stud1.pop("eligible to vote")
stud2.popitem()
del stud3["eligible to vote"]

print(stud1)
print(stud2)
print(stud3)

# Copy
temp1 = dict(stud1)
temp2 = stud2.copy()

print(temp1)
print(temp2)