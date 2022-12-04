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
print("decade = score/2 creates a " + str(type(decade)) + """data type, which is why I typecasted the variable 
        decade into an integer then a string.""")
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



