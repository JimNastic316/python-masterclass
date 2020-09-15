import random

highest = 10
answer = random.randint(1,highest)
print(answer)       #TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

#if guess != answer:
while guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
print("Well done, you guessed it")


