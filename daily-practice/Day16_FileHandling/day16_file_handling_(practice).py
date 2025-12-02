# 09/27/2025
# Practice: Write a program thats asks the user for their names & saves it to names.txt
#           Then read and display all names stored in the file

usr_name = input("What is your name? ")

with open("names.txt", "a") as name_file:
    name_file.write(f"{usr_name}\n")

with open("names.txt") as name_file:
    print(name_file.read())