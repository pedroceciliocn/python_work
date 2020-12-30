prompt = "\nTell me a topping: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit': #removing 'quit' from the last message
		active = False
	else:
		print(f"Ok, ill add {message.title()} to your pizza.")