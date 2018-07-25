<h1 id="pywormbase.endpointGroups.cross_references">pywormbase.endpointGroups.cross_references</h1>


<h2 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin">CrossReferencesMixin</h2>

```python
CrossReferencesMixin(self, /, *args, **kwargs)
```

<h3 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_symbol">get_xrefs_for_symbol</h3>

```python
CrossReferencesMixin.get_xrefs_for_symbol(self, species, symbol, db_type=None, external_db=None, object_type=None)
```
http://parasite.wormbase.org/rest/documentation/info/xref_external
<h3 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_id">get_xrefs_for_id</h3>

```python
CrossReferencesMixin.get_xrefs_for_id(self, id, all_levels=False, db_type='core', external_db=None, object_type=None, species=None)
```
http://parasite.wormbase.org/rest/documentation/info/xref_id
<h3 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_gene_and_species">get_xrefs_for_gene_and_species</h3>

```python
CrossReferencesMixin.get_xrefs_for_gene_and_species(self, gene_name, species, db_type='core', external_db=None)
```
http://parasite.wormbase.org/rest/documentation/info/xref_name
