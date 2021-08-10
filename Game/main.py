from enemy import Enemy, Troll, Vampyre, VampyreKing

dracula = VampyreKing("Dracula")
print(dracula)
dracula.take_damage(12)
print(dracula)


# ugly_troll = Troll("Pug")
# print("Ugly troll - {}".format(ugly_troll))
#
# another_troll = Troll("Ug")
# print("Another troll - {}".format(another_troll))
#
# brother = Troll("Urg")
# print("Another troll - {}".format(brother))
#
# ugly_troll.grunt()
# another_troll.grunt()
# brother.grunt()
#
# vamp = Vampyre("Vamp")
# print("Vampyer - {}".format(vamp))
#
# vampyre_2 = Vampyre("Vamp the 2nd")
# print("Another vampyre - {}".format(vampyre_2))
#
# vamp.talk()
# vampyre_2.talk()
#
# vamp.take_damage(3)
# vampyre_2.take_damage(4)
# another_troll.take_damage(3)
#
#
# vamp._lives = 0
# vamp._hit_points = 1
# print(vamp)