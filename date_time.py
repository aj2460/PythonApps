import datetime

print(datetime.datetime.now())

day1=datetime.datetime(2019,5,26,10,0,0)
print(day1)
today=datetime.datetime.now()

print(today)

delta=today-day1

print(today-day1)
print(delta)

print(delta.days)
print(delta.seconds)	

print(today.strftime("%Y-%m-%d-%H-%M-%S"))


print(today.strftime("%A %d-%m-%Y-%I-%M-%S"))

after=today + datetime.timedelta(days=3)
print(after)

import time

print("Delay 2 sec")
time.sleep(2)