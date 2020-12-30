#Using conditional test
prompt = "\nTell me a topping: "
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)
	if message != 'quit':
		print(f"Ok, ill add {message.title()} to your pizza.")