import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_1_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    #Kortin saldo alussa oikein
    def test_2_kortin_alku_saldo(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    #Rahan lataaminen kasvattaa saldoa oikein
    def test_3_rahan_lataaminen_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)
    
    #Saldo vähenee oikein, jos rahaa on tarpeeksi
    def test_4_saldo_vähenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)
        
    #Saldo ei muutu, jos rahaa ei ole tarpeeksi
    def test_5_saldo_pysyy_jos_ei_rahaa(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    # Metodi palauttaa True, jos rahat riittivät 
    def test_6_palauttaa_true_arvon(self):
        self.maksukortti.ota_rahaa(1000)
        
    # (cont'd) ja muuten False
    def test_7_palauttaa_false_arvon(self):
        self.maksukortti.ota_rahaa(2000)

