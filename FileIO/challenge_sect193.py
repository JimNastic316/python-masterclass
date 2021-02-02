with open("sample.txt", 'w') as tables:
    for i in range(2, 13):
        for j in range(1, 13):
            print(f"{j:>2} times {i} is {i*j}", file=tables)
            # print("{1:>2} times {0} is {2}".format(i, j, i * j))
        print("-" * 20, file=tables)