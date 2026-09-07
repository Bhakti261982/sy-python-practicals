food = 0
travel = 0
shopping = 0

food = float(input("Enter Food expense: "))
travel = float(input("Enter Travel expense: "))
shopping = float(input("Enter Shopping expense: "))

total = food + travel + shopping

print("\nMONTHLY EXPENSE SUMMARY")
print("------------------------")
print("Food     :", food)
print("Travel   :", travel)
print("Shopping :", shopping)
print("------------------------")
print("Total    :", total)
