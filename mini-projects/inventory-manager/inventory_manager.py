import inventory_item

class InventoryManager: # Define class that manages items in inventory
    def __init__(self,  items=None): # Initialize with a list of items
        if items is None:   # If there is no item list
            self.items = [] # Start with an empty list
        else:   # Else
            self.items = items  # Use existing list

    def add_item(self): # Function to add item to item list
        item_name = input("What is the name of the item? ") # Ask user for item name
        item_price = float(input("What is the price of the item? "))   # Ask user for item price
        item_quantity = int(input("What is the quantity of the item? ")) # Ask user for item quantity
        item = inventory_item.InventoryItem(item_name, item_price, item_quantity)   # Create an inventory item with name, price and quantity
        self.items.append(item) # Append the item to the items list
        print(f"{item.name} added successfully!")    # Prints item was added successfully
    
    def display_items(self):    # Function to display items
        if not self.items:  # If item list is empty
            print("No items in inventory yet.") # Prints No items in inventory yet.
        else:   # Else
            for item in self.items: # Loop through each item in the item list
                print(item) # Print item
    
    def find_item(self, item_name): # Function to find an item in the inventory by name
        for item in self.items:  # Loop through each InventoryItem in the list
            if item.name.lower() == item_name.lower():  # Compare names
                return item  # Return the found item object
        return None  # If not found, return None