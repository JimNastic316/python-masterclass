empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

#create a new list by concatenating
numbers = even + odd
print(numbers)

# using sorted() creates a copy
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

# using .sorted() copies in place (changes original)
# second_sorted_numbers = numbers
#
# print(second_sorted_numbers)
# print(numbers)
# second_sorted_numbers.sort()
# print(second_sorted_numbers)
# print(numbers)

digits = sorted("432985617")
print(digits)
letters = ("qwertyuiopasdfghjklzxcvbnm")
sorted_letters = sorted(letters)
print(letters)
print(sorted_letters)

