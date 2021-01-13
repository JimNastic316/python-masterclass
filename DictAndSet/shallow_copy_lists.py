animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"]
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