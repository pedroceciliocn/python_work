print("Give me two numbers, and I'll add them.")
first_number = input(f"\nFirst number: ")
second_number = input("Second number: ")

try:
	print(int(first_number) + int(second_number))
except ValueError:
	print("You can't add texts!")