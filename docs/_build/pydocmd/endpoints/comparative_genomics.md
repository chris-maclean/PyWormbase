<h1 id="pywormbase.endpointGroups.comparative_genomics">pywormbase.endpointGroups.comparative_genomics</h1>


<h2 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin">ComparativeGenomicsMixin</h2>

```python
ComparativeGenomicsMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Comparative Genomics section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET /genetree/id/:id
GET /genetree/member/id/:id
GET /genetree/member/symbol/:species/:symbol
GET /homology/id/:id
GET /homology/symbol/:species/:symbol
```

Any arguments listed with a `*` are required


<h3 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_dump">get_gene_tree_dump</h3>

```python
ComparativeGenomicsMixin.get_gene_tree_dump(self, id, aligned=False, nh_format='simple', sequence='protein')
```
`GET /genetree/id/:id`

__Arguments__

- __id* (str)__: a genetree ID like 'WBGT00000000021203'
- __aligned (boolean)__: Default: False
- __nh_format (str)__: Default: 'simple'
- __sequence (str)__: Default: 'protein'

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_gene_tree_dump('WBGT00000000021203')
```

__Returns__

`data (dict)`: a dictionary with the data returned by the API

__See also: http://parasite.wormbase.org/rest/documentation/info/genetree__



<h3 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_by_member">get_gene_tree_by_member</h3>

```python
ComparativeGenomicsMixin.get_gene_tree_by_member(self, id, aligned=False, db_type='core', nh_format='simple', object_type=None, sequence='protein', species=None)
```
`GET /genetree/id/:id`

__Arguments__

- __id* (str)__: a genetree ID like 'WBGT00000000021203'
- __aligned (boolean)__: Default: False
- __db_type (str)__: Default: 'core'
- __nh_format (str)__: Default: 'simple'
- __object_type (str)__: Default: None
- __sequence (str)__: Default: 'protein'
- __species (str)__: Default: None

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_gene_tree_by_member('WBGT00000000021203')
```

__Returns__

`data (dict)`: a dictionary with the data returned by the API

__See also: http://parasite.wormbase.org/rest/documentation/info/genetree_member_id__



<h3 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_with_gene">get_gene_tree_with_gene</h3>

```python
ComparativeGenomicsMixin.get_gene_tree_with_gene(self, symbol, species, aligned=False, db_type='core', external_db=None, nh_format='simple', object_type=None, sequence='protein')
```
`GET genetree/member/symbol/:species/:symbol`

__Arguments__

- __symbol* (str)__: Symbol or display name of a gene
- __species* (str)__: species name/alias
- __aligned (boolean)__: Default: False
- __db_type (str)__: Default: 'core'
- __external_db (str)__: Default: None
- __nh_format (str)__: Default: 'simple'
- __object_type (str)__: Default: None
- __sequence (str)__: Default: 'protein'

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_gene_tree_with_gene('Bm994', 'brugia_malayi_prjna10729')
```

__Returns__

`data (dict)`: a dictionary with the data returned by the API

__See also: http://parasite.wormbase.org/rest/documentation/info/genetree_member_symbol__



<h3 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_orthologues_by_gene">get_orthologues_by_gene</h3>

```python
ComparativeGenomicsMixin.get_orthologues_by_gene(self, gene_id, aligned=True, response_format='full', sequence='protein', species=None, target_species=None, target_taxon=None, orthologue_type='all')
```
`GET homology/id/:id`

__Arguments__

- __gene_id* (str)__: A stable ID
- __aligned (boolean)__: Default: True
- __response_format (str)__: Must be one of ['full', 'condensed'] Default: 'full'
- __sequence (str)__: Must be one of ['none', 'cdna', 'proteint'] Default: 'protein'
- __species (str)__: Default: None
- __target_species (str)__: Default: None
- __target_taxon (int)__: Default: None
- __orthologue_type (str)__: Must be one of ['orthologues', 'paralogues', 'projections', 'all'] Default: 'all'

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_orthologues_by_gene('WBGene00221255')
```

__Returns__

`data (dict)`: a dictionary with the data returned by the API

__See also: http://parasite.wormbase.org/rest/documentation/info/homology_ensemblgene__



<h3 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_orthologues_by_symbol">get_orthologues_by_symbol</h3>

```python
ComparativeGenomicsMixin.get_orthologues_by_symbol(self, species, symbol, aligned=True, external_db=None, response_format='full', sequence='protein', target_species=None, target_taxon=None, orthologue_type='all')
```
`GET homology/symbol/:species/:symbol`

__Arguments__

- __species* (str)__: Species name/alias
- __symbol* (str)__: Symbol or display name of a gene
- __aligned (boolean)__: Default: True
- __external_db (str)__: Default: None
- __response_format (str)__: Must be one of ['full', 'condensed'] Default: 'full'
- __sequence (str)__: Must be one of ['none', 'cdna', 'proteint'] Default: 'protein'
- __target_species (str)__: Default: None
- __target_taxon (int)__: Default: None
- __orthologue_type (str)__: Must be one of ['orthologues', 'paralogues', 'projections', 'all'] Default: 'all'

__Raises__

- `Exception`: If an invalid value is provided for one of the restricted keyword arguments

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_orthologues_by_gene('brugia_malayi_prjna10729', 'Bm994')
```

__Returns__

`data (dict)`: a dictionary with the data returned by the API


__See also: http://parasite.wormbase.org/rest/documentation/info/homology_symbol__



