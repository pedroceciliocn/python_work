#Large shirts:
##positional
def make_shirt(size='large', text='I love Python'):
	print(f"Your shirt size is {size} and the message printed is '{text}'.")

make_shirt() #using default values (large and i love python)
make_shirt('medium') #medium shirt with default message
make_shirt('small', 'I love you all S2') #any size with different message
