from random import choice

num_char_list = ('a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

selected = []
print("The selected numbers or characters are: ")
for roll in range(4):
	selected.append(choice(num_char_list))

print(selected)

######################### another way (without repeating)
selected = []
while len(selected) < 4:
	current_selected = choice(num_char_list)

	if current_selected not in selected:
		print(f"The {current_selected} is one selected.")
		selected.append(current_selected)



##################################################################
from random import choice

def sort_selected_ticket(num_char_list):
	selected = []

	while len(selected) < 4:
		current_selected = choice(num_char_list)

		if current_selected not in selected:
			selected.append(current_selected)

	return selected

def create_new_ticket(num_char_list):
	my_ticket = []

	while len(my_ticket) < 4:
		current_ticket = choice(num_char_list)

		if current_ticket not in my_ticket:
			my_ticket.append(current_ticket)

	return my_ticket

def check_ticket(played_ticket, selected):
	for element in played_ticket:
		if element not in selected:
			return False

	return True

num_char_list = ['a', 'b', 'c', 'd', 'e', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
selected = sort_selected_ticket(num_char_list)

plays = 0
won = False

max_tries = 1_000_000

while not won:
	new_ticket = create_new_ticket(num_char_list)
	won = check_ticket(new_ticket, selected)
	plays += 1
	if plays >= max_tries:
		break

if won:
	print("You are the winner!")
	print(f"Your ticket is: {new_ticket}")
	print(f"And the winner ticker is: {selected}!")
	print(f"You needed only {plays} tries to win!")

else:
	print(f"Tried {plays}x and didnt win.")
	print(f"Your ticket was: {new_ticket}")
	print(f"The selected ticket was: {selected}")