from .util import wormbase_get, wormbase_post

class LookupMixin:
    def lookup_by_id(self,
        id,
        db_type=None,
        expand=False,
        format='full',
        species=None):
        """http://parasite.wormbase.org/rest-10/documentation/info/lookup"""

        params = {
            'db_type': db_type,
            'expand': expand,
            'format': format,
            'species': species
        }

        return wormbase_get(self.version_string + '/lookup/id/' + id, query=params)

    def lookup_by_name(self,
        name,
        biotypes=None,
        level='gene',
        xrefs=None):
        """http://parasite.wormbase.org/rest-10/documentation/info/lookup_genome"""

        params = {
            'biotypes': biotypes,
            'level': level,
            'xrefs': xrefs
        }

        return wormbase_get(self.version_string + '/lookup/genome/' + name, query=params)


    # Deprecated by Wormbase? Returns 404
    def batch_lookup_by_id(self,
        ids,
        db_type=None,
        expand=False,
        format='full',
        object_type=None,
        species=None):
        """http://parasite.wormbase.org/rest-10/documentation/info/lookup_post"""

        params = {
            'db_type': db_type,
            'expand': expand,
            'format': format,
            'object_type': object_type,
            'species': species
        }

        id_list = []
        if type(ids) is str:
            id_list = ids.split(',')
        else:
            id_list = ids
        
        return wormbase_post(self.version_string + '/lookup/id', query=params, data={ 'ids': id_list })

    def get_symbol_from_external_db(self,
        species,
        symbol,
        expand=False,
        format='full'):
        """http://parasite.wormbase.org/rest-10/documentation/info/symbol_lookup"""

        params = {
            'expand': expand,
            'format': format
        }

        return wormbase_get(self.version_string + '/lookup/symbol/' + species + '/' + symbol, query=params)

    def batch_get_symbol_from_external_db(self,
        species,
        symbols,
        expand=False,
        format='full'):
        """http://parasite.wormbase.org/rest-10/documentation/info/symbol_post"""

        params = {
            'expand': expand,
            'format': format
        }

        symbol_list = []
        if type(symbols) is str:
            symbol_list = symbols.split(',')
        else:
            symbol_list = symbols

        return wormbase_post(self.version_string + '/lookup/symbol/' + species, query=params, data={ 'symbols': symbol_list })