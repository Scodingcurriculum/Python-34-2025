#Start code here
import time
score = 0
db = {"Capital of France" : "Paris", "Capital of Germany": "Berlin","Capital of Australia":"Canberra", "Capital of New Zealand":"Wellington"}
start = time.time()
print("Welcome to the country capital quiz  !!!!")
for i in db.keys():
  print(i)
  ans = input("Answer ==> ")
  if ans.lower() == db[i].lower():
    score += 1
end = time.time()
timer_cnt = end - start
print("Final Score: " + str(score))
print("Time taken to complete the quiz:  " + str(1) + " seconds")
