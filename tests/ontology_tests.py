import sys
sys.path.append('../')
import unittest
import test_util
from wormbase_parasite import WormbaseClient

class TestOntologyMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(type(response) is dict)

    def test_ancestry(self):
        self.assertTrue(type(self.api.get_ancestry('GO:0005667')) is list)

    def test_ancestry_chart(self):
        self.doTest(self.api.get_ancestry_chart('GO:0005667'))

    def test_get_descendants(self):
        self.assertTrue(type(self.api.get_descendants('GO:0005667')) is list)

    def test_ontology_by_id(self):
        self.doTest(self.api.get_ontology_by_id('GO:0005667'))

    def test_ontology_by_name(self):
        self.assertTrue(type(self.api.get_ontology_by_name(
            'transcription')) is list)

if __name__ == '__main__':
    unittest.main()
