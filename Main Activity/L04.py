#Start code here
part = input("Where does it pain? ")
#Additionally add all possible inputs and use .lower() method to resolve the case differences # your own code
if part.lower() == "eye" or part.lower() == "eys":
  print("Visit an Opthalmologist")
elif part == "Ear" or part == "Nose" or part == "Throat":
  print("Visit an ENT specialist")
elif part == "Stomach":
  print("Visit a Gastroenterologist")
elif part == "Brain":
  print("Visit a Neurologist")
elif part == "Bones":
  print("Visit an Orthopedic")
else:
  print("Visit a general medicine practitione")
#Additionally add more specialists.   # your own code
