"""
Number Range Checker
0–50 → Low  
51–100 → Medium  
>100 → High  
"""

num = float(input("Enter a number: "))

if 0 <= num <= 50:
    print("Low")
elif 51 <= num <= 100:
    print("Medium")
else:
    print("High")