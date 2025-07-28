#Start code here
from weather import Weather
weather = Weather()
cities = ["New York", "Paris", "Tokyo", "Sydney"]
list_of_lats = [40.7128, 48.8566, 35.6895, -33.8688]
list_of_longs = [-74.0060, +2.3522, 139.6917, 151.2093]
for i in cities:
  pos = cities.index(i)
  city = weather.get_current_weather(list_of_lats[pos], list_of_longs[pos])
  print("-------------Weather Report------------------")
  print("Name of the city:  " + i)
  print("Temperature: " + str(city.temperature) + " °C")
  print("Wind speed: " + str(city.wind_speed) + " km/h")
  print("Conditions:  " + str(city.conditions))
  print("--------------------------------------------------")
  city = ""
  variable_name = 0
