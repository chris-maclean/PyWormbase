import logging
from .endpointGroups import ComparativeGenomics
from .endpointGroups import CrossReferences
from .endpointGroups import Information
from .endpointGroups import Lookup

class WormbaseClient(
    ComparativeGenomics, 
    CrossReferences, 
    Information,
    Lookup):
    def __init__(self, version=None):
        self.version = str(version)
        self.version_string = 'rest-' + self.version if self.version else 'rest'