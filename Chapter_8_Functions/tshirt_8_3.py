#T-Shirt:
##positional
def make_shirt(size, text):
	print(f"Your shirt size is {size} and the message printed is '{text}'.")

make_shirt('P', 'S2')

##using keyword arguments
make_shirt(text='S2', size='P')