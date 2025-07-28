#Start code here
score = 0
db = {"Capital of France" : "Paris", "Capital of Germany": "Berlin","Capital of Australia":"Canberra", "Capital of New Zealand":"Wellington"}
for i in db.keys():
  print(i)
  ans = input("Answer ==> ")
  if ans.lower() == db[i].lower():
    score += 1
print("Final Score: " + str(score))
