#Learning C:
filename = '/home/pedro/Documentos/python_work/Chapter_10_Files_and_Exceptions/10_1/learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines() 
									
for line in lines:
	line = line.replace('Python', 'C')
	print(line.rstrip())

