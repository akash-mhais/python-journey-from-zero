"""
Temperature Message
temp > 40 → Very Hot  
temp > 30 → Hot  
temp > 20 → Warm  
temp < 20 → Cold  
"""

temp = float(input("Enter the temperature in Celsius: "))

if temp > 40:
    print("It's Very Hot.")
elif temp > 30:
    print("It's Hot.")
elif temp > 20:
    print("It's Warm.")
else:
    print("It's Cold.")