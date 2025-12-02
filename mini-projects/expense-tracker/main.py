# 10/27/2025

import json

expenses = []

def add_expense_option():
    item = input("What did you buy? ")
    item_price = float(input("How much did it cost? "))
    item_quantity = int(input("How many did you buy? "))
    total_cost = item_price * item_quantity
    item_expense = (item, item_price, item_quantity, total_cost)
    expenses.append(item_expense)

def view_expenses_option():
    for expense in expenses:
        print(f"Item: {expense[0]}, Price: {expense[1]}, Quantity: {expense[2]}, Total cost: {expense[3]:.2f}")

def view_total_option():
    total = 0
    if not expenses:
        print("No expenses yet.")
        return
    else:
        for expense in expenses:
            total += expense[3]
    print(f"Total spent so far is ${total:.2f}")
    
def exit_option():
    with open("expenses.json", "w") as file:
        data_to_save = []
        for expense in expenses:
            data_to_save.append({
                "item": expense[0],
                "price": expense[1],
                "quantity": expense[2],
                "total cost": expense[3]
            })
        json.dump(data_to_save, file)
    exit()

def menu():
    print("Welcome to the Expense Tracker! \n1. Add expense \n2. View expenses \n3. View total \n4. Exit")
    option = input("Choose an option: ")

    if option == "1":
        add_expense_option()
    elif option == "2":
        view_expenses_option()
    elif option == "3":
        view_total_option()
    elif option == "4":
        exit_option()
    else:
        print("You must enter a number for the option")

try:
    with open("expenses.json", "r") as file:
        loaded_expenses = json.load(file)
        for expense_data in loaded_expenses:
            expense = expenses(expense_data[0], expense_data[1], expense_data[2], expense_data[3])
            expenses.append(expense)
except FileNotFoundError:
    expenses = []

while True:
    menu()
    