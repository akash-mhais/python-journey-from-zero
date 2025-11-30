"""
Convert minutes → hours & minutes
Example: 150 minutes = 2 hours 30 minutes
"""

minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining = minutes % 60

print(f"{hours} hour(s) {remaining} minute(s)")

# // → floor division → gives hours
# % → remainder → leftover minutes