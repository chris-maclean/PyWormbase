from requests import get, post
import json
import logging

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
    return {
        'status_code': response.status_code,
        'data': response_json
    }

def wormbase_post(endpoint, data=None, query=None):
    """Performs an HTTP POST request to the specified endpoint"""

    response = post('/'.join([BASE_URL, endpoint]),
        params=query,
        data=json.dumps(data),
        headers=HEADERS)

    if not (200 <= response.status_code < 300):
        print(response)
        raise Exception("Wormbase POST returned with non-200 status code") 

    response_json = response.json()

    return {
        'status_code': response.status_code,
        'data': response_json
    }
    