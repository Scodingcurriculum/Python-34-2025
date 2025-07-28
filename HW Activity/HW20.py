#Start code here
import requests
import json
country = input("Enter the name of Country: ")
URL = f"https://restcountries.com/v3.1/name/{country}"
r = requests.get(URL)
data = r.json()[0]
capital = data.get('capital', ['Unknown'])[0]
Population = data.get('population')
region = data.get('region')
print(f"Title: {country}")
print(f"Capital: {capital}")
print(f"Region: {region}")
print(f"Population:{Population}")
