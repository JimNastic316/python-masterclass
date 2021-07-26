from player import Player

tim = Player("Tim")

from enemy import Enemy, Troll

random_monster = Enemy("Basic enemy", 12, 1)
print(random_monster)

random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)

random_monster.take_damage(9)
print(random_monster)

ugly_troll = Troll()
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug", 18, 1)
print("Another troll - {}".format(another_troll))

brother = Troll("Urg", 23)
print("Another troll - {}".format(brother))