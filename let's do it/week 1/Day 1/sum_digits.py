#Take a number like "527" → output the sum of digits → 5 + 2 + 7 = 14

num = input("Enter a number: ")
total = 0

for digit in num:
    total += int(digit)

print("Sum of digits:", total)
