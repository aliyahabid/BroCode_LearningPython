first_name, last_name = "Aliyah", "Abid"
full_name = first_name + " " + last_name
print("Hello, " + full_name + "! I know many things... For example, I know the following: \n")

print("Your name has " + str(len(full_name) - 1) + " letters in it. ")
print('The letter "I" is "' + str(first_name.find("i") + 1) + " letters into your first name and " +
      str(last_name.find("i") + 1) + " letters into your last name.\n")

age = 20
age += 1
print("On your birthday, you will turn " + str(age) + ".")
# print(type(age)) can show you what data type age is.

height = 168.5
print("You are " + str(height) + " cm tall.")
# print(type(height)) can show you what data type height is.

current_age = score = 20
decade = score / 2
print("You're " + str(current_age) + " years old right now and " + str(score) + " years is called a score, " +
      "which is twice the amount of time in a decade. A decade is " + str(int(decade)) + " years.\n")
print("decade = score/2 creates a " + str(type(decade)) + """data type, which is why I typecasted the variable 
        decade into an integer then a string.""")
print('Otherwise, the variable would have printed as ' + str(decade) + ".")

birth_year, disney_princess, DC_superhero = 2002, "Mulan", "Wonder Woman"
print("You were born in " + str(birth_year) + ", your favorite Disney princess is " + disney_princess +
      ", and your favorite DC superhero is " + DC_superhero + ".\n")
thanos_buzzword = "reAlitY"
thanos_sent_finisher = " can be whatever I want..."
print(thanos_buzzword.capitalize() + thanos_sent_finisher)
print(thanos_buzzword.upper() + thanos_sent_finisher)
print(thanos_buzzword.lower() + thanos_sent_finisher)
print("True or false, thanos_buzzword is a digit: " + str(thanos_buzzword.isdigit()) + "\n")

print('True or false, "' + str(full_name) + '" is "alpha", AKA alphabetical: ' + str(full_name.isalpha()))
print('True or false, "' + str(first_name) + '" is "alpha", AKA alphabetical: ' + str(first_name.isalpha()))
print('How many times does the letter "a" appear in "' + str(full_name) + '"? ' + str(full_name.lower().count("a")))
print('What would my name look like if all "A"s became "E"s? ' + full_name.lower().replace("a", "e") + "\n")

print(thanos_buzzword * 3)
BJ = "Beetlejuice"
print(BJ * 3 + "\n")

x = 1  # int
y = 2.0  # float
z = "3"  # str

y = int(y)
z = int(z)
print(x, y, z, z * 3)
x, y, z = float(z), float(y), float(z)
print(x, y, z, z * 3)
print("\n")

# Inputs
# user_name = input("Username: ")
# user_name = user_name.lower()
# user_age = int(input("Age: "))
# user_height = float(input("Height (cm): "))
# print("Welcome, " + user_name + "!")

# Math Functions
import math

print("Different versions of negative pi:")
neg_pi = -3.14
print(round(neg_pi))
print(math.ceil(neg_pi))
print(math.floor(neg_pi))
print(abs(neg_pi))
# pow() gives you a base value to a certain power.
print(pow(neg_pi, 2))
print(math.sqrt(abs(neg_pi)))

print(" ")
a = 4
b = 73
c = -23
print(max(a, b, c, neg_pi))
print(min(b, neg_pi))
print("")

# String indexing and slicing
cat_name = "Navraj"

# Indexing
cat_first_initial = cat_name[0]
cat_first2letters = cat_name[0:2]
cat_nickname = cat_name[:3]
cat_nickname2 = cat_name[3:6]
# Indexes always start at 0, instead of 1.
# The first index is inclusive and the stopping index is exclusive,
# which is why 0:2 is Na and 0:3 is Nav.
print(cat_first_initial)
print(cat_first2letters)
print(cat_nickname)
print(cat_nickname2)
funky_name = cat_name[0:6:1]
funky_name2 = cat_name[0:6:2]
funky_name3 = cat_name[::3]
print(funky_name)
print(funky_name2)
print(funky_name3)
reversed_cat_name = cat_name[::-1]
print(reversed_cat_name)

# Slicing
print(" ")
website = "https://www.google.com"
website_title = slice(12, -4)
website2 = "https://www.wikipedia.org"
# website[12:-4]
print(website[website_title])
print(website2[website_title])
print(" ")

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


# Unsuccessful Testing Nested If Statements
movies_question = input("Do you like movies? (y/n) ")
disney_movies_question = input("Do you like Disney movies? (y/n) ")
mulan_question = input("Do you like Mulan? (y/n) ")
yes = "y"
no = "n"

print(movies_question)
if movies_question == yes:
    print(disney_movies_question)
    if disney_movies_question == yes:
        print(mulan_question)
        if mulan_question == yes:
            print("Nice! Let's be friends!")
        else:
            print("Fair enough.")
    else:
        print("Oh, cool.")
else:
    print("Oh, okay.")
