# 09/14/2025
# If Statements Exercise
# Write a weight convertor program
# It asks the user for weight
# Then it asks them (K)g or (L)bs
# Then it converts it to the other weight

weight = input("Input weight to be converted: ")
unit = input("Input weight unit.(K)g or (L)bs: ")

if unit.lower() == 'k':
    converted_weight = float(weight) * 2.205
    print(f"{weight} kg is {converted_weight} lbs")
elif unit.lower() == 'l':
    converted_weight = float(weight) * 0.453
    print(f"{weight} lbs is {converted_weight} kg")
else:
    print("Invalid unit. Enter 'k' for kg and 'l' for lbs")