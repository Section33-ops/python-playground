# 10/02/2025
import csv

# Writing to csv files
with open("friends.csv", "w", newline="") as file:
    writer = csv.writer(file)
    
    writer.writerow(["name", "color"]) # Header
    """
    writer.writerow(["Paul", "Red"])    # One row of data
    """

    friends = [["Paul", "Red"], ["John", "Blue"], ["Mary", "Green"]]
    
    # firends = [writer.writerow([friend[0], friend[1]]) for friend in friends]
    for friend in friends:
        writer.writerow(friend)
    

# Reading csv files
with open("friends.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)    # Skips the header row
    for row in reader:
        print(f"{row[0]} favorite color is {row[1]}")
        
        



