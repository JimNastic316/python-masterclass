def factorial(num: int) -> int:
    """
    Calculates and prints factorial of a given number
    :param num: number to use to calculate the factorial
    :return: integer
    """
    if num <= 1:
        return 1
    else:
        ans = 2
        for i in range(3, num + 1):
            # print("I is {}, and num is {}".format(i, num))
            ans = ans * i
            # print("ans is {}".format(ans))
        return ans


for j in range(36):
    print(j, factorial(j))


    # ans = 1
    # if num <= 1:
    #     print(num, ans)
    # else:
    #     for i in range(1, num + 1):
    #         ans = ans * i
    #         print(num, ans)

