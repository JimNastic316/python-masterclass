for i in range(1,21):
    print("i is now {}".format(i))
print()
# don't need to enter a start value
for i in range(10):
    print("i is now {}".format(i))

print()
# if want to step in increments of say 2
# need to specify a start valuse, or
# won't work
for i in range(0, 10, 2):
    print("i is now {}".format(i))

print()
# if want to go backwards, need to start
# at the largest number, or won't
# work
for i in range(10, 0, -2):
    print("i is now {}".format(i))

print()
age = int(input("How old are you? "))

# if  age >= 16 and age <= 65:
# if 16 <= age <= 65:
# instead of the code above, can also use below code
if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

for i in range(0, 100 ,7):
    print(i)


