# 10/02/2025

from questions import questions # Imports questions from the questions module
import csv  # Import the csv module
import os   # Import the os module


def play_quiz():    # Function to run the entire quiz
    score = 0   # Initialize score as 0

    player_name = input("Enter a user name to start playing: ") # Prompt the player for a user name 
    welcome = input(f"Welcome {player_name}\nPress Enter to start ...\n")   # Greet the player and wait for the player to press Enter to start the quiz

    for question in questions:  # Loop through each question
        print(question["question"]) # Print question
        for choice in question["choices"]:  # Loop through each answer choice and display it to the player
            print(choice)   # Print answer

        while True: # Keep asking for input until the user provides a valid answer (A, B, C, or D)
            user_answer = input("Your answer: ").upper()    # Prompts user for answer
            if user_answer in ["A", "B", "C", "D"]: # Checks if user answer is valid
                break   # Break out of the condition and continue the loop
            else:   # Runs if user entered invalid answer
                print("Invalid option. Please enter A, B, C, or D.")  #   

        if user_answer == question["answer"]:   # Checks if user answer is correct
            print("Correct!")   # Prints Correct if player's answer is correct
            score += 1 # Add 1 to score
        else:   # Runs if user answer is wrong
            print("Wrong!") # Print Wrong if user answer is wrong
        
    print(f"Your score is {score}/{len(questions)}") # Prints user score / total number of questions

    if not os.path.exists("scores.csv"):    # Checks if scores.csv file exists. Code runs if scores.csv does not exist
            with open("scores.csv", "w", newline="") as scores_file:    # Opens scores.csv file in write mode
                writer = csv.writer(scores_file)
                writer.writerow(["Player name", "Score"])   # Writes Player name, Score in scores.csv file

    # Write score to csv file
    with open("scores.csv", "a") as scores_file:    # Opens scores.csv in append mode
        writer = csv.writer(scores_file)
        writer.writerow([player_name, score])   # Appends the player name and score to the scores.csv file


if __name__ == "__main__":
    play_quiz() # Runs the quiz