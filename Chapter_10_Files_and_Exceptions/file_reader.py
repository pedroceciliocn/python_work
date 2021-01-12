#Reading an Entire File
with open('pi_digits.txt') as file_object:
	contents = file_object.read()
print(contents.rstrip()) #rstrip() method is removing blank line from the end


#Reading line by line
filename = 'pi_digits.txt'

with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())


#Making a list of lines from a file
filename = 'pi_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines() #this method takes each line from the file
									#and stores it in a list
for line in lines:
	print(line.rstrip())






