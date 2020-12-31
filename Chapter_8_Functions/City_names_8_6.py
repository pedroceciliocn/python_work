def city_country(city_name, country):
	location = f"{city_name}, {country}"
	return location.title()

address = city_country('salgueiro', 'brazil')
print(address)