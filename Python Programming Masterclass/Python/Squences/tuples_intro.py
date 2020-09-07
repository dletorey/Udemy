# # t = ("a", "b", "c") # the brackets are optional, but it's good practise
# # print(t)
# # exercise 123 tuples are immutable
# # welcome = "Welcome to my nightmare", "Alice Cooper", 1975
# # bad = "Bad Company", "Bad Company", 1974
# # budgie = "Nightflight", "Budgie", 1981
# # imelda = "More Mayhem", "Emilda May", 2011
# # metallica = "Ride the Lightning", "Metallica", 1984
# #
# # print(metallica)
# # print(metallica[0])
# # print(metallica[1])
# # print(metallica[2])
# #
# # metallica2 = list(metallica)
# # print(metallica2)
# # metallica2[0] = "Master of Puppets"
# # print(metallica2)
#
# # Exercise 126 More Unpacking
#
# welcome = "Welcome to my nightmare", "Alice Cooper", 1975
# bad = "Bad Company", "Bad Company", 1974
# budgie = "Nightflight", "Budgie", 1981
# imelda = "More Mayhem", "Emilda May", 2011
# metallica = "Ride the Lightning", "Metallica", 1984
#
# # print(metallica)
# # print(metallica[0])
# # print(metallica[1])
# # print(metallica[2])
# title, artist, year = metallica
# print(title)
# print(artist)
# print(year)
#
# table = ("Coffee table", 200, 100, 75, 34.50)
# print(table[1] * table[2])
#
# name, length, width, height, price = table
# print(length * width)

# exercise 127 nested tuples and lists

albums = [("Welcome to my nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]
print(len(albums))
# print using index
for album in albums:
    print("Album: {}\tArtist: {}\tYear: {}"
          .format(album[0],album[1],album[2]))
# print using unpacked names
for alb in albums:
    album, artist, year = alb
    print("Album: {}\tArtist: {}\tYear: {}"
          .format(album, artist, year))

# print unpacking tuples first
for album, artist, year in albums:
    print("Album: {}\tArtist: {}\tYear: {}"
          .format(album, artist, year))