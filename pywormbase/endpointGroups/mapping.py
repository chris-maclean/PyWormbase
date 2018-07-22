from ..util import wormbase_get, wormbase_post

class MappingMixin:
    def cdna2genomic(self,
        id,
        object_type,
        region,
        species=None):
        """https://parasite.wormbase.org/rest-10/documentation/info/assembly_cdna"""

        params = {
            'object_type': object_type,
            'species': species
        }

        return wormbase_get(self.version_string + '/map/cdna/' + id + '/' + region, query=params)

    def cds2genomic(self,
        id,
        object_type,
        region,
        species=None):
        """https://parasite.wormbase.org/rest-10/documentation/info/assembly_cds"""
        
        params = {
            'object_type': object_type,
            'species': species
        }

        return wormbase_get(self.version_string + '/map/cds/' + id + '/' + region, query=params)

    def protein2genomic(self,
        id,
        region,
        object_type=None,
        species=None):
        """https://parasite.wormbase.org/rest-10/documentation/info/assembly_translation"""
        
        params = {
            'object_type': object_type,
            'species': species
        }

        return wormbase_get(self.version_string + '/map/translation/' + id + '/' + region, query=params)
