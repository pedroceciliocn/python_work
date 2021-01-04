#Cities:
def describe_city(city_name, country='brazil'):
	print(f"{city_name.title()} is in {country.title()}.")

describe_city('salgueiro')
describe_city('verdejante')
describe_city('leipzig', 'germany')