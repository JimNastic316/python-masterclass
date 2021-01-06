from contents import pantry, recipes

display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key


while True:
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")

    choice = input(": ")

    if choice =="0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        shopping_list = {} #emplty shopping list
        for food_item, required_quantity in ingredients.items():
            quanitiy_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quanitiy_in_pantry:
                print(f"\t{food_item} in pantry")
            else:
                quanity_to_buy = required_quantity - quanitiy_in_pantry
                print(f"\tYou need to buy {quanity_to_buy} of {food_item}")
                shopping_list[food_item] = quanity_to_buy
        print(f"You need to buy:  ")
        print(shopping_list)
