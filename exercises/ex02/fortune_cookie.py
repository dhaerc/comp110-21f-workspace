"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730240220"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


print("Your fortune cookie says...")

random_value: int = randint(1,3)

if random_value == 1:
    print("New adventures and memories will be coming your way!")
else:
    if random_value == 2:
        print("Your luck will soon bring you to find new fortune!")
    else:
        print("New love will soon bring new experiences.")
print("Now, go spread positive vibes!")