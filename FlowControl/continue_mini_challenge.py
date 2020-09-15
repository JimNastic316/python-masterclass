# Write a program to print out all the numbers from
# 0 to 20 that aren't divisible by 3 or 5
# The aim is to use the continue statement, but it is possible
# without
# i=0
# while i < 21:
#     if i%3 == 0 and i>0:
#         continue
#     print(i)
#     i += 1
# using continue
for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    print(i)

# without continue
for x in range(21):
    if x % 3 != 0 and x % 5 != 0:
        print(x)
