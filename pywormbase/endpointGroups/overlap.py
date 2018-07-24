from .util import wormbase_get, wormbase_post

class OverlapMixin:
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
        """https://parasite.wormbase.org/rest/documentation/info/overlap_id"""

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
        """https://parasite.wormbase.org/rest/documentation/info/overlap_region"""

        params = {
            'feature': feature,
            'biotype': biotype,
            'cell_type': cell_type,
            'db_type': db_type,
            'logic_name': logic_name,
            'misc_set': misc_set,
            'object_type': object_type,
            'species_set': species_set,
            'trim_upstream': trim_upstream,
            'trim_downstream': trim_downstream
        }

        return wormbase_get(self.version_string + '/overlap/region/' + species + '/' + region, query=params)

    def get_features_for_translation(self,
        id,
        db_type=None,
        feature='protein_feature',
        species=None,
        data_type=None):
        """https://parasite.wormbase.org/rest/documentation/info/overlap_translation"""


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
