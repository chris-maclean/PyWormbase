<h1 id="wormbase_parasite.endpoint_groups.util">wormbase_parasite.endpoint_groups.util</h1>


<h2 id="wormbase_parasite.endpoint_groups.util.wormbase_get">wormbase_get</h2>

```python
wormbase_get(endpoint, query=None)
```
Performs an HTTP GET request to the specified endpoint

This method is not for use outside of the `endpoint_groups` module. All requests to the WormBase ParaSite REST API should go through #::pywormbase.WormbaseClient

__Parameters__

- __endpoint (str)__: the full endpoint that will be called. Should include the base URL (e.g., `https://parasite.wormbase.org/`), the version identifier(e.g., `/rest/`) as well as the endpoint (e.g., `/genetree/id/WBGT00000000021203`).

__Arguments__

- __query (dict)__: a dictionary of querystring arguments that should be applied to the URL. Default: `None`

__Raises__

- `Exception`: If Wormbase replies with a non-200 status code

__Returns__

A dictionary that represents exactly the data returned by the WormBase ParaSite API, converted from a JSON object to a Python dictionary using `requests.Response.json()`

<h2 id="wormbase_parasite.endpoint_groups.util.wormbase_post">wormbase_post</h2>

```python
wormbase_post(endpoint, data=None, query=None)
```
Performs an HTTP POST request to the specified endpoint

This method is not for use outside of the `endpoint_groups` module. All requests to the WormBase ParaSite REST API should go through #::pywormbase.WormbaseClient

__Parameters__

- __endpoint (str)__: the full endpoint that will be called. Should include the base URL (e.g., `https://parasite.wormbase.org/`), version identifier (e.g., `/rest/`) as well as the endpoint (e.g., `/lookup/id`)

__Arguments__

- __data (str)__: a JSON-encoded string holding the payload for the POST request. Default: `None`.
- __query (dict)__: a dictionary of querystring arguments that should be applied to the URL. Default: `None`

__Raises__

- `Exception`: If Wormbase replies with a non-200 status code

__Returns__

A dictionary that represents exactly the data returned by the WormBase ParaSite API, converted from a JSON object to a Python dictionary using `requests.Response.json()`

