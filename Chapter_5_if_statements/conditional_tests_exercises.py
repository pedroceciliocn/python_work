#5-1. Conditional Tests:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

color = 'green'
print("\nIs color == 'green'? I predict True.")
print(color == 'green')

print("\nIs color == 'blue'? I predict False.")
print(color == 'blue')

brand = 'errea'
print("\nIs brand == 'errea'? I predict True.")
print(brand == 'errea')

print("\nIs brand == 'macron'? I predict False.")
print(brand == 'macron')

game = 'cyberpunk'
print("\nIs game == 'cyberpunk'? I predict True.")
print(game == 'cyberpunk')

print("\nIs game == 'ac'? I predict False.")
print(game == 'ac')

fruit = 'apple'
print("\nIs fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("\nIs fruit == 'orange'? I predict False.")
print(fruit == 'orange')

#5-2. More Conditional Tests:
string_doida = 'abaporu'
print(string_doida == 'apaboru')
print(string_doida == 'abaporu')

print(string_doida.lower() == 'abaporu')
print(string_doida.lower() == 'ABAPORU')

answer = 42
if answer == 42:
	print("You are correct! Congratulations!")
else:
	if answer != 42:
		if answer < 42:
			print("That is not the correct answer. The correct is bigger. Please try again!")
		else:
			if answer > 42:
				print("That is not the correct answer. The correct is smaller. Please try again!")

##another way:
answer = 50
if answer == 42:
	print("You are correct! Congratulations!")
elif answer != 42:
	if answer < 42:
		print("That is not the correct answer. The correct is bigger. Please try again!")
	elif answer < 42:
		print("That is not the correct answer. The correct is smaller. Please try again!")


answer = 36
if answer == 42:
	print("You are correct! Congratulations!")
else:
	if answer <= 42 or answer >= 42:
		print("That is not the correct answer. Please try again!")


number = 5
if number%2 == 0 and number != 0:
	print("Your number is positive and even.")
else:
	print("Your number is odd and negative or zero.")


times = ['salgueiro', 'serrano', 'cabense', 'petrolina', 'ypiranga', 'central', 'porto', 'vitória', 'araripina', 'afogados', 'serra talhada', 'belo jardim', 'timbaúba', 'itacuruba']
team = "Salgueiro"
if team.lower() in times:
	print(f"The {team.title()} is a team from interior of Pernambuco state.")

team = 'santa'
if team not in times:
	print(f"The {team.title()} is not a team from interior of Pernambuco state.")