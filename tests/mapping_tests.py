import sys
sys.path.append('../')
import unittest
from wormbase_parasite import WormbaseClient
import test_util

class TestMappingMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))

    def test_cdna2genomic(self):
        self.doTest(self.api.cdna2genomic('Bm4789', 'transcript', '100..300'))

    def test_cds2genomic(self):
        self.doTest(self.api.cds2genomic('Bm4789', 'transcript', '1..300'))

    def test_protein2genomic(self):
        self.doTest(self.api.protein2genomic('Bm4789', '1..100'))

if __name__ == '__main__':
    unittest.main()
