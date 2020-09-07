# t = ("a", "b", "c") # the brackets are optional, but it's good practise
# print(t)
# exercise 123 tuples are immutable
welcome = "Welcome to my nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica)
print(metallica[0])
print(metallica[1])
print(metallica[2])

metallica2 = list(metallica)
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)
