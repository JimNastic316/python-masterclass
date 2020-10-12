flowers = [
    "Daffodil",
    "Evening Promreose",
    "Hydrangea",
    "Iris",
    "lavender",
    "Sunflower",
    "Tiger Lily",
]
# iterates over the list
# for flower in flowers:
#     print(flower)

# use .join to interate over the list
# note no for loop required
separator =  ", "
output = separator.join(flowers)
print(output)

# can use string literals with .join
print(" | ". join(flowers))