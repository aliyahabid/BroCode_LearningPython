# Loops (While and for)
import time

# While loops

# While loop = a statement that will execute its block of code
# as long as its condition remains true

# name = ""
# while len(name) == 0:
#   name = input("Enter your name: ")

# print("Hello "+name)

# Alternatively, you could write

# name = None
# while not name:
#   name = input("Enter your name: ")
# print("Hello "+name)

# For Loops
# for loop = a statement that will execute ts block of code a limited amount of times
# i is shorthand for index

# for i in range(10):
#   print(i+1)

# for i in range(50,100+1):
#   print(i)

# for i in range(50,100+1,2):
#   print(i)

# for i in "Aliyah":
#    print(i)

# Countdown example:
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("Surprise!")

# Nested loops

# With nested loops, the "inner loop" will finish all of its iterations
# before finishing one iteration of the "outer loop"
# A common convention is to write "j" for index in inner loops.


# The following example will create a rectangle formed from the symbol of your choice.
# Columns = width and rows = height
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))
symbol = input ("Enter a symbol of your choice: ")

# The second print statement is a new line once we exit the inner loop.
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()


