# jabber = open("/home/jimnastic/Documents/PythonFiles/sample.txt", 'r')
# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end = '')
# jabber.close()
# Another way to get the same result is to use "with"
# no need to close file, as "with" takes care of that
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():  # used upper in this example
#             print(line, end = '')  # changes to single space, and newline
# Using READLINE()
with open("sample.txt", 'r') as jabber:
    line = jabber.readline()