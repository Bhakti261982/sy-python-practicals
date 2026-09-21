products = [
    "Laptop",
    "Mobile",
    "Keyboard",
    "Mouse",
    "Headphones",
    "Printer"
]

print("========== INVENTORY CATALOG ==========")

print("Available Products:")
for i, product in enumerate(products):
    print(i, "-", product)

item = input("\nEnter item name to search: ")

found = False

for index in range(len(products)):
    if products[index].lower() == item.lower():
        print("\nItem found!")
        print("Product:", products[index])
        print("Index:", index)
        found = True
        break

if not found:
    print("\nItem not found in the inventory.")