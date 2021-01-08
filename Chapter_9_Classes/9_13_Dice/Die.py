from random import randint

class Die:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		return randint(1, self.sides)



six_side = Die()
for roll in range(10):
	print(six_side.roll_die())



ten_side = Die(sides=10)
for roll in range(10):
	print(ten_side.roll_die())


twenty_side = Die(sides=20)
for roll in range(10):
	print(twenty_side.roll_die())


#more "clean" mode:
results = []
six_side = Die()

for roll in range(10):
	results.append(six_side.roll_die())

print("10x rolls from a six side die:")
print(results)

results = []
ten_side = Die(sides=10)

for roll in range(10):
	results.append(ten_side.roll_die())

print("10x rolls from a ten side die:")
print(results)


results = []
twenty_side = Die(sides=20)

for roll in range(10):
	results.append(twenty_side.roll_die())

print("10x rolls from a twenty side die:")
print(results)