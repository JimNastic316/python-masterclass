vehicles = {
    "dream": "Honda 250T",
    "er5": "Kawasaki ER5",
    "can-am": "Bomardier Can-Am 250",
    "virago": "Yamaha XV250",
    "tenere": "Yamaha XT650",
    "jimny": "Suziki Jimny 1.5",
    "fiesta": "Ford Fiesta Ghia 1.4",
    "roadster": "Trimph Street Triple"
}

vehicles["starfighter"] = "Lockhee F-104"
vehicles["learjet"] = "Bombardier Lear jet 75"
vehicles["toy"] = "glider"

#Upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

del vehicles ["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1", "You wish. Sell the Learjet and maybe")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

for key, value in vehicles.items():
    print(key, value, sep = ", ")