# value = 8
# answer = 0
#
# for x in range(1, 13):
#     answer = value * x
#     print("{0} times {1} is {2}".format(x, value, answer))
for value in range(11):
    value = value *2
    print(value)
print("*" *79)

for value in range(0, 21, 2):
    print(value)
print("*" *79)

asteroids = [9617, 9618, 9619, 9620, 9621, 9622, 13681]

for asteroid in asteroids:
    if asteroid == 9617:
        print("Grahamchapman")
    elif asteroid == 9618:
        print("Johncleese")
    elif asteroid == 9619:
        print("Terrygilliam")
        break
    elif asteroid == 9620:
        print("Ericidle")
    elif asteroid == 9621:
        print("Michaelpalin")
    else:
        print("Terryjones")
else:
    print("MontyPython")

print("*"*79)

for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)
print("*"*79)

quote = """
It's not pining. It's passed on. This parrot is no more. It has ceased to be.
It's expired and gone to meet its maker.
This is a late parrot.
It's a stiff. Bereft of life, it rests in peace.
If you hadn't nailed it to the perch, it would be pushing up the daisies.
It's rung down the curtain and joined the choir invisible.
THIS IS AN EX-PARROT.
"""

period_count = 0
for char in quote:
    if char == '.':
        period_count = period_count + 1
print(period_count)