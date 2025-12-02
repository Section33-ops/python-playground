# 09/26/2025
# Practice: Make a Person class with name and age
# Create a Student class that inherits from Person and adds grade
# Test it with multiple students

# Person class
class Person:    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
    
# Student class inheriting from Person class
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Test with multiple students
student1 = Student("Alice Smith", 16, 10)
student2 = Student("Bob Johnson", 17, 11)
student3 = Student("Charlie Brown", 15, 9)

print(student1)
print(student2)
print(student3)

print(f"{student1.name} is in grade {student1.grade}.")
print(f"{student2.name}'s age is {student2.age}.")