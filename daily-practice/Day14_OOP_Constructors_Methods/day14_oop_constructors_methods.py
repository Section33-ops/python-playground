# 09/23/2025
# Practice: Create a Car class with make, model, and year
#           Add a method drive() that prints “The car is driving.”

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def drive(self):
        print(f"{self.make} {self.model} is driving.")

car1 = Car("Honda", "Accord", "2015") 
car1.drive()