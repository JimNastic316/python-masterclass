import time, random

from time import time as my_timer
input("Press enter to start")
wait_time = random.randint(1, 6)
print(wait_time)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X",time.localtime((start_time))))
print("Ended at " + time.strftime("%X", time.localtime((end_time))))
print(f"Your reaction time was {end_time - start_time} seconds.")