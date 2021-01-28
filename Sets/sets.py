# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)
#
# for animal in farm_animals:
#     print(animal)
#
# print("*" * 40)
#
# wild_animals = set(["lion", "tiger", "panther", "elephant"])
# print(wild_animals)
# for animal in wild_animals:
#     print(animal)
#
# farm_animals.add("horse")
# wild_animals.add("horse")
# print(farm_animals)
# print(wild_animals)

# empty_set = set()
# empty_set2 = {}
# empty_set.add("a")
# print(empty_set)
# empty_set2.add("a")
# print(empty_set2)

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# square = set(squares_tuple)
# print(squares_tuple)
# print(square)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))
#
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares_tuple)
# print(len(squares_tuple))
# print(squares)
# print(len(squares))
#
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print(squares.union(even))
# print("*" * 40)
# # intersection and "&" are used to represent union
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# even = set(range(0, 40 ,2))
# print(sorted(even))
# squares_tuple = (4, 6, 9 ,16, 25)
# squares = set(squares_tuple)
# print(squares)
#
# print("even minus squares")
# print(even.difference((squares)))
# print(even - squares)
#
# print("squares minus even")
# print(squares.difference(even))
# print(squares - even)
#
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# even = set(range(0, 40 ,2))
# print(sorted(even))
# squares_tuple = (4, 6, 9 ,16, 25)
# squares = set(squares_tuple)
# print(squares)

# print("symmetric even minus squares")
# print(even.symmetric_difference(squares))
# # print(even ^ squares)
#
# print("symmetric squares minuse even")
# print(squares.symmetric_difference(even))
# print(squares ^ even)

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # no error, doesn't exist
# print(squares)
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")

# even = set(range(0, 40 ,2))
# print(sorted(even))
# squares_tuple = (4, 6,16)
# squares = set(squares_tuple)
# print(squares)

# issubset
# if squares.issubset(even):
#     print("squares is a subset of even")
# if even.issubset(squares):
#     print("even is a subset of squares")   # won't print
# # issuperset
# if even.issuperset(squares):
#     print("even is s a superset of squares")
# if squares.issuperset(even):
#     print("squares is s superset of even") # won't print