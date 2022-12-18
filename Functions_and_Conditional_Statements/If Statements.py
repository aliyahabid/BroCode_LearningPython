# If Statements

# The order of your if statements matter.
user_age = int(input("How old are you? "))
if user_age >=70:
    print("You've been eligible to vote for a LONG time!")
elif user_age >= 16:
    print("You can register to vote in the USA!")
elif user_age <= 0:
    print("You haven't been born yet...")
else:
    print("Unfortunately, you are not yet old enough to vote.")

# elif = else if statements
# elif can be used for more than two conditions. You can also use nested if statements.
# else statements run if all above conditions are false.

# Logical operators (and, or, not)
# Logical operators are used to check if two or more conditional statements are true.

print(" ")

temp = float(input("What's the current temperature in degrees Fahrenheit? "))

if temp >= 70 and temp <= 90:
    print("The temperature should be pretty comfortable.")
elif temp < 70 or temp > 90:
    print("The temperature isn't too comfortable right now.")

# Alternatively, you could use the "not" operator. For example,
# if not(temp >= 70 and temp <= 90):
#     print("The temperature isn't too comfortable right now.")
# elif not(temp < 70 or temp > 90):
#     print("The temperature should be pretty comfortable.")