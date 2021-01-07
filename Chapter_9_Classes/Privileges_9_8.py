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

class Privileges:
	def __init__(self):
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		print("The admin privileges are: ")
		for privilege in self.privileges:
			print(privilege)


class Admin(User):
	def __init__(self, first_name, last_name, user_age, user_location):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an admin user.
		"""
		super().__init__(first_name, last_name, user_age, user_location)
		self.privileges = Privileges()


adm = Admin('edward', 'elwric', 8, 'petrolina')

adm.privileges.show_privileges()