fruit = {"orange": "a sweet, orange, citus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

print(fruit)

veg = {
    "cabbage": "every child's favorite",
    "sprouts":  "mmmm, lovely",
    "spinach":  "can I have more fruit, please"
}

print(veg)

# adds fruit dictoinary to veg dictionary
veg.update(fruit)
print(veg)
print(fruit)
print(fruit.update(veg))
print(fruit)
# print(fruit.update(veg))
# print ()
# print(veg)
# print(fruit)