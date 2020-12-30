prompt = "\nTell me your age: "
prompt += "\nOr type 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit': #removing 'quit' from the last message
		active = False
	else: 
		message = int(message)
		if message < 3:
			print(f"So you have less than 3 years old? Your ticket is free then.")
		if message >= 3 and message <= 12:
			print(f"So you have more than 2 and less than 12 years old? Your ticket costs $10.")
		if message > 12:
			print(f"So you have more than 12 years old? Your ticket costs $15.")
