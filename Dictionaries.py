# Dictionaries

# Dictionaries are changeable, unordered collections of unique key:value pairs.
# They're fast because they use hashing, which allows us to access a value quickly.

# The data types don't matter.

capitals = {'USA':'Washington DC','India':'New Delhi',
            'Mexico':'Mexico City', 'China':'Beijing'}
# Instead of using numbered indices to access the values, we use the associated key.

# print(capitals['India'])
# The above line of code works but is unsafe because your code will have an error if
# there is no key by that name. For example, there is no key called 'Germany', so
# if you write print(capitals['Germany']), your code will not work.
# The following is a safer way to find the values of a key.

print(capitals.get('India'))
print(capitals.get('Germany'))

# The following lines are methods to print only the keys or only the values.
print(capitals.keys())
for keys in capitals.keys():
    print(keys)

print("")

print(capitals.values())
for values in capitals.values():
    print(values)

print("")

# The following line prints both keys and values.
print(capitals.items())

for keys, values in capitals.items():
    print(keys, values)

print("")

# Altering a Dictionary

# Since dictionaries are mutable, we can alter them after the program is already running.
# The update method can add key:value pairs and alter pairs already in the dictionary.

capitals.update({'Germany':'Berlin', 'France':'Paris', 'USA':'Washington D.C.'})

for keys, values in capitals.items():
    print(keys, values)

print("")

# The pop method can remove a key:value pair.

capitals.pop('Mexico')
for keys, values in capitals.items():
    print(keys, values)

print("")

# The clear method removes everything from the dictionary.
capitals.clear()
for keys, values in capitals.items():
    print(keys, values)

print("The dictionary doesn't have items anymore.")



