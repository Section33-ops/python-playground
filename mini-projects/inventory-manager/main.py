# 10/18/2025

from inventory_item import InventoryItem
from inventory_manager import InventoryManager
import json

my_manager = InventoryManager()   # Create an instance of InventoryManager to manage items


def menu(): # Function that displays the main menu to the user
    print("1. Add item \n2. Display items \n3. Update item \n4. Exit")  # Print menu options
    option = input("Choose an option(1,2,3,4): ")   # Ask the user to select an option

    if option == "1":  # If the user chooses 1
        add_item_option()   # Call the function to add an item
    elif option == "2": # # If the user chooses 2
        display_items_option()  # Call the function to display all items
    elif option == "3": # If the user chooses option 3
        update_item_option()    # Call the function to update an item (currently a placeholder)
    elif option == "4": # If the user chooses option 4
        exit_option()   # Call the function to exit the program

def add_item_option(): # Function to add a new item
    my_manager.add_item()   # Calls the add_item() method from InventoryManager to handle input and storage

def display_items_option(): # Function to display all items in the inventory
    my_manager.display_items()  # Calls the dispaly_items() method from InventoryManager to print each item

def update_item_option():   # Function to update an existing item's price or quantity
    my_manager.display_items()  # Displays items in inventory
    item_to_update = input("What item do you want to update? ") # User enters item to be updated
    item = my_manager.find_item(item_to_update) # Checks if item is in inventory
    if item:    # If item is inventory
        print("1. Price \n2. Quantity") # Print update options
        update_option = input("Choose one you want to update: ")    # Ask user for update option
        if update_option == "1":    # If update option is 1
             item.update_price()    # Calls item update_price() method
        elif update_option == "2":  # If update option is 2
            item.update_quantity()  # Calls item update_quantity() method
    else:   # If item is not found
        print("Item not found!")    # Print item not found

def exit_option():  # Function to exit the program
    with open("items.json", "w") as file:
        data_to_save = []
        for item in my_manager.items:
            data_to_save.append({
                "name": item.name,
                "price": item.price,
                "quantity": item.quantity
            })
        json.dump(data_to_save, file)
    exit()  # Terminates the program


# Load items ONCE when the program starts
try:
    with open("items.json", "r") as file:
        loaded_items = json.load(file)
        for item_data in loaded_items:
            item = InventoryItem(item_data["name"], item_data["price"], item_data["quantity"])
            my_manager.items.append(item)
except (FileNotFoundError, json.JSONDecodeError):
    my_manager.items = []

while True: # Infinite loop to keep showing the menu until the user chooses to exit
    menu()  # Calls the menu function on each iteration