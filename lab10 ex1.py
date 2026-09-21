assets = []

n = int(input("Enter number of assets: "))

for i in range(n):
    cost = float(input(f"Enter cost of asset {i + 1}: "))
    assets.append(cost)

print("\nAsset Costs:")
print(assets)


assets.sort(reverse=True)

print("\nAssets from Highest to Lowest:")
print(assets)


print("\nTop 3 Priciest Assets:")

for i in range(min(3, len(assets))):
    print(f"{i + 1}. ₹{assets[i]:.2f}")