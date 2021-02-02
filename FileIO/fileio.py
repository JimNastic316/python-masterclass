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
# with open("sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end = '')
#         line = jabber.readline()

# using READLINES()
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end ='')
# Print list of lines in reverse, preserving the lines
with open("sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:    # this reads in reverse
    print(line, end ='')

# Note the difference when READ() is used instead of READLINES()
with open("sample.txt", 'r') as jabber:
    lines = jabber.read()   # note this 
print(lines)

for line in lines[::-1]:
    print(line, end ='')