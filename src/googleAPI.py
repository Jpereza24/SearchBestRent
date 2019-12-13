import os
import requests
import json
import time
from dotenv import load_dotenv
load_dotenv()

def searchPlaces(query, location):
    API_key = os.getenv('key')
    endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    places = []
    params = {
        'query': query,
        'location': location,
        'radius': 0.25,
        'key': API_key
    }
    res = requests.get(endpoint_url, params = params)
    results =  json.loads(res.content)
    places.extend(results['results'])
    time.sleep(2)
    while "next_page_token" in results:
        params['pagetoken'] = results['next_page_token'],
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
    return places


def getLocationAPI(result):
    location = []
    for i in range(len(result)):
        latitude = result[i]['geometry']['location']['lat']
        longitude = result[i]['geometry']['location']['lng']
        name = result[i]['name']
        address = result[i]['formatted_address']
        loc = {
            'name': name,
            'address': address,
            'location':{
                'type':'Point',
                'coordinates':[longitude,latitude]
            }
        }
        location.append(loc)
    return location  