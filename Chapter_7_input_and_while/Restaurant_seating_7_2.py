prompt = "Hello sr, be welcome!"
prompt += "\nTell us how many people are in your group, please: "

group = input(prompt)
group = int(group)

if group > 8:
	print("\nWe are sorry, but you will need to wait for a table.")
else:
	print("\nCome in! Your table is ready!")
