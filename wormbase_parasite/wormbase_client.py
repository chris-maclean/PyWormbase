import logging
from os import environ
from .endpoint_groups import ComparativeGenomics
from .endpoint_groups import CrossReferences
from .endpoint_groups import Information
from .endpoint_groups import Lookup
from .endpoint_groups import Mapping
from .endpoint_groups import Ontology
from .endpoint_groups import Overlap
from .endpoint_groups import Sequence

# Set the log level for our logger
DEFAULT_LOG_LEVEL = 'WARNING'
LOG_LEVEL = getattr(logging, environ['LOG_LEVEL'].upper()) if 'LOG_LEVEL' in environ else DEFAULT_LOG_LEVEL

# Squelch some messages from other loggers
logging.getLogger("urllib3").setLevel(logging.WARNING)

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
    
    This client inherits from mixins in the #endpoint_groups module. Those mixins hold the source code that retrieves data from the Wormbase REST API.

    # Arguments
    version (str or int): The desired REST API version number. This number will be included in the base URL when making calls to the API. Omit to use the latest version. Visit http://parasite.wormbase.org/rest/ to see the latest version.


    # Example
    ```python
    >>> import wormbase_parasite
    >>> api_latest = wormbase_parasite.WormbaseClient()
    >>> api_latest.get_release_info()
    {'status_code': 200, 'data': {'wbps_release': '10', 'wb_release': '263'}}
    >>> api_v9 = wormbase_parasite.WormbaseClient(9)
    >>> api_v9.get_release_info()
    {'status_code': 200, 'data': {'wbps_release': '9', 'wb_release': '258'}}
    ```

    # See also: http://parasite.wormbase.org/rest/
    """
    
    def __init__(self, version=None):
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()
        self.logger.setLevel(LOG_LEVEL)

        self.version = str(version) if version else None
        """The stringified value of the REST API version number that is being used by this client"""
        
        self.version_string = 'rest-{}'.format(self.version) if self.version else 'rest'
        """The string that represents the API version in the Wormbase API URLs (e.g., 'rest')"""
