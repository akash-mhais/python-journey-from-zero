"""
Check Character Type
Input a single character:
vowel
consonant
digit
special character
"""

char = input("Enter a single character: ")

if char.isalpha():
    if char.lower() in 'aeiou':
        print(f"{char} is a Vowel.")
    else:
        print(f"{char} is a Consonant.")
elif char.isdigit():
    print(f"{char} is a Digit.")
else:
    print(f"{char} is a Special Character.")
