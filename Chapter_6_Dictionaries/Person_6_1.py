#Person:
person = {
	'first_name': 'pedro',
	'last_name': 'neto',
	'age': 26,
	'city': 'petrolina',
}

name = person['first_name'].title() + person['last_name'].title()

#print(f"His name is {person['first_name'].title()} {person['last_name'].title()}.")
print(f"His name is {name}.")
print(f"He has {person['age']} years old.")
print(f"And lives in {person['city'].title()}.")