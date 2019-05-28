from .util import wormbase_get, wormbase_post

class ComparativeGenomicsMixin:
    """A mixin with methods for accessing the Comparative Genomics section of the Wormbase ParaSite REST API
    
    This mixin provides access to the following endpoints:

    ```
    GET /genetree/id/:id
    GET /genetree/member/id/:id
    GET /genetree/member/symbol/:species/:symbol
    GET /homology/id/:id
    GET /homology/symbol/:species/:symbol
    ```

    Any arguments listed with a `*` are required

    """
    
    def get_gene_tree_dump(self, 
        id,
        aligned=False, 
        nh_format='simple', 
        sequence='protein'):
        """`GET /genetree/id/:id`

        # Arguments
        id* (str): a genetree ID like 'WBGT00000000021203'
        aligned (boolean): Default: False
        nh_format (str): Must be one of ['full', 'display_label_composite', 'simple', 'species', 'species_short_name', 'ncbi_taxon', 'ncbi_name', 'njtree', 'phylip'] Default: 'simple'
        sequence (str): Must be one of ['none', 'cdna', 'protein'] Default: 'protein'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_gene_tree_dump('WBGT00000000021203')
        ```
        
        # Returns
        data (dict): a dictionary with the data returned by the API

        # See also: http://parasite.wormbase.org/rest/documentation/info/genetree

        """

        ALLOWED_NH_FORMATS = ['full', 'display_label_composite', 'simple', 'species',
                              'species_short_name', 'ncbi_taxon', 'ncbi_name', 'njtree', 'phylip']
        if nh_format and nh_format not in ALLOWED_NH_FORMATS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(nh_format, ALLOWED_NH_FORMATS))

        ALLOWED_SEQS = ['none', 'cdna', 'protein']
        if sequence and sequence not in ALLOWED_SEQS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(sequence, ALLOWED_SEQS))
        
        params = {
            'aligned': int(aligned),
            'nh_format': nh_format,
            'sequence': sequence
        }

        return wormbase_get('{}/genetree/id/{}'.format(self.version_string, id), query=params)

    def get_gene_tree_by_member(self, 
        id, 
        aligned=False, 
        db_type='core', 
        nh_format='simple', 
        object_type=None, 
        sequence='protein', 
        species=None):
        """`GET /genetree/id/:id`

        # Arguments
        id* (str): a genetree ID like 'WBGT00000000021203'
        aligned (boolean): Default: False
        db_type (str): Default: 'core'
        nh_format (str): Must be one of ['full', 'display_label_composite', 'simple', 'species', 'species_short_name', 'ncbi_taxon', 'ncbi_name', 'njtree', 'phylip'] Default: 'simple'
        object_type (str): Default: None
        sequence (str): Must be one of ['none', 'cdna', 'protein'] Default: 'protein'
        species (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_gene_tree_by_member('WBGT00000000021203')
        ```

        # Returns
        data (dict): a dictionary with the data returned by the API

        # See also: http://parasite.wormbase.org/rest/documentation/info/genetree_member_id

        """

        ALLOWED_NH_FORMATS = ['full', 'display_label_composite', 'simple', 'species',
                              'species_short_name', 'ncbi_taxon', 'ncbi_name', 'njtree', 'phylip']
        if nh_format and nh_format not in ALLOWED_NH_FORMATS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(nh_format, ALLOWED_NH_FORMATS))

        ALLOWED_SEQS = ['none', 'cdna', 'protein']
        if sequence and sequence not in ALLOWED_SEQS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(sequence, ALLOWED_SEQS))

        params = {
            'aligned': int(aligned),
            'db_type': db_type,
            'nh_format': nh_format,
            'object_type': object_type,
            'sequence': sequence,
            'species': species
        }

        return wormbase_get('{}/genetree/member/id/{}'.format(self.version_string, id), query=params)

    def get_gene_tree_with_gene(self,
        symbol,
        species,
        aligned=False,
        db_type='core',
        external_db=None,
        nh_format='simple',
        object_type=None,
        sequence='protein'):
        """`GET genetree/member/symbol/:species/:symbol` 
        
        # Arguments
        symbol* (str): Symbol or display name of a gene
        species* (str): species name/alias
        aligned (boolean): Default: False
        db_type (str): Default: 'core'
        external_db (str): Default: None
        nh_format (str): Must be one of ['full', 'display_label_composite', 'simple', 'species', 'species_short_name', 'ncbi_taxon', 'ncbi_name', 'njtree', 'phylip'] Default: 'simple'
        object_type (str): Default: None
        sequence (str): Must be one of ['none', 'cdna', 'protein'] Default: 'protein'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_gene_tree_with_gene('Bm994', 'brugia_malayi_prjna10729')
        ```

        # Returns
        data (dict): a dictionary with the data returned by the API
        
        # See also: http://parasite.wormbase.org/rest/documentation/info/genetree_member_symbol
        
        """

        ALLOWED_NH_FORMATS = ['full', 'display_label_composite', 'simple', 'species',
                              'species_short_name', 'ncbi_taxon', 'ncbi_name', 'njtree', 'phylip']
        if nh_format and nh_format not in ALLOWED_NH_FORMATS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(nh_format, ALLOWED_NH_FORMATS))

        ALLOWED_SEQS = ['none', 'cdna', 'protein']
        if sequence and sequence not in ALLOWED_SEQS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(sequence, ALLOWED_SEQS))
        
        params = {
            'aligned': int(aligned),
            'db_type': db_type,
            'external_db': external_db,
            'nh_format': nh_format,
            'object_type': object_type,
            'sequence': sequence
        }

        return wormbase_get('{}/genetree/member/symbol/{}/{}'.format(self.version_string, species, symbol), query=params)

    def get_orthologues_by_gene(self,
        gene_id,
        aligned=True,
        response_format='full',
        sequence='protein',
        species=None,
        target_species=None,
        target_taxon=None,
        orthologue_type='all'):
        """`GET homology/id/:id` 
        
        # Arguments
        gene_id* (str): A stable ID
        aligned (boolean): Default: True
        response_format (str): Must be one of ['full', 'condensed'] Default: 'full'
        sequence (str): Must be one of ['none', 'cdna', 'protein'] Default: 'protein'
        species (str): Default: None
        target_species (str): Default: None
        target_taxon (int): Default: None
        orthologue_type (str): Must be one of ['orthologues', 'paralogues', 'projections', 'all'] Default: 'all'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_orthologues_by_gene('WBGene00221255')
        ```

        # Raises
        Exception: If an invalid value is provided for `response_format`, `sequence`, or `orthologue_type`

        # Returns
        data (dict): a dictionary with the data returned by the API
        
        # See also: http://parasite.wormbase.org/rest/documentation/info/homology_ensemblgene
        
        """

        params = {
            'aligned': int(aligned),
            'format': response_format,
            'sequence': sequence,
            'species': species,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        ALLOWED_FORMATS = ['full', 'condensed']
        if response_format and response_format not in ALLOWED_FORMATS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(response_format, ALLOWED_FORMATS))

        ALLOWED_SEQS = ['none', 'cdna', 'protein']
        if sequence and sequence not in ALLOWED_SEQS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(sequence, ALLOWED_SEQS))

        ALLOWED_ORTHOS = ['orthologues', 'paralogues', 'projections', 'all']
        if orthologue_type and orthologue_type not in ALLOWED_ORTHOS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(orthologue_type, ALLOWED_ORTHOS))

        return wormbase_get('{}/homology/id/{}'.format(self.version_string, gene_id), query=params)

    def get_orthologues_by_symbol(self,
        species,
        symbol,
        aligned=True,
        external_db=None,
        response_format='full',
        sequence='protein',
        target_species=None,
        target_taxon=None,
        orthologue_type='all'):
        """`GET homology/symbol/:species/:symbol`

        # Arguments
        species* (str): Species name/alias
        symbol* (str): Symbol or display name of a gene
        aligned (boolean): Default: True
        external_db (str): Default: None
        response_format (str): Must be one of ['full', 'condensed'] Default: 'full'
        sequence (str): Must be one of ['none', 'cdna', 'protein'] Default: 'protein'
        target_species (str): Default: None
        target_taxon (int): Default: None
        orthologue_type (str): Must be one of ['orthologues', 'paralogues', 'projections', 'all'] Default: 'all'

        # Raises
        Exception: If an invalid value is provided for one of the restricted keyword arguments

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_orthologues_by_gene('brugia_malayi_prjna10729', 'Bm994')
        ```

        # Raises
        Exception: If an invalid value is provided for `response_format`, `sequence`, or `orthologue_type`

        # Returns
        data (dict): a dictionary with the data returned by the API
        
        
        # See also: http://parasite.wormbase.org/rest/documentation/info/homology_symbol
        
        """

        ALLOWED_FORMATS = ['full', 'condensed']
        if response_format and response_format not in ALLOWED_FORMATS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(response_format, ALLOWED_FORMATS))

        ALLOWED_SEQS = ['none', 'cdna', 'protein']
        if sequence and sequence not in ALLOWED_SEQS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(sequence, ALLOWED_FORMATS))

        ALLOWED_ORTHOS = ['orthologues', 'paralogues', 'projections', 'all']
        if orthologue_type and orthologue_type not in ALLOWED_ORTHOS:
            raise Exception('Format type {} is not supported. Allowable format values are {}'
                            .format(orthologue_type, ALLOWED_FORMATS))

        params = {
            'aligned': int(aligned),
            'external_db': external_db,
            'format': response_format,
            'sequence': sequence,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        return wormbase_get('{}/homology/symbol/{}/{}/'.format(self.version_string, species, symbol), query=params)
