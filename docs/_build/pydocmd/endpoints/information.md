<h1 id="pywormbase.endpointGroups.information">pywormbase.endpointGroups.information</h1>


<h2 id="pywormbase.endpointGroups.information.InformationMixin">InformationMixin</h2>

```python
InformationMixin(self, /, *args, **kwargs)
```

<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_assemblies_for_species">get_assemblies_for_species</h3>

```python
InformationMixin.get_assemblies_for_species(self, species, bands=False)
```
http://parasite.wormbase.org/rest/documentation/info/assembly_info
<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_genome">get_info_for_genome</h3>

```python
InformationMixin.get_info_for_genome(self, genome_name, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genome
<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_all_genomes">get_info_for_all_genomes</h3>

```python
InformationMixin.get_info_for_all_genomes(self, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genomes
<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_genome_with_assembly">get_info_for_genome_with_assembly</h3>

```python
InformationMixin.get_info_for_genome_with_assembly(self, assembly_id, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genomes_assembly
<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_taxonomy_node">get_info_for_taxonomy_node</h3>

```python
InformationMixin.get_info_for_taxonomy_node(self, taxon_name, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genomes_taxonomy
<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_quality_scores_for_genome">get_quality_scores_for_genome</h3>

```python
InformationMixin.get_quality_scores_for_genome(self, genome_name)
```
http://parasite.wormbase.org/rest/documentation/info/info_quality_name
<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_release_info">get_release_info</h3>

```python
InformationMixin.get_release_info(self)
```
http://parasite.wormbase.org/rest/documentation/info/info_wormbase_version
<h3 id="pywormbase.endpointGroups.information.InformationMixin.get_available_species">get_available_species</h3>

```python
InformationMixin.get_available_species(self)
```
http://parasite.wormbase.org/rest/documentation/info/species
