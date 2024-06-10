#!/usr/bin/env python3

# Greetings
print("Welcome!")

# Data handling, conversion/casting
g = input("Guess the number: ")
guess = int(g)

# Flow control, data verification
if guess == 5:
    print("You win!")
else:
    print("You lose!")
