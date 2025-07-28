#Start code here
import time
ans = 1
cart_items = []
cart_item_price = []
Items = {"pen":3, "pencil": 2, "notebook":7, "backpack":25}
while ans == 1:
  item_name = input("Enter the item you want to purchase:  ").lower()
  qty = int(input("Enter the quantity of itmes: "))
  if item_name == "pen":
    cart_items.append("pen")
    cart_item_price.append(int(Items[item_name] * qty))
  elif item_name == "pencil":
    cart_items.append("pencil")
    cart_item_price.append(int(Items[item_name] * qty))
  elif item_name == "backpack":
    cart_items.append("backpack")
    cart_item_price.append(int(Items[item_name] * qty))
  else:
    print("Enter a valid item!!!")
  print("Hello World")
  ans = int(input("Do you want to shop more ? Enter 1 for YES : "))
print("Checking Out----")
for i in range(4):
  time.sleep(1)
  print("-----")
print("Your shopping cart: ")
for i in range(len(cart_items)):
  print(cart_items[i] + "  :  " + str(cart_item_price[i]) + " $")
print("-------------------------------------")
total_price = sum(cart_item_price)
#Additionally calculate the discount # your own code
if total_price >= 50:
  print("Total price after applying a discount of 5$ =  " + str(total_price - 5) + " $")
else:
  print("Total price =   " + str(total_price) + " $")
