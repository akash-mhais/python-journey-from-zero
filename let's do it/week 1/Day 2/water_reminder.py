"""
Water Reminder -
If drink < 3 liters → "Drink more water"
"""
drink = float(input("Enter amount of water you drank today (in liters): "))

if drink < 3:
    print("Drink more water.")  
else:
    print("You have drunk enough water today.")