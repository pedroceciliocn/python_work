def get_formatted_location(city, country):
	"""Generate a neatly formatted city name with its country."""
	location = f"{city}, {country}"
	return location.title()
