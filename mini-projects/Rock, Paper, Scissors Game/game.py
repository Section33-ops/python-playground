# 10/01/2025

import random   # Import the random module

options = ["rock", "paper", "scissors"]

play = input("Do you want to play? (Y)es or (N)o ").lower() # Prompts user to ask if they want to play

while play == "y":  # Keep playing if user's prompt is 'y'
    usr_choice = input("Rock, Paper, Scissors SHOOT! ").lower() # Prompt user for their choice
    computer_choice = random.choice(options)    # Computer randomly selects a choice
    
    if computer_choice == "scissors" and usr_choice == "paper": # Scissors beat rock
        print(f"You lose! I chose {computer_choice}")
    elif computer_choice == "paper" and usr_choice == "rock":# Paper beats rock
        print(f"You lose! I chose {computer_choice}")
    elif computer_choice == "rock" and usr_choice == "scissors":# Rock beats scissors
        print(f"You lose! I chose {computer_choice}")
    elif computer_choice == usr_choice: # Check if it's a tie
        print(f"Again! I chose {computer_choice}")
        continue    # Continues with the loop if it's a tie
    else:   
        print(f"You win! I chose {computer_choice}")

    # Ask user if they want to continue
    if computer_choice != usr_choice:
        play = input("Do you want to continue playing? (Y)es or (N)o ").lower()
    
    