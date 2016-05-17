# Computers handle time using ticks. All computers keep track of time since 12:00am, January 1, 1970, known as epoch
# time. To get the date or time in Python we need to use the standard time module.

import time

ticks = time.time()
print("Ticks since epoch:", ticks)

# To get the current time on the machine, you can use the function localtime:
timenow = time.localtime(time.time())
print("Current time :", timenow)

# You can access each of the elements of the array:
timenow = time.localtime(time.time())
print("Year:", timenow[0])
print("Month:", timenow[1])
print("Day:", timenow[2])

# and use a combination for your own formatting.  One alternative is to use the asctime function:
timenow = time.asctime(time.localtime(time.time()))
print(timenow)
