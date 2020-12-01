LOW = int(1)
HIGH = int(100)
def fizz_buzz(num: object) -> object:
    """
    Function takes a variable and checks to see if it is divisible
    by 3, 5, or both.
    :param num: variable to check
    :return: string determined on if is divisible by 3, 5, both, neither
    """
    ans = None
    while True:
        if num % 3 == 0:
            if num % 5 == 0:
                ans = "fizz buzz"
            else:
                ans = "fizz"
        #    return(ans)
        # elif num % 3 == 0:
        #     ans = "fizz"
        #    return(ans)
        elif num % 5 == 0:
            ans = "buzz"
        #    return(ans)
        else:
            ans = str(num)

        return ans


# for next_number in range(LOW, HIGH + 1):
#     print(fizz_buzz(next_number))
next_number = 0
print("Lets play fizz buzz, I'll go first")
while next_number < 99:
    next_number += 1
    print("Computer : {}".format(fizz_buzz(next_number)))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_guess = input("Player : ")
    if players_guess != correct_answer:
        print("Sorry, the correct answer is {}"
              .format(correct_answer))
        break
else:
    print("Good job, you did it!")



