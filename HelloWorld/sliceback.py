#                    1         2
#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)


backwards = letters[25::-1]
print(backwards)

backwards = letters[::-1]
print(backwards)

challenge1 = letters[16:13:-1]
print(challenge1)
challenge2 = letters[4::-1]
print(challenge2)
challenge3 = letters[25:17:-1]
print(challenge3)

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])
