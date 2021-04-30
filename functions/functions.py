def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" "  * left_margin, text)

def center_text(*args, sep=' ', end='\n', file=None, flush=False):
    text = ""
    # text = str(text)
    for arg in args:
        text += str(arg) + sep
    left_margin = (30 - len(text) // 2)
    print(" " * left_margin, text, end=end, file=file, flush=flush)

# call the function
# python_food()
center_text("spam and eggs")
center_text("spam, spam and eggs")
center_text("spam, spam, spam, and spam")
# numbers have no len, but
# "text = str(text)" converts text to string
center_text(12)

center_text("first", "second", 3, 4, "spam", sep=":")

# every python function returns a value, default = None
# print(python_food())
