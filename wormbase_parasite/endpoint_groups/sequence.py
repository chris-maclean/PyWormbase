from .util import wormbase_get, wormbase_post

class SequenceMixin:
    """A mixin with methods for accessing the Overlap section of the Wormbase ParaSite REST API
    
    This mixin provides access to the following endpoints:

    ```
    GET  /sequence/id/:id
    POST /sequence/id
    GET  /sequence/region/:species/:region
    POST /sequence/region/:species
    ```

    Any arguments listed with a `*` are required

    """

    def get_sequence(self,
        id,
        db_type=None,
        expand_3prime=None,
        expand_5prime=None,
        data_format=None,
        mask=None,
        mask_feature=False,
        multiple_sequences=False,
        object_type=None,
        species=None,
        sequence_type='genomic'):
        """`GET sequence/id/:id`
        
        # Arguments
        id* (str): A stable ID
        db_type (str): Default: None
        expand_3prime (int): Default: None
        expand_5prime (int): Default: None
        format (str): Default: None
        mask (str): Must be one of ['hard', 'soft'] Default: None
        mask_feature (boolean): Default: False
        multiple_sequences (boolean): Default: False
        object_type (str): Default: None
        species (str): Default: None
        sequence_type (str): Must be one of ['genomic', 'cds', 'cdna', 'protein'] Default: 'genomic'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_sequence('WBGene00221255')
        ```

        # Raises
        Exception: If an invalid value is provided for `format`, `mask`, or `sequence_type`

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/sequence_id
         
        """

        ALLOWED_FORMATS = ['fasta']
        if data_format and data_format not in ALLOWED_FORMATS:
            raise Exception('Format type {} is not supported. Allowable mask values are {}'
                .format(data_format, ALLOWED_FORMATS))

        ALLOWED_MASKS = ['hard', 'soft']
        if mask and mask not in ALLOWED_MASKS:
            raise Exception('Mask type {} is not supported. Allowable mask values are {}'
                .format(mask, ALLOWED_MASKS))

        ALLOWED_SEQUENCE_TYPES = [
            'genomic',
            'cds',
            'cdna',
            'protein'
        ]

        if sequence_type and sequence_type not in ALLOWED_SEQUENCE_TYPES:
            raise Exception('Sequence type {} is not supported. Allowable sequence type values are {}'
                .format(sequence_type, ALLOWED_SEQUENCE_TYPES))

        params = {
            'db_type': db_type,
            'expand_3prime': expand_3prime,
            'expand_5prime': expand_5prime,
            'mask': mask,
            'mask_feature': int(mask_feature),
            'multiple_sequences': int(multiple_sequences),
            'object_type': object_type,
            'species': species,
            'sequence_type': sequence_type
        }

        return wormbase_get('{}/sequence/id/{}'.format(self.version_string, id), query=params)

    def batch_get_sequence(self,
        ids,
        db_type=None,
        expand_3prime=None,
        expand_5prime=None,
        data_format=None,
        mask=None,
        mask_feature=False,
        object_type=None,
        species=None,
        sequence_type='genomic'):
        """`POST sequence/id`
        
        # Arguments
        ids* (str or list): A string of comma-separated stable IDs, or a list of these IDs
        db_type (str): Default: None
        expand_3prime (int): Default: None
        expand_5prime (int): Default: None
        data_format (str): Must be one of ['fasta'] Default: None
        mask (str): Must be one of ['hard', 'soft'] Default: None
        mask_feature (boolean): Default: False
        multiple_sequences (boolean): Default: False
        object_type (str): Default: None
        species (str): Default: None
        sequence_type (str): Must be one of ['genomic', 'cds', 'cdna', 'protein'] Default: 'genomic'

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        id_list = ["WBGene00221255", "__VAR(gene_stable_id_2)__"]
        client.batch_get_sequence(id_list)

        id_string = "WBGene00221255,__VAR(gene_stable_id_2)__"
        client.batch_get_sequence(id_string)
        ```

        # Raises
        Exception: If an invalid value is provided for `data_format, `mask`, or `sequence_type`

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/sequence_id_post
         
        """

        id_list = []
        if not type(ids) is list:
            id_list = ids.split(',')
        else:
            id_list = ids

        ALLOWED_FORMATS = ['fasta']
        if data_format and data_format not in ALLOWED_FORMATS:
            raise Exception('Format type {} is not supported. Allowable mask values are {}'
                            .format(data_format, ALLOWED_FORMATS))

        ALLOWED_MASKS = ['hard', 'soft']
        if mask and mask not in ALLOWED_MASKS:
            raise Exception('Mask type {} is not supported. Allowable mask values are {}'
                            .format(mask, ALLOWED_MASKS))

        ALLOWED_SEQUENCE_TYPES = [
            'genomic',
            'cds',
            'cdna',
            'protein'
        ]

        if sequence_type and sequence_type not in ALLOWED_SEQUENCE_TYPES:
            raise Exception('Sequence type {} is not supported. Allowable sequence type values are {}'
                            .format(sequence_type, ALLOWED_SEQUENCE_TYPES))


        params = {
            'db_type': db_type,
            'expand_3prime': expand_3prime,
            'expand_5prime': expand_5prime,
            'mask': mask,
            'mask_feature': int(mask_feature),
            'object_type': object_type,
            'species': species,
            'sequence_type': sequence_type
        }

        return wormbase_post('{}/sequence/id'.format(self.version_string), query=params, data={ 'ids' : id_list })

    def get_sequence_for_region(self,
        region,
        species,
        coord_system=None,
        coord_system_version=None,
        expand_3prime=None,
        expand_5prime=None,
        data_format=None,
        mask=None,
        mask_feature=False):
        """`GET sequence/region/:species/:region`
        
        # Arguments
        region* (str): Query region. A maximum of 10MB is allowed to be requested at any one time
        species* (str): Species name/alias
        coord_system (str): Default: None
        coord_system_version (str): Default: None
        expand_3prime (int): Default: None
        expand_5prime (int): Default: None
        data_format (str): Must be one of ['fasta'] Default: None
        mask (str): Must be one of ['hard', 'soft'] Default: None
        mask_feature (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        client.get_sequence_for_region('Bm_v4_Chr2_contig_001:13847151-13862157:1', 'brugia_malayi_prjna10729')
        ```

        # Raises
        Exception: If an invalid value is provided for `data_format`, or `mask`

        # Returns
        data (dict): a dictionary representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/sequence_region
         
        """

        ALLOWED_FORMATS = ['fasta']
        if data_format and data_format not in ALLOWED_FORMATS:
            raise Exception('Format type {} is not supported. Allowable mask values are {}'
                .format(data_format, ALLOWED_FORMATS))

        ALLOWED_MASKS = ['hard', 'soft']
        if mask and mask not in ALLOWED_MASKS:
            raise Exception('Mask type {} is not supported. Allowable mask values are {}'
                .format(mask, ALLOWED_MASKS))

        params = {
            'coord_system': coord_system,
            'coord_system_version': coord_system_version,
            'expand_3prime': expand_3prime,
            'expand_5prime': expand_5prime,
            'mask': mask,
            'mask_feature': int(mask_feature),
            'data_format': data_format
        }

        return wormbase_get('{}/sequence/region/{}/{}'.format(self.version_string, species, region), query=params)

    def batch_get_sequence_for_region(self,
        species,
        regions,
        data_format=None,
        coord_system=None,
        coord_system_version=None,
        expand_3prime=None,
        expand_5prime=None,
        mask=None,
        mask_feature=False,):
        """`POST sequence/region/:species`
        
        # Arguments
        species* (str): Species name/alias
        regions* (str or list): A comma-separated string of query regions, or a list of these regions
        data_format (str): Must be one of ['fasta'] Default: None
        coord_system (str): Default: None
        coord_system_version (str): Default: None
        expand_3prime (int): Default: None
        expand_5prime (int): Default: None
        mask (str): Must be one of ['hard', 'soft'] Default: None
        mask_feature (boolean): Default: False

        # Example
        ```python
        client = wormbase_parasite.WormbaseClient()
        region_list = ["Bm_v4_Chr2_contig_001:13847151-13862157:1", "Bmal_v3_scaffold139:57600..85000"]
        client.batch_get_sequence_for_region('brugia_malayi_prjna10729', region_list)

        region_string = "Bm_v4_Chr2_contig_001:13847151-13862157:1,Bmal_v3_scaffold139:57600..85000"
        client.batch_get_sequence_for_region('brugia_malayi_prjna10729', region_string)
        ```

        # Raises
        Exception: If an invalid value is provided for `data_format`, or `mask`

        # Returns
        data (list): a list of dictionaries representing the data returned by the API
        
        # See also: https://parasite.wormbase.org/rest/documentation/info/sequence_region_post
         
        """

        ALLOWED_FORMATS = ['fasta']
        if data_format and data_format not in ALLOWED_FORMATS:
            raise Exception('Format type {} is not supported. Allowable mask values are {}'
                .format(data_format, ALLOWED_FORMATS))

        ALLOWED_MASKS = ['hard', 'soft']
        if mask and mask not in ALLOWED_MASKS:
            raise Exception('Mask type {} is not supported. Allowable mask values are {}'
                .format(mask, ALLOWED_MASKS))

        region_list = []
        if not type(regions) is list:
            region_list = regions.split(',')
        else:
            region_list = regions

        params = {
            'coord_system': coord_system,
            'coord_system_version': coord_system_version,
            'expand_3prime': expand_3prime,
            'expand_5prime': expand_5prime,
            'mask': mask,
            'mask_feature': int(mask_feature),
            'data_format': data_format
        }

        return wormbase_post('{}/sequence/region/{}'.format(self.version_string, species), query=params, data={ 'regions' : region_list })
