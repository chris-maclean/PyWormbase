from ..util import wormbase_get, wormbase_post

class ComparativeGenomicsMixin:
    def get_gene_tree_dump(self, 
            id,
            aligned=False, 
            nh_format='simple', 
            sequence='protein'):
            """http://parasite.wormbase.org/rest/documentation/info/genetree"""
            
            params = {
                'aligned': aligned,
                'nh_format': nh_format,
                'sequence': sequence
            }

            return wormbase_get(self.version_string + '/genetree/id/' + id, query=params)

    def get_gene_tree_by_member(self, 
        id, 
        aligned=False, 
        db_type='core', 
        nh_format='simple', 
        object_type=None, 
        sequence='protein', 
        species=None):
        """http://parasite.wormbase.org/rest/documentation/info/genetree_member_id"""

        params = {
            'aligned': aligned,
            'db_type': db_type,
            'nh_format': nh_format,
            'object_type': object_type,
            'sequence': sequence,
            'species': species
        }

        return wormbase_get(self.version_string + '/genetree/member/id/' + id, query=params)

    def get_gene_tree_with_gene(self,
        symbol,
        species,
        aligned=False,
        db_type='core',
        external_db=None,
        nh_format='simple',
        object_type=None,
        sequence='protein'):
        """http://parasite.wormbase.org/rest-10/documentation/info/genetree_member_symbol"""
        
        params = {
            'aligned': aligned,
            'db_type': db_type,
            'external_db': external_db,
            'nh_format': nh_format,
            'object_type': object_type,
            'sequence': sequence
        }

        return wormbase_get(self.version_string + '/genetree/member/symbol/' + species + '/' + symbol, query=params)

    def get_orthologues_by_gene(self,
        gene_id,
        aligned=True,
        format='full',
        sequence='protein',
        species=None,
        target_species=None,
        target_taxon=None,
        orthologue_type='all'):
        """http://parasite.wormbase.org/rest-10/documentation/info/homology_ensemblgene"""

        params = {
            'aligned': aligned,
            'format': format,
            'sequence': sequence,
            'species': species,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        return wormbase_get(self.version_string + '/homology/id/' + id, query=params)

    def get_orthologues_by_symbol(self,
        species,
        symbol,
        aligned=True,
        external_db=None,
        format='full',
        sequence='protein',
        target_species=None,
        target_taxon=None,
        orthologue_type='all'):
        """http://parasite.wormbase.org/rest-10/documentation/info/homology_symbol"""

        params = {
            'aligned': aligned,
            'external_db': external_db,
            'format': format,
            'sequence': sequence,
            'target_species': target_species,
            'target_taxon': target_taxon,
            'type': orthologue_type
        }

        return wormbase_get(self.version_string + '/homology/symbol/' + species + '/' + symbol, query=params)