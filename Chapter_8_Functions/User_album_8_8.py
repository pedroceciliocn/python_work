def make_album(artist_name, title, number_of_songs = None):
	"""Return a dictionary of informations about an album."""
	album = {'artist': artist_name, 'title': title}
	if number_of_songs:
		album['number_of_songs'] = number_of_songs
	return album
while True:
	print("\nPlease tell me the album informations:")
	print("(enter 'q' at any time to quit)")

	a_name = input("Artist name: ")
	if a_name == 'q':
		break
	a_title = input("Album title: ")
	if a_title == 'q':
		break
	n_songs = input("Number of songs (if you dont know, there is no problem, just press enter) :")
	if n_songs == 'q':
		break

	album_info = make_album(a_name, a_title, n_songs)
	print(f"\n{album_info}")
