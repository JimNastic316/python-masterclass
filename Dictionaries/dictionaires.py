fruit = {"orange": "a sweet, orange, citus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}


print(fruit)

# for i in range(10):
#     for snack in fruit:
#         print(snack + " is " + fruit[snack])
#     print('-' * 40)

# Print out the keys
# for key in fruit:
#     print(key)

# # Print out the values
# for key in fruit:
#     print(fruit[key])
#
# print(fruit.keys())
# print(fruit.values())

# Add a key
# fruit["tomato"] = "not good with ice cream"
print(fruit)
print(fruit.items())
f_tuple = tuple(fruit.items())
print(f_tuple)

for snack in f_tuple:
    item, description = snack
    print(item + " is " + description)

print(dict(f_tuple))