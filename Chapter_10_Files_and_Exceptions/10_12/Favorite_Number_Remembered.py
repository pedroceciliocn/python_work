import json

filename = 'favnumber.json'

try:
	with open(filename) as f:
		fav_number = json.load(f)
except FileNotFoundError:
	fav_number = input("What is your favorite number? ")
	with open(filename, 'w') as f:
		json.dump(fav_number, f)
else:
	print(f"I already know your favorite number! It's {fav_number}.")









