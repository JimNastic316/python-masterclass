locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in a forest"
}

loc = 1
# exits = [
#     {"Q": 0},                                  # 0
#     {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # 1
#     {"N": 5, "Q": 0},                          # 2
#     {"W": 1, "Q": 0},                          # 3
#     {"N": 1, "W": 2, "Q": 0},                  # 4
#     {"W": 2, "S": 1, "Q": 0}                   # 5
# ]
# FIRST PART OF CHALLENGE
# Challenge is to change exits to dictionaries, not lists
# to do so, you just reformat exits into a dictionary
# and don't need to change the code
exits = {
    0: {"Q": 0},                                  # 0
    1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # 1
    2: {"N": 5, "Q": 0},                          # 2
    3: {"W": 1, "Q": 0},                          # 3
    4: {"N": 1, "W": 2, "Q": 0},                  # 4
    5: {"W": 2, "S": 1, "Q": 0}                   # 5
}

namedExits = {
    1: {"2": 2, "3": 3, "4": 4, "5": 5},
    2: {"5": 5},
    3: {"1": 1},
    4: {"1": 1, "2": 2},
    5: {"1": 1, "2": 2}
}

# SECOND PART OF CHALLENGE
# Add some code to validate input. For example, allow user
# to type "Go West" or "North" instead of just N, S, E, W
vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5"

}

# print(locations[0].split()) # splits on spaces as default
#
# print(locations[3].split())     # splits on spaces
# print(locations[3].split(','))  # splits on ','

loc = 1
while True:
    # availableExits = ""
    # for direction in exits[loc].keys():
    #     availableExits += direction + ", "
    # Better way than concatenating strings with a a loop is below
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(namedExits[loc])

    direction = input("Available exits are " + availableExits + " ").upper()
    print()
    # Parse the user input using our vocabulary dictionary if needed
    if len(direction) > 1:  # if more than 1 letter was input, check vocab
        #### checks users input against the vocabulary dictionary
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break

    if direction in allExits:
        loc = allExits[direction]
        print(f"Moved to {loc}")
    else:
        print("You cannot go in that direction")
