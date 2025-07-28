#Start code here
print("My fruit basket")
fruits = []
n = input("How many fruits do you have at home: ")
for i in range(0, int(n)):
  fruit_name = input("Enter the name of fruit: ")
  fruits.append(fruit_name)
  print(fruits)
print("Lets sort our fruit basket: ")
fruits.sort() # your own code
print(fruits)
choice = "y"
while choice == "y":
  print("Which fruit would you like to eat today?")
  fruit_name = input("")
  fruits.remove(fruit_name)
  print(fruits)
  choice = input("Do you want to eat more fruit? ")
