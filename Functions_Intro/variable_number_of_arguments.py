def sum_numbers(*addends: float) -> float:
    """
    Calculates the sum of number passed as arguments
    :param addends: list of numbers to be added
    :return: the sum of numbers passed
    """
    total = 0
    for i in addends:
        total += i
    return total


print(sum_numbers(1, 2, 3))
print(sum_numbers(3, 7, 10, 99, 12))