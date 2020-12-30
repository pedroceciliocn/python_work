#Using conditional test
prompt = "\nTell me a topping: "
prompt += "\nEnter 'quit' to end the program. "

while True:
	message = input(prompt)
	if message == 'quit': #removing 'quit' from the last message
		break
	if message != 'quit':
		print(f"Ok, ill add {message.title()} to your pizza.")

