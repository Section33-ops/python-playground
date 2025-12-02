# 09/21/2025
import os   # Import the os module
import csv  # Import the csv module

tasks = []

def save_tasks(task):   # Function to save tasks to tasks.csv
    with open("tasks.csv", "w", newline="")as tasks_file:   # Open file for appending
        writer = csv.writer(tasks_file)
        writer.writerow([task])
    pass

def load_tasks():
    # Load tasks from tasks.csv only when the program starts or when the user requests to view tasks.
    if os.path.exists("tasks.csv"):  # Check if the file exists first
        with open("tasks.csv", "r", newline="") as tasks_file:
            reader = csv.reader(tasks_file)
            return [row[0] for row in reader]  # Return tasks as a list of strings
    return []  # Return empty list if no tasks exist yet

def delete_tasks(delete_task):  # Function to remove tasks
    if delete_task in tasks:    # Checks if the task the user wants to delete is an existing task
        tasks.remove(delete_task)   # Remove task from the tasks list
        print(f"Removed: {delete_task}")    # Print Removed: task
        save_tasks(tasks)   # Save the remaining tasks to the tasks file
    else:   # If the task the user wants to delete does not exist
        print("Task not found!")    # Print "Task not found!"

print("Welcome!")   # Print "Welcome!"

tasks = load_tasks()    # Loads tasks from file

while True: # While True
    os.system('cls' if os.name == 'nt' else 'clear')    # Refreshes the terminal after evry action

    menu = input("To-do List Menu: \n1. Add task \n2. Remove task \n3. View tasks \n4. Quit \nChoose: ")    # Prints options to user and prompts them to choose

    if menu == "1": # If user entered option "1"
        add_task = input("Add task: ")  # Ask user for task to add
        tasks.append(add_task)  # Append user's task to tasks list
        save_tasks(add_task)    # Save user's task to tasks.csv
        
    elif menu == "2":   # If user entered option "2"
        remove_task = input("Remove task: ")    # Ask user for task to remove
        delete_tasks(remove_task)   # Remove task from tasks.csv
        
    elif menu == "3":   # If user entered option "3"
        if tasks:   # If there are tasks
            print("Your tasks: ")   # Print "Your tasks: "
            for task in tasks:  # Loop through each task in tasks list
                print(f"- {task}")  # Print each task
        else:   # If there no tasks
            print("No tasks yet!")  # Print "No tasks yet!"
        
    elif menu == "4":   # If user entered option "4"
        print("Goodbye!")   # Print "Goodbye!"
        break   # Break out of the loop which exists the program
        
    
    else:   # If user entered wrong option
        print("Invalid option!")    # Print "Invalid option!"
    
    input("\nPress Enter to continue...")   # Asks user to press ENTER to continue. This is used to paused the loop
                                            # so the user has time to read the current terminal before it is cleared