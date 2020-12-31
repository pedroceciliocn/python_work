def make_album(artist_name, title, number_of_songs = None):
	"""Return a dictionary of informations about an album."""
	album = {'artist': artist_name, 'title': title}
	if number_of_songs:
		album['number_of_songs'] = number_of_songs
	return album

album_info = make_album('Nirvana', 'Nevermind')
print(album_info)

album_info = make_album('Alice in Chains', 'Dirt')
print(album_info)

album_info = make_album('Mad Season', 'Above')
print(album_info)

album_info = make_album('Wolf Alice', 'Visions of a Life', 12)
print(album_info)