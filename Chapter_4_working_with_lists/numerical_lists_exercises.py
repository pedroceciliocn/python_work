#4-3. Counting to Twenty:
for number in range(1, 21):
	print(number)


#4-4. One Million:
numbers = list(range(1, 1000001))
for number in numbers:
	print(number)

#4-5. Summin a Million:
print(f"The min number in the list is {min(numbers)}.\n")
print(f"The max number in the list is {max(numbers)}\n.")
print(f"The sum of the numbers in the list is {sum(numbers)}.")

#4-6. Odd Numbers:
numbers = list(range(1, 20, 2))
for number in numbers:
	print(number)

#4-7. Threes:
multiples_of_3 = list(range(3, 31, 3))
for multiple in multiples_of_3:
	print(multiple)

#4-8. Cubes:
cubes = []
for value in range(1, 11):
	cube= value ** 3
	cubes.append(cube)

print(cubes)

## another way:
cubes = []
for value in range(1, 11):
	cubes.append(value**3)

print(cubes)

#4-9. Cube Comprehension:
cubes = [value**3 for value in range(1, 11)]
print(cubes)