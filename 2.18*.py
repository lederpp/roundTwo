# Look Over

import time

timeZone = eval(input("Enter the time zone offset to GMT: "))

currentTime = time.time()

totalSeconds = int(currentTime)                 # total seconds since unix epoch

currentSecond = totalSeconds % 60               # obtain current second

totalMinutes = totalSeconds // 60               # obtain total minutes

currentMinute = totalMinutes % 60               # current minute in the hour

totalHours = totalMinutes // 60                 # total hours

currentHour = (totalHours + timeZone) % 24      # current hour

print("The current time is ", currentHour, ':', currentMinute, ':', currentSecond)


