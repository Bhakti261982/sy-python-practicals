print("=========Montly expensive=========")
expenses=0.0
while True:
    value=float(input("Enter your amount :"))
    if value == -1:
        break
    expenses =expenses+value
    print("Total expenese :",expenses)
