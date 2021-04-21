# Create a program that allows a user to choose one of
# up to 9 time zones from a menu. You can choose any
# zones you want from the all_timezones list
#
# The program will then display the time in that timezone, as
# well as local time and UTC time
#
# Entering 0 as the choice will quit the program
#
# Display the dates and times in a format suitable for the
# user of your program to understand, and include the
# timezone name when displaying the chosen time.

import datetime
import pytz

available_zones = {'1': "Africa/Tunis",
                   '2': "Asia/Kolkata",
                   '3': "Australia/Adelaide",
                   '4': "Europe/Brussels",
                   '5': "Europe/London",
                   '6': "Japan",
                   '7': "Pacific/Tahiti",
                   '8': "US/Hawaii",
                   '9': "Zulu"}
while True:
    print("Please choose (0 to quit)")
    for place in available_zones:
        print(f"\t {place} - {available_zones[place]}")

    choice = input("Enter your selection: ")
    print(f"You chose {choice}")

    if choice == '0':
        print("Good bye")
        break

    elif choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)

        print(f"The time in {available_zones[choice]} is {world_time.strftime('%A %x %X %z')} {world_time.tzname()}")
        print(f"Local time is {datetime.datetime.now().strftime('%A %x %X')}")
        print(f"UTC time is {datetime.datetime.utcnow().strftime('%A %x %X')}")

    else:
        print(f"{choice} is invalid, try again")
