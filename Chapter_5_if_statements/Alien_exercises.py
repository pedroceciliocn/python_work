#5-3. Alien Colors #1:
alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points!")
if alien_color == 'yellow' or alien_color == 'red':
	print("You earned 0 points :(")

alien_color = 'red'
if alien_color == 'green':
	print("You just earned 5 points!")

#5-4. Alien Colors #2:
alien_color = 'yellow'
if alien_color == 'green':
	print("You just earned 5 points!")
if alien_color != 'green':
	print("You just earned 10 points!")

alien_color = 'yellow' #take care, because if we put anything here different
#from green (even not a color), else test will pass.
if alien_color == 'green':
	print("You just earned 5 points!")
else:
	print("You just earned 10 points!")

#5-5. Alien Colors #3:
alien_color = 'red'

if alien_color == 'green':
	print("You just earned 5 points!")
elif alien_color == 'yellow':
	print("You just earned 10 points!")
elif alien_color == 'red':
	print("You just earned 15 points!")

alien_color = 'green'

if alien_color == 'green':
	points = 5
elif alien_color == 'yellow':
	points = 10
elif alien_color == 'red':
	points = 15

print(f"You just earned {points} points!")

#5-6. Stages of Life:
age = 26
if age < 2:
	print("That person is a baby.")
elif age < 4:
	print("That person is a toddler.")
elif age < 13:
	print("That person is a kid.")
elif age < 20:
	print("That person is a teenager.")
elif age < 65:
	print("That person is an adult.")
elif age > 65:
	print("That person is an elder.")

#5-7. Favorite Fruit:
favorite_fruits = ['banana', 'mango', 'orange']

if 'banana' in favorite_fruits:
	print("You really like bananas!")
if 'mango' in favorite_fruits:
	print("You really like mangos!")
if 'orange' in favorite_fruits:
	print("You really like oranges!")
if 'kiwi' in favorite_fruits:
	print("You really like kiwis!")
if 'apple' in favorite_fruits:
	print("You really like apples!")