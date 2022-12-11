# Tuples

# Tuples are collections of elements that are ordered and unchangeable.
# They're useful for grouping related data.

student = ('Navraj', 6, 'male', 'brown and white')
student2 = ('Fireball', 8, 'male', 'orange and white')

# The count method counts how many times a value appears.

print(student.count('male'))

# The index method tells you where a value appears.

print(student.index('brown and white'))

# You can display all of the values of a tuple using a for loop.

for x in student:
    print(x, end="/")

print("")

# You can check if a certain value exists within a tuple by using if statements.

if "Navraj" in student:
    print("Navraj is here.")

if "Fireball" in student2:
    print("Fireball is here.")