# Tuples are ordered and immutable
# parenthesis not required, but good practice
welcome = ("Welcome to my Nightmare", "Alice Cooper", 1975)
bad = ("Bad Company", "Bad Company", 1974)
budgie = ("Nightflight", "Budgie", 1981)
imelda = ("More Mayhem", "Emilda May", 2011)
metallica = ("Ride the Lightning", "Metallica", 1984)

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

#unpack tuple
title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("Coffee table", 200, 100, 75, 34.50)
# Not so easy to understand that below code displays
# length * width
print(table[1] * table[2])

# Better way is to unpack tuple
name, length, width, height, price = table
print(length * width)