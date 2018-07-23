from .util import wormbase_get, wormbase_post

class InformationMixin:
    def get_assemblies_for_species(self, species, bands=False):
        """http://parasite.wormbase.org/rest-10/documentation/info/assembly_info"""
        params = {
            'bands': bands
        }

        return wormbase_get(self.version_string + '/info/assembly/' + species, query=params)

    def get_info_for_region(self, region_name, species, bands=False):
        params = {
            'bands': bands
        }

        return wormbase_get(self.version_string + '/info/assembly/' + species + '/' + region_name, query=params)

    def get_info_for_genome(self, genome_name, expand=False):
        """http://parasite.wormbase.org/rest-10/documentation/info/info_genome"""
        params = {
            'expand': expand
        }

        return wormbase_get(self.version_string + '/info/genomes/' + genome_name, query=params)

    def get_info_for_all_genomes(self, expand=False):
        """http://parasite.wormbase.org/rest-10/documentation/info/info_genomes"""
        params = {
            'expand': expand
        }

        return wormbase_get(self.version_string + '/info/genomes', query=params)

    def get_info_for_genome_with_assembly(self, assembly_id, expand=False):
        """http://parasite.wormbase.org/rest-10/documentation/info/info_genomes_assembly"""
        params = {
            'expand': expand
        }

        return wormbase_get(self.version_string + '/info/genomes/assembly/' + assembly_id, query=params)

    def get_info_for_taxonomy_node(self, taxon_name, expand=False):
        """http://parasite.wormbase.org/rest-10/documentation/info/info_genomes_taxonomy"""
        params = {
            'expand': expand
        }

        return wormbase_get(self.version_string + '/info/genomes/taxonomy/' + taxon_name, query=params)

    def get_quality_scores_for_genome(self, genome_name):
        """http://parasite.wormbase.org/rest-10/documentation/info/info_quality_name"""
        return wormbase_get(self.version_string + '/info/quality/' + genome_name)

    def get_release_info(self):
        """http://parasite.wormbase.org/rest-10/documentation/info/info_wormbase_version"""
        return wormbase_get(self.version_string + '/info/version/')

    def get_available_species(self):
        """http://parasite.wormbase.org/rest-10/documentation/info/species"""
        return wormbase_get(self.version_string + '/info/species')
