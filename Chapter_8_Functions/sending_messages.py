#Sending Messages:
def send_messages(messages, sent_messages):
	"""
	Simulate printing each message, until none are left.
	Move each message to sent_messages after printing.
	"""
	while messages:
		current_message = messages.pop()
		print(f"Printing message: {current_message}")
		sent_messages.append(current_message)

def show_messages(sent_messages):
	"""Show all the messages that were printed."""
	print("\nThe following messages have been printed:")
	for sent_message in sent_messages:
		print(sent_message)