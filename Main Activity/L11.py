#Start code here
import random
while True:
  #Additionally - add 2 attempts # your own code
  attempts = 2
  riddles = ["What has to be broken before you can use it?", "I’m tall when I’m young, and I’m short when I’m old. What am I?", "What is full of holes but still holds water?", "What question can you never answer yes to?"]
  answers = ["egg", "Candle", "Sponge", "Are you asleep?"]
  question = random.choice(riddles)
  pos = riddles.index(question)
  print(question)
  c_ans = answers[pos].lower()
  while attempts != 0:
    u_ans = input("Enter your answer:  ").lower()
    if u_ans == c_ans:
      print("✔ Correct!!")
      break
    else:
      print("❌ Wrong answer!!")
      attempts -= 1
      print(str(attempts) + "  attempt remaining.")
