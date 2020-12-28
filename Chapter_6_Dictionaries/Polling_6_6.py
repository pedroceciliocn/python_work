#Polling:
#A dictionary of similar objects
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

friends = ['jen', 'alex', 'hayley', 'edward', 'phil', 'cam', 'sarah']

for friend in friends:
	if friend in favorite_languages.keys():
		print(f"Thank you {friend.title()}!")
	else:
		print(f"{friend.title()}, please take our poll!")
