#Start code here
import time
import math
min2 = int(input("Enter min: "))
sec = int(input("Enter sec: "))
timer = int(min2 * 60 + sec)
while timer != 0:
  print(timer)
  timer -= 1
  time.sleep(1)
#Additionally- replace the while loop with the for loop # your own code
for i in range(timer, 0, -5):
  print(i)
  time.sleep(5)
print("Time Up")
