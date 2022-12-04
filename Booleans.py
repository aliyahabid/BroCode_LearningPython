# Booleans
thanos_buzzword = "reAlitY"
thanos_sent_finisher = " can be whatever I want..."
print("True or false, thanos_buzzword is a digit: " + str(thanos_buzzword.isdigit()) + "\n")

first_name, last_name = "Aliyah", "Abid"
full_name = first_name + " " + last_name
print('True or false, "' + str(full_name) + '" is "alpha", AKA alphabetical: ' + str(full_name.isalpha()))
print('True or false, "' + str(first_name) + '" is "alpha", AKA alphabetical: ' + str(first_name.isalpha()))
print('How many times does the letter "a" appear in "' + str(full_name) + '"? ' + str(full_name.lower().count("a")))
print('What would my name look like if all "A"s became "E"s? ' + full_name.lower().replace("a", "e") + "\n")