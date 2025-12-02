# 09/17/2025
# Practice: Create a student class with name and age

class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def about_student(self):
        print(f"Student Name: {self.name} Student Age: {self.age}")


student1 = Student("John", 15)
student2 = Student("Paul", 16)

student1.about_student()
student2.about_student()