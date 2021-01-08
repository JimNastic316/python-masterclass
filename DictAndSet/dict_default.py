from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0)
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans", 0)
print(f"beans: {beans_quantity}")

ketchup_quantity = pantry.get("ketchup", 0)
print(f"ketchup: {ketchup_quantity}")

# default can be a string value as well
z_quantity = pantry.setdefault("zucchini", "eight")

print()
print("'pantry'now contains...")
for key, value in sorted(pantry.items()):
    print(key, value)
# setdefault will check and see if the key is in the dict, and add
# that key if it does not exist
# get will not
