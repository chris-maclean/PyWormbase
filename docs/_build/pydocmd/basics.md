<h1 id="wormbase_parasite">wormbase_parasite</h1>


<h2 id="wormbase_parasite.wormbase_client">wormbase_parasite.wormbase_client</h2>


<h3 id="wormbase_parasite.wormbase_client.WormbaseClient">WormbaseClient</h3>

```python
WormbaseClient(self, version=None)
```
The main entry point to all Wormbase ParaSite interactions

This client inherits from mixins in the `endpoint_groups` module. Those mixins hold the source code that retrieves data from the Wormbase REST API.

__Arguments__

- __version (str or int)__: The desired REST API version number. This number will be included in the base URL when making calls to the API. Omit to use the latest version. Visit http://parasite.wormbase.org/rest/ to see the latest version.


__Example__

```python
>>> import wormbase_parasite
>>> api_latest = wormbase_parasite.WormbaseClient()
>>> api_latest.get_release_info()
{'status_code': 200, 'data': {'wbps_release': '10', 'wb_release': '263'}}
>>> api_v9 = wormbase_parasite.WormbaseClient(9)
>>> api_v9.get_release_info()
{'status_code': 200, 'data': {'wbps_release': '9', 'wb_release': '258'}}
```

__See also: http://parasite.wormbase.org/rest/__


