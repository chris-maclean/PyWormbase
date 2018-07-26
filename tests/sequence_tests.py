import sys
sys.path.append('../')
import unittest
from pywormbase import WormbaseClient
import test_util


class TestSequenceMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))

    def test_sequence(self):
        self.doTest(self.api.get_sequence("WBGene00221255"))
    
    def test_batch_sequence_with_list(self):
        self.assertTrue(type(self.api.batch_get_sequence(
            ["WBGene00221255", "__VAR(gene_stable_id_2)__"])) is list)
    
    def test_batch_sequence_with_string(self):
        self.assertTrue(type(self.api.batch_get_sequence(
            "WBGene00221255,__VAR(gene_stable_id_2)__")) is list)

    def test_sequence_for_region(self):
        self.doTest(self.api.get_sequence_for_region(
            'Bm_v4_Chr2_contig_001:13847151-13862157:1', 'brugia_malayi_prjna10729'))
        
    def test_batch_sequence_for_region_with_list(self):
        region_list = ["Bm_v4_Chr2_contig_001:13847151-13862157:1",
                       "Bmal_v3_scaffold139:57600..85000"]
        self.assertTrue(type(self.api.batch_get_sequence_for_region(
            'brugia_malayi_prjna10729', region_list)) is list)

    def test_batch_sequence_for_region_with_string(self):
        region_string = "Bm_v4_Chr2_contig_001:13847151-13862157:1,Bmal_v3_scaffold139:57600..85000"
        self.assertTrue(type(self.api.batch_get_sequence_for_region(
            'brugia_malayi_prjna10729', region_string)) is list)

    

if __name__ == '__main__':
    unittest.main()
