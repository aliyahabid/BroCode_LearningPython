# Random Module

# Numbers generated in the random module are not truly random, rather they're pseudo-random.
import random

# The following example will print a random integer between 1 and 6.
x = random.randint(1, 6)
print(x)

# This example will print a random floating point number (so between 0 and 1).
y = random.random()
print(y)

# We can generate a random choice from a list or other collection.

RPS_List = ["Rock", "Paper", "Scissors"]
z = random.choice(RPS_List)
print(z)

# You can also shuffle a list like so:
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "A", "K"]
random.shuffle(cards)
print("\nA suit of cards shuffled could look like the following:")
print(cards)
print(cards[0])




