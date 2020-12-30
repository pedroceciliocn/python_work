sandwich_orders = ['americano', 'pastrami', 'pastrami', 'hamburguer', 'natural', 'misto', 'hot dog', 'pastrami']
finished_sandwiches = []
print("Sorry but we have no Pastrami sandwiches at the time.")
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print(f"I made your {current_sandwich.title()} sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for finished_sandwiche in finished_sandwiches:
	print(finished_sandwiche.title())
