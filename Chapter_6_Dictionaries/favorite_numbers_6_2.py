#Favorite Numbers:
favorite_numbers = {
	'pedro': 22,
	'artur': 47,
	'gabriel': 1,
}

number = favorite_numbers['pedro']
print(f"Pedros's favorite number is {number}.")

number = favorite_numbers['artur']
print(f"Artur's favorite number is {number}.")

number = favorite_numbers['gabriel']
print(f"Gabriel's favorite number is {number}.")

#using for loop through all key-value pairs:
for name, number in favorite_numbers.items():
	print(f"{name.title()}'s favorite number is {number}.")
