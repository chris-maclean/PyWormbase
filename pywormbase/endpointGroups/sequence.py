from .util import wormbase_get, wormbase_post

class SequenceMixin:
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
        """https://parasite.wormbase.org/rest/documentation/info/sequence_id"""

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
            'mask_feature': mask_feature,
            'multiple_sequences': multiple_sequences,
            'object_type': object_type,
            'species': species,
            'sequence_type': sequence_type
        }

        return wormbase_get(self.version_string + '/sequence/id/' + id, query=params)

    def batch_get_sequence(self,
        ids,
        db_type=None,
        expand_3prime=None,
        expand_5prime=None,
        mask=None,
        mask_feature=False,
        multiple_sequences=False,
        object_type=None,
        species=None,
        sequence_type='genomic'):
        """https://parasite.wormbase.org/rest/documentation/info/sequence_id_post"""

        id_list = []
        if not type(ids) is list:
            id_list = ids.split(',')
        else:
            id_list = ids


        params = {
            'db_type': db_type,
            'expand_3prime': expand_3prime,
            'expand_5prime': expand_5prime,
            'mask': mask,
            'mask_feature': mask_feature,
            'multiple_sequences': multiple_sequences,
            'object_type': object_type,
            'species': species,
            'sequence_type': sequence_type
        }

        return wormbase_post(self.version_string + '/sequence/id', query=params, data={ 'ids' : id_list })

    def get_sequence_for_region(self,
        region,
        species,
        coord_system=None,
        coord_system_version=None,
        expand_3prime=None,
        expand_5prime=None,
        mask=None,
        mask_feature=False,
        data_format=None):
        """https://parasite.wormbase.org/rest/documentation/info/sequence_region"""

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
            'mask_feature': mask_feature,
            'data_format': data_format
        }

        return wormbase_get(self.version_string + '/sequence/region/' + species + '/' + region, query=params)

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
        """https://parasite.wormbase.org/rest/documentation/info/sequence_region_post"""

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
            'mask_feature': mask_feature,
            'data_format': data_format
        }

        return wormbase_post(self.version_string + '/sequence/region/' + species, query=params, data={ 'regions' : region_list })