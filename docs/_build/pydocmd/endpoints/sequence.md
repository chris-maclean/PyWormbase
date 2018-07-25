<h1 id="pywormbase.endpointGroups.sequence">pywormbase.endpointGroups.sequence</h1>


<h2 id="pywormbase.endpointGroups.sequence.SequenceMixin">SequenceMixin</h2>

```python
SequenceMixin(self, /, *args, **kwargs)
```

<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.get_sequence">get_sequence</h3>

```python
SequenceMixin.get_sequence(self, id, db_type=None, expand_3prime=None, expand_5prime=None, data_format=None, mask=None, mask_feature=False, multiple_sequences=False, object_type=None, species=None, sequence_type='genomic')
```
https://parasite.wormbase.org/rest/documentation/info/sequence_id
<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.batch_get_sequence">batch_get_sequence</h3>

```python
SequenceMixin.batch_get_sequence(self, ids, db_type=None, expand_3prime=None, expand_5prime=None, mask=None, mask_feature=False, multiple_sequences=False, object_type=None, species=None, sequence_type='genomic')
```
https://parasite.wormbase.org/rest/documentation/info/sequence_id_post
<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.get_sequence_for_region">get_sequence_for_region</h3>

```python
SequenceMixin.get_sequence_for_region(self, region, species, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, mask=None, mask_feature=False, data_format=None)
```
https://parasite.wormbase.org/rest/documentation/info/sequence_region
<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin.batch_get_sequence_for_region">batch_get_sequence_for_region</h3>

```python
SequenceMixin.batch_get_sequence_for_region(self, species, regions, data_format=None, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, mask=None, mask_feature=False)
```
https://parasite.wormbase.org/rest/documentation/info/sequence_region_post
