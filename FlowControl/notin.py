activity = input("What would you like to do today? ")

# if "cinema" not in activity:
# instead of code above, use 'activity.casefold' to convert
# in case user enters CINEMA or Cinema, etc
if "cinema" not in activity.casefold():
    print("But I wanted to go the the cinema")