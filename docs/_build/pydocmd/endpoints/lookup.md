<h1 id="wormbase_parasite.endpoint_groups.lookup">wormbase_parasite.endpoint_groups.lookup</h1>


<h2 id="wormbase_parasite.endpoint_groups.lookup.LookupMixin">LookupMixin</h2>

```python
LookupMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Information section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET /lookup/id/:id
GET /lookup/genome/:name
POST /lookup/id
GET /lookup/symbol/:species/:symbol
POST /lookup/symbol/:species/:symbol
```

Any arguments listed with a `*` are required


<h3 id="wormbase_parasite.endpoint_groups.lookup.LookupMixin.lookup_by_id">lookup_by_id</h3>

```python
LookupMixin.lookup_by_id(self, id, db_type=None, expand=False, format='full', species=None)
```
`GET lookup/id/:id`

__Arguments__

- __id* (str)__: A stable ID
- __db_type (str)__: Default: None
- __expand (boolean)__: Default: False
- __format (str)__: Must be one of ['full', 'condensed'] Default: 'full'
- __species (str)__: Default: None

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.lookup_by_id('WBGene00221255')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest-10/documentation/info/lookup__



<h3 id="wormbase_parasite.endpoint_groups.lookup.LookupMixin.lookup_by_name">lookup_by_name</h3>

```python
LookupMixin.lookup_by_name(self, name, biotypes=None, level='gene', xrefs=False)
```
`GET lookup/genome/:name`

__Arguments__

- __name* (str)__: The production name of the genome
- __biotypes (str)__: Default: None
- __level (str)__: Must be one of ['gene', 'transcript', 'translation', 'protein_feature'] Default: 'gene'
- __xrefs (boolean)__: Default: False

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.lookup_by_id('WBGene00221255')
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest-10/documentation/info/lookup_genome__



<h3 id="wormbase_parasite.endpoint_groups.lookup.LookupMixin.batch_lookup_by_id">batch_lookup_by_id</h3>

```python
LookupMixin.batch_lookup_by_id(self, ids, db_type=None, expand=False, format='full', object_type=None, species=None)
```
`POST lookup/id`

__Arguments__

- __ids* (str or list)__: A comma-separated string of gene IDs, or a list of these IDs
- __db_type (str)__: Default: None
- __expand (boolean)__: Default: False
- __format (str)__: Must be one of ['full', 'condensed'] Default: 'full'
- __object_type (str)__: Default: None
- __species (str)__: Default: None

__Example__

```python
client = wormbase_parasite.WormbaseClient()
id_list = ["WBGene00221255", "__VAR(gene_stable_id_2)__" ]
client.batch_lookup_by_id(id_list)
id_string = "WBGene00221255,__VAR(gene_stable_id_2)__"
client.batch_lookup_by_id(id_string)
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest-10/documentation/info/lookup_post__



<h3 id="wormbase_parasite.endpoint_groups.lookup.LookupMixin.get_symbol_from_external_db">get_symbol_from_external_db</h3>

```python
LookupMixin.get_symbol_from_external_db(self, species, symbol, expand=False, format='full')
```
`GET lookup/symbol/:species/:symbol`

__Arguments__

- __species* (str)__: Species name/alias
- __symbol* (str)__: A name or symbol from an annotation source that has been linked to a genetic feature
- __expand (boolean)__: Default: False
- __format (str)__: Must be one of ['full', 'condensed'] Default: 'full'

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.batch_lookup_by_id('brugia_malayi_prjna10729', 'Bm994')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API


__See also: http://parasite.wormbase.org/rest/documentation/info/symbol_lookup__



<h3 id="wormbase_parasite.endpoint_groups.lookup.LookupMixin.batch_get_symbol_from_external_db">batch_get_symbol_from_external_db</h3>

```python
LookupMixin.batch_get_symbol_from_external_db(self, species, symbols, expand=False, format='full')
```
`POST lookup/symbol/:species`

__Arguments__

- __species* (str)__: Species name/alias
- __symbols* (str or list)__: A comma-separated string of symbols, or a list of these symbols
- __expand (boolean)__: Default: False
- __format (str)__: Must be one of ['full', 'condensed'] Default: 'full'

__Example__

```python
client = wormbase_parasite.WormbaseClient()
symbol_list = ["Bm994", "__VAR(gene_symbol2)__"]
client.batch_get_symbol_from_external_db('brugia_malayi_prjna10729', symbol_list)
symbol_string = "Bm994,__VAR(gene_symbol2)__"
client.batch_get_symbol_from_external_db('brugia_malayi_prjna10729', symbol_string)
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API


__See also: https://parasite.wormbase.org/rest-10/documentation/info/symbol_post__



