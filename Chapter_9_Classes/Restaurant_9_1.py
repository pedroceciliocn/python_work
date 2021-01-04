#Restaurant
class Restaurant:
	"""A simple attempt to model a restaurant."""
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name}.")
		print(f"The cuisine type is {self.type}.")

	def open_restaurant(self):
		print(f"The {self.name} restaurant is now open.")

restaurant = Restaurant('Bode Assado das Gêmeas', 'Bode Assado')

print(restaurant.name)
print(restaurant.type)

restaurant.open_restaurant()
