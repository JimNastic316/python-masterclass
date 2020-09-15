# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
# for i in range(0, 100, 7):
#     print(i)
i = 0
while i < 100:
    print(i)
    if i > 0 and i % 11 == 0:
        break
    i +=7
# Above works but class solution:
# for i in range(0, 100, 7):
#     print(i)
#     if i > 0 and i % 11 == 0:
#         break
