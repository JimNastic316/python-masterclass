animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}

things = animals
things_copy = animals.copy() # creates a new, separate
print(animals)
print(things)

# changing value in animals changes value in things
# but not in things_copy
animals["teddy"] = "toy"
print(animals)
print(things)
print(things_copy)