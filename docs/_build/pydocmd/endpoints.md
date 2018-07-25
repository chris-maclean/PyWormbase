<h1 id="pywormbase.endpointGroups">pywormbase.endpointGroups</h1>


<h2 id="pywormbase.endpointGroups.comparative_genomics">pywormbase.endpointGroups.comparative_genomics</h2>


<h3 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin">ComparativeGenomicsMixin</h3>

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


<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_dump">get_gene_tree_dump</h4>

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

`See also`: http://parasite.wormbase.org/rest/documentation/info/genetree


<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_by_member">get_gene_tree_by_member</h4>

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

`See also`: http://parasite.wormbase.org/rest/documentation/info/genetree_member_id


<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_gene_tree_with_gene">get_gene_tree_with_gene</h4>

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

`See also`: http://parasite.wormbase.org/rest/documentation/info/genetree_member_symbol


<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_orthologues_by_gene">get_orthologues_by_gene</h4>

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

`See also`: http://parasite.wormbase.org/rest/documentation/info/homology_ensemblgene


<h4 id="pywormbase.endpointGroups.comparative_genomics.ComparativeGenomicsMixin.get_orthologues_by_symbol">get_orthologues_by_symbol</h4>

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


`See also`: http://parasite.wormbase.org/rest/documentation/info/homology_symbol


<h2 id="pywormbase.endpointGroups.cross_references">pywormbase.endpointGroups.cross_references</h2>


<h3 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin">CrossReferencesMixin</h3>

```python
CrossReferencesMixin(self, /, *args, **kwargs)
```

<h4 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_symbol">get_xrefs_for_symbol</h4>

```python
CrossReferencesMixin.get_xrefs_for_symbol(self, species, symbol, db_type=None, external_db=None, object_type=None)
```
http://parasite.wormbase.org/rest/documentation/info/xref_external
<h4 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_id">get_xrefs_for_id</h4>

```python
CrossReferencesMixin.get_xrefs_for_id(self, id, all_levels=False, db_type='core', external_db=None, object_type=None, species=None)
```
http://parasite.wormbase.org/rest/documentation/info/xref_id
<h4 id="pywormbase.endpointGroups.cross_references.CrossReferencesMixin.get_xrefs_for_gene_and_species">get_xrefs_for_gene_and_species</h4>

```python
CrossReferencesMixin.get_xrefs_for_gene_and_species(self, gene_name, species, db_type='core', external_db=None)
```
http://parasite.wormbase.org/rest/documentation/info/xref_name
<h2 id="pywormbase.endpointGroups.information">pywormbase.endpointGroups.information</h2>


<h3 id="pywormbase.endpointGroups.information.InformationMixin">InformationMixin</h3>

```python
InformationMixin(self, /, *args, **kwargs)
```

<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_assemblies_for_species">get_assemblies_for_species</h4>

```python
InformationMixin.get_assemblies_for_species(self, species, bands=False)
```
http://parasite.wormbase.org/rest/documentation/info/assembly_info
<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_genome">get_info_for_genome</h4>

