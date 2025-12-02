class InventoryItem:    # Define class that represents an item in inventory
    def __init__(self, name, price, quantity):  # Initialize the item with name, price and quantity
        self.name = name    # Set item name
        self.price = price  # Set item price
        self.quantity = quantity    # Set item quantity
    
    def update_price(self): # Function to update the price of the item
        new_price = float(input("Enter new price: "))   # User inputs new price
        if new_price > 0:   # Checks that the new price greater than zero
            self.price = new_price  # Update self.price with new_price
            return self.price   # Return the new price of the item
        else:   # If new price is negative
            print("Invalid")   # Prints Invalid 

    def update_quantity(self):  # Function to update the quantity of item
        new_quantity = int(input("How many items do you want to add or remove: "))  # User inputs new quantity
        print(f"Updated quantity: {new_quantity}")  # Prints the number of items to add or remove based on user input
        new_quantity = new_quantity + self.quantity # Add or subtract user’s input to current quantity to get new quantity

        if new_quantity >= 0:   # Check that the new quantity is not negative
            self.quantity = new_quantity    # Sets self.quantity to new_quantity
            return self.quantity    # Return the new quantity of item
        else:   # If quantity is negative
            return "Quantity cannot be negative"    # Returns message "Quantity cannot be negative"
    
    # Function to display all info about item
    def __str__(self):
        return f"Item: {self.name}, Price: ${self.price}, Quantity: {self.quantity}"
