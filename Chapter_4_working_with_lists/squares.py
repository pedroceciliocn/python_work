squares = []
for value in range(1, 11):
	square = value ** 2
	squares.append(square)

print(squares) #the first 10 square numbers (the square of each integer from 1
#through 10)


#code written more concisely, omiting the temporary variable square and appendi-
#ng each new value
#directly to the list:
squares = []
for value in range(1, 11):
	squares.append(value**2)

print(squares) #the first 10 square numbers (the square of each integer from 1 
#through 10)

#doing the same job using list comprehesion:
squares = [value**2 for value in range(1, 11)]
print(squares)