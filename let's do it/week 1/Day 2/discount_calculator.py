"""
Shop Discount
amount > 500 → 10% discount  
amount > 1000 → 20% discount
"""

amount = float(input("Enter the total amount: "))

if amount > 1000:
    discount = amount * 0.20
    final_amount = amount - discount
    print(f"You get a 20% discount. Final amount to pay: {final_amount}")
elif amount > 500:
    discount = amount * 0.10
    final_amount = amount - discount
    print(f"You get a 10% discount. Final amount to pay: {final_amount}")   