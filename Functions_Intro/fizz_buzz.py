LOW = 1
HIGH =100
def fizz_buzz(num):
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




