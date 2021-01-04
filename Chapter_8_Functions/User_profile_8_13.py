#Using abitrary keyword arguments
def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('pedro', 'neto',
							location='petrolina',
							field='cs & ds',
							favorite_team='vasco da gama')
print(user_profile)

#you will often see the parameter name **kwargs doing this job