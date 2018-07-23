<h1 id="pywormbase">pywormbase</h1>


<h2 id="pywormbase.wormbaseClient">pywormbase.wormbaseClient</h2>


<h3 id="pywormbase.wormbaseClient.WormbaseClient">WormbaseClient</h3>

```python
WormbaseClient(self, version=None)
```
The main entry point to all Wormbase interactions

This client inherits from mixins in the endpointGroups module. Those mixins hold the source code that retrieves data from the Wormbase REST API.

Parameters
----------
version : str or int
          The desired REST API version number. This number will be included in the base URL when making calls to the API. Omit to use the latest version. Visit http://parasite.wormbase.org/rest/ to see the latest version.

