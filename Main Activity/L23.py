#Start code here
import requests
import pygal
url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&limit=5"
place = []
mag = []
r = requests.get(url)
data = r.json()
for i in range(5):
  dict1 = data.get('features', ['Unknown'][0])[i]
  place.append(dict1['properties']['place'])
  mag.append(dict1['properties']['mag'])
  dict1 = None
for i in range(len(place)):
  print(str(place[i]) + " : " + str(mag[i]))
bar_chart = pygal.Bar()
bar_chart.title = "The Magnitude of Earthquakes"
bar_chart.add("Places", mag)
bar_chart.x_labels = place
bar_chart.render()
#Additionally, ask students to set limit =9 to get first 9 earthquakes. # your own code
#Additional activity # your own code
max_mag_index = mag.index(max(mag))
print(f"Highest magnitude Earthquake took place at: {place[max_mag_index]}")
