from .util import wormbase_get, wormbase_post

class InformationMixin:
    """A mixin with methods for accessing the Information section of the Wormbase ParaSite REST API

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

    """
    
    def get_assemblies_for_species(self, species, bands=False):
        """`GET /info/assembly/:species`
        
        # Arguments
        species* (str): Species name/alias
        bands (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_assemblies_for_species('brugia_malayi_prjna10729')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: http://parasite.wormbase.org/rest/documentation/info/assembly_info
        
        """

        params = {
            'bands': int(bands)
        }

        return wormbase_get('{}/info/assembly/{}'.format(self.version_string, species), query=params)

    def get_info_for_region(self, region_name, species, bands=False):
        """`GET /info/assembly/:species/:region_name`
        
        # Arguments
        region_name* (str): The (top level) sequence region name
        species* (str): Species name/alias
        bands (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_info_for_region('Bm_v4_Chr2_contig_001', 'brugia_malayi_prjna10729')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/assembly_stats
        
        """

        params = {
            'bands': int(bands)
        }

        return wormbase_get('{}/info/assembly/{}/{}'.format(self.version_string, species, region_name), query=params)

    def get_info_for_genome(self, genome_name, expand=False):
        """`GET /info/genomes/:name`
        
        # Arguments
        name* (str): The production name of the genome
        expand (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_info_for_genome('brugia_malayi_prjna10729')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/info_genome
        
        """

        params = {
            'expand': int(expand)
        }

        return wormbase_get('{}/info/genomes/{}'.format(self.version_string, genome_name), query=params)

    def get_info_for_all_genomes(self, expand=False):
        """`GET /info/genomes`
        
        # Arguments
        expand (boolean): Default: False **Warning** Setting this value to `True` can dramatically increase this function's runtime!

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_info_for_all_genomes()
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/info_genomes
        
        """

        params = {
            'expand': int(expand)
        }

        return wormbase_get('{}/info/genomes'.format(self.version_string), query=params)

    def get_info_for_genome_with_assembly(self, assembly_id, expand=False):
        """`GET /info/genomes/assembly/:assembly_id`
        
        # Arguments
        expand (boolean): Default: False **Warning** Setting this value to `True` can dramatically increase this function's runtime!

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_info_for_genome_with_assembly('GCA_000951595.1')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/info_genomes_assembly
        
        """

        params = {
            'expand': int(expand)
        }

        return wormbase_get('{}/info/genomes/assembly/{}'.format(self.version_string, assembly_id), query=params)

    def get_info_for_taxonomy_node(self, taxon_name, expand=False):
        """`GET /info/genomes/taxonomy/:taxon_name`
        
        # Arguments
        taxon_name* (str): Taxon name or NCBI taxonomy ID
        expand (boolean): Default: False **Warning** Setting this value to `True` can dramatically increase this function's runtime!

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_info_for_taxonomy_node('Brugia')
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/info_genomes_taxonomy
        
        """

        params = {
            'expand': int(expand)
        }

        return wormbase_get('{}/info/genomes/taxonomy/{}'.format(self.version_string, taxon_name), query=params)

    def get_quality_scores_for_genome(self, genome_name):
        """`GET /info/quality/:genome_name`
        
        # Arguments
        genome_name* (str): The production name of the genome

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_quality_scores_for_genome('brugia_malayi_prjna10729')
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/info_quality_name
        
        """

        return wormbase_get('{}/info/quality/{}'.format(self.version_string, genome_name))

    def get_release_info(self):
        """`GET /info/version`

        This function takes no arguments, but its response is determined by the API version number specified during initialization of the `WormbaseClient` object.
        
        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_release_info()
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/info_wormbase_version
        
        """

        return wormbase_get('{}/info/version/'.format(self.version_string))

    def get_available_species(self):
        """`GET /info/species`

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_available_species()
        ```

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/species
        
        """

        return wormbase_get('{}/info/species'.format(self.version_string))
