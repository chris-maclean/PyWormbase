import sys
sys.path.append('../')
import unittest
from pywormbase import WormbaseClient

class TestInformationMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def test_batch_symbol(self):
        symbols = ["Bm994", "__VAR(gene_symbol2)__" ]
        res = self.api.batch_get_symbol_from_external_db('brugia_malayi_prjna10729', symbols)
        self.assertTrue(type(res) is dict)
        self.assertEqual(res.get('status_code'), 200)

    def test_batch_id(self):
        ids = ["WBGene00221255", "__VAR(gene_stable_id_2)__" ]
        res = self.api.batch_lookup_by_id(ids)
        self.assertTrue(type(res) is dict)
        self.assertEqual(res.get('status_code'), 200)
        
if __name__ == '__main__':
    unittest.main()