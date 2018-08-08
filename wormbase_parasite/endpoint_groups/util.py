from requests import get, post
import urllib
import json
import logging


BASE_URL = 'http://parasite.wormbase.org'
HEADERS = {
    'Content-Type':'application/json',
    'Accept':'application/json'
}

def wormbase_get(endpoint, query=None):
    """Performs an HTTP GET request to the specified endpoint

    This method is not for use outside of the #endpoint_groups module. All requests to the WormBase ParaSite REST API should go through #::pywormbase.WormbaseClient
    
    # Parameters
    endpoint (str): the full endpoint that will be called. Should include the base URL (e.g., `https://parasite.wormbase.org/`), the version identifier(e.g., `/rest/`) as well as the endpoint (e.g., `/genetree/id/WBGT00000000021203`).

    # Arguments
    query (dict): a dictionary of querystring arguments that should be applied to the URL. Default: `None`

    # Raises
    Exception: If Wormbase replies with a non-200 status code

    # Returns
    A dictionary that represents exactly the data returned by the WormBase ParaSite API, converted from a JSON object to a Python dictionary using `requests.Response.json()`
    """

    encoded_endpoint = urllib.parse.quote(endpoint)
    
    response = get('/'.join([BASE_URL, encoded_endpoint]),
        params=query,
        headers=HEADERS)

    if not (200 <= response.status_code < 300):
        raise Exception("Wormbase GET returned with non-200 status code")
    
    return response.json()

def wormbase_post(endpoint, data=None, query=None):
    """Performs an HTTP POST request to the specified endpoint

    This method is not for use outside of the #endpoint_groups module. All requests to the WormBase ParaSite REST API should go through #::pywormbase.WormbaseClient
    
    # Parameters
    endpoint (str): the full endpoint that will be called. Should include the base URL (e.g., `https://parasite.wormbase.org/`), version identifier (e.g., `/rest/`) as well as the endpoint (e.g., `/lookup/id`)

    # Arguments
    data (str): a JSON-encoded string holding the payload for the POST request. Default: `None`.
    query (dict): a dictionary of querystring arguments that should be applied to the URL. Default: `None`

    # Raises
    Exception: If Wormbase replies with a non-200 status code

    # Returns
    A dictionary that represents exactly the data returned by the WormBase ParaSite API, converted from a JSON object to a Python dictionary using `requests.Response.json()`
    """

    encoded_endpoint = urllib.parse.quote(endpoint)

    response = post('/'.join([BASE_URL, encoded_endpoint]),
        params=query,
        data=json.dumps(data),
        headers=HEADERS)

    if not (200 <= response.status_code < 300):
        print(response)
        raise Exception("Wormbase POST returned with non-200 status code") 

    return response.json()
