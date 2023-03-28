import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
    
    def test_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myytyjen_edullisten_lounaita_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_myytyjen_maukkaita_lounaita_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_cash_money_increases_correctly_for_cheap_lunch_if_payment_enough(self):
        self.kassapaate.syo_edullisesti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_cash_money_increases_correctly_for_tasty_lunch_if_payment_enough(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    
    def test_change_is_correct_cheap_lunch(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(500), 260)
    
    def test_change_is_correct_tasty_lunch(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)
    
    def test_payment_not_sufficient(self):
        payment1 = self.kassapaate.syo_edullisesti_kateisella(100)
        payment2 = self.kassapaate.syo_maukkaasti_kateisella(300)

        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(payment1, 100)
        self.assertEqual(payment2, 300)
    
    def test_card_payment_correct_lunch_amount(self):
        payment1 = self.kassapaate.syo_edullisesti_kortilla(Maksukortti(600))
        payment2 = self.kassapaate.syo_maukkaasti_kortilla(Maksukortti(600))

        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(payment1, True)
        self.assertEqual(payment2, True)
    
    def test_card_payment_correct_amount_debited_inexpensive(self):
        self.maksukortti = Maksukortti(600)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        
        self.assertEqual(self.maksukortti.saldo, 360)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        
    def test_card_payment_correct_amount_debited_tasty(self):
        self.maksukortti = Maksukortti(600)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_card_payment_not_enough_money_inexpensive(self):
        self.maksukortti = Maksukortti(200)
        payment = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(payment, False)
    

    def test_card_payment_not_enough_money_tasty(self):
        self.maksukortti = Maksukortti(200)
        payment = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)

        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(payment, False)
    
    def test_loading_money__card_balance_changes_correct(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, (300))

        self.assertEqual(self.maksukortti.saldo, 500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100300)

    def test_loading_wrong_amount_of_money_on_card(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -5)

        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)