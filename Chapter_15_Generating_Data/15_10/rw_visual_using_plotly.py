#Using List Compprehension this time
# Rolling Two Dice
from plotly.graph_objs import Scatter, Layout
from plotly import offline

from random_walk import RandomWalk

rw = RandomWalk(50_000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))



## Create three D6 dice.
#die_1 = Die()
#die_2 = Die()


## Make some rolls, and store results in a list (using list comprehension).
"""
results = []
for roll_num in range(50_000):
	result = die_1.roll() * die_2.roll()
	results.append(result)
"""
#results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

## Analyze the results (using list comprehension).
"""
frequencies = []
max_result = die_1.num_sides * die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
"""
#max_result = die_1.num_sides + die_2.num_sides
#frequencies = [results.count(value) for value in range(2, max_result+1)]


## Visualize the results.
##rw = RandomWalk(50_000)
##rw.fill_walk()

##point_numbers = list(range(rw.num_points))

data = [Scatter(x=rw.x_values, y=rw.y_values)]

x_axis_config = {'title': 'X', 'dtick': 1}
y_axis_config = {'title': 'Y'}
my_layout = Layout(title='Random Walk', 
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='rw.html')


#while True:
	# Make a random walk.
#	rw = RandomWalk(50_000)
#	rw.fill_walk()

	# Plot the points in the walk.
#	plt.style.use('classic')
#	fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
#	point_numbers = range(rw.num_points)
#	ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
#		edgecolors='none', s=1, zorder=1)

	# Emphasize the first and last points.
#	ax.scatter(0, 0, c='green', edgecolors='none', s=50, zorder=2)
#	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', 
#	s=50, zorder=2)

	# Remove the axes.
#	ax.get_xaxis().set_visible(False)
#	ax.get_yaxis().set_visible(False)

#	plt.show()

#	keep_running = input("Make another walk? (y/n): ")
#	if keep_running == 'n':
#		break