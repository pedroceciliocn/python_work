dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#trying to change item in the tuple
#dimensions[0] = 250 #doesnt work

#looping through all values in a tuple:
dimensions = (200, 50)
for dimension in dimensions:
	print(dimension)

#writing over a tuple:
dimensions = (200, 50)
print("original dimentions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)