total_bill = float(input("Enter your total bill: "))
partial_amount = float(input("Enter the amount that has already been paid: "))
def find_due_cost(total_bill, partial_amount):
    due_cost = total_bill - partial_amount
    return due_cost
due_cost = find_due_cost(total_bill, partial_amount)
if due_cost < 0:
    print("Invalid input.")
elif due_cost == 0:
    print("You have no due amount! ")
else:
    print(f"Your due cost is: {due_cost}")
    