```python
InformationMixin.get_info_for_genome(self, genome_name, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genome
<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_all_genomes">get_info_for_all_genomes</h4>

```python
InformationMixin.get_info_for_all_genomes(self, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genomes
<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_genome_with_assembly">get_info_for_genome_with_assembly</h4>

```python
InformationMixin.get_info_for_genome_with_assembly(self, assembly_id, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genomes_assembly
<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_info_for_taxonomy_node">get_info_for_taxonomy_node</h4>

```python
InformationMixin.get_info_for_taxonomy_node(self, taxon_name, expand=False)
```
http://parasite.wormbase.org/rest/documentation/info/info_genomes_taxonomy
<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_quality_scores_for_genome">get_quality_scores_for_genome</h4>

```python
InformationMixin.get_quality_scores_for_genome(self, genome_name)
```
http://parasite.wormbase.org/rest/documentation/info/info_quality_name
<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_release_info">get_release_info</h4>

```python
InformationMixin.get_release_info(self)
```
http://parasite.wormbase.org/rest/documentation/info/info_wormbase_version
<h4 id="pywormbase.endpointGroups.information.InformationMixin.get_available_species">get_available_species</h4>

```python
InformationMixin.get_available_species(self)
```
http://parasite.wormbase.org/rest/documentation/info/species
<h2 id="pywormbase.endpointGroups.lookup">pywormbase.endpointGroups.lookup</h2>


<h3 id="pywormbase.endpointGroups.lookup.LookupMixin">LookupMixin</h3>

```python
LookupMixin(self, /, *args, **kwargs)
```

<h4 id="pywormbase.endpointGroups.lookup.LookupMixin.lookup_by_id">lookup_by_id</h4>

```python
LookupMixin.lookup_by_id(self, id, db_type=None, expand=False, format='full', species=None)
```
http://parasite.wormbase.org/rest/documentation/info/lookup
<h4 id="pywormbase.endpointGroups.lookup.LookupMixin.lookup_by_name">lookup_by_name</h4>

```python
LookupMixin.lookup_by_name(self, name, biotypes=None, level='gene', xrefs=None)
```
http://parasite.wormbase.org/rest/documentation/info/lookup_genome
<h4 id="pywormbase.endpointGroups.lookup.LookupMixin.batch_lookup_by_id">batch_lookup_by_id</h4>

```python
LookupMixin.batch_lookup_by_id(self, ids, db_type=None, expand=False, format='full', object_type=None, species=None)
```
http://parasite.wormbase.org/rest/documentation/info/lookup_post
<h4 id="pywormbase.endpointGroups.lookup.LookupMixin.get_symbol_from_external_db">get_symbol_from_external_db</h4>

```python
LookupMixin.get_symbol_from_external_db(self, species, symbol, expand=False, format='full')
```
http://parasite.wormbase.org/rest/documentation/info/symbol_lookup
<h4 id="pywormbase.endpointGroups.lookup.LookupMixin.batch_get_symbol_from_external_db">batch_get_symbol_from_external_db</h4>

```python
LookupMixin.batch_get_symbol_from_external_db(self, species, symbols, expand=False, format='full')
```
http://parasite.wormbase.org/rest/documentation/info/symbol_post
<h2 id="pywormbase.endpointGroups.mapping">pywormbase.endpointGroups.mapping</h2>

Support for the Mapping endpoints of the Wormbase REST API

The endpoints available are:

```
/map/cdna/:id/:region
/map/cds/:id/:region
/map/translation/:id/:region
```


<h3 id="pywormbase.endpointGroups.mapping.MappingMixin">MappingMixin</h3>

```python
MappingMixin(self, /, *args, **kwargs)
```

<h4 id="pywormbase.endpointGroups.mapping.MappingMixin.cdna2genomic">cdna2genomic</h4>

```python
MappingMixin.cdna2genomic(self, id, object_type, region, species=None)
```
https://parasite.wormbase.org/rest/documentation/info/assembly_cdna
<h4 id="pywormbase.endpointGroups.mapping.MappingMixin.cds2genomic">cds2genomic</h4>

```python
MappingMixin.cds2genomic(self, id, object_type, region, species=None)
```
https://parasite.wormbase.org/rest/documentation/info/assembly_cds
<h4 id="pywormbase.endpointGroups.mapping.MappingMixin.protein2genomic">protein2genomic</h4>

```python
MappingMixin.protein2genomic(self, id, region, object_type=None, species=None)
```
https://parasite.wormbase.org/rest/documentation/info/assembly_translation
<h2 id="pywormbase.endpointGroups.ontology">pywormbase.endpointGroups.ontology</h2>


<h3 id="pywormbase.endpointGroups.ontology.OntologyMixin">OntologyMixin</h3>

```python
OntologyMixin(self, /, *args, **kwargs)
```

<h4 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ancestry">get_ancestry</h4>

```python
OntologyMixin.get_ancestry(self, id, ontology=None)
```
https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors
<h4 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ancestry_chart">get_ancestry_chart</h4>

```python
OntologyMixin.get_ancestry_chart(self, id, ontology=None)
```
https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors_chart
<h4 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_descendants">get_descendants</h4>

```python
OntologyMixin.get_descendants(self, id, closest_term=False, ontology=None, subset=None, zero_distance=False)
```
https://parasite.wormbase.org/rest/documentation/info/ontology_descendants
<h4 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ontology_by_id">get_ontology_by_id</h4>

```python
OntologyMixin.get_ontology_by_id(self, id, relation=False, simple=False)
```
https://parasite.wormbase.org/rest/documentation/info/ontology_id
<h4 id="pywormbase.endpointGroups.ontology.OntologyMixin.get_ontology_by_name">get_ontology_by_name</h4>

```python
OntologyMixin.get_ontology_by_name(self, name, ontology=None, relation=None, simple=False)
```
https://parasite.wormbase.org/rest/documentation/info/ontology_name
<h2 id="pywormbase.endpointGroups.overlap">pywormbase.endpointGroups.overlap</h2>


<h3 id="pywormbase.endpointGroups.overlap.OverlapMixin">OverlapMixin</h3>

```python
OverlapMixin(self, /, *args, **kwargs)
```

<h4 id="pywormbase.endpointGroups.overlap.OverlapMixin.get_overlapping_features">get_overlapping_features</h4>

```python
OverlapMixin.get_overlapping_features(self, feature, id, biotype=None, db_type=None, logic_name=None, misc_set=None, object_type=None, species=None, species_set='mammals')
```
https://parasite.wormbase.org/rest/documentation/info/overlap_id
<h4 id="pywormbase.endpointGroups.overlap.OverlapMixin.get_overlap_by_region">get_overlap_by_region</h4>

```python
OverlapMixin.get_overlap_by_region(self, feature, region, species, biotype=None, cell_type=None, db_type='core', logic_name=None, misc_set=None, object_type=None, species_set='mammals', trim_downstream=False, trim_upstream=False)
```
https://parasite.wormbase.org/rest/documentation/info/overlap_region
<h4 id="pywormbase.endpointGroups.overlap.OverlapMixin.get_features_for_translation">get_features_for_translation</h4>

```python
OverlapMixin.get_features_for_translation(self, id, db_type=None, feature='protein_feature', species=None, data_type=None)
```
https://parasite.wormbase.org/rest/documentation/info/overlap_translation
<h2 id="pywormbase.endpointGroups.sequence">pywormbase.endpointGroups.sequence</h2>


<h3 id="pywormbase.endpointGroups.sequence.SequenceMixin">SequenceMixin</h3>

```python
SequenceMixin(self, /, *args, **kwargs)
```

<h4 id="pywormbase.endpointGroups.sequence.SequenceMixin.get_sequence">get_sequence</h4>

```python
SequenceMixin.get_sequence(self, id, db_type=None, expand_3prime=None, expand_5prime=None, data_format=None, mask=None, mask_feature=False, multiple_sequences=False, object_type=None, species=None, sequence_type='genomic')
```
https://parasite.wormbase.org/rest/documentation/info/sequence_id
<h4 id="pywormbase.endpointGroups.sequence.SequenceMixin.batch_get_sequence">batch_get_sequence</h4>

```python
SequenceMixin.batch_get_sequence(self, ids, db_type=None, expand_3prime=None, expand_5prime=None, mask=None, mask_feature=False, multiple_sequences=False, object_type=None, species=None, sequence_type='genomic')
```
https://parasite.wormbase.org/rest/documentation/info/sequence_id_post
<h4 id="pywormbase.endpointGroups.sequence.SequenceMixin.get_sequence_for_region">get_sequence_for_region</h4>

```python
SequenceMixin.get_sequence_for_region(self, region, species, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, mask=None, mask_feature=False, data_format=None)
```
https://parasite.wormbase.org/rest/documentation/info/sequence_region
<h4 id="pywormbase.endpointGroups.sequence.SequenceMixin.batch_get_sequence_for_region">batch_get_sequence_for_region</h4>

```python
SequenceMixin.batch_get_sequence_for_region(self, species, regions, data_format=None, coord_system=None, coord_system_version=None, expand_3prime=None, expand_5prime=None, mask=None, mask_feature=False)
```
https://parasite.wormbase.org/rest/documentation/info/sequence_region_post
