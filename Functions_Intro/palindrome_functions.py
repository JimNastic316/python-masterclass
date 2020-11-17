def is_palindrome(string):
    """
    Checks to see if a string is a palindrome, aka
    reads forwards the same as backwards
    :param string: The string to check
    :return: True if is a palindrome, False if not
    """
    return string[::-1].upper() == string.upper()

# word = input("Please enter a word to check: ")
# upperWord = str.upper(word)
# if is_palindrome(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))


def palindrome_sentence(sentence):
    """
    Checks to see if a sentence is a palindrome aka
    reads forwards the same as backwards

    The function will ignore whitespace, capitalization, and
    punctuation in the sentence.
    :param sentence: The sentence to check
    :return: True if `sentence` is a palindrome, else false
    """
    string = ""
    # Itarates over every character in the sentence
    for char in sentence:
        # if is an alphanumeric character, adds to string
        # Otherwise is ignored
        if char.isalnum():
            string += char
    print(string)
    # return string[::-1].upper() == string.upper()
    return is_palindrome(string)

word = input("Please enter a sentence to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))