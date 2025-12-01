"""
Movie Ticket Pricing
If age <= 12 → 100 Rs  
13–18 → 150 Rs  
>18 → 200 Rs
"""
age = int(input("Enter your age: "))
if age <= 12:
    print("Your ticket price is 100 Rs.")
elif 13 <= age <= 18:
    print("Your ticket price is 150 Rs.")
else:
    print("Your ticket price is 200 Rs.")
    
