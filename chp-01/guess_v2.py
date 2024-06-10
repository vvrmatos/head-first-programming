#!/usr/bin/env python

# Greetings
print("Welcome!")

# Data handling, conversion/casting
g = input("Guess the number: ")
guess = int(g)

# Flow control, data verification
if guess == 5:
    print("You win!")
else:
    if guess > 5:
        print("Too high")
    else:
        print("Too low")

print("Game over!")
