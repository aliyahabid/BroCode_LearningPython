# Data Types and Variables

age = 20
age += 1
print("On your birthday, you will turn " + str(age) + ".")
print(type(age))
# The above line can show you what data type age is.

x = 1  # int
y = 2.0  # float
z = "3"  # string

y = int(y)
z = int(z)
print(x, y, z, z * 3)
x, y, z = float(z), float(y), float(z)
print(x, y, z, z * 3)

# Scopes

# A scope is the region that a variable is recognized.
# A variable is only available from inside the region it's created.
# Global and locally scoped versions of a variable can be created.
# Global variables have a global scope (they're available inside and outside of functions).

# In the example below, the local variable last_name has a local scope because it's declared inside a function.

print("")

name = "Aliyah"
def display_name():
    last_name = "Abid"
    print(name)

print(name)
display_name()
def name_sentence():
    print("Welcome, " + name)

name_sentence()

# Python follows the LEGB rule.
# L - Local
# E - Enclosing
# G - Global
# B - Built-in