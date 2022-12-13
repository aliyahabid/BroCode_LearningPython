# Changing the first letters of strings and concatenating

thanos_buzzword = "reAlitY"
thanos_sent_finisher = " can be whatever I want..."
print(thanos_buzzword.capitalize() + thanos_sent_finisher)
print(thanos_buzzword.upper() + thanos_sent_finisher)
print(thanos_buzzword.lower() + thanos_sent_finisher)
print(thanos_buzzword * 3)
BJ = "Beetlejuice"
print(BJ * 3 + "\n")
# Constants are capitalized, so BJ is actually a constant--not a variable.

# Variables and String Typecasting

height = 168.5
print("You are " + str(height) + " cm tall.")
# print(type(height)) can show you what data type height is.

current_age = score = 20
decade = score / 2
print("You're " + str(current_age) + " years old right now and " + str(score) + " years is called a score, " +
      "which is twice the amount of time in a decade. A decade is " + str(int(decade)) + " years.\n")
print("decade = score/2 creates a " + str(type(decade)) + """ data type, 
which is why I typecasted the variable decade into an integer then a string.""")
print('Otherwise, the variable would have printed as ' + str(decade) + ".")

birth_year, disney_princess, DC_superhero = 2002, "Mulan", "Wonder Woman"
print("You were born in " + str(birth_year) + ", your favorite Disney princess is " + disney_princess +
      ", and your favorite DC superhero is " + DC_superhero + ".\n")

# String length and counting instances of a character in a string
first_name, last_name = "Aliyah", "Abid"
full_name = first_name + " " + last_name

print("Your name has " + str(len(full_name) - 1) + " letters in it. ")
print('The letter "I" is "' + str(first_name.find("i") + 1) + " letters into your first name and " +
      str(last_name.find("i") + 1) + " letters into your last name.\n")

# String Formatting

# The str.format() is an optional method that gives users more control when displaying output.
# The curly braces or {} are format fields, which act as placeholders for a value or a variable--
# they work in order. However, you can also use a positional argument by listing the index of
# the values you want to insert inside the format field.

animal = "cow"
item = "moon"

print("The {} jumped over the {}.".format(animal, "moon"))
print("The {} made {} on the {}.".format(animal,"milk", item))
print(" ")

# Positional argument:
print("The {2} couldn't eat {0} on the {1}.".format("grass", item, animal))
print("{0} ran into another {0}, but one was an {1}.".format("Santa","imposter"))
print(" ")

# Keyword argument pair:
print("The {animal} climbed the {plant}.".format(plant="tree", animal="cat"))
print("The {animal} barked at the other {animal}.".format(animal="dog",scene="grass"))
print(" ")

text = "A {} and a {} walked into a bar."
print(text.format("mechanic", "writer"))
print(" ")

username = "robokop"

# You can insert a number into a format field to allocate a specific amount of space for the values
# you'll insert. You can do that by writing the number after a colon in the curly braces.
# You can add padding when formatting as seen in the following examples.

print("Welcome user {}. Here is your dashboard.".format(username))
print("Welcome user {:10}. Here is your dashboard.".format(username)) # Default: left alignment
print("Welcome user {:<10}. Here is your dashboard.".format(username)) # Left alignment
print("Welcome user {:>10}. Here is your dashboard.".format(username)) # Right alignment
print("Welcome user {:^10}. Here is your dashboard.".format(username)) # Center alignment
print(" ")

# Keyword argument examples:
print("Welcome user {username:10}. Here is your {screen}.".format(username="whigpartyman",screen="dashboard"))
print("Welcome user {username:20}. Here is your {screen}.".format(username="whigpartyman",screen="dashboard"))

# Positional argument example:
print("Welcome user {0:^20}. Here is your {1}.".format("whigpartyman","dashboard"))



