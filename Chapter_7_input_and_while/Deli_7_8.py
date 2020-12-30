sandwich_orders = ['americano', 'hamburguer', 'natural', 'misto', 'hot dog']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(f"I made your {current_sandwich.title()} sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche.title())
