#Start code here
import time
t = time.localtime()
currentTime = time.strftime("%H:%M:%S", t)
print(currentTime)
hr = int(currentTime[0:2])
if hr > 5 and hr < 12:
  print("Good Morning")
if hr > 12 and hr < 17:
  print("Good afternoon")
if hr > 17 and hr < 21:
  print("Good evening")
if hr > 21 and hr < 24:
  print("Good Night")
