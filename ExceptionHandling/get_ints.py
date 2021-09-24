def getint():
    while True:
        try:
            num = int(input("Please enter a number "))
            return num
        except ValueError:
            print("Invalid number entered, please try again")

