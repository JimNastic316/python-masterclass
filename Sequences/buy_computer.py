available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"]
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
# Create an empty list
computer_parts = []
while current_choice != "0":
    if current_choice in valid_choices:

        # current choice is a string, need corresponding int
        index = int(current_choice) - 1
        chosen_part = available_parts[index]

        # If the chosen part is already in the list, remove it
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)

        # If the chosen part is not in the list, add it
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list contains:\n{} ".format(computer_parts))

    else:
        print("Please add options from the list below: ")

        for number, part in enumerate(available_parts):
            print("\t{0}: {1}".format(available_parts.index(part)+1, part))

    current_choice = input("Enter your choice: ")

print("Your final list is\n {}".format(computer_parts))