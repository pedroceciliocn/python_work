#Sorting list permanently with sort():
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

##reverse order:
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

#sorting a list temporarily with sorted():
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the reverse sorted list:")
print(sorted(cars, reverse = True))

print("\nHere is the original list again:")
print(cars)

#printing a list in reverse order (like chronological):
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars) #reverse() changes the order permanently, but you can revert to the
#original by using reverse() again.

#finding the lenght of a list:
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars)) #Why not working???? (its working ok on terminal), seems like
#we need print()

#3-8. Seeing the World:
locations = ['Paris', 'Berlin', 'Prague', 'Toronto', 'Sidney']
print(locations)

print(f"Sorted locations: {sorted(locations)}.") #tempo reverse.
print(f"Orignal order locations: {locations}.") #original list stills the same.

print(f"Reverse sorted locations: {sorted(locations, reverse = True)}.") #tempo
#reverse.
print(f"Orignal order locations: {locations}.") #orignal list stills the same.

locations.reverse() #reverting perma.
print(f"'Chronological' Reversed order locations: {locations}.") #chronological 
#perma reversed.

locations.reverse() #reverting perma back to the original order.
print(f"'Chronological' Reversed again to the original order locations: {locations}.")

locations.sort()
print(f"Sorted locations: {locations}.")

locations.sort(reverse = True)
print(f"Reverse Sorted locations: {locations}.")

#3-9. Dinner Guests:
guest_list = ['akira toryiama', 'david bowie', 'diego maradona']
print(f"The number of invited people is {len(guest_list)}.")

#3-10. Every Function:
languages = ['R', 'Python', 'C', "C++", "Java", "Java Script", "CSS", "HTML"]
print(languages)
print(languages[0])
print(languages[-2])

message = f"My most used language until now is {languages[0]}."
print(message)

languages[7] = 'prolog'
print(languages)

languages.append('HTML')
print(languages)

languages.insert(4, 'C#')
print(languages)

del languages[4]
print(languages)

popped_languages = languages.pop()
print(languages)
print(popped_languages)

last_added = languages.pop()
print(f"The last language that ive learned was {last_added.title()}.")

languages.remove('C++')
print(languages)

hardest = 'C'
languages.remove(hardest)
print(languages)
print(f"\n{hardest} was the hardest language that i have contacted in the past.")

languages.sort()
print(languages)

languages.sort(reverse = True)
print(languages)

print(sorted(languages))

languages.reverse()
print(languages)
print(len(languages))




