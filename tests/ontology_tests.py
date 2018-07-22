import sys
sys.path.append('../')
import unittest
from pywormbase import WormbaseClient

class TestOntologyMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def test_get_descendents(self):
        res = self.api.get_descendants('GO:0005667')
        self.assertTrue(type(res) is dict)
        self.assertEqual(res.get('status_code'), 200)

if __name__ == '__main__':
    unittest.main()