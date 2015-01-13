#!/usr/local/bin/python3
"""let a user guess a number"""

secret = 13
attempts = 0
while True:
    guess = int(input("Guess a number: "))
    attempts += 1
    if guess == secret:
        print("Correct! Well done, the number was ", guess)
        break
    elif guess < secret:
        print("Guess higher")
    elif guess > secret:
        print("Guess lower")

    if attempts >= 5:
        print("Sorry, the number was", secret)
        break
        

    
        