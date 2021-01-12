filename = 'guest.txt'

with open(filename, 'w') as file_object:
	name = input("Tell me your name: ")
	if name:
		file_object.write(name)
