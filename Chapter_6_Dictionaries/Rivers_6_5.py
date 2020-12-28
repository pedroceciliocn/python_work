#printing a sentence about each river
rivers = {
	'nile': 'egypt',
	'são francisco': 'brazil',
	'amazonas': 'brazil',
	'yangtze': 'china',
	'mississippi - missouri': 'united states',
}

for river, location in rivers.items():
	print(f"The {river.title()} runs through {location.title()}.")


#printing the name of the rivers
for river in rivers.keys():
	print(river.title())

#printing the name of the countries
for country in rivers.values():
	print(country.title())