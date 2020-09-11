# day = "Saturday"
# temperature = 30
# raining = True
#
# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go Swimming")
# else:
#     print("Learn Python")
#
# print("-" * 80)

# line below is unreachable, as 0 = False, so will never be True
if 0:
    print("True")
else:
    print("False")
print("-" * 80)
name = input("Please enter your name: ")
#if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")