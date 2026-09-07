total = 0
count = 0

while True:
    expense = float(input("Enter daily expense: "))

    if expense == 0:
        break

    total = total + expense
    count = count + 1

print("\nMonthly Expense Summary")
print("Total Expenditure =", total)
print("Number of Expenses =", count)
