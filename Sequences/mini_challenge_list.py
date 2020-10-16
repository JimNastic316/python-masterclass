# Use a for loop to produce a list of ints, rather than strings
# Can either modify the contents of the 'values_list' in place,
# or create a new list of ints

values_list = ["9", "223", "372", "036", "854", "775", "807"]

# This replaces the strings with ints
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)

# This option creates a new list
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print(integer_values)