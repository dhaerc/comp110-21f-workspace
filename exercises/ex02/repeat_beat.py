"""Repeating a beat in a loop."""

__author__ = "730240220"


beat: str = input("What beat do you want to repeat? ")
repeats: int = int(input("How many times do you want to repeat it? "))

i: int = 0
beat_length: int = len(beat)
additive: str = ""

if repeats <= 0:
    print("No beat...")
else:
    while i < beat_length:
        output: str = beat[i]
        additive = additive + output
        i = i + 1
final: str = additive + " "
print(final * (repeats - 1) + additive)