print("1")
for i in range(1,13):
    # i**2 = square, i**3 = cubed
    print("No. {0} squared is {1} and cubed is {2}".format(i, i **2, i **3))
print()

print("2")

for i in range(1,13):
    # same as above, add column width of 2, 3, and 4
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i **2, i **3))
print()


print("3")
for i in range(1,13):
    #left align, kind of like an arrow that points to where will be
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i **2, i **3))
print()

print("4")
for i in range(1,13):
    #centered, doesn't look so great, no half spaces
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i **2, i **3))

print()
print("5")
# default to 15 decimal spaces
print("Pi is approximately {0:12}".format(22 / 7))

# using 'f' specifies a floating point value after {0:12f} defaults to 6 decimal places
print("Pi is approximately {0:12f}".format(22 / 7))

# using .50f species 50 spaces after the decimal point
# Python overides 12 width with precision of 50
print("Pi is approximately {0:12.50f}".format(22 / 7))

# 52 field width, 50 precision
print("Pi is approximately {0:52.50f}".format(22 / 7))

# 62 field width, 50 precision
print("Pi is approximately {0:62.50f}".format(22 / 7))


# 72 field width, 50 precision
print("Pi is approximately {0:72.50f}".format(22 / 7))

print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))




