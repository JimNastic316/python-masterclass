def build_tuple(*args):
    return args

message_tuple = build_tuple("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(number_tuple))
print(number_tuple)
