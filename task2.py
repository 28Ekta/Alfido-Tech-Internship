#Task 2: Number Guessing Game
# Develop a Python game where the user guesses a randomly generated number between 1 and 100.

import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

attempts = 0

while True:
    guess = input("Enter your guess: ")
    
    # Validate input
    if not guess.isdigit():
        print("Please enter a valid integer.")
        continue
    
    guess = int(guess)
    attempts += 1
    
    if guess < secret_number:
        print("Too low. Try again!")
    elif guess > secret_number:
        print("Too high. Try again!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
