jabber = open("/home/jimnastic/Documents/PythonFiles/sample.txt", 'r')
for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end = '')
jabber.close()