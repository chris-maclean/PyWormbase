<h1 id="pywormbase.endpointGroups.sequence">pywormbase.endpointGroups.sequence</h1>


<h2 id="pywormbase.endpointGroups.sequence.SequenceMixin">SequenceMixin</h2>

```python
SequenceMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Overlap section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET  /sequence/id/:id
POST /sequence/id
GET  /sequence/region/:species/:region
POST /sequence/region/:species
```

Any arguments listed with a `*` are required


<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.get_sequence">get_sequence</h3>

```python
SequenceMixin.get_sequence(self, id, db_type=None, expand_3prime=None, expand_5prime=None, data_format=None, mask=None, mask_feature=False, multiple_sequences=False, object_type=None, species=None, sequence_type='genomic')
```
`GET sequence/id/:id`

__Arguments__

- __id* (str)__: A stable ID
- __db_type (str)__: Default: None
- __expand_3prime (int)__: Default: None
- __expand_5prime (int)__: Default: None
- __format (str)__: Default: None
- __mask (str)__: Must be one of ['hard', 'soft'] Default: None
- __mask_feature (boolean)__: Default: False
- __multiple_sequences (boolean)__: Default: False
- __object_type (str)__: Default: None
- __species (str)__: Default: None
- __sequence_type (str)__: Must be one of ['genomic', 'cds', 'cdna', 'protein'] Default: 'genomic'

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_sequence('WBGene00221255')
```

__Raises__

- `Exception`: If an invalid value is provided for `format`, `mask`, or `sequence_type`

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/sequence_id__



<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.batch_get_sequence">batch_get_sequence</h3>

```python
SequenceMixin.batch_get_sequence(self, ids, db_type=None, expand_3prime=None, expand_5prime=None, data_format=None, mask=None, mask_feature=False, object_type=None, species=None, sequence_type='genomic')
```
`POST sequence/id`

__Arguments__

- __ids* (str or list)__: A string of comma-separated stable IDs, or a list of these IDs
- __db_type (str)__: Default: None
- __expand_3prime (int)__: Default: None
- __expand_5prime (int)__: Default: None
- __data_format (str)__: Must be one of ['fasta'] Default: None
- __mask (str)__: Must be one of ['hard', 'soft'] Default: None
- __mask_feature (boolean)__: Default: False
- __multiple_sequences (boolean)__: Default: False
- __object_type (str)__: Default: None
- __species (str)__: Default: None
- __sequence_type (str)__: Must be one of ['genomic', 'cds', 'cdna', 'protein'] Default: 'genomic'

__Example__

```python
client = pywormbase.WormbaseClient()
id_list = ["WBGene00221255", "__VAR(gene_stable_id_2)__"]
client.batch_get_sequence(id_list)

id_string = "WBGene00221255,__VAR(gene_stable_id_2)__"
client.batch_get_sequence(id_string)
```

__Raises__

- `Exception`: If an invalid value is provided for `data_format, `mask`, or `sequence_type`

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/sequence_id_post__



<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.get_sequence_for_region">get_sequence_for_region</h3>

```python
SequenceMixin.get_sequence_for_region(self, region, species, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, data_format=None, mask=None, mask_feature=False)
```
`GET sequence/region/:species/:region`

__Arguments__

- __region* (str)__: Query region. A maximum of 10MB is allowed to be requested at any one time
- __species* (str)__: Species name/alias
- __coord_system (str)__: Default: None
- __coord_system_version (str)__: Default: None
- __expand_3prime (int)__: Default: None
- __expand_5prime (int)__: Default: None
- __data_format (str)__: Must be one of ['fasta'] Default: None
- __mask (str)__: Must be one of ['hard', 'soft'] Default: None
- __mask_feature (boolean)__: Default: False

__Example__

```python
client = pywormbase.WormbaseClient()
client.get_sequence_for_region('Bm_v4_Chr2_contig_001:13847151-13862157:1', 'brugia_malayi_prjna10729')
```

__Raises__

- `Exception`: If an invalid value is provided for `data_format`, or `mask`

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/sequence_region__



<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.batch_get_sequence_for_region">batch_get_sequence_for_region</h3>

```python
SequenceMixin.batch_get_sequence_for_region(self, species, regions, data_format=None, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, mask=None, mask_feature=False)
```
`POST sequence/region/:species`

__Arguments__

- __species* (str)__: Species name/alias
- __regions* (str or list)__: A comma-separated string of query regions, or a list of these regions
- __data_format (str)__: Must be one of ['fasta'] Default: None
- __coord_system (str)__: Default: None
- __coord_system_version (str)__: Default: None
- __expand_3prime (int)__: Default: None
- __expand_5prime (int)__: Default: None
- __mask (str)__: Must be one of ['hard', 'soft'] Default: None
- __mask_feature (boolean)__: Default: False

__Example__

```python
client = pywormbase.WormbaseClient()
region_list = ["Bm_v4_Chr2_contig_001:13847151-13862157:1", "Bmal_v3_scaffold139:57600..85000"]
client.batch_get_sequence_for_region('brugia_malayi_prjna10729', region_list)

region_string = "Bm_v4_Chr2_contig_001:13847151-13862157:1,Bmal_v3_scaffold139:57600..85000"
client.batch_get_sequence_for_region('brugia_malayi_prjna10729', region_string)
```

__Raises__

- `Exception`: If an invalid value is provided for `data_format`, or `mask`

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/sequence_region_post__



