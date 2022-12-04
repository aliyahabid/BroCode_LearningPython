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