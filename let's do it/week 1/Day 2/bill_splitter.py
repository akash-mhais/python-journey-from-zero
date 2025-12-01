"""
Project: Bill Splitter

You will build a program that splits a restaurant bill among friends.

✔ Inputs:

Total bill amount
Number of friends
Tip percentage

✔ Output:
Total Amount: 1500
Tip (10%): 150
Grand Total: 1650
Each Friend Pays: 330

✔ Code Structure:
bill = float(input("Enter total bill: "))
friends = int(input("Enter number of friends: "))
tip_percent = float(input("Enter tip percentage: "))

tip = (bill * tip_percent) / 100
grand_total = bill + tip
each = grand_total / friends

print(f"Each friend should pay: {each}")

"""

bill = float(input("Enter total bill: "))
friends = int(input("Enter number of friends: "))
tip_percent = float(input("Enter tip percentage: "))

tip = (bill * tip_percent) / 100
grand_total = bill + tip
each = grand_total / friends

print(f"Total Amount: {bill}")
print(f"Tip ({tip_percent}%): {tip}")
print(f"Grand Total: {grand_total}")
print(f"Each Friend Pays: {each}")
