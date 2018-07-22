from requests import get, post
import json

BASE_URL = 'http://parasite.wormbase.org'
HEADERS = {
    'Content-Type':'application/json',
    'Accept':'application/json'
}

def wormbase_get(endpoint, query=None):
    """Performs an HTTP GET request to the specified endpoint"""
    
    response = get('/'.join([BASE_URL, endpoint]), 
        params=query,
        headers=HEADERS)

    if not (200 <= response.status_code < 300):
        raise Exception("Wormbase GET returned with non-200 status code")
    
    response_json = response.json()
    response_json.update({ 'status_code' : response.status_code })
    return response_json

def wormbase_post(endpoint, data=None):
    """Performs an HTTP POST request to the specified endpoint"""

    response = post('/'.join([BASE_URL, endpoint]),
        data=data,
        headers=HEADERS)

    if not (200 < response.status_code < 300):
        raise Exception("Wormbase POST returned with non-200 status code") 

    response_json = response.json()
    response_json.update({ 'status_code' : response.status_code })
    return response_json
