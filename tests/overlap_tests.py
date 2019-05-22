import sys
sys.path.append('../')
import unittest
from wormbase_parasite import WormbaseClient
import test_util


class TestOverlapMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient()

    def doTest(self, response):
        self.assertTrue(type(response) is list)

    def test_overlapping_features(self):
        self.doTest(self.api.get_overlapping_features(
            'gene', 'WBGene00221255'))

    def test_overlap_by_region(self):
        self.doTest(self.api.get_overlap_by_region(
            'gene', 'Bm_v4_Chr2_contig_001:13847151-13862157', 'brugia_malayi_prjna10729'))

    def test_features_for_translation(self):
        self.doTest(self.api.get_features_for_translation('Bm4789.1'))

if __name__ == '__main__':
    unittest.main()
