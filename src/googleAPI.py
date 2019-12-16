import os
import requests
import json
import time
from dotenv import load_dotenv
load_dotenv()

def googleAPI(query):
    authToken = os.getenv("key")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}".format(query,authToken)
    res = requests.get(url).json()
    location ={}
    if res['status']!='ZERO_RESULTS' and res['status']!='REQUEST_DENIED' and res['status']!='INVALID_REQUEST':
        latitude = res['results'][0]['geometry']['location']['lat']
        longitude = res['results'][0]['geometry']['location']['lng']
        location['type']='Point'
        location['coordinates']=[longitude, latitude]
    else:
        location['type']='Point'
        location['coordinates']='No hay coincidencias'
    return location

def get_lat_long(result):
    latitude = result['geometry']['location']['lat']
    longitude = result['geometry']['location']['lng']
    location = {
            'type':'Point',
            'coordinates':[longitude, latitude]
        }
    return location