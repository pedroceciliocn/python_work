#Checking for special items:
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")


# but if the pizzeria runs out of green peppers?
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
	else:
		print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

#Checking that a list is not empty:
requested_toppings = []

if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

#Using multiple lists:
availabe_toppings = ['mushrooms', 'olives', 'green peppers',
					 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in availabe_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we dont have {requested_topping}.")

print("\nFinished making your pizza!")