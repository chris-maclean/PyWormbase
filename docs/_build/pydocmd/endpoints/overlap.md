<h1 id="wormbase_parasite.endpoint_groups.overlap">wormbase_parasite.endpoint_groups.overlap</h1>


<h2 id="wormbase_parasite.endpoint_groups.overlap.OverlapMixin">OverlapMixin</h2>

```python
OverlapMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Overlap section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET /overlap/id/:id
GET /overlap/region/:species/:region
GET /overlap/translation/:id
```

Any arguments listed with a `*` are required


<h3 id="wormbase_parasite.endpoint_groups.overlap.OverlapMixin.get_overlapping_features">get_overlapping_features</h3>

```python
OverlapMixin.get_overlapping_features(self, feature, id, biotype=None, db_type=None, logic_name=None, misc_set=None, object_type=None, species=None, species_set='mammals')
```
`GET overlap/id/:id`

__Arguments__

- __feature* (str)__: The type of feature to retrieve. Must be one or more of ['gene', 'transcript', 'cds', 'exon', 'repeat', 'simple', 'misc'] Multiple values are accepted
- __id* (str)__: A stable ID
- __biotype (str)__: Default: None
- __db_type (str)__: Default: None
- __logic_name (str)__: Default: None
- __misc_set (str)__: Default: None
- __object_type (str)__: Default: None
- __species (str)__: Default: None
- __species_set (str)__: Default: 'mammals'

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_overlapping_features('none', 'WBGene00221255')
```

__Raises__

- `Exception`: If an invalid value is provided for `feature`

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/overlap_id__



<h3 id="wormbase_parasite.endpoint_groups.overlap.OverlapMixin.get_overlap_by_region">get_overlap_by_region</h3>

```python
OverlapMixin.get_overlap_by_region(self, feature, region, species, biotype=None, cell_type=None, db_type='core', logic_name=None, misc_set=None, object_type=None, species_set='mammals', trim_downstream=False, trim_upstream=False)
```
`GET overlap/region/:species/:region`

__Arguments__

- __feature* (str)__: The type of feature to retrieve. Must be one or more of ['gene', 'transcript', 'cds', 'exon', 'repeat', 'simple', 'misc'] Multiple values are accepted
- __region* (str)__: Query region. A maximum of 5MB is allowed to be requested at any one time
- __species* (str)__: Default: None
- __biotype (str)__: Default: None
- __db_type (str)__: Default: None
- __logic_name (str)__: Default: None
- __misc_set (str)__: Default: None
- __object_type (str)__: Default: None

- __species_set (str)__: Default: 'mammals'

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_overlap_by_region('none', 'Bm_v4_Chr2_contig_001:13847151-13862157', 'brugia_malayi_prjna10729')
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/overlap_region__



<h3 id="wormbase_parasite.endpoint_groups.overlap.OverlapMixin.get_features_for_translation">get_features_for_translation</h3>

```python
OverlapMixin.get_features_for_translation(self, id, db_type=None, feature='protein_feature', species=None, data_type=None)
```
`GET overlap/translation/:id`

__Arguments__

- __id* (str)__: A stable ID
- __db_type (str)__: Default: None
- __feature (str)__: The type of feature to retrieve. Must be one or more of ['protein_feature', 'residue_overlap', 'translation_exon']
- __species (str)__: Default: None
- __data_type (str)__: Default: 'none'

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_features_for_translation('Bm4789')
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/overlap_translation__



