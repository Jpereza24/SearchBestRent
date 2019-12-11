import os
from dotenv import load_dotenv
import base64
import requests as rq
import json
import urllib
load_dotenv()

def get_oauth_token():
    url = "https://api.idealista.com/oauth/token"
    apikey = os.getenv("API_key")
    secretkey = os.getenv("Secret_key")
    key = apikey + ':' + secretkey
    auth = str(base64.b64encode(key.encode("utf-8")), "utf-8")
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8', 'Authorization':'Basic '+ auth}
    params = urllib.parse.urlencode({'grant_type' : 'client_credentials'})
    content = rq.post(url,headers = headers, params=params)
    bearer_token = json.loads(content.text)['access_token']
    return bearer_token

def search_api(token, url):  
    headers = {'Content-Type': 'Content-Type: multipart/form-data;', 'Authorization' : 'Bearer ' + token}
    content = rq.post(url, headers = headers)
    result = json.loads(content.text)
    return result