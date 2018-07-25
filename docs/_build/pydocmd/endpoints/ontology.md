<h1 id="pywormbase.endpointGroups.ontology">pywormbase.endpointGroups.ontology</h1>


<h2 id="pywormbase.endpointGroups.ontology.OntologyMixin">OntologyMixin</h2>

```python
OntologyMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Ontology section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET /ontology/ancestors/:id
GET /ontology/ancestors/chart/:id
GET /ontology/descendants/:id
GET /ontology/id/:id
GET /ontology/name/:name
```

Any arguments listed with a `*` are required


<h3 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ancestry">get_ancestry</h3>

```python
OntologyMixin.get_ancestry(self, id, ontology=None)
```
`GET ontology/ancestors/:id`

__Arguments__

- __id* (str)__: an ontology term identifier
- __ontology (str)__: Default: None

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_ancestry('GO:0005667')
```

__Returns__

`data (list)`: a list of dictionaries describing the ancestors of the given gene

__See also: https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors__



<h3 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ancestry_chart">get_ancestry_chart</h3>

```python
OntologyMixin.get_ancestry_chart(self, id, ontology=None)
```
`GET /ontology/ancestors/chart/:id`

__Arguments__

- __id* (str)__: an ontology term identifier
- __ontology (str)__: Default: None

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_ancestry_chart('GO:0005667')
```

__Returns__

`data (dict)`: a list of dictionaries reconstructing the entire ancestry of a term from is_a and part_of relationships the ancestors of the given gene

__See also: https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors_chart__



<h3 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_descendants">get_descendants</h3>

```python
OntologyMixin.get_descendants(self, id, closest_term=False, ontology=None, subset=None, zero_distance=False)
```
`GET /ontology/descendants/:id`

__Arguments__

- __id* (str)__: an ontology term identifier
- __ontology (str)__: Default: None

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_ancestry_chart('GO:0005667')
```

__Returns__

`data (dict)`: a list of dictionaries reconstructing the entire ancestry of a term from is_a and part_of relationships the ancestors of the given gene

__See also: https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors_chart__



<h3 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ontology_by_id">get_ontology_by_id</h3>

```python
OntologyMixin.get_ontology_by_id(self, id, relation=False, simple=False)
```
https://parasite.wormbase.org/rest/documentation/info/ontology_id
<h3 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ontology_by_name">get_ontology_by_name</h3>

```python
OntologyMixin.get_ontology_by_name(self, name, ontology=None, relation=None, simple=False)
```
https://parasite.wormbase.org/rest/documentation/info/ontology_name
