#                   1
#         01234567890123
#
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
# using negative indexing
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])
# or even better, just subtract 14 from original
print()

print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

#          01234567890123
#parrot = "Norwegian Blue"

#slicing
print(parrot[:9])  # Norwegian
print(parrot[10:]) # Blue

# using a step in a slice
print()
letters = "abcdefghijklmnopqrstuvwxyz"
print(letters[0:26:2])
print(letters[1:26:2])
print()
print(letters[0:26:4])
print(letters[1:26:4])
