from .util import wormbase_get, wormbase_post

class LookupMixin:
    """A mixin with methods for accessing the Information section of the Wormbase ParaSite REST API

    This mixin provides access to the following endpoints:

    ```
    GET /lookup/id/:id
    POST /lookup/id
    GET /lookup/symbol/:species/:symbol
    POST /lookup/symbol/:species/:symbol
    ```

    Any arguments listed with a `*` are required

    """
    
    def lookup_by_id(self,
        id,
        db_type=None,
        expand=False,
        format='full',
        species=None):
        """`GET lookup/id/:id`
        
        # Arguments
        id* (str): A stable ID
        db_type (str): Default: None
        expand (boolean): Default: False
        format (str): Must be one of ['full', 'condensed'] Default: 'full'
        species (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.lookup_by_id('WBGene00221255')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/lookup
        
        """

        params = {
            'db_type': db_type,
            'expand': int(expand),
            'format': format,
            'species': species
        }
        return wormbase_get('{}/lookup/id/'.format(self.version_string) + id, query=params)

    def batch_lookup_by_id(self,
        ids,
        db_type=None,
        expand=False,
        format='full',
        object_type=None,
        species=None):
        """`POST lookup/id`
        
        # Arguments
        ids* (str or list): A comma-separated string of gene IDs, or a list of these IDs
        db_type (str): Default: None
        expand (boolean): Default: False
        format (str): Must be one of ['full', 'condensed'] Default: 'full'
        object_type (str): Default: None
        species (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        id_list = ["WBGene00221255", "__VAR(gene_stable_id_2)__" ]
        client.batch_lookup_by_id(id_list)
        id_string = "WBGene00221255,__VAR(gene_stable_id_2)__"
        client.batch_lookup_by_id(id_string)
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/lookup_post
        
        """

        params = {
            'db_type': db_type,
            'expand': int(expand),
            'format': format,
            'object_type': object_type,
            'species': species
        }

        id_list = []
        if type(ids) is str:
            id_list = ids.split(',')
        else:
            id_list = ids
        
        return wormbase_post('{}/lookup/id'.format(self.version_string), query=params, data={ 'ids': id_list })

    def get_symbol_from_external_db(self,
        species,
        symbol,
        expand=False,
        format='full'):
        """`GET lookup/symbol/:species/:symbol`

        # Arguments
        species* (str): Species name/alias
        symbol* (str): A name or symbol from an annotation source that has been linked to a genetic feature
        expand (boolean): Default: False
        format (str): Must be one of ['full', 'condensed'] Default: 'full' 

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.batch_lookup_by_id('brugia_malayi_prjna10729', 'Bm994')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API


        # See also: http://parasite.wormbase.org/rest/documentation/info/symbol_lookup
        
        """
        
        params = {
            'expand': int(expand),
            'format': format
        }

        return wormbase_get('{}/lookup/symbol/{}/{}'.format(self.version_string, species, symbol), query=params)

    def batch_get_symbol_from_external_db(self,
        species,
        symbols,
        expand=False,
        format='full'):
        """`POST lookup/symbol/:species`

        # Arguments
        species* (str): Species name/alias
        symbols* (str or list): A comma-separated string of symbols, or a list of these symbols
        expand (boolean): Default: False
        format (str): Must be one of ['full', 'condensed'] Default: 'full' 

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        symbol_list = ["Bm994", "__VAR(gene_symbol2)__"]
        client.batch_get_symbol_from_external_db('brugia_malayi_prjna10729', symbol_list)
        symbol_string = "Bm994,__VAR(gene_symbol2)__"
        client.batch_get_symbol_from_external_db('brugia_malayi_prjna10729', symbol_string)
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API


        # See also: https://parasite.wormbase.org/rest/documentation/info/symbol_post
        
        """
        
        params = { 
            'expand': int(expand), 
            'format': format
        }

        symbol_list = []
        if type(symbols) is str:
            symbol_list = symbols.split(',')
        else:
            symbol_list = symbols

        return wormbase_post('{}/lookup/symbol/{}/'.format(self.version_string, species), 
                query=params, 
                data={ 'symbols': symbol_list })
