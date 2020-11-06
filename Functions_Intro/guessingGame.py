import random

def get_integer(prompt):
    while True:
        temp = input(prompt)
        # verifies that the input is a number
        if temp.isnumeric():
            # return will break the while loop here
            return int(temp)
        else:
            print("{0} is not a valid number".format(temp))

highest = 1000
answer = random.randint(1,highest)
print(answer)       #TODO: Remove after testing
guess = 0
print("Please guess a number between 1 and {}: ".format(highest))


#if guess != answer:
while guess != answer:
    guess = get_integer(": ")
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")

print("Well done, you guessed it")


