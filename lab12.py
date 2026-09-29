
location = (18.5204, 73.8567)

print("GPS Location:", location)


print("Latitude:", location[0])
print("Longitude:", location[1])

print("Number of coordinates:", len(location))

print("Last coordinate:", location[-1])

print("Is latitude 18.5204 present?", 18.5204 in location)


print("Coordinates using slicing:", location[0:2])

extra = ("Pune",)
new_location = location + extra

print("Location with city:", new_location)

print("Repeated coordinates:", location * 2)