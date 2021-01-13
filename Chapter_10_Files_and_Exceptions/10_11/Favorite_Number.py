import json

filename = 'favnumber.json'

fav_number = input("What is your favorite number? ")
with open(filename, 'w') as f:
	json.dump(fav_number, f)