#Start code here
weight_on_earth = float(input("Enter your weight on the Earth:  "))
print("=======================================")
print("Choose a planet: - ")
print("1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("5. Saturn")
print("6. Uranus")
print("7. Neptune")
print("=======================================")
ch = int(input("Enter your choice: - "))
name = ""
gravity = 1
if ch == 1:
  gravity = 0.38
  name = "Mercury"
elif ch == 2:
  gravity = 0.91
  name = "Venus"
elif ch == 3:
  gravity = 0.38
  name = "Mars"
elif ch == 4:
  gravity = 2.34
  name = "Jupiter"
elif ch == 5:
  gravity = 1.06
  name = "Saturn"
elif ch == 6:
  gravity = 0.92
  name = "Uranus"
elif ch == 7:
  gravity = 1.19
  name = "Neptune"
else:
  print("Invalid choice!!")
if name != "":
  wt = weight_on_earth * gravity
  print("Your weight on " + name + " = " + str(wt) + " kg ")
