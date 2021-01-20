import matplotlib.pyplot as plt

from die import Die

## Create three D6 dice.
die_1 = Die()
die_2 = Die()


## Make some rolls, and store results in a list (using list comprehension).
"""
results = []
for roll_num in range(50_000):
	result = die_1.roll() * die_2.roll()
	results.append(result)
"""
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

## Analyze the results (using list comprehension).
"""
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
"""
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]


plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.bar(range(2, max_result+1), frequencies)
ax.set_title("Results of rolling two D6 50000 times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)

plt.show()
