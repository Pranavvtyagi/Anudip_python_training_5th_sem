# Number Guessing Game

import random

# Generate secret number between 1 and 50
secret_number = random.randint(1, 50)

attempts = 0

print("Guess the secret number between 1 and 50")

while True:

    guess = int(input("Enter your guess: "))

    attempts = attempts + 1

    if guess > secret_number:
        print("Too High")

    elif guess < secret_number:
        print("Too Low")

    else:
        print("Correct Guess")
        print("Total Attempts =", attempts)
        break
