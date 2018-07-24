import sys
sys.path.append('../')
import unittest
from pywormbase import WormbaseClient
import test_util

class TestCrossReferenceMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))
        self.assertTrue(test_util.is_status_200(response))

    def test_xrefs_for_symbol(self):
        self.doTest(self.api.get_xrefs_for_symbol(
            'brugia_malayi_prjna10729', 'Bm994'))

    def test_xrefs_for_id(self):
        self.doTest(self.api.get_xrefs_for_id('ENSG00000157764'))

    def test_xrefs_for_gene_and_species(self):
        self.doTest(self.api.get_xrefs_for_gene_and_species(
            'Bm994', 'brugia_malayi_prjna10729'))

if __name__ == '__main__':
    unittest.main()
