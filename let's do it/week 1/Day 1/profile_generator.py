#Create a small profile summary + write to a file.

name = input("Enter name: ")
age = input("Enter age: ")
city = input("Enter city: ")
hobby = input("Enter hobby: ")
fav_lang = input("Enter favourite language: ")

profile = f"""
------ USER PROFILE ------
Name: {name}
Age: {age}
City: {city}
Hobby: {hobby}
Favourite Language: {fav_lang}
--------------------------
"""

print(profile)

with open("output.txt", "w") as file:
    file.write(profile)
print("Profile saved to output.txt")


"""
Take user details
Use f-string for clean formatting
with open("output.txt", "w")
"w" = write mode
Saves text into file
The output is also printed on screen
"""