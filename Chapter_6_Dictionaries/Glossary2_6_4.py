#Glossary 2:
glossary = {
	'dictionary': 'a glossary',
	'list': 'a bunch of words or data about something',
	'loop': 'something repeating over and over again',
	'if': 'i had a heart',
}

#using for loop through all key-value pairs:
for word, meaning in glossary.items():
	print(f"{word.title()}: {meaning}.")