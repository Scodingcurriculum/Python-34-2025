#Start code here
import requests
#Additionally, ask the user for the limit  # your own code
n = int(input("Enter the number of Earthquakes (between 1 to 10) you want to view:   "))
url = f"https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit={n}"
r = requests.get(url)
data = r.json()
print("\n------------Earthquake Report--------------\n")
for i in range(n):
  dict1 = data.get('features', ['Unknown'][0])[i]
  place = dict1['properties']['place']
  mag = dict1['properties']['mag']
  print(str(i + 1) + ".)  " + str(place) + "   :  " + str(mag))
  dict1 = None
  mag = ""
  place = ""
print("\n--------------------------------------------\n")
