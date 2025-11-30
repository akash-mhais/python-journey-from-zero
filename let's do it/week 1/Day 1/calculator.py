"""
Problem 1 — Simple Calculator
Take 2 numbers from user
Print:
1. sum
2. difference
3. product
4. division
5. remainder
"""
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
# Sum
print("Sum is :", num1 + num2)
# Difference
print("Difference is: ", num1 - num2)
# Product
print("Product is: ", num1 * num2)
# Division
if num2 != 0:
    print("Division is: ", num1 / num2)
else:
    print("Division is: Undefined (cannot divide by zero)")
# Remainder
if num2 != 0:
    print("Remainder is: ", num1 % num2)    
else:
    print("Remainder is: Undefined (cannot divide by zero)")
