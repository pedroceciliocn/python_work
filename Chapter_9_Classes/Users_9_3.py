#Users:
class User:
	def __init__(self, first_name, last_name, user_age, user_location):
		self.f_name = first_name
		self.l_name = last_name   #try later to unite both names in a same parameter
		self.age = user_age
		self.location = user_location

	def describe_user(self):
		print(f"Name: {self.f_name.title()} {self.l_name.title()}.")
		print(f"Age: {self.age} years old.")
		print(f"Location: {self.location.title()}.")

	def greet_user(self):
		print(f"Hello {self.f_name.title()} {self.l_name.title()} from {self.location.title()}, you're welcome!")


user_0 = User('pedro', 'neto', 26, 'petrolina')
user_1 = User('gabriel', 'cruz', 24, 'petrolina')
user_2 = User('artur', 'cruz', 25, 'recife')

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user() 