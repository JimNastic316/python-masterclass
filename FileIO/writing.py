# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", 'w') as city_file:
#     for city in cities:
#         print(city, file=city_file)

# cities.txt already exists after preve is run
cities = []

with open("cities.txt", 'r') as city_file:
    for city in city_file:
        cities.append(city.strip('\n'))  # strip takes of beginning or end, not in the middle

print(cities)
for city in cities:
    print(city)