from .util import wormbase_get, wormbase_post

class OntologyMixin:
    """A mixin with methods for accessing the Ontology section of the Wormbase ParaSite REST API
    
    This mixin provides access to the following endpoints:

    ```
    GET /ontology/ancestors/:id
    GET /ontology/ancestors/chart/:id
    GET /ontology/descendants/:id
    GET /ontology/id/:id
    GET /ontology/name/:name
    ```

    Any arguments listed with a `*` are required

    """
    def get_ancestry(self,
        id,
        ontology=None):
        """`GET ontology/ancestors/:id`

        # Arguments
        id* (str): an ontology term identifier
        ontology (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_ancestry('GO:0005667')
        ```

        # Returns
        data (list): a list of dictionaries describing the ancestors of the given gene
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors
        
        """

        params = {
            'ontology': ontology
        }

        return wormbase_get(self.version_string + '/ontology/ancestors/' + id, query=params)

    def get_ancestry_chart(self,
        id,
        ontology=None):
        """`GET /ontology/ancestors/chart/:id`
        
        # Arguments
        id* (str): an ontology term identifier
        ontology (str): Default: None

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_ancestry_chart('GO:0005667')
        ```

        # Returns
        data (dict): a list of dictionaries reconstructing the entire ancestry of a term from is_a and part_of relationships the ancestors of the given gene
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors_chart
        
       """

        params = {
            'ontology': ontology
        }

        return wormbase_get(self.version_string + '/ontology/ancestors/chart/' + id, query=params)

    def get_descendants(self,
        id,
        closest_term=False,
        ontology=None,
        subset=None,
        zero_distance=False):
        """`GET /ontology/descendants/:id`
        
        # Arguments
        id* (str): an ontology term identifier
        closest_term (boolean): Default: False
        ontology (str): Default: None
        subset (str): Default: None
        zero_distance (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_descendants('GO:0005667')
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest-10/documentation/info/ontology_descendants
        
       """

        params = {
            'ontology': ontology,
            'closest_term': int(closest_term),
            'subset': subset,
            'zero_distance': int(zero_distance)
        }

        return wormbase_get(self.version_string + '/ontology/descendants/' + id, query=params)

    def get_ontology_by_id(self,
        id,
        relation=False,
        simple=False):
        """`GET ontology/id/:id`
        
        # Arguments
        id* (str): an ontology term identifier
        relation (str): Default: None
        simple (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_ontology_by_id('GO:0005667')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/ontology_id
         
        """

        params = {
            'relation': relation,
            'simple': int(simple)
        }

        return wormbase_get(self.version_string + '/ontology/id/' + id, query=params)

    def get_ontology_by_name(self,
        name,
        ontology=None,
        relation=None,
        simple=False):
        """`GET ontology/id/:id`
        
        # Arguments
        name* (str): an ontology name. SQL wildcards are supported
        ontology (str): Default: None
        relation (str): Default: None
        simple (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_ontology_by_name('transcription factor complex')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/ontology_name
         
        """

        params = {
            'ontology': ontology,
            'relation': relation,
            'simple': int(simple)
        }

        return wormbase_get(self.version_string + '/ontology/name/' + name, query=params)
