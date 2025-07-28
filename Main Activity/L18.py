#Start code here
cart_items = []
cart_item_price = []
#Add more items like colors, markers, diaries etc. # your own code
Items = {"pen":3, "pencil": 2, "notebook":7, "backpack":25}
print("We have: pen, pencil and notebook.  ")
item_name = input("Enter the item you want to purchase:  ").lower()
qty = int(input("Enter the quantity of it: "))
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
print(f"You have selected :  {qty} {cart_items}")
