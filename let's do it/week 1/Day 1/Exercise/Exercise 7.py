"""
Problem 4 — Percentage Calculator
Input:
total marks
obtained marks
Print percentage up to 2 decimals.
"""
total_marks = float(input("Enter total marks: "))
obtained_marks = float(input("Enter obtained marks: "))
if total_marks != 0:
    percentage = (obtained_marks / total_marks) * 100
    print("Percentage: {:.2f}%".format(percentage))
else:
    print("Total marks cannot be zero.")
