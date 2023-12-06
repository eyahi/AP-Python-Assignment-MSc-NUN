def make_album(artist, title, tracks=None):
    album = {'artist': artist, 'title': title}
    if tracks:
        album['tracks'] = tracks
    return album


album1 = make_album('Travis', 'Rodeo')
album2 = make_album('Drake', 'Her Loss')
album3 = make_album('Tory', 'Alone at prom')


print(album1)
print(album2)
print(album3)


album_with_tracks = make_album('Rema', 'Ravage', tracks=5)
print(album_with_tracks)


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


def make_great(magicians):
    great_magicians = []
    for magician in magicians:
        great_magician = "The Great " + magician
        great_magicians.append(great_magician)
    return great_magicians


magicians_list = ['Merlin', 'Houdini', 'Gandalf']


print("\nOriginal List of Magicians:")
show_magicians(magicians_list)


great_magicians_list = make_great(magicians_list.copy())
print("\nList of Magicians after 'The Great' Modification:")
show_magicians(great_magicians_list)

print("\nOriginal List of Magicians (Unchanged):")
show_magicians(magicians_list)