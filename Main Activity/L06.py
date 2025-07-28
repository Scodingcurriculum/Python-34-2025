#Start code here
flag = 0
overspent_amount = 0
pocket_money = 10
total = 0
for i in range(1, 8):
  expense = float(input("Enter expense for day " + str(i) + " :  "))
  #Additionally, validate the input for non-negative amount # your own code
  if expense >= 0:
    total += expense
  else:
    #Set a flag to indicate that the input is negative number # your own code
    flag = 1
    break
if flag == 0:
  print("Total Pocket money given:  " + str(pocket_money * 7) + " $")
  print("Total expenses of the week:  " + str(total) + " ")
  if total > pocket_money * 7:
    overspent_amount = total - pocket_money * 7
    print("Total Overspent Amount:  " + str(overspent_amount) + " $")
    print("Be careful!! You are overspending")
  else:
    print("Going great")
else:
  print("Invalid Inputs !!!")
