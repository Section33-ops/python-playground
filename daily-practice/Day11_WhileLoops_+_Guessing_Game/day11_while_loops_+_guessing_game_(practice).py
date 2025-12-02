# 09/16/2025
# Practice: Build your own Number Guessing Game

import random   # Import the random module

random_number = random.randint(1, 20)   # Random number between 1 and 20
usr_attempts = 0    # Initial user attempt(0)
usr_limit = 7   # User guess limit

while usr_attempts < usr_limit: # Runs code while user attempt is lower than guess limit
    usr_guess = int(input("\nEnter a number between 1 and 20. \nYou have 7 chances: ")) # Ask user for a guess
    usr_attempts += 1   # Increase user attempt by 1
    if usr_guess == random_number:  # If user's guess is equal to random number
        print(f"You win. The number is {random_number}.\nYou won in {usr_attempts} attempts")   # Print You win. The number and the number of  attempts
        break   # Break out of the loop
    elif usr_guess >= random_number:    # Else if user guess is more than the random number
        print("Too high. Try again.")   # Print "Too high. Try again."
    elif usr_guess <= random_number:    # Else if user guess is lower than random number
        print("Too low. Try again.")    # Print "Too low. Try again."
else:   # Else if the user is out of attempts
    print(f"You lose. The number is {random_number}.")  # Print "You lose. The number is {random number}."