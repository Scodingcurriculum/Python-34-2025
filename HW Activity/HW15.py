#Start code here
from weather import Weather
weather = Weather()
list_temp = []
cities = ["London", "Paris", "New York", "Tokyo"]
lat = [51.5074456, 48.8575, 40.7127281, 35.6768601]
lon = [-0.1277653, 2.3514, -74.0060152, 139.7638947]
for i in range(0, 4):
  city = weather.get_current_weather(lat[i], lon[i])
  list_temp.append(float(city.temperature))
  print("Temperature of " + cities[i] + ":   " + str(city.temperature))
# Find a city with max temperature # your own code
index = list_temp.index(max(list_temp))
print(f"City with highest temperature : {cities[index]}")
# Find a city with min temperature # your own code
index = list_temp.index(min(list_temp))
print(f"City with lowes temperature : {cities[index]}")
