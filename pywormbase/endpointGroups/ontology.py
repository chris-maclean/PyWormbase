from .util import wormbase_get, wormbase_post

class OntologyMixin:
    def get_ancestry(self,
        id,
        ontology=None):
        """https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors"""

        params = {
            'ontology': ontology
        }

        return wormbase_get(self.version_string + '/ontology/ancestors/' + id, query=params)

    def get_ancestry_chart(self,
        id,
        ontology=None):
        """https://parasite.wormbase.org/rest/documentation/info/ontology_ancestors_chart"""

        params = {
            'ontology': ontology
        }

        return wormbase_get(self.version_string + '/ontology/ancestors/chart/' + id, query=params)

    def get_descendants(self,
        id,
        closest_term=False,
        ontology=None,
        subset=None,
        zero_distance=False):
        """https://parasite.wormbase.org/rest/documentation/info/ontology_descendants"""

        params = {
            'ontology': ontology,
            'closest_term': closest_term,
            'subset': subset,
            'zero_distance': zero_distance
        }

        return wormbase_get(self.version_string + '/ontology/descendants/' + id, query=params)

    def get_ontology_by_id(self,
        id,
        relation=False,
        simple=False,):
        """https://parasite.wormbase.org/rest/documentation/info/ontology_id"""

        params = {
            'relation': relation,
            'simple': simple
        }

        return wormbase_get(self.version_string + '/ontology/id/' + id, query=params)

    def get_ontology_by_name(self,
        name,
        ontology=None,
        relation=None,
        simple=False):
        """https://parasite.wormbase.org/rest/documentation/info/ontology_name"""

        params = {
            'ontology': ontology,
            'relation': relation,
            'simple': simple
        }

        return wormbase_get(self.version_string + '/ontology/name/' + name, query=params)
