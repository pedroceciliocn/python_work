#4-10. Slices:
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("The first three items in the list are:")
for player in players[:3]:
	print(player.title())

print("Three items from the middle of the list are:")
for player in players[1:4]:
	print(player.title())

#or
print("Three items from the middle of the list are:")
for player in players[1:-1]:
	print(player.title())


print("The last three items in the list are:")
for player in players[-3:]:
	print(player.title())





#4-11. My Pizzas, Your Pizzas:
pizzas = ['calabresa', '4 queijos', 'bacon']
#for pizza in pizzas:
#	print(pizza.title())


#for pizza in pizzas:
#	print(f"I like {pizza.title()} pizza.\n")


#for pizza in pizzas:
#	print(f"I like {pizza.title()} pizza.\n")
	
#print("I really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('marguerita')

friend_pizzas.append('portuguesa')

print("\nMy favorite pizzas are:")
for pizza in pizzas[:]:
	print(pizza.title())

print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas[:]:
	print(friend_pizza.title())


#4-12: More loops:
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nMy favorite foods are:")
for my_food in my_foods[:]:
	print(my_food.title())

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods[:]:
	print(friend_food.title())