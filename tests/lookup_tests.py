import sys
sys.path.append('../')
import unittest
import test_util
from pywormbase import WormbaseClient

class TestLookupMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))
        self.assertTrue(test_util.is_status_200(response))

    def test_batch_symbol(self):
        symbols = ["Bm994", "__VAR(gene_symbol2)__" ]
        self.doTest(self.api.batch_get_symbol_from_external_db('brugia_malayi_prjna10729', symbols))

    def test_batch_id(self):
        ids = ["WBGene00221255", "__VAR(gene_stable_id_2)__" ]
        self.doTest(self.api.batch_lookup_by_id(ids))

    def test_lookup_id(self):
        self.doTest(self.api.lookup_by_id('WBGene00221255'))

    def test_lookup_by_name(self):
        self.doTest(self.api.lookup_by_name('brugia_malayi_prjna10729'))

    def test_lookup_symbol_external_db(self):
        self.doTest(self.api.get_symbol_from_external_db('brugia_malayi_prjna10729', 'Bm994'))
        
if __name__ == '__main__':
    unittest.main()
