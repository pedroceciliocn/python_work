#Returning a dictionary
def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

#storing a person age as well
def build_person(first_name, last_name, age = None):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)