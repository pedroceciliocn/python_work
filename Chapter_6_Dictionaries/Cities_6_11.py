cities = {
	'salgueiro': {
		'country': 'brazil',
		'state': 'pernambuco',
		'population': 59_769,
		'fact': 'Known as the "Encruzilhada do Nordeste" because it is located '
		 'in the most central part of the Northeast Region.',
	},

	'petrolina': {
		'country': 'brazil',
		'state': 'pernambuco',
		'population': 217_093,
		'fact': 'Petrolina was founded in 1870. Its region was frequented '
		 'assiduously by the Italian Capuchin friar Henrique, who carried out ' 
		 'intense missionary sermons in the riverside villages of the '
		 'São Francisco River.',
	},

	'verdejante': {
		'country': 'brazil',
		'state': 'pernambuco',
		'population': 9_430 ,
		'fact': 'The Capital of Pega de Boi.',
	}, 
}

for city, city_info in cities.items():
	print(f"\nCity: {city}")
	location = f"{city_info['country'].title()} on {city_info['state'].title()} state."
	population = city_info['population']
	fact = city_info['fact']

	print(f"\tLocation: {location}")
	print(f"\tPopulation: {population}")
	print(f"\tFact: {fact}")

