# 09/30/2025
# practice: Improve calculator project - add error handling so it doesn't crash when someone enters text insted of numbers

calculator_open= input("Do you want to use the calculator. (Y)es or (N)o: ").lower() 

while calculator_open == "y":
    try:
            
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
    except ValueError:
        print("Invalid Input. Please enter numbers")
    except ZeroDivisionError:
        print("You can't divide by zero")
    finally:
        print("Thanks for using the calculator!")
