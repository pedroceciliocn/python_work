filename = 'guest.txt'
flag = True

with open(filename, 'a') as file_object:
	while flag == True:
		name = input("Tell me your name: ")
		if name == 'exit':
			flag = False
		else:
			file_object.write(f"{name}\n")
			print(f"Hi {name}! Your name has been added to the guest book.\n")
		

