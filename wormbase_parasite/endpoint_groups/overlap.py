from .util import wormbase_get, wormbase_post

class OverlapMixin:
    """A mixin with methods for accessing the Overlap section of the Wormbase ParaSite REST API
    
    This mixin provides access to the following endpoints:

    ```
    GET /overlap/id/:id
    GET /overlap/region/:species/:region
    GET /overlap/translation/:id
    ```

    Any arguments listed with a `*` are required

    """

    def get_overlapping_features(self,
        feature,
        id,
        biotype=None,
        db_type=None,
        logic_name=None,
        misc_set=None,
        object_type=None,
        species=None,
        species_set='mammals'):
        """`GET overlap/id/:id`
        
        # Arguments
        feature* (str): The type of feature to retrieve. Must be one or more of ['gene', 'transcript', 'cds', 'exon', 'repeat', 'simple', 'misc'] Multiple values are accepted
        id* (str): A stable ID
        biotype (str): Default: None
        db_type (str): Default: None
        logic_name (str): Default: None
        misc_set (str): Default: None
        object_type (str): Default: None
        species (str): Default: None
        species_set (str): Default: 'mammals'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_overlapping_features('none', 'WBGene00221255')
        ```

        # Raises
        Exception: If an invalid value is provided for `feature`

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/overlap_id
         
        """

        ALLOWED_FEATURES = [
            'gene',
            'transcript',
            'cds',
            'exon',
            'repeat',
            'simple',
            'misc'
        ]

        if not feature in ALLOWED_FEATURES:
            raise Exception('Feature type {} not a valid argument. Allowed features are {}'
                .format(feature, ALLOWED_FEATURES))

        params = {
            'feature': feature,
            'biotype': biotype,
            'db_type': db_type,
            'logic_name': logic_name,
            'misc_set': misc_set,
            'object_type': object_type,
            'species': species,
            'species_set': species_set
        }

        return wormbase_get(self.version_string + '/overlap/id/' + id, query=params)

    def get_overlap_by_region(self,
        feature,
        region,
        species,
        biotype=None,
        cell_type=None,
        db_type='core',
        logic_name=None,
        misc_set=None,
        object_type=None,
        species_set='mammals',
        trim_downstream=False,
        trim_upstream=False):
        """`GET overlap/region/:species/:region`
        
        # Arguments
        feature* (str): The type of feature to retrieve. Must be one or more of ['gene', 'transcript', 'cds', 'exon', 'repeat', 'simple', 'misc'] Multiple values are accepted
        region* (str): Query region. A maximum of 5MB is allowed to be requested at any one time
        species* (str): Default: None
        biotype (str): Default: None
        db_type (str): Default: None
        logic_name (str): Default: None
        misc_set (str): Default: None
        object_type (str): Default: None

        species_set (str): Default: 'mammals'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_overlap_by_region('none', 'Bm_v4_Chr2_contig_001:13847151-13862157', 'brugia_malayi_prjna10729')
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/overlap_region
         
        """

        ALLOWED_FEATURES = [
            'gene',
            'transcript',
            'cds',
            'exon',
            'repeat',
            'simple',
            'misc'
        ]

        if not feature in ALLOWED_FEATURES:
            raise Exception('Feature type {} not a valid argument. Allowed features are {}'
                            .format(feature, ALLOWED_FEATURES))

        params = {
            'feature': feature,
            'biotype': biotype,
            'cell_type': cell_type,
            'db_type': db_type,
            'logic_name': logic_name,
            'misc_set': misc_set,
            'object_type': object_type,
            'species_set': species_set,
            'trim_upstream': int(trim_upstream),
            'trim_downstream': int(trim_downstream)
        }

        return wormbase_get(self.version_string + '/overlap/region/' + species + '/' + region, query=params)

    def get_features_for_translation(self,
        id,
        db_type=None,
        feature='protein_feature',
        species=None,
        data_type=None):
        """`GET overlap/translation/:id`
        
        # Arguments
        id* (str): A stable ID
        db_type (str): Default: None
        feature (str): The type of feature to retrieve. Must be one or more of ['protein_feature', 'residue_overlap', 'translation_exon']
        species (str): Default: None
        data_type (str): Default: 'none'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_features_for_translation('Bm4789')
        ```

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/overlap_translation
         
        """

        ALLOWED_FEATURES = [
            'protein_feature',
            'residue_overlap',
            'translation_exon'
        ]

        if not feature in ALLOWED_FEATURES:
            raise Exception('Feature type {} not a valid argument. Allowed features are {}'
                .format(feature, ALLOWED_FEATURES))

        params = {
            'db_type': db_type,
            'feature': feature,
            'species': species,
            'type': data_type
        }

        return wormbase_get(self.version_string + '/overlap/translation/' + id, query=params)
