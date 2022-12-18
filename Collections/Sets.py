# Sets

# Sets are unordered, unindexed collections of elements.
# There are no duplicate values in sets.

dishes = {'plate', 'bowl', 'cup'}
utensils = {'fork', 'spoon', 'knife'}

for x in utensils:
    print(x)

print("")

utensils.add('spork')
utensils.remove('knife')

for x in utensils:
    print(x)

print("")

# The clear method removes all elements in the set.
# utensils.clear()

for x in dishes:
    print(x)

print("")


# To add the elements of one set (eg. set2) to another (eg. set1), you can write set1.update(set2).
dishes.update(utensils)

for x in dishes:
    print(x)

print("")

# The first set now includes the other, but the second does not include the first.
for x in utensils:
    print(x)

print("")

# To join sets, you can use the union() method.

dinner_table = utensils.union(dishes)
for x in dinner_table:
    print(x)

# New set examples:
astrology_signs = {"Aries", 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
                      'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'}
names = {'Aries', 'Jimmy', 'Leo', 'Verna', 'Lina'}

print("")

# Comparing Sets

# You can compare the elements of sets using the difference and intersection methods.

# The following will print what elements are in names that aren't in astrology_signs.
print(names.difference(astrology_signs))

for x in names.difference(astrology_signs):
    print(x, end=". ")

print("\n")

# The following will print what elements both sets have in common.
print(names.intersection(astrology_signs))



