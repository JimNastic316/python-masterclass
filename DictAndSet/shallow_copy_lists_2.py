lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

things = animals
things_copy = animals.copy() # creates a new, separate
print(animals)
print(things)
print(things_copy)

print()
things["teddy"].append("toy")
print(animals["teddy"])
print(things["teddy"])
print(things_copy["teddy"])

animals["teddy"].append("added via 'animals'")
things["teddy"].append("added via 'things'")
things_copy["teddy"].append("added via 'things_copy'")

print()
print(animals["teddy"])
print(things["teddy"])
print(things_copy["teddy"])
print(teddy_list)

