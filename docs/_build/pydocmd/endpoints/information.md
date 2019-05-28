<h1 id="wormbase_parasite.endpoint_groups.information">wormbase_parasite.endpoint_groups.information</h1>


<h2 id="wormbase_parasite.endpoint_groups.information.InformationMixin">InformationMixin</h2>

```python
InformationMixin(self, /, *args, **kwargs)
```
A mixin with methods for accessing the Information section of the Wormbase ParaSite REST API

This mixin provides access to the following endpoints:

```
GET /info/assembly/:species
GET /info/assembly/:species/:region_name
GET /info/genomes/:name
GET /info/genomes
GET /info/genomes/assembly/:assembly_id
GET /info/genomes/taxonomy/:taxon_name
GET /info/quality/:genome_name
GET /info/version
GET /info/species
```

Any arguments listed with a `*` are required


<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_assemblies_for_species">get_assemblies_for_species</h3>

```python
InformationMixin.get_assemblies_for_species(self, species, bands=False)
```
`GET /info/assembly/:species`

__Arguments__

- __species* (str)__: Species name/alias
- __bands (boolean)__: Default: False

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_assemblies_for_species('brugia_malayi_prjna10729')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: http://parasite.wormbase.org/rest/documentation/info/assembly_info__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_info_for_region">get_info_for_region</h3>

```python
InformationMixin.get_info_for_region(self, region_name, species, bands=False)
```
`GET /info/assembly/:species/:region_name`

__Arguments__

- __region_name* (str)__: The (top level) sequence region name
- __species* (str)__: Species name/alias
- __bands (boolean)__: Default: False

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_info_for_region('Bm_v4_Chr2_contig_001', 'brugia_malayi_prjna10729')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/assembly_stats__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_info_for_genome">get_info_for_genome</h3>

```python
InformationMixin.get_info_for_genome(self, genome_name, expand=False)
```
`GET /info/genomes/:name`

__Arguments__

- __name* (str)__: The production name of the genome
- __expand (boolean)__: Default: False

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_info_for_genome('brugia_malayi_prjna10729')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/info_genome__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_info_for_all_genomes">get_info_for_all_genomes</h3>

```python
InformationMixin.get_info_for_all_genomes(self, expand=False)
```
`GET /info/genomes`

__Arguments__

- __expand (boolean)__: Default: False **Warning** Setting this value to `True` can dramatically increase this function's runtime!

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_info_for_all_genomes()
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/info_genomes__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_info_for_genome_with_assembly">get_info_for_genome_with_assembly</h3>

```python
InformationMixin.get_info_for_genome_with_assembly(self, assembly_id, expand=False)
```
`GET /info/genomes/assembly/:assembly_id`

__Arguments__

- __expand (boolean)__: Default: False **Warning** Setting this value to `True` can dramatically increase this function's runtime!

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_info_for_genome_with_assembly('GCA_000951595.1')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/info_genomes_assembly__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_info_for_taxonomy_node">get_info_for_taxonomy_node</h3>

```python
InformationMixin.get_info_for_taxonomy_node(self, taxon_name, expand=False)
```
`GET /info/genomes/taxonomy/:taxon_name`

__Arguments__

- __taxon_name* (str)__: Taxon name or NCBI taxonomy ID
- __expand (boolean)__: Default: False **Warning** Setting this value to `True` can dramatically increase this function's runtime!

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_info_for_taxonomy_node('Brugia')
```

__Returns__

`data (list)`: a list of dictionaries representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/info_genomes_taxonomy__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_quality_scores_for_genome">get_quality_scores_for_genome</h3>

```python
InformationMixin.get_quality_scores_for_genome(self, genome_name)
```
`GET /info/quality/:genome_name`

__Arguments__

- __genome_name* (str)__: The production name of the genome

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_quality_scores_for_genome('brugia_malayi_prjna10729')
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/info_quality_name__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_release_info">get_release_info</h3>

```python
InformationMixin.get_release_info(self)
```
`GET /info/version`

This function takes no arguments, but its response is determined by the API version number specified during initialization of the `WormbaseClient` object.

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_release_info()
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/info_wormbase_version__



<h3 id="wormbase_parasite.endpoint_groups.information.InformationMixin.get_available_species">get_available_species</h3>

```python
InformationMixin.get_available_species(self)
```
`GET /info/species`

__Example__

```python
client = wormbase_parasite.WormbaseClient()
client.get_available_species()
```

__Returns__

`data (dict)`: a dictionary representing the data returned by the API

__See also: https://parasite.wormbase.org/rest/documentation/info/species__



