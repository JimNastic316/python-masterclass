import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

# with shelve.open('recipes') as recipes:
with shelve.open('recipes', writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans on toast"] = beans_on_toast
    # recipes["scrambled eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # recipes["soup"] = soup

    # Code below doesn't work, doesn't update the db file
    # recipes["blt"].append["butter"]
    # recipes["pasta"]. append["tomato"]

    # One way to update a shelve option 1
    # Faster running  than writeback = True method2
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list
    #
    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # Works with writeback=True
    # recipes["soup"].append("croutons")

    for snack in recipes:
        print(snack, recipes[snack])