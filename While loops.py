# While loops

# While loop = a statement that will execute its block of code
# as long as its condition remains true

name = ""
while len(name) == 0:
    name = input("Enter your name: ")

print("Hello "+name)

# Alternatively, you could write

# name = None
# while not name:
#   name = input("Enter your name: ")
# print("Hello "+name)