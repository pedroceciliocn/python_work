def show_names(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		print(contents)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
	show_names(filename)