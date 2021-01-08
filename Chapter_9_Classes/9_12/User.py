#Privileges:
class User:
	def __init__(self, first_name, last_name, user_age, user_location):
		self.f_name = first_name
		self.l_name = last_name   #try later to unite both names in a same parameter
		self.age = user_age
		self.location = user_location
		self.login_attempts = 0

	def describe_user(self):
		print(f"Name: {self.f_name.title()} {self.l_name.title()}.")
		print(f"Age: {self.age} years old.")
		print(f"Location: {self.location.title()}.")

	def greet_user(self):
		print(f"Hello {self.f_name.title()} {self.l_name.title()} from {self.location.title()}, you're welcome!")

	def increment_login_attempts(self):
		self.login_attempts = self.login_attempts + 1

	def reset_login_attempts(self):
		self.login_attempts = 0

