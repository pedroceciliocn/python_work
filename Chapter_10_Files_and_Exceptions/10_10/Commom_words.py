def count_common_words(filename):
	"""Count the approximate number of words in a file."""
	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		print(f"Sorry, the file {filename} does not exist.")
	else:
		words = contents#.split()
		num_comm_words = words.count('the ')
		print(f"The file {filename} has about {num_comm_words} 'the' words.")

filenames = ['Les Misérables.txt', 'Leviathan.txt', 'On Liberty.txt', 'The History of Don Quixote.txt', 'the_little_prince.txt']
for filename in filenames:
	count_common_words(filename)