#Using get() access values
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points']) #when you ask a key that doesnt exist, youll get an error

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


