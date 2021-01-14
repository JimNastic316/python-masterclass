from challenge_simple_deep_copy import my_deepcopy
import copy

# Dictionary containing embedded list
original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}

copy_1 = copy.deepcopy(original)
copy_2 = my_deepcopy(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1].append("Cashier")

jp_list = original["J-P"]
jp_list[1].append("Courier")

print(original)
print(copy_1)
print(copy_2)