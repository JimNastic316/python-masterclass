import sys

def getint(prompt):
    while True:
        try:
            num = int(input(prompt))
            return num
        except ValueError:
            print("Invalid number entered, please try again")
        except EOFError:
            sys.exit(1)

def divide(num1, num2):
    try:
        print("{} diveded by {} is {}".format(num1, num2, num1 / num2))
    except ZeroDivisionError:
        print("You can't divide my zero")
        sys.exit(2)



first_number = getint("Please enter the first number ")
second_number = getint("Please enter the second number ")
divide(first_number, second_number)
