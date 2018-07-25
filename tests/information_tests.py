import sys
sys.path.append('../')
import unittest
from pywormbase import WormbaseClient
import test_util

class TestInformationMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient()
    
    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))

    def test_release_info(self):
        self.doTest(self.api.get_release_info())

    def test_available_species(self):
        self.doTest(self.api.get_available_species())

    def test_assemblies(self):
        self.doTest(self.api.get_assemblies_for_species('brugia_malayi_prjna10729'))

    def test_info_for_region(self):
        self.doTest(self.api.get_info_for_region(
            'Bm_v4_Chr2_contig_001', 'brugia_malayi_prjna10729'))

    def test_info_for_genome(self):
        self.doTest(self.api.get_info_for_genome('brugia_malayi_prjna10729'))

    def test_info_for_all_genomes(self):
        self.doTest(self.api.get_info_for_all_genomes())

    def test_info_for_genome_with_assembly(self):
        self.doTest(self.api.get_info_for_genome_with_assembly(
            'GCA_000951595.1'))

    def test_info_for_taxonomy_node(self):
        self.doTest(self.api.get_info_for_taxonomy_node('Brugia'))

    def test_quality_scores(self):
        self.doTest(self.api.get_quality_scores_for_genome(
            'brugia_malayi_prjna10729'))

if __name__ == '__main__':
    unittest.main()
