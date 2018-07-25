import sys
sys.path.append('../')
import unittest
import test_util
from pywormbase import WormbaseClient

class TestOntologyMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))

    def test_get_descendants(self):
        self.doTest(self.api.get_descendants('GO:0005667'))

    def test_ancestry(self):
        self.assertTrue(self.api.get_ancestry('GO:0005667'))

if __name__ == '__main__':
    unittest.main()
