from .util import wormbase_get, wormbase_post

class CrossReferencesMixin:
    def get_xrefs_for_symbol(self, 
        species, 
        symbol, 
        db_type=None, 
        external_db=None, 
        object_type=None):
        """http://parasite.wormbase.org/rest/documentation/info/xref_external"""
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
        """http://parasite.wormbase.org/rest/documentation/info/xref_id"""
        params = {
            'all_levels': all_levels,
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
        """http://parasite.wormbase.org/rest/documentation/info/xref_name"""

        params = {
            'db_type': db_type,
            'external_db': external_db
        }

        return wormbase_get(self.version_string + '/xrefs/name/' + species + '/' + gene_name, query=params)