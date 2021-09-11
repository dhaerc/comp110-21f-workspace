"""Counting letters in a string."""

__author__ = "730240220"

letter: str = input("What letter do you want to search for? ")
word: str = input("Enter a word: ")
word_length: int = len(word)
counter: int = 0
total: int = 0

while counter < word_length:
    if word[counter] == letter:
        total = total + 1
    else:
        total = total + 0
    counter = counter + 1
print("Count: " + str(total))