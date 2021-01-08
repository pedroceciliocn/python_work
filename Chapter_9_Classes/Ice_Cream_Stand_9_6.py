#Ice Cream Stand:
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

class IceCreamStand(Restaurant):
	""" ."""
	def __init__(self, restaurant_name, cuisine_type):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an ice cream stand.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ['chocolate', 'vanilla', 'manga', 'lemon', 'flakes']

	def list_icecream_flavors(self):
		#print(f"The flavors of ice cream available are: {self.flavors}")
		print("The flavors of ice cream available are: ")
		for flavor in self.flavors:
			print(flavor.title())



##barraca_sorvete = IceCreamStand('Zecas', 'Sorveteria') #check 9-10
#restaurant.set_number_served(20)
#restaurant.increment_number_served(10)
#print(restaurant.number_served)
##barraca_sorvete.list_icecream_flavors() #check 9-10