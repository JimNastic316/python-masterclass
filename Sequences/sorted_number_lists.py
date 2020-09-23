even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

# Put the contents of odd into even
even.extend(odd)
print("Now even is:")
print(even)
another_list=even

print("Now odd is:")
print(odd)

# This will append the contents of even to odd, but as a separate list
odd.append(even)
print("Now odd is:")
print(odd)

even.sort()
print("Now even is:")
print(even)
print("another_list is also sorted: ")
print(another_list)

# Below won't work, because can't sort list and int
# odd.sort()
# print("Now odd is:")
# print(odd)
