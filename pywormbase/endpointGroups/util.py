from requests import get, post
import json
import logging

BASE_URL = 'http://parasite.wormbase.org'
HEADERS = {
    'Content-Type':'application/json',
    'Accept':'application/json'
}

def wormbase_get(endpoint, query=None):
    """Performs an HTTP GET request to the specified endpoint
    
    # Parameters
    endpoint [str] - the full endpoint that will be called. Should include the version identifier(e.g., `/rest/`) as well as the operation identifier(e.g., `/genetree/id/WBGT00000000021203`)

    # Arguments
    query [dict] - a dictionary of querystring arguments that should be applied to the URL. Default: `None`

    # Raises
    Exception - if Wormbase replies with a non-200 status code

    # Returns
    A dict with the following keys 
    
        status_code - the HTTP status code associated with the response
        data - precisely what is returned by the Wormbase REST API
    """
    
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
    """Performs an HTTP POST request to the specified endpoint
    
    # Parameters
    endpoint [str] - the full endpoint that will be called. Should include the version identifier(e.g., `/rest/`) as well as the operation identifier(e.g., `/lookup/id`)

    # Arguments
    data [str] - a JSON-encoded string holding the payload for the POST request. Default: `None`.

    query [dict] - a dictionary of querystring arguments that should be applied to the URL. Default: `None`

    # Raises
    Exception - if Wormbase replies with a non-200 status code

    # Returns
    A dict with the following keys 
    
        status_code - the HTTP status code associated with the response
        data - precisely what is returned by the Wormbase REST API
    """

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
    
