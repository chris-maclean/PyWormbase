<h1 id="pywormbase.endpointGroups.cross_references">pywormbase.endpointGroups.cross_references</h1>


<h2 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin">CrossReferencesMixin</h2>

```python
CrossReferencesMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Cross References section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET /xrefs/symbol/:species/:symbol
GET /xrefs/id/:id
GET /xrefs/name/:species/:name
```

Any arguments listed with a `*` are required


<h3 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_symbol">get_xrefs_for_symbol</h3>

```python
CrossReferencesMixin.get_xrefs_for_symbol(self, species, symbol, db_type='core', external_db=None, object_type=None)
```
`GET xrefs/symbol/:species/:symbol`

__Arguments__

- __species* (str)__: Species name/alias
- __symbol* (str)__: Symbol or display name of gene
- __db_type (str)__: Default: 'core'
- __external_db (str)__: Default: None
- __object_type (str)__: Default: None

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_xrefs_for_symbol('brugia_malayi_prjna10729', 'Bm994')
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: http://parasite.wormbase.org/rest/documentation/info/xref_external__



<h3 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_id">get_xrefs_for_id</h3>

```python
CrossReferencesMixin.get_xrefs_for_id(self, id, all_levels=False, db_type='core', external_db=None, object_type=None, species=None)
```
`GET xrefs/id/:id`

__Arguments__

- __id* (str)__: A Stable ID
- __db_type (str)__: Default: 'core'
- __external_db (str)__: Default: None
- __object_type (str)__: Default: None
- __species (str)__: Default: None

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_xrefs_for_id('ENSG00000157764')
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest-10/documentation/info/xref_id__



<h3 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_gene_and_species">get_xrefs_for_gene_and_species</h3>

```python
CrossReferencesMixin.get_xrefs_for_gene_and_species(self, gene_name, species, db_type='core', external_db=None)
```
`GET /xrefs/name/:species/:name`

__Arguments__

- __gene_name* (str)__: Symbol or display name of a gene
- __species* (str)__: Species name/alias
- __db_type (str)__: Default: 'core'
- __external_db (str)__: Default: None

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_xrefs_for_gene_and_species('Bm994', 'brugia_malayi_prjna10729')
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest-10/documentation/info/xref_id__



