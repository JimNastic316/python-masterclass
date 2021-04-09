import time

print(f"The epoch on this system starts at {time.strftime('%c', time.gmtime(0))}")

# print("The current timezone is {0} with an offset of {1}".format(time.tzname[0], time.timezone))
print(f"The current timezone is {time.tzname[0]} with an offset of {time.timezone}")

if time.daylight != 0:
    print("Daylight Saving Time is in effect for this location")
    print("The DST timezone is " + time.tzname[1])

print(f"Local time is {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())}")
# print("Local time is " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
print(f"UTC time is {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())}")

