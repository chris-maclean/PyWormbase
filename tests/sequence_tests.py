import sys
sys.path.append('../')
import unittest
from pywormbase import WormbaseClient
import test_util


class TestOverlapMethods(unittest.TestCase):
    def setUp(self):
        self.api = WormbaseClient(10)

    def doTest(self, response):
        self.assertTrue(test_util.is_dict(response))
        self.assertTrue(test_util.is_status_200(response))

    def test_sequence(self):
        self.doTest(self.api.get_sequence("WBGene00221255"))
    
    def test_batch_sequence_with_list(self):
        self.doTest(self.api.batch_get_sequence(
            ["WBGene00221255", "__VAR(gene_stable_id_2)__"]))
    
    def test_batch_sequence_with_string(self):
        self.doTest(self.api.batch_get_sequence(
            "WBGene00221255,__VAR(gene_stable_id_2)__"))

    def test_sequence_for_region(self):
        self.doTest(self.api.get_sequence_for_region(
            'Bm_v4_Chr2_contig_001:13847151-13862157:1', 'brugia_malayi_prjna10729'))
        
    def test_batch_sequence_for_region_with_list(self):
        self.doTest(self.api.batch_get_sequence_for_region(
            'brugia_malayi_prjna10729', ["Bm_v4_Chr2_contig_001:13847151-13862157:1", "Bmal_v3_scaffold139:57600..85000"]))

    def test_batch_sequence_for_region_with_string(self):
        self.doTest(self.api.batch_get_sequence_for_region(
            'brugia_malayi_prjna10729', "Bm_v4_Chr2_contig_001:13847151-13862157:1,Bmal_v3_scaffold139:57600..85000"))

    

if __name__ == '__main__':
    unittest.main()
