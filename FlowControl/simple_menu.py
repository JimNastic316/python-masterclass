# low = 1
# high = 9
# #selection = 0
# menu = True
# while menu:
#     #while selection != "0":
#     print("Please select an option from {} to {}, or 0 to quit"
#           .format(low, high))
#     print("1. One\n2. Two\n3. Three\n4. Four\n5. Five\n"
#           "6. Six\n7. Seven\n8. Eight\n9. Nine\n0. Quit")
#     selection = int(input("Enter your selection: "))
#     if selection == 0:
#         print("Goodbye")
#         menu = False
#     elif low <=selection <= high:
#         print(selection)
#     else:
#         print("That is an invalid choice")
#
# print("User ended")
#
#selection = input("Enter your selection: ")
# Define selection to be an invalid entry, just to hold something
selection = "-"
while selection != "0":
    if selection in "123456789":
        print("You chose {}".format(selection))
    else:
        print("Please select an option from {} to {}, or 0 to quit"
              .format(1, 9))
        print("\t1. One\n\t2. Two\n\t3. Three\n\t4. Four\n\t5. Five\n"
              "\t6. Six\n\t7. Seven\n\t8. Eight\n\t9. Nine\n\t0. Quit")
    selection = input("Enter your selection: ")

print("User ended")
