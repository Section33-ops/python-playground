# 09/18/2025
# Practice: Build a Calculator (add, subtract, multiply, divide)
calculator_open= input("Do you want to use the calculator. (Y)es or (N)o: ").lower() 

while calculator_open == "y":
    
    first_num = float(input("Enter the first number: " ))
    operator = input("Enter the math operator.(+ - * /): ")
    second_num = float(input("Enter the second number: " ))

    if operator == "+":
        result = first_num + second_num
        print(f"{first_num} {operator} {second_num} = {result}")
    elif operator == "-":
        result = first_num - second_num
        print(f"{first_num} {operator} {second_num} = {result}")
    elif operator == "*":
        result = first_num * second_num
        print(f"{first_num} {operator} {second_num} = {result}")
    elif operator == "/":
        result = first_num / second_num
        print(f"{first_num} {operator} {second_num} = {result}")
    else:
        print("Invalid operator. Please use +, -, *, or /")

    calculator_open= input("Do you want to use the calculator. (Y)es or (N)o: ").lower() 
