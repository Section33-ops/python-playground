# 10/01/2025
# Appending to a text file
file = open("notes.txt", "a",)
file.write("This is my first note!\n")
file.close()

# Reading a text file
file = open("notes.txt", "r",)
print(file.read())
file.close()

# Using with() statement to read a file
with open("notes2.txt", "r") as file:
    print(file.read())

# Using with() statement to append to a file
with open("notes2.txt", "a") as file:
    file.write("\nLearning Python is fun!")