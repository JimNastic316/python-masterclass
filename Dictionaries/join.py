myList = ['a', 'b', 'c', 'd']
letters = 'abcdefghijklmnopqrstuvwxyz'

# Ineffecient way
# newString = ''
# for c in myList:
#     newString += c +', '

# Better faster way
newString =", ".join(letters)


print(newString)