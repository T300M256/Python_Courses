#!/usr/local/bin/python3
"""excersises use of modules"""

import random

secret = random.randint(1,99)

while True:
    guess = int(input("Guess a number: "))
    if guess == secret:
        print("You guessed it!")
        break
    elif guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")

    