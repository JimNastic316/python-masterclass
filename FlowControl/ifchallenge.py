name = input("What is your name? ")
age = int(input("How old are you? "))

if 18 <= age < 31:
    print("{}, welcome to the holiday!".format(name))
else:
    print("Sorry {}, but you are not allowed to come".format(name))