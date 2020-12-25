current_users = ['admin', 'pedro94', 'artur95', 'gabriel97', 'ed12']
lower_current_users = []
for current_user in current_users:
	lower_current_users.append(current_user.lower())

new_users = ['Ed12', 'gabriel97', 'jubileuousado', 'napoleon', 'jaskier']

if new_users:
	for new_user in new_users:
		if new_user.lower() in current_users:
			print(f"Sorry, the username {new_user} already been taked, you need to enter a new one.")
		else:
			print(f"The username {new_user} is available.")
else:
	print("There is no new users!")


#or using comprehension list
#lower_current_users = [current_user.lower() for current_user in current_users]