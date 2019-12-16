import os
import requests
import json
import time
from dotenv import load_dotenv
load_dotenv()

def googleAPI(query):
    #Function to connect with Google API and get the info.
    authToken = os.getenv("key")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}".format(query,authToken)
    res = requests.get(url).json()
    location ={}
    #This conditional is to get the latitude and longitude of the places I require in case there is any result, if there is no results I put the else condition.
    if res['status']!='ZERO_RESULTS' and res['status']!='REQUEST_DENIED' and res['status']!='INVALID_REQUEST':
        latitude = res['results'][0]['geometry']['location']['lat']
        longitude = res['results'][0]['geometry']['location']['lng']
        location['type']='Point'
        location['coordinates']=[longitude, latitude]
    else:
        location['type']='Point'
        location['coordinates']='No hay coincidencias'
    return location

