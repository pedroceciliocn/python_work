from User import User

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