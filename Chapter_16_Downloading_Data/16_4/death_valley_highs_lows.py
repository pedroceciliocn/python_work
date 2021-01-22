import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
filename = 'data/sitka_weather_2018_simple.csv'
place_name = ''
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	print(header_row)
	date_index = header_row.index('DATE')
	high_index = header_row.index('TMAX')
	low_index = header_row.index('TMIN')
	name_index = header_row.index('NAME')

	# Get dates and high and low temperatures from this file.
	dates, highs, lows = [], [], []
	for row in reader:
		# Get the station name
		if not place_name:
			place_name = row[name_index]
			print(place_name)


		current_date = datetime.strptime(row[2], '%Y-%m-%d')
		try:
			high = int(row[high_index])
			low = int(row[low_index])
		except ValueError:
			print(f"Missing data for {current_date}")
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot
title = f"Daily high and low temperatures - 2018\n{place_name}"
ax.set_title(title, fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
plt.ylim([0, 130])

plt.show()