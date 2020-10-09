menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon","sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"]
]
# print meals that do not contain spam
for meal in menu:
    if "spam" not in meal:
        print(meal)
        #print items
        for item in meal:
            print(item)

    # for the meals that do contain spam
    # show spam score
    else:
        print("{0} has a spam score of {1}"
              .format(meal, meal.count ("spam")))