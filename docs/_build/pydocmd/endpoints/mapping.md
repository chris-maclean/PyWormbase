<h1 id="wormbase_parasite.endpoint_groups.mapping">wormbase_parasite.endpoint_groups.mapping</h1>


<h2 id="wormbase_parasite.endpoint_groups.mapping.MappingMixin">MappingMixin</h2>

```python
MappingMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Information section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET /map/cdna/:id/:region
GET /map/cds/:id/:region
GET /map/translation/:id/:region
```

Any arguments listed with a `*` are required


<h3 id="wormbase_parasite.endpoint_groups.mapping.MappingMixin.cdna2genomic">cdna2genomic</h3>

```python
MappingMixin.cdna2genomic(self, id, object_type, region, species=None)
```
`GET /map/cdna/:id/:region`

__Arguments__

- __id* (str)__: A stable ID
- __object_type* (str)__: Object type
- __region* (str)__: Query region
- __species (str)__: Default: None

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.cdna2genomic('Bm4789', 'transcript', '100..300')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/assembly_cdna__



<h3 id="wormbase_parasite.endpoint_groups.mapping.MappingMixin.cds2genomic">cds2genomic</h3>

```python
MappingMixin.cds2genomic(self, id, object_type, region, species=None)
```
`GET /map/cds/:id/:region`

__Arguments__

- __id* (str)__: A stable ID
- __object_type* (str)__: Object type
- __region* (str)__: Query region
- __species (str)__: Default: None

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.cds2genomic('Bm4789', 'transcript', '1..300')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/assembly_cds__



<h3 id="wormbase_parasite.endpoint_groups.mapping.MappingMixin.protein2genomic">protein2genomic</h3>

```python
MappingMixin.protein2genomic(self, id, region, object_type=None, species=None)
```
`GET /map/translation/:id/:region`

__Arguments__

- __id* (str)__: A stable ID
- __region* (str)__: Query region
- __object_type (str)__: Object type
- __species (str)__: Default: None

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.cds2genomic('Bm4789', '1..100')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/assembly_translation__



