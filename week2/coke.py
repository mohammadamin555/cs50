amount_due = 0.50

while amount_due > 0.00:
    user = float(input("insert a coin: "))
    if user in [0.25 , 0.10 , 0.05]:
        amount_due = amount_due - user
        print(f"amount_due {amount_due:.2f}\n")
print(f"Change owed: {abs(amount_due)}")