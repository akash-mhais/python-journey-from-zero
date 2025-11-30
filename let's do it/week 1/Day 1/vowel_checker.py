#Check if character is vowel or consonant.

ch = input("Enter a letter: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")


# .lower() converts to lowercase
# "aeiou" contains all vowels
# in checks membership
