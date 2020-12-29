#Favorite Numbers:
favorite_numbers = {
	'pedro': [22, 24], 
	'artur': [47, 74, 95],
	'gabriel': [1],
}

for name, numbers in favorite_numbers.items():
	if len(numbers) == 1:
		print(f"\n{name.title()}'s favorite number is:")
	else:
		print(f"\n{name.title()}'s favorite numbers are:")
	for number in numbers:
		print(f"\t{number}")

