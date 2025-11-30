"""
Problem 3 — Age Calculator
Ask user:
name
birth year
"""
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))
current_year = 2025
age = current_year - birth_year
print("Hello", name + " you are", age, "years old.")
