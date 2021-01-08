# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}
# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

text_converted = text.casefold()

#iterate over every character in the string
for char in text_converted:
    # if char is alphanumeric (isalnum())
    if char.isalnum():
        word_count[char]= word_count.setdefault(char, 0) + 1


# Print the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)