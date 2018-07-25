<h1 id="pywormbase">pywormbase</h1>


<h2 id="pywormbase.wormbaseClient">pywormbase.wormbaseClient</h2>


<h3 id="pywormbase.wormbaseClient.WormbaseClient">WormbaseClient</h3>

```python
WormbaseClient(self, version=None)
```
The main entry point to all Wormbase ParaSite interactions

This client inherits from mixins in the `endpointGroups` module. Those mixins hold the source code that retrieves data from the Wormbase REST API.

__Arguments__

- __version (str or int)__: The desired REST API version number. This number will be included in the base URL when making calls to the API. Omit to use the latest version. Visit http://parasite.wormbase.org/rest/ to see the latest version.


__Example__

```python
>>> import pywormbase
>>> api_latest = pywormbase.WormbaseClient()
>>> api_latest.get_release_info()
{'status_code': 200, 'data': {'wbps_release': '10', 'wb_release': '263'}}
>>> api_v9 = pywormbase.WormbaseClient(9)
>>> api_v9.get_release_info()
{'status_code': 200, 'data': {'wbps_release': '9', 'wb_release': '258'}}
```

See also: http://parasite.wormbase.org/rest/

