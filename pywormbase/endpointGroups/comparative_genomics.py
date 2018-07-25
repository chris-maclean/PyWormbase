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
            nh_format (str): Default: 'simple'
            sequence (str): Default: 'protein'

            # Example
            ```python
            client = pywormbase.WormbaseClient()
            client.get_gene_tree_dump('WBGT00000000021203')
            ```
            
            # Returns
            data (dict): a dictionary with the data returned by the API

            See also: http://parasite.wormbase.org/rest/documentation/info/genetree

            """
            
            params = {
                'aligned': aligned,
                'nh_format': nh_format,
                'sequence': sequence
            }

            return wormbase_get(self.version_string + '/genetree/id/' + id, query=params)

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
        nh_format (str): Default: 'simple'
        object_type (str): Default: None
        sequence (str): Default: 'protein'
        species (str): Default: None

        # Example
        ```python
        client = pywormbase.WormbaseClient()
        client.get_gene_tree_by_member('WBGT00000000021203')
        ```

        # Returns
        data (dict): a dictionary with the data returned by the API

        See also: http://parasite.wormbase.org/rest/documentation/info/genetree_member_id

        """

        params = {
            'aligned': aligned,
            'db_type': db_type,
            'nh_format': nh_format,
            'object_type': object_type,
            'sequence': sequence,
            'species': species
        }

        return wormbase_get(self.version_string + '/genetree/member/id/' + id, query=params)

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
        nh_format (str): Default: 'simple'
        object_type (str): Default: None
        sequence (str): Default: 'protein'

        # Example
        ```python
        client = pywormbase.WormbaseClient()
        client.get_gene_tree_with_gene('Bm994', 'brugia_malayi_prjna10729')
        ```

        # Returns
        data (dict): a dictionary with the data returned by the API
        
        See also: http://parasite.wormbase.org/rest/documentation/info/genetree_member_symbol
        
        """
        
        params = {
            'aligned': aligned,
            'db_type': db_type,
            'external_db': external_db,
            'nh_format': nh_format,
            'object_type': object_type,
            'sequence': sequence
        }

        return wormbase_get(self.version_string + '/genetree/member/symbol/' + species + '/' + symbol, query=params)

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
        sequence (str): Must be one of ['none', 'cdna', 'proteint'] Default: 'protein'
        species (str): Default: None
        target_species (str): Default: None
        target_taxon (int): Default: None
        orthologue_type (str): Must be one of ['orthologues', 'paralogues', 'projections', 'all'] Default: 'all'

        # Example
        ```python
        client = pywormbase.WormbaseClient()
        client.get_orthologues_by_gene('WBGene00221255')
        ```

        # Returns
        data (dict): a dictionary with the data returned by the API
        
        See also: http://parasite.wormbase.org/rest/documentation/info/homology_ensemblgene
        
        """

        params = {
            'aligned': aligned,
            'format': response_format,
            'sequence': sequence,
            'species': species,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        return wormbase_get(self.version_string + '/homology/id/' + gene_id, query=params)

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
        sequence (str): Must be one of ['none', 'cdna', 'proteint'] Default: 'protein'
        target_species (str): Default: None
        target_taxon (int): Default: None
        orthologue_type (str): Must be one of ['orthologues', 'paralogues', 'projections', 'all'] Default: 'all'

        # Raises
        Exception: If an invalid value is provided for one of the restricted keyword arguments

        # Example
        ```python
        client = pywormbase.WormbaseClient()
        client.get_orthologues_by_gene('brugia_malayi_prjna10729', 'Bm994')
        ```

        # Returns
        data (dict): a dictionary with the data returned by the API
        
        
        See also: http://parasite.wormbase.org/rest/documentation/info/homology_symbol
        
        """

        params = {
            'aligned': aligned,
            'external_db': external_db,
            'format': response_format,
            'sequence': sequence,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        return wormbase_get(self.version_string + '/homology/symbol/' + species + '/' + symbol, query=params)
