import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(100)
        
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 11.00 euroa")

    def test_saldo_vähenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(100)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 9.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)

        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_metodi_palauttaa_true_jos_raha_riittivät(self):
        

        self.assertEqual(self.maksukortti.ota_rahaa(600), True)
    
    def test_metodi_palauttaa_false_jos_raha_ei_riittivät(self):
        

        self.assertEqual(self.maksukortti.ota_rahaa(1500), False)


