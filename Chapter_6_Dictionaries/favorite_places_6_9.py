favorite_places = {
	'jen': ['dagobah', 'tatooine', 'vegetta'],
	'sarah': ['brazil'],
	'edward': ['rancho', 'namekusei'],
}

for name, places in favorite_places.items():
	if len(places) == 1:
		print(f"\n{name.title()}'s favorite place is:")
	else:
		print(f"\n{name.title()}'s favorite places are:")
	for place in places:
		print(f"\t{place.title()}")