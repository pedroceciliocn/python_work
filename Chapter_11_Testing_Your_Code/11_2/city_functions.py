def get_formatted_location(city, country, population=''):
	"""Generate a neatly formatted city name with its country."""
#	population = int(population)
	if population:
		location = f"{city}, {country} - population {population}"
	else:
		location = f"{city}, {country}"		
	return location.title()


