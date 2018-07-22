import logging
from .endpointGroups import ComparativeGenomics
from .endpointGroups import CrossReferences
from .endpointGroups import Information
from .endpointGroups import Lookup
from .endpointGroups import Mapping
from .endpointGroups import Ontology
from .endpointGroups import Overlap
from .endpointGroups import Sequence

class WormbaseClient(
    ComparativeGenomics, 
    CrossReferences, 
    Information,
    Lookup,
    Mapping,
    Ontology,
    Overlap,
    Sequence):
    def __init__(self, version=None):
        self.version = str(version)
        self.version_string = 'rest-' + self.version if self.version else 'rest'