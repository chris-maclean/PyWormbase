import sys
sys.path.append('../')
import unittest
from wormbase_parasite import WormbaseClient
import test_util

class TestComparativeMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))

    def test_gene_tree_dump(self):
        self.doTest(self.api.get_gene_tree_dump('WBGT00000000021203'))

    def test_gene_tree_by_member(self):
        self.doTest(self.api.get_gene_tree_by_member('WBGene00221255'))

    def test_gene_tree_with_gene(self):
        self.doTest(self.api.get_gene_tree_with_gene(
            'Bm994', 'brugia_malayi_prjna10729'))

    def test_orthologues_by_gene(self):
        self.doTest(self.api.get_orthologues_by_gene('WBGene00221255'))

    def test_orthologues_by_symbol(self):
        self.doTest(self.api.get_orthologues_by_symbol(
            'brugia_malayi_prjna10729', 'Bm994'))

if __name__ == '__main__':
    unittest.main()
