<h1 id="pywormbase.endpointGroups">pywormbase.endpointGroups</h1>


<h2 id="pywormbase.endpointGroups.mapping">pywormbase.endpointGroups.mapping</h2>

Support for the Mapping endpoints of the Wormbase REST API

The endpoints available are:

```
/map/cdna/:id/:region
/map/cds/:id/:region
/map/translation/:id/:region
```


<h2 id="pywormbase.endpointGroups.comparative_genomics">pywormbase.endpointGroups.comparative_genomics</h2>


<h3 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin">ComparativeGenomicsMixin</h3>

```python
ComparativeGenomicsMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Comparative Genomics section of the Wormbase REST API

This mixin provides access to the following endpoints:

```
GET /genetree/id/:id
GET /genetree/member/id/:id
GET /genetree/member/symbol/:species/:symbol
GET /homology/id/:id
GET /homology/symbol/:species/:symbol
```

<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_dump">get_gene_tree_dump</h4>

```python
ComparativeGenomicsMixin.get_gene_tree_dump(self, id, aligned=False, nh_format='simple', sequence='protein')
```
GET /genetree/id/:id

__Parameters__

- __id __: str
    a genetree ID like _WBGT00000000021203_

__Keyword Arguments__

aligned : boolean
    Returns the aligned string if true. Otherwise, return the original sequence (no insertions)
    Default: False

See http://parasite.wormbase.org/rest/documentation/info/genetree for more details

<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_by_member">get_gene_tree_by_member</h4>

```python
ComparativeGenomicsMixin.get_gene_tree_by_member(self, id, aligned=False, db_type='core', nh_format='simple', object_type=None, sequence='protein', species=None)
```
http://parasite.wormbase.org/rest/documentation/info/genetree_member_id
<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_with_gene">get_gene_tree_with_gene</h4>

```python
ComparativeGenomicsMixin.get_gene_tree_with_gene(self, symbol, species, aligned=False, db_type='core', external_db=None, nh_format='simple', object_type=None, sequence='protein')
```
http://parasite.wormbase.org/rest-10/documentation/info/genetree_member_symbol
<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_orthologues_by_gene">get_orthologues_by_gene</h4>

```python
ComparativeGenomicsMixin.get_orthologues_by_gene(self, gene_id, aligned=True, format='full', sequence='protein', species=None, target_species=None, target_taxon=None, orthologue_type='all')
```
http://parasite.wormbase.org/rest-10/documentation/info/homology_ensemblgene
<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_orthologues_by_symbol">get_orthologues_by_symbol</h4>

```python
ComparativeGenomicsMixin.get_orthologues_by_symbol(self, species, symbol, aligned=True, external_db=None, format='full', sequence='protein', target_species=None, target_taxon=None, orthologue_type='all')
```
http://parasite.wormbase.org/rest-10/documentation/info/homology_symbol
<h2 id="pywormbase.endpointGroups.cross_references">pywormbase.endpointGroups.cross_references</h2>


<h2 id="pywormbase.endpointGroups.information">pywormbase.endpointGroups.information</h2>


<h2 id="pywormbase.endpointGroups.ontology">pywormbase.endpointGroups.ontology</h2>


<h2 id="pywormbase.endpointGroups.overlap">pywormbase.endpointGroups.overlap</h2>


<h2 id="pywormbase.endpointGroups.sequence">pywormbase.endpointGroups.sequence</h2>


<h2 id="pywormbase.endpointGroups.util">pywormbase.endpointGroups.util</h2>


<h3 id="pywormbase.endpointGroups.util.wormbase_get">wormbase_get</h3>

```python
wormbase_get(endpoint, query=None)
```
Performs an HTTP GET request to the specified endpoint

__Parameters__

endpoint [str] - the full endpoint that will be called. Should include the version identifier(e.g., `/rest-10/`) as well as the operation identifier(e.g., `/genetree/id/WBGT00000000021203`)

__Arguments__

- __query [dict] - a dictionary of querystring arguments that should be applied to the URL. Default__: `None`

__Raises__

Exception - if Wormbase replies with a non-200 status code

__Returns__

A dict with the following keys

    status_code - the HTTP status code associated with the response
    data - precisely what is returned by the Wormbase REST API

<h3 id="pywormbase.endpointGroups.util.wormbase_post">wormbase_post</h3>

```python
wormbase_post(endpoint, data=None, query=None)
```
Performs an HTTP POST request to the specified endpoint

__Parameters__

endpoint [str] - the full endpoint that will be called. Should include the version identifier(e.g., `/rest-10/`) as well as the operation identifier(e.g., `/lookup/id`)

__Arguments__

- __data [str] - a JSON-encoded string holding the payload for the POST request. Default__: `None`.

- __query [dict] - a dictionary of querystring arguments that should be applied to the URL. Default__: `None`

__Raises__

Exception - if Wormbase replies with a non-200 status code

__Returns__

A dict with the following keys

    status_code - the HTTP status code associated with the response
    data - precisely what is returned by the Wormbase REST API

