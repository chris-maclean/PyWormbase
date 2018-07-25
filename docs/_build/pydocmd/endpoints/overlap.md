<h1 id="pywormbase.endpointGroups.overlap">pywormbase.endpointGroups.overlap</h1>


<h2 id="pywormbase.endpointGroups.overlap.OverlapMixin">OverlapMixin</h2>

```python
OverlapMixin(self, /, *args, **kwargs)
```

<h3 id="pywormbase.endpointGroups.overlap.OverlapMixin.get_overlapping_features">get_overlapping_features</h3>

```python
OverlapMixin.get_overlapping_features(self, feature, id, biotype=None, db_type=None, logic_name=None, misc_set=None, object_type=None, species=None, species_set='mammals')
```
https://parasite.wormbase.org/rest/documentation/info/overlap_id
<h3 id="pywormbase.endpointGroups.overlap.OverlapMixin.get_overlap_by_region">get_overlap_by_region</h3>

```python
OverlapMixin.get_overlap_by_region(self, feature, region, species, biotype=None, cell_type=None, db_type='core', logic_name=None, misc_set=None, object_type=None, species_set='mammals', trim_downstream=False, trim_upstream=False)
```
https://parasite.wormbase.org/rest/documentation/info/overlap_region
<h3 id="pywormbase.endpointGroups.overlap.OverlapMixin.get_features_for_translation">get_features_for_translation</h3>

```python
OverlapMixin.get_features_for_translation(self, id, db_type=None, feature='protein_feature', species=None, data_type=None)
```
https://parasite.wormbase.org/rest/documentation/info/overlap_translation
