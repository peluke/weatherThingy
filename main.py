import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
from geopy import geocoders

g = geocoders.GoogleV3(os.environ.get('api_key'))
wapiURL = os.environ.get('wapiURL')
inputAddress = input("City:")
#do the geocode
location = g.geocode(inputAddress, timeout=10)
wapi = wapiURL + str(location.latitude) + '&lon=' + str(location.longitude)

json_data = requests.get(wapi).json()
temp_k = json_data['main']['temp']
temp_f = str((temp_k - 273.15) * 1.8 + 32)


print(location.latitude, location.longitude)
# print(zipcode)
# print(location.raw)
print(location.address)
print(temp_f[0:4])