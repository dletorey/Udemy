from demo import albums
SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
SONG_TIME_INDEX = 2
while True:
    print("Please choose your album (invalid choice exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}"
              .format(index + 1, title))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONGS_LIST_INDEX]
    else:
        break
    print("Please choose your song:")
    for index, (track_num, song, duration) in enumerate(songs_list):
        print("{}: {} - {}"
              .format(track_num, song, duration))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        duration = songs_list[song_choice - 1][SONG_TIME_INDEX]
        print("Playing {} - {}"
              .format(title,duration))
    print("-" * 10)