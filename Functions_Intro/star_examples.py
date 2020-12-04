numbers = (0, 1, 2, 3, 4, 5)
more_numbers = (6, 7, 8, 9)

# print(numbers, sep=";")
# print(numbers, more_numbers, sep=";")
# print(*numbers ,sep=";")
# print(*numbers, *more_numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")

def test_star(*args):
    print(args)
    for x in args:
        print(x)

test_star(1, 2, 3, 4, 5, "hello", "world", 1+2)
print()
test_star()