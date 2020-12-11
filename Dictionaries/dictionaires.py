fruit = {"orange": "a sweet, orange, citus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow, citrus fruit",
         "grape": "a small sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}


print(fruit)

for i in range(10):
    for snack in fruit:
        print(snack + " is " + fruit[snack])
    print('-' * 40)