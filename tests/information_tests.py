import sys
sys.path.append('../')
import unittest
from pywormbase import WormbaseClient

class TestInformationMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def test_release_info(self):
        res = self.api.get_release_info()
        self.assertTrue(type(res) is dict)
        self.assertEqual(res.get('status_code'), 200)

    def test_available_species(self):
        res = self.api.get_available_species()
        self.assertTrue(type(res) is dict)
        self.assertEqual(res.get('status_code'), 200)

if __name__ == '__main__':
    unittest.main()