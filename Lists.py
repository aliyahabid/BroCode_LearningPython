# Lists

# Lists are used to store multiple elements within a single variable.
# Each item in a list is referred to as an "element."

food = ["pizza", "macaroni and cheese", "udon noodles", "buffalo wings"]
print("The food list: ") # Line 1

# You can update a list later in the code.

print("") # Line 2
print(food[0] + " and " + food[3]) # Line 3
print("") # Line 4
food[3] = "mashed potatoes"

for x in food:
    print(x) # Lines 5-8

print("") # Line 9
print(food) # Line 10

food.append("broccoli")
food.append("beef")
food.remove("udon noodles")
for x in food:
    print(x) # Lines 11-14
print("")

food.pop()
for x in food:
    print(x) # Lines 16-19
print("")

food.insert(0,"cake")
for x in food:
    print(x) # Lines 21-24
print("")

food.sort()
for x in food:
    print(x) # Lines 26-29

food.clear()
for x in food:
    print(x)

# listname.clear() clears the list of all of its data/elements.

print("")


# 2D Lists

# 2D lists are lists of lists.

entrees = ["baked ziti", "spaghetti and meatballs", "fettucine alfredo"]
drinks = ["coke", "water", "lemonade", "unsweetened tea"]
desserts = ["chocolate cake", "ice cream"]

menu = [entrees, drinks, desserts]

print(menu)
print(menu[2])
print("We have these drink options for diabetics: " + menu[1][1] + " and " + drinks[3])
# You can write either menu[1][1] or drinks[3] to get "unsweetened tea."

