<h1 id="pywormbase.endpointGroups.lookup">pywormbase.endpointGroups.lookup</h1>


<h2 id="pywormbase.endpointGroups.lookup.LookupMixin">LookupMixin</h2>

```python
LookupMixin(self, /, *args, **kwargs)
```

<h3 id="pywormbase.endpointGroups.lookup.LookupMixin.lookup_by_id">lookup_by_id</h3>

```python
LookupMixin.lookup_by_id(self, id, db_type=None, expand=False, format='full', species=None)
```
http://parasite.wormbase.org/rest/documentation/info/lookup
<h3 id="pywormbase.endpointGroups.lookup.LookupMixin.lookup_by_name">lookup_by_name</h3>

```python
LookupMixin.lookup_by_name(self, name, biotypes=None, level='gene', xrefs=None)
```
http://parasite.wormbase.org/rest/documentation/info/lookup_genome
<h3 id="pywormbase.endpointGroups.lookup.LookupMixin.batch_lookup_by_id">batch_lookup_by_id</h3>

```python
LookupMixin.batch_lookup_by_id(self, ids, db_type=None, expand=False, format='full', object_type=None, species=None)
```
http://parasite.wormbase.org/rest/documentation/info/lookup_post
<h3 id="pywormbase.endpointGroups.lookup.LookupMixin.get_symbol_from_external_db">get_symbol_from_external_db</h3>

```python
LookupMixin.get_symbol_from_external_db(self, species, symbol, expand=False, format='full')
```
http://parasite.wormbase.org/rest/documentation/info/symbol_lookup
<h3 id="pywormbase.endpointGroups.lookup.LookupMixin.batch_get_symbol_from_external_db">batch_get_symbol_from_external_db</h3>

```python
LookupMixin.batch_get_symbol_from_external_db(self, species, symbols, expand=False, format='full')
```
http://parasite.wormbase.org/rest/documentation/info/symbol_post
