#Start code here
import requests
import json
URL = "https://api.nasa.gov/planetary/apod?api_key=" + "cpOIyD3wNNTcmfRzbisEjAytRfGwQv8fOkPdNDzh"
r = requests.get(URL)
data = r.json()
copyright2 = data['copyright']
date = data['date']
title = data['title']
#Additional activity # your own code
explanation = data['explanation']
img_url = data['hdurl']
print("Copyright:  " + copyright2)
print("Title:  " + title)
print("Date:  " + date)
print("Image URL:  " + img_url)
print("Explanation: + explanation)
print("Note: Open the Image URL in a new tab to see the image")
