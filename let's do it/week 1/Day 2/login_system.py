"""
Simple Login System
username == "admin"  
password == "1234"
"""
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Login failed. Invalid username or password.")