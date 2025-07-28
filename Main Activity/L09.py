#Start code here
ans = "yes"
#Additionally create a dictionary # your own code
dict1 = {}
while ans == "yes" or ans == "YES":
  phrase = input("Enter a phrase:  ")
  my_list = ["and", "of", "the", "in", "on", "at", "a", "an"]
  split_phrase = phrase.split()
  print(split_phrase)
  acronym = ""
  for word in split_phrase:
    if word.lower() not in my_list:
      acronym += word[0].upper()
  #Additionally add the word and acronyms to the dictionary # your own code
  dict1.update({phrase: acronym}) # your own code
  print(acronym)
  ans = input("Do you want to continue? (Type 'yes' or 'YES')")
#Additionally print the contents of the a dictionary # your own code
print(dict1)
