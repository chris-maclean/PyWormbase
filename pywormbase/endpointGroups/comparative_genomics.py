from .util import wormbase_get, wormbase_post

class ComparativeGenomicsMixin:
    """A mixin with methods for accessing the Comparative Genomics section of the Wormbase REST API
    
    This mixin provides access to the following endpoints:

    ```
    GET /genetree/id/:id
    GET /genetree/member/id/:id
    GET /genetree/member/symbol/:species/:symbol
    GET /homology/id/:id
    GET /homology/symbol/:species/:symbol
    ```
    """
    
    def get_gene_tree_dump(self, 
            id,
            aligned=False, 
            nh_format='simple', 
            sequence='protein'):
            """`GET /genetree/id/:id`

            http://parasite.wormbase.org/rest/documentation/info/genetree

            # Parameters
            id (str) a genetree ID like _WBGT00000000021203_

            # Arguments
            aligned (boolean) Default: False
            nh_format (str) Default: 'simple'
            sequence (str) Default: 'protein'
            
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
        id (str): a genetree ID like 'WBGT00000000021203'
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
        """http://parasite.wormbase.org/rest/documentation/info/genetree_member_symbol"""
        
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
        format='full',
        sequence='protein',
        species=None,
        target_species=None,
        target_taxon=None,
        orthologue_type='all'):
        """http://parasite.wormbase.org/rest/documentation/info/homology_ensemblgene"""

        params = {
            'aligned': aligned,
            'format': format,
            'sequence': sequence,
            'species': species,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        return wormbase_get(self.version_string + '/homology/id/' + id, query=params)

    def get_orthologues_by_symbol(self,
        species,
        symbol,
        aligned=True,
        external_db=None,
        format='full',
        sequence='protein',
        target_species=None,
        target_taxon=None,
        orthologue_type='all'):
        """http://parasite.wormbase.org/rest/documentation/info/homology_symbol"""

        params = {
            'aligned': aligned,
            'external_db': external_db,
            'format': format,
            'sequence': sequence,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        return wormbase_get(self.version_string + '/homology/symbol/' + species + '/' + symbol, query=params)
