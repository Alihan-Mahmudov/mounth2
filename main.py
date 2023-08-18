# HW 1

# class Person:
#     def __init__(self, fullname, age, is_married):
#         self.fullname = fullname
#         self.age = age
#         self.is_married = is_married
#
#     def introduce_myself(self):
#         print(f"Full Name: {self.fullname}")
#         print(f"Age: {self.age}")
#         print(f"Marital Status: {'Married' if self.is_married else 'Single'}")
#
#
# class Student(Person):
#     def __init__(self, fullname, age, is_married, marks):
#         super().__init__(fullname, age, is_married)
#         self.marks = marks
#
#     def calculate_average(self):
#         total_marks = sum(self.marks.values())
#         average = total_marks / len(self.marks)
#         return average
#
#
# class Teacher(Person):
#     def __init__(self, fullname, age, is_married, experience, base_salary):
#         super().__init__(fullname, age, is_married)
#         self.experience = experience
#         self.base_salary = base_salary
#
#     def calculate_salary(self):
#         standard_salary = self.base_salary + (self.experience - 3) * 0.05 * self.base_salary
#         return standard_salary
#
#
# def create_students():
#     students = [
#         Student("Max", 18, False, {"Math": 90, "Science": 85, "History": 75}),
#         Student("Maria", 17, False, {"Math": 75, "Science": 80, "History": 95}),
#         Student("Alihan", 16, False, {"Math": 85, "Science": 70, "History": 80})
#     ]
#     return students
#
#
# teacher = Teacher("John Doe", 35, True, 7, 50000)
#
# teacher.introduce_myself()
# print(f"Salary: {teacher.calculate_salary():.2f} som\n")
#
# students = create_students()
#
# for student in students:
#     student.introduce_myself()
#     print("Marks:")
#     for subject, mark in student.marks.items():
#         print(f"{subject}: {mark}")
#     average = student.calculate_average()
#     print(f"Average Mark: {average:.2f}\n")


# HW 2

import random

print(random.randint(0,2))