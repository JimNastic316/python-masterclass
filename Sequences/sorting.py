from typing import List

pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers: List[float] = [2.3, 4.5, 8.7, 3.1, 9.2, 1.6]
# Using 'sorted() creates a new list, and leaves original the same
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
# Using '.sort' changes the original list
numbers.sort()
print(numbers)

# Will return 'None'
# numbers.sort() modifies the list 'in place'
# another_sorted_numbers = numbers.sort()
# print(another_sorted_numbers)

# Can pass string literal to built in function sorted()
missing_letter = sorted("The quick brown fox jumped over the lazy dog")
print(missing_letter)
