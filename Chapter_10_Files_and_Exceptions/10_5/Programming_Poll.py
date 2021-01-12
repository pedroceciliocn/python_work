filename = 'poll.txt'
flag = True

with open(filename, 'a') as file_object:
	while flag == True:
		response = input("Why you like programming? ")
		if response == 'exit':
			flag = False
		else:
			file_object.write(f"{response}\n")
		