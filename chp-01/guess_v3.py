#!/usr/bin/env python

from random import randint

# Greetings
print("Welcome!")

secret = randint(1, 10)
guess = 0


# Conditional Loop, generally infinite (while True)
while guess != secret:
    g = input("Guess the number: ")
    guess = int(g)
    if guess == secret:
        print("You win!")
    else:
        if guess > secret:
            print("Too high")
        else:
            print("Too low")
print("Game over!")
