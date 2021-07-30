from enemy import Enemy, Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print("Another troll - {}".format(brother))

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()

vampyre = Vampyre("Chocula")
print("Vampyer - {}".format(vampyre))

vampyre_2 = Vampyre("Chocula the 2nd")
print("Another vampyre - {}".format(vampyre_2))

vampyre.talk()
vampyre_2.talk()

vampyre.take_damage(3)
vampyre_2.take_damage(4)
another_troll.take_damage(3)

while vampyre.alive:
    vampyre.take_damage(1)
    print(vampyre)