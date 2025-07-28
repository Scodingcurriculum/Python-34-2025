#Start code here
my_list = ["Piper", "pickled", "picked", "Peter", "peppers"]
print(my_list)
print("Enter correct order using index positions (0 to 5) : ")
order = []
for i in range(len(my_list)):
  pos = int(input("Enter position:  "))
  #Additionally handle index out of range ex # your own code
  if 0 <= pos < len(my_list):
    order.append(pos)
  else:
    print("Index out of range!")
    break
correct_sentence = []
for i in order:
  correct_sentence.append(my_list[i])
final_sentence = " ".join(correct_sentence)
print(final_sentence)
if final_sentence == "Peter Piper picked pickled peppers":
  print("✅The sentence is correct!!")
else:
  print("❌Try Again!!")
