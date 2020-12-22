#creating a List with motorcycles brands
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#modifying elements in a List
motorcycles[0] = 'ducati'
print(motorcycles)

#adding elements to the end of a List
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

#starting with an empty List then appending items 1 by 1
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#inserting elements in a List
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati') #seems like r functions
print(motorcycles)

#removing elements from a List using del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#removing elements from a List using pop() Method that removes the last item from a List but you
# can still use its data, that comes off to another variable
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#we can use that Method to show a output with something like "what the last motorcycle that i bought?"
motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#popping items from any position in a List
motorcycles = ['honda', 'yamaha', 'suzuki']

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#Revoming a Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

##printing a reason for removing 'ducati' from the List
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")




