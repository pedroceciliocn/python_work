prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city == 'quit': #removing 'quit' from the last message
		break
	else:
		print(f"I'd love to go to {city.title()}!")