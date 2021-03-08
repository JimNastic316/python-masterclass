import shelve

# with shelve.open('ShelfTest') as fruit:
fruit = shelve.open("ShelfTest")
<<<<<<< HEAD
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['lemon'] = "sour, yellow citrus fruit"
# fruit['grape'] = "small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"
=======
fruit['orange'] = "a sweet, orange, citrus fruit"
fruit['apple'] = "good for making cider"
fruit['lemon'] = "sour, yellow citrus fruit"
fruit['grape'] = "small, sweet fruit growing in bunches"
fruit['lime'] = "a sour, green citrus fruit"
>>>>>>> master

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# <<<<<<< HEAD
# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)
print(fruit.items())
=======
while True:
    shelf_key = input("Please enter a fruit: ")
    if shelf_key =="quit":
        break
    description = fruit.get(shelf_key)
    print(description)

>>>>>>> master
fruit.close()

