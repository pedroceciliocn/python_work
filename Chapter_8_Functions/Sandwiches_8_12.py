def make_sandwich(*items):
	"""Summarize the sandwich we are about to make."""
	print("\nMaking a sandwich with the following items:")
	for item in items:
		print(f"- {item}")

make_sandwich('pepperoni')
make_sandwich('mushrooms', 'green peppers', 'extra cheese')
make_sandwich('cheese', 'salame', 'catupiry')