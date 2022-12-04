# If Statements

user_age = int(input("How old are you? "))
if user_age >= 16:
    print("You can register to vote in the USA!")
elif user_age <= 0:
    print("You haven't been born yet...")
else:
    print("Unfortunately, you are not yet old enough to vote.")

# elif = else if statements
# elif can be used for more than two conditions. You can also use nested if statements.
# else statements run if all above conditions are false.
