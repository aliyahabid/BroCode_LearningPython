# Data Types and variables

age = 20
age += 1
print("On your birthday, you will turn " + str(age) + ".")
print(type(age))
# The above line can show you what data type age is.

x = 1  # int
y = 2.0  # float
z = "3"  # str

y = int(y)
z = int(z)
print(x, y, z, z * 3)
x, y, z = float(z), float(y), float(z)
print(x, y, z, z * 3)
print("\n")