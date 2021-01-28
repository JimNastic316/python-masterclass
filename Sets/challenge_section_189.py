# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels sorted in
# alphabetical order
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.

# vowel_set = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
vowel_set = frozenset("aeiouAEIOU")
# print(vowel_set)
# no_vowels = set()

user_input = input(f"Enter a list of characters ")
input_set = set(user_input)
no_vowels = input_set.difference(vowel_set)
print(sorted(no_vowels))
