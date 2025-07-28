#Start code here
import requests
word = input("Enter a word: ")
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
r = requests.get(url)
data = r.json()
meanings = data[0]['meanings']
for i in meanings:
  part_of_speech = i['partOfSpeech']
  print("----------------------------------------------")
  print(f"Part of Speech: {part_of_speech}")
  print("----------------------------------------------")
  definitions = i['definitions']
  for j in definitions:
    print("*   " + j['definition'])
  print("----------------------------------------------")
