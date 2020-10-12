# Use a for loop to produce a list of ints, rather than strings
# Can either modify the contents of the 'values_list' in place,
# or create a new list of ints

list_of_strings = ["9", "223", "372", "036", "854", "775", "807"]
print(list_of_strings)

for index in range(len(list_of_strings) - 1):
    int list_of_ints[index] = int(list_of_strings[index])

# list_of_ints = "|".join(list_of_strings)
print(list_of_ints)

for num in list_of_ints:
    num += num
    print(num)