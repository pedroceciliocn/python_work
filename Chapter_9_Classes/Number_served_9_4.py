#Number Served:
class Restaurant:
	"""A simple attempt to model a restaurant."""
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name}.")
		print(f"The cuisine type is {self.type}.")

	def open_restaurant(self):
		print(f"The {self.name} restaurant is now open.")

restaurant = Restaurant('Bode Assado das Gêmeas', 'Bode Assado')

print(restaurant.name)
print(restaurant.type)
print(restaurant.number_served)

restaurant.open_restaurant()

restaurant.number_served = 5
print(restaurant.number_served)


#adding a method called set_number_served():
class Restaurant:
	"""A simple attempt to model a restaurant."""
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name}.")
		print(f"The cuisine type is {self.type}.")

	def open_restaurant(self):
		print(f"The {self.name} restaurant is now open.")

	def set_number_served(self, served):
		self.number_served = served


restaurant = Restaurant('Bode Assado das Gêmeas', 'Bode Assado')
restaurant.set_number_served(10)
print(restaurant.number_served)

#adding a method called increment_number_served():
class Restaurant:
	"""A simple attempt to model a restaurant."""
	def __init__(self, restaurant_name, cuisine_type):
		self.name = restaurant_name
		self.type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"The restaurant is called {self.name}.")
		print(f"The cuisine type is {self.type}.")

	def open_restaurant(self):
		print(f"The {self.name} restaurant is now open.")

	def set_number_served(self, served):
		self.number_served = served

	def increment_number_served(self, atm_served):
		self.number_served += atm_served


restaurant = Restaurant('Bode Assado das Gêmeas', 'Bode Assado')
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
print(restaurant.number_served)