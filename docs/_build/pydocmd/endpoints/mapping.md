<h1 id="pywormbase.endpointGroups.mapping">pywormbase.endpointGroups.mapping</h1>

Support for the Mapping endpoints of the Wormbase REST API

The endpoints available are:

```
/map/cdna/:id/:region
/map/cds/:id/:region
/map/translation/:id/:region
```


<h2 id="pywormbase.endpointGroups.mapping.MappingMixin">MappingMixin</h2>

```python
MappingMixin(self, /, *args, **kwargs)
```

<h3 id="pywormbase.endpointGroups.mapping.MappingMixin.cdna2genomic">cdna2genomic</h3>

```python
MappingMixin.cdna2genomic(self, id, object_type, region, species=None)
```
https://parasite.wormbase.org/rest/documentation/info/assembly_cdna
<h3 id="pywormbase.endpointGroups.mapping.MappingMixin.cds2genomic">cds2genomic</h3>

```python
MappingMixin.cds2genomic(self, id, object_type, region, species=None)
```
https://parasite.wormbase.org/rest/documentation/info/assembly_cds
<h3 id="pywormbase.endpointGroups.mapping.MappingMixin.protein2genomic">protein2genomic</h3>

```python
MappingMixin.protein2genomic(self, id, region, object_type=None, species=None)
```
https://parasite.wormbase.org/rest/documentation/info/assembly_translation
