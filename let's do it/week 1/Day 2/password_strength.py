"""
Password Strength
If length < 6 → weak  
6–10 → medium  
>10 → strong  
"""
password = input("Enter your password: ")
length = len(password)

if length < 6:
    print("Your password is weak.")
elif 6 <= length <= 10:
    print("Your password is medium.")
else:
    print("Your password is strong.")