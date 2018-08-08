from .util import wormbase_get, wormbase_post

class CrossReferencesMixin:
    """A mixin with methods for accessing the Cross References section of the Wormbase ParaSite REST API

    This mixin provides access to the following endpoints:

    ```
    GET /xrefs/symbol/:species/:symbol
    GET /xrefs/id/:id
    GET /xrefs/name/:species/:name
    ```

    Any arguments listed with a `*` are required

    """
    
    def get_xrefs_for_symbol(self, 
        species, 
        symbol, 
        db_type='core', 
        external_db=None, 
        object_type=None):
        """`GET xrefs/symbol/:species/:symbol`

        # Arguments
        species* (str): Species name/alias
        symbol* (str): Symbol or display name of gene
        db_type (str): Default: 'core'
        external_db (str): Default: None
        object_type (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_xrefs_for_symbol('brugia_malayi_prjna10729', 'Bm994')
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: http://parasite.wormbase.org/rest/documentation/info/xref_external
        
        """
        
        params = {
            'db_type': db_type,
            'external_db': external_db,
            'object_type': object_type
        }

        return wormbase_get(self.version_string + '/xrefs/symbol/' + species + '/' + symbol, query=params)

    def get_xrefs_for_id(self, 
        id, 
        all_levels=False, 
        db_type='core', 
        external_db=None, 
        object_type=None, 
        species=None):
        """`GET xrefs/id/:id`

        # Arguments
        id* (str): A Stable ID
        db_type (str): Default: 'core'
        external_db (str): Default: None
        object_type (str): Default: None
        species (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_xrefs_for_id('ENSG00000157764')
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API

        # See also: https://parasite.wormbase.org/rest-10/documentation/info/xref_id

        """

        params = {
            'all_levels': int(all_levels),
            'db_type': db_type,
            'external_db': external_db,
            'object_type': object_type,
            'species': species
        }

        return wormbase_get(self.version_string + '/xrefs/id/' + id, query=params)

    def get_xrefs_for_gene_and_species(self,
        gene_name,
        species,
        db_type='core',
        external_db=None):
        """`GET /xrefs/name/:species/:name`  
        
        # Arguments
        gene_name* (str): Symbol or display name of a gene
        species* (str): Species name/alias
        db_type (str): Default: 'core'
        external_db (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_xrefs_for_gene_and_species('Bm994', 'brugia_malayi_prjna10729')
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API

        # See also: https://parasite.wormbase.org/rest-10/documentation/info/xref_id

        """

        params = {
            'db_type': db_type,
            'external_db': external_db
        }

        return wormbase_get(self.version_string + '/xrefs/name/' + species + '/' + gene_name, query=params)