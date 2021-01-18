locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of aroad before a small brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in a forest"
}

exits = [
    {"Q": 0},                                  # 0
    {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # 1
    {"N": 5, "Q": 0},                          # 2
    {"W": 1, "Q": 0},                          # 3
    {"N": 1, "W": 2, "Q": 0},                  # 4
    {"W": 2, "S": 1, "Q": 0}                   # 5
]

loc = 1
while True:
    availableExits = ""
    for direction