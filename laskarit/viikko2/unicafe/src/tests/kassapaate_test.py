import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_luodun_kassapaatteen_saldo_ja_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_kateisella_syo_maukkaasti_lisaa_kassan_saldoa_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)

    def test_kateisella_syo_maukkaasti_vaihtorahat_oikein(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
    
    def test_kateisella_syo_maukkaasti_myytyjen_maukkaiden_maara_oikein(self):
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 1)
        
        self.kassa.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassa.maukkaat, 2)

    def test_kateisella_syo_edullisesti_lisaa_kassan_saldoa_oikein(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)

    def test_kateisella_syo_edullisesti_vaihtorahat_oikein(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)

    def test_kateisella_syo_edullisesti_myytyjen_edullisten_maara_oikein(self):
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 1)
        
        self.kassa.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassa.edulliset, 2)

    def test_maukkaasti_kassan_saldo_ei_suurene_jos_maksu_liian_pieni(self):
        self.kassa.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_edullisesti_kassan_saldo_ei_suurene_jos_maksu_liian_pieni(self):
        self.kassa.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_ei_vaihtorahoja_jos_tasaraha(self):        
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(240), 0)

    def test_maukkaiden_saldo_ei_suurene_jos_maksu_liian_pieni(self):
        self.kassa.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_edullisten_saldo_ei_suurene_jos_maksu_liian_pieni(self):
        self.kassa.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_kateisella_syo_maukkaasti_jos_maksu_liian_pieni_rahat_oikein_takaisin(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(399), 399)

    def test_kateisella_syo_edullisesti_jos_maksu_liian_pieni_rahat_oikein_takaisin(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(239), 239)

    def test_jos_kortilla_tarpeeksi_rahaa_maksaa_maukkaat_summa_veloitetaan_kortilta(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 600)

    def test_jos_kortilla_ei_tarpeeksi_rahaa_maksaa_maukkaat_summaa_ei_veloiteta_kortilta(self):
        kortti = Maksukortti(339)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 339)

    def test_metodi_palauttaa_true_jos_kortilla_tarpeeksi_rahaa_maksaa_maukkaat(self):
        self.assertTrue(self.kassa.syo_maukkaasti_kortilla(self.kortti))

    def test_jos_kortilla_tarpeeksi_rahaa_maksaa_edulliset_summa_veloitetaan_kortilta(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kortti.saldo, 760)

    def test_jos_kortilla_ei_tarpeeksi_rahaa_maksaa_edulliset_summaa_ei_veloiteta_kortilta(self):
        kortti = Maksukortti(239)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 239)

    def test_metodi_palauttaa_true_jos_kortilla_tarpeeksi_rahaa_maksaa_edulliset(self):
        self.assertTrue(self.kassa.syo_edullisesti_kortilla(self.kortti))

    def test_jos_kortilla_tarpeeksi_rahaa_maksaa_edulliset_kassan_myytyjen_edullisten_maara_kasvaa(self):
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 1)

        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.edulliset, 2)
    
    def test_jos_kortilla_ei_tarpeeksi_rahaa_maksaa_edulliset_kassan_myytyjen_edullisten_maara_ei_kasva(self):
        kortti = Maksukortti(239)
        self.kassa.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassa.edulliset, 0)

    def test_metodi_palauttaa_false_jos_kortilla_ei_tarpeeksi_rahaa_maksaa_edulliset(self):
        kortti = Maksukortti(239)
        self.assertFalse(self.kassa.syo_edullisesti_kortilla(kortti))
    
    def test_jos_kortilla_tarpeeksi_rahaa_maksaa_maukkaat_kassan_myytyjen_maukkaiden_maara_kasvaa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 1)

        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassa.maukkaat, 2)

    def test_jos_kortilla_ei_tarpeeksi_rahaa_maksaa_maukkaat_kassan_myytyjen_maukkaiden_maara_ei_kasva(self):
        kortti = Maksukortti(399)
        self.kassa.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassa.maukkaat, 0)

    def test_metodi_palauttaa_false_jos_kortilla_ei_tarpeeksi_rahaa_maksaa_maukkaat(self):
        kortti = Maksukortti(399)
        self.assertFalse(self.kassa.syo_maukkaasti_kortilla(kortti))

    def test_korttiostos_ei_muuta_kassan_rahamaaraa(self):
        self.kassa.syo_maukkaasti_kortilla(self.kortti)
        self.kassa.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_kasvaa_ladatulla_summalla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 400)
        self.assertEqual(self.kortti.saldo, 1400)

    def test_kortille_rahaa_ladattaessa_kassan_saldo_kasvaa_ladatulla_summalla(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 400)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
    
    def test_kortille_rahaa_ladattaessa_jos_summa_negatiivinen_kortin_saldo_ei_muutu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kortti.saldo, 1000)
    
    def test_kortille_rahaa_ladattaessa_jos_summa_negatiivinen_kassan_saldo_ei_muutu(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
