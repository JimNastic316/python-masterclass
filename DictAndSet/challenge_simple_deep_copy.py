# write a function that takes a dictionary as an argument
# and returns a deep copy of the dictionary without using
# the 'copy' module

from contents import recipes

def my_deepcopy(dictionary: dict) -> dict:
    """
    Copy a dictionary, creating copies of the 'list' or 'dict' values
    :param dictionary: The dictionary to copy
    :return: a copy of dictionary, with values being copies of the original values
    """

    #
    dictionary_copy = {}
    for key, value in dictionary.items():
        new_value = value.copy()
        dictionary_copy[key] = new_value
    return dictionary_copy




# create a new, empty dictionary

# iterate over the keys and values of the dictionary


# for each key, copy the value,
# then add a copy of the value to the dictionary

# test data
recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300 #value is '3' in recipes
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])