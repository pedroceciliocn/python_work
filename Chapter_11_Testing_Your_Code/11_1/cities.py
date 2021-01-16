from city_functions import get_formatted_location

print("Enter 'q' at any time to quit.")
while True:
	city = input("\nPlease give me the city name: ")
	if city == 'q':
		break
	country = input("Please give me the country name: ")
	if country == 'q':
		break

	formatted_location = get_formatted_location(city, country)
	print(f"\tNeatly formatted location: {formatted_location}.")

	