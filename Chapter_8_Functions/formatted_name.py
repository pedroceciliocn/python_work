#Returning a simple value
def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#Making an argument optional
##but this way, middle_name will be needed anyway
def get_formatted_name(first_name, middle_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {middle_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

##so we need to make middle_name the last argument, and add a default value with an empty string
def get_formatted_name(first_name, last_name, middle_name = ''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = f"{first_name} {middle_name} {last_name}"
	else:
		full_name = f"{first_name} {last_name}"
	return full_name.title()

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)