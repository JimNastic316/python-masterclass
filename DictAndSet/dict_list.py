available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive"
                   }
current_choice = None

# Create an empty list
computer_parts = []

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        # if user picks something that is already in the
        # computer_parts list, it will be removed
        if chosen_part in computer_parts:
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)
        # if user picks something that is not already in the
        # computer_parts list, it will be appended(added)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append(chosen_part)
        print(f"Your list now contains: {computer_parts}")

    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to quit")

    current_choice = input("> ")


