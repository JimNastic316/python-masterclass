vehicles = {
    "dream": "Honda 250T",
    "roadster": "BMW R1100",
    "er5": "Kawasaki ER5",
    "can-am": "Bomardier Can-Am 250",
    "virago": "Yamaha XV250",
    "tenere": "Yamaha XT650",
    "jimny": "Suziki Jimny 1.5",
    "fiesta": "Ford Fiesta Ghia 1.4",
}

my_car = vehicles["fiesta"]
print(my_car)

commuter = vehicles["virago"]
print(commuter)

learner = vehicles.get("er5")
print(learner)
#
# for auto in vehicles:
#     car = vehicles.get(auto)
#     print(car)