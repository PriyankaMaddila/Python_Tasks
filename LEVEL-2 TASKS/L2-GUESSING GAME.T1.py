#LEVEL2-T1
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Define a function to check the user's guess
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

# Play the game
print("Welcome to the Number Guessing Game!")
while True:
    # Get the user's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Check the user's guess
    result = check_guess(guess, secret_number)

    # Print the result
    print(result)

    # Increment the number of attempts
    attempts += 1

    # Check if the user has won
    if result == "Correct":
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break
