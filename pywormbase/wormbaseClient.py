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
    """The main entry point to all Wormbase ParaSite interactions
    
    This client inherits from mixins in the #endpointGroups module. Those mixins hold the source code that retrieves data from the Wormbase REST API.

    # Arguments
    version (str or int): The desired REST API version number. This number will be included in the base URL when making calls to the API. Omit to use the latest version. Visit http://parasite.wormbase.org/rest/ to see the latest version.


    # Example
    ```python
    >>> import pywormbase
    >>> api_latest = pywormbase.WormbaseClient()
    >>> api_latest.get_release_info()
    {'status_code': 200, 'data': {'wbps_release': '10', 'wb_release': '263'}}
    >>> api_v9 = pywormbase.WormbaseClient(9)
    >>> api_v9.get_release_info()
    {'status_code': 200, 'data': {'wbps_release': '9', 'wb_release': '258'}}
    ```

    See also: http://parasite.wormbase.org/rest/
    """
    
    def __init__(self, version=None):
        self.version = str(version) if version else None
        """The stringified value of the REST API that is being used by this client"""
        
        self.version_string = 'rest-' + self.version if self.version else 'rest'
        """The string that represents the API version in the Wormbase API URLs (e.g., 'rest-10')"""
