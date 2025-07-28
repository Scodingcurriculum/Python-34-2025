#Start code here
landmark = ""
#Additionally- define a function Tips() for the visitor instructions. # your own code
def Tips(landmark):
  print("Tips to visit  " + landmark + " ------------------------------------")
  if landmark == "Machu Picchu":
    print("☀️ Why: Clear skies, ideal for hiking and views.")
    print("🧥 Tip: June–August is most popular — book early.")
    print("🚫 Avoid: November–March (rainy season, trails may be muddy or closed).")
    print("------------------------------------------------")
  elif landmark == "Colosseum":
    print("🌤️ Why: Mild temperatures, fewer crowds than summer.")
    print("🚫 Avoid: July–August (very hot and packed with tourists).")
    print("------------------------------------------------")
def MachuPicchu():
  landmark = "Machu Picchu"
  print("Name: " + "Machu Picchu")
  print("Located at : " + "Incan site near Cuzco, Peru,")
  print("Discovered by:  " + " Hiram Bingham")
  print("Features:  " + "It features agricultural terraces, plazas, residential areas, and temples.")
  print("------------------------------------------------")
  Tips(landmark)
def Colosseum():
  landmark = "Colosseum"
  print("Name: " + "The Colosseum")
  print("Located at : " + "Rome")
  print("Built by:  " + "Emperor Vespasian")
  print("Features:  " + "The amphitheater measures 620 by 513 feet, has a complex system of vaults.\n  It was capable of holding 50,000 spectators, who watched a variety of events.")
  print("------------------------------------------------")
  Tips(landmark)
Colosseum()
MachuPicchu()
