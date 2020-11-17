def multiply(x, y):
    """
    Takes two numbers and multiplies them
    :param x: The first number
    :param y: The second number
    :return: The product of `x` and `y`
    """
    result = x * y
    return result


answer = multiply(10.5, 4)
print(answer)

forty_two = multiply(6, 7)
print(forty_two)
print()
for val in range(1, 10):
    two_times = multiply(2, val)
    print(two_times)