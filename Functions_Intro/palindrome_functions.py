# def is_palindrome(string):
#     # backwards = string[::-1]
#     # return backwards == string
#     # instead of above, use below line,
#     # also ignor case so if user enters 'Radar'
#     # Program will say is a palindrome
#     return string[::-1].upper() == string.upper()

# word = input("Please enter a word to check: ")
# upperWord = str.upper(word)
# if is_palindrome(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))


def palindrome_sentence(sentence):
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char

    return string[::-1].upper() == string.upper()

word = input("Please enter a sentence to check: ")
if palindrome_sentence(word):
    print("'{}' is a palindrome".format(word))
else:
    print("'{}' is not a palindrome".format(word))