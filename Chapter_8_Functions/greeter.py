#Defining a function
def greet_user():
	"""Display a simple greeting."""
	print("Hello!")

greet_user()

#Passing information to a function
def greet_user(username):
	"""Display a simple greeting."""
	print(f"Hello, {username.title()}!")

greet_user('jesse')