LOW = 1
HIGH =100
def fizz_buzz(num: int) ->str:
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


for number in range(LOW, HIGH + 1):
    print(fizz_buzz(number))




