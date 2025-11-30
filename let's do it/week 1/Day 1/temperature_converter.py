"""
Problem 5 — Temperature Converter
Take Celsius
Convert to Fahrenheit
Formula:
F = (C × 9/5) + 32
"""
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit: {:.2f}°F".format(fahrenheit))

