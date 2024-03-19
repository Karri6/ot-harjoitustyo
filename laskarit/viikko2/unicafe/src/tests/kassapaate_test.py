import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti  = Maksukortti(1000)

    def test_1_kassa_luotu_oikein(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.kassa_edulliset(), 0)
        self.assertEqual(self.kassa.kassa_maukkaat(), 0)
        
    # Jos maksu riittävä: kassassa oleva rahamäärä kasvaa
    # lounaan hinnalla ja vaihtorahan suuruus on oikea
    def test_2_syo_edullisesti_kateisella(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihto, 60)
        self.assertEqual(self.kassa.kassa_edulliset(), 1)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1002.4)

    # Jos maksu on riittävä: myytyjen lounaiden määrä kasvaa
    def test_3_lounaiden_maara(self):
        self.kassa.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassa.kassa_maukkaat(), 1)
        
    # Jos maksu ei ole riittävä: kassassa oleva rahamäärä ei muutu, 
    # kaikki rahat palautetaan vaihtorahana ja myytyjen lounaiden määrässä 
    # ei muutosta
    def test_4_maksu_ei_riita(self):
        vaihto = self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihto, 100)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)
        self.assertEqual(self.kassa.kassa_edulliset(), 0)
        
    # Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    def test_5_edullisesti_kortilla(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassa_edulliset(), 1)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)

    # Jos kortilla on tarpeeksi rahaa, myytyjen lounaiden määrä kasvaa
    def test_6_maukkaasti_kortilla(self):        
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassa_maukkaat(), 1)

    # Jos kortilla on tarpeeksi rahaa, veloitetaan summa kortilta ja palautetaan True
    def test_7_palauttaa_true_kortilla(self):
        return self.kassa.syo_maukkaasti_kortilla(self.kortti)
    
    # Jos kortilla ei ole tarpeeksi rahaa, kortin rahamäärä ei muutu,
    # myytyjen lounaiden määrä muuttumaton ja palautetaan False
    def test_8_kortilla_ei_rahaa(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), False)
        self.assertEqual(self.kortti.saldo_euroina(), 1)
        self.assertEqual(self.kassa.kassa_edulliset(), 0)

    
    # Kassassa oleva rahamäärä ei muutu kortilla ostettaessa
    def test_9_korttimaksu_kassamuuttumaton(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000)

    # Kortille rahaa ladattaessa kortin saldo muuttuu 
    # ja kassassa oleva rahamäärä kasvaa ladatulla summalla
    def test_10_rahan_talletues(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo_euroina(), 20)
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1010)

    #haarautumisprossan nostoa
    def test_11_negatiivinen_talletus(self):
        raha = self.kassa.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(raha, -100)

    def test_12_ei_rahaa_maukkaasti_kateisella(self):
        vaihto = self.kassa.syo_maukkaasti_kateisella(200)
        self.assertEqual(vaihto, 200)

    def test_13_kortin_saldo_loppu(self):
        self.kortti.ota_rahaa(900)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), False)
        


    