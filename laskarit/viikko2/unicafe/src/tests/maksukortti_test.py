import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "saldo: 20.0")

    def test_saldo_vahenee_oikein_kun_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_metodi_palauttaa_true_jos_rahat_riittivat_muuten_false(self):
        self.assertTrue(self.maksukortti.ota_rahaa(500))
        self.assertFalse(self.maksukortti.ota_rahaa(1500))
