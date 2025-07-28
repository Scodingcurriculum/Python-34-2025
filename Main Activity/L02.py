#Start code here
print("Hello Everyone!!Here's my introduction: \n")
name = str(input("What is your name?  "))
age = int(input("What is your age?  "))
grade = int(input("What is your grade?  "))
city = input("In which city do you live?  ")
#Additional Activity- input validation # your own code
if name != "" and age >= 0 and grade != "" and city != "":
  print(f"My name is {name}. I am {age} years old and I study in grade {grade}. I live in  {city}")
  #Additionally, add your introduction. Include hobbies as a list. # your own code
  Hobbies = ["Swimming", "Reading", "Travelling"]
  print("My hobbies are: ")
  print(Hobbies)
else:
  print("Invalid inputs by the user !!")
