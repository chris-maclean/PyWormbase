from .util import wormbase_get, wormbase_post

class MappingMixin:
    """A mixin with methods for accessing the Information section of the Wormbase ParaSite REST API

    This mixin provides access to the following endpoints:

    ```
    GET /map/cdna/:id/:region
    GET /map/cds/:id/:region
    GET /map/translation/:id/:region
    ```

    Any arguments listed with a `*` are required

    """

    def cdna2genomic(self,
        id,
        object_type,
        region,
        species=None):
        """`GET /map/cdna/:id/:region`
                
        # Arguments
        id* (str): A stable ID
        object_type* (str): Object type
        region* (str): Query region
        species (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.cdna2genomic('Bm4789', 'transcript', '100..300')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/assembly_cdna
        
        """

        params = {
            'object_type': object_type,
            'species': species
        }

        return wormbase_get('{}/map/cdna/{}/{}'.format(self.version_string, id, region), query=params)

    def cds2genomic(self,
        id,
        object_type,
        region,
        species=None):
        """`GET /map/cds/:id/:region`
                
        # Arguments
        id* (str): A stable ID
        object_type* (str): Object type
        region* (str): Query region
        species (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.cds2genomic('Bm4789', 'transcript', '1..300')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/assembly_cds
         
        """
        
        params = {
            'object_type': object_type,
            'species': species
        }

        return wormbase_get('{}/map/cds/{}/{}'.format(self.version_string, id, region), query=params)

    def protein2genomic(self,
        id,
        region,
        object_type=None,
        species=None):
        """`GET /map/translation/:id/:region`
                
        # Arguments
        id* (str): A stable ID
        region* (str): Query region
        object_type (str): Object type
        species (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.cds2genomic('Bm4789', '1..100')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/assembly_translation
        
        """
        
        params = {
            'object_type': object_type,
            'species': species
        }

        return wormbase_get('{}/map/translation/{}/{}'.format(self.version_string, id, region), query=params)
