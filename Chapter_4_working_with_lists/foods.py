my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

#OBS
#note that we need to copy using slice or both variables will point to the same
#list
my_foods = ['pizza', 'falafel', 'carrot cake']

#this doesnt work:
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print(f"My fav foods now are:\n{my_foods}.")
print(f"\nMy friends fav foods now are:\n{friend_foods}.")

print("Now they are the same!